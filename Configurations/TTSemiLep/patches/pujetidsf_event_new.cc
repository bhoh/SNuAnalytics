/*
  Temporary on-the-fly PU JetId SF calculator. Returns the product of SFs for all jets with pt > 30. && |eta| < 4.7
*/

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TSystem.h"
#include "TFile.h"
#include "TMath.h"
#include "TH1.h"

#include <string>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <array>
#include <string>

class PUJetIdEventSF : public multidraw::TTreeFunction {
public:
  PUJetIdEventSF(char const* filename, char const* yr, char const* wp);

  char const* getName() const override { return "PUJetIdEventSF"; }
  TTreeFunction* clone() const override { return new PUJetIdEventSF(filename_.c_str(), year.c_str(), wpStr_.c_str()); }

  void beginEvent(long long) override;
  unsigned getNdata() override;
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  enum WP {
    kTight,
    kMedium,
    kLoose,
    nWPs
  };

  std::string filename_{};

  std::string wpStr_{};
  WP wp_{nWPs};

  static std::string year;

  static long long currentEntry;
  static UIntValueReader* nJet;
  static UIntValueReader* nLepton;
  static FloatArrayReader* Lepton_eta;
  static FloatArrayReader* Lepton_phi;
  static FloatArrayReader* Jet_pt;
  static FloatArrayReader* Jet_eta;
  static FloatArrayReader* Jet_phi;
  static IntArrayReader* Jet_jetId;
  static IntArrayReader* Jet_genJetIdx;
  static IntArrayReader * Jet_puId;

  typedef std::array<std::unique_ptr<TH1>, nWPs> MapSet;
  typedef std::array<MapSet, 2> MapSets;
  static MapSets sfMapSets;
  static MapSets sfMapSets_SystUncty;
  static MapSets effMapSets;

  static void setValues(long long);

  static std::vector<std::array<float, nWPs> > scalefactors;
};

/*static*/
std::string PUJetIdEventSF::year{""};
long long PUJetIdEventSF::currentEntry{-2};
UIntValueReader* PUJetIdEventSF::nJet{};
UIntValueReader* PUJetIdEventSF::nLepton{};
FloatArrayReader* PUJetIdEventSF::Lepton_eta{};
FloatArrayReader* PUJetIdEventSF::Lepton_phi{};
FloatArrayReader* PUJetIdEventSF::Jet_pt{};
FloatArrayReader* PUJetIdEventSF::Jet_eta{};
FloatArrayReader* PUJetIdEventSF::Jet_phi{};
IntArrayReader * PUJetIdEventSF::Jet_jetId{};
IntArrayReader * PUJetIdEventSF::Jet_puId{};
IntArrayReader* PUJetIdEventSF::Jet_genJetIdx{};
PUJetIdEventSF::MapSets PUJetIdEventSF::effMapSets{};
PUJetIdEventSF::MapSets PUJetIdEventSF::sfMapSets{};
PUJetIdEventSF::MapSets PUJetIdEventSF::sfMapSets_SystUncty{};
std::vector<std::array<float, PUJetIdEventSF::nWPs> > PUJetIdEventSF::scalefactors{};

PUJetIdEventSF::PUJetIdEventSF(char const* filename, char const* yr, char const* wp) :
  TTreeFunction(),
  filename_{filename},
  wpStr_{wp}
{


  if (year.size() == 0)
    year = yr;
  else if (year != yr)
    throw std::runtime_error("PUJetIdEventSF already set up for " + year);

  if (year == "UL2016" || year == "UL2016APV"){

    if (wpStr_ == "loose")
      wp_ = kTight; // nanoAODv8/9 level issue
    else if (wpStr_ == "medium")
      wp_ = kMedium;
    else if (wpStr_ == "tight")
      wp_ = kLoose; // nanoAODv8/9 level issue
    else
      throw std::runtime_error("unknown working point " + wpStr_);
  
  }
  else{
      
    if (wpStr_ == "loose")
      wp_ = kLoose;
    else if (wpStr_ == "medium")
      wp_ = kMedium;
    else if (wpStr_ == "tight")
      wp_ = kTight;
    else
      throw std::runtime_error("unknown working point " + wpStr_);
 
  }

  //cout << "debug 1-1" << endl;

}

void
PUJetIdEventSF::beginEvent(long long _iEntry)
{
  //cout << "debug 1-2" << endl;
  setValues(_iEntry);
  //cout << "debug 1-3" << endl;
}
unsigned
PUJetIdEventSF::getNdata()
{
  return scalefactors.size();
}
double
PUJetIdEventSF::evaluate(unsigned iJ)
{
  //cout << "debug 1-4" << endl;
  return scalefactors[iJ][wp_];
}


void
PUJetIdEventSF::setValues(long long _iEntry)
{
  if (_iEntry == currentEntry)
    return;

  currentEntry = _iEntry;

  std::array<float,3> scalefactor{};
  scalefactors.clear();
  scalefactors.resize(3);

  for(auto& scalefactor : scalefactors)
    std::fill_n(scalefactor.begin(), nWPs, 1.);

  unsigned nJ{*nJet->Get()};

  for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    double pt{Jet_pt->At(iJ)};
    double eta{Jet_eta->At(iJ)};

    //BHO: pt cut 25. -> 15. fixed.
    //     min pT for jet: 15 GeV
    //     PU Id eff. binning minimum 15 GeV
    if (pt < 25. || pt > 50.|| std::abs(eta) >= 2.5 || Jet_jetId->At(iJ)<6)
    // excluding also the jets with jetId < 6 since we are considering only these jets in the selection before PUid selection.
    // 
    //  <2 -> ask tightId
    //  <4 -> ask tightIdLepVeto
    //  <6 -> ask tightId+tightIdLepVeto
      continue;

    bool isLeptonMatched = false;
    for (unsigned ilep = 0; ilep < *(nLepton->Get()); ilep++){
      float lepEta = Lepton_eta->At(ilep);
      float lepPhi = Lepton_phi->At(ilep);
      float jetEta = Jet_eta->At(iJ);
      float jetPhi = Jet_phi->At(iJ);
      float dPhi = abs(lepPhi - jetPhi);
      if (dPhi > TMath::Pi())  
        dPhi = 2*TMath::Pi() - dPhi;

      float dR2 = (lepEta - jetEta) * (lepEta - jetEta) + dPhi * dPhi;
      
      if (dR2 < 0.3*0.3)  isLeptonMatched =true;
    }
    if (isLeptonMatched) continue;

    unsigned mapType{};
    if (Jet_genJetIdx->At(iJ) != -1)
      mapType = 0;
    else
      mapType = 1;

    for (unsigned iWP{0}; iWP != nWPs; ++iWP) {
      // if mapTap = 0 efficiency h2 are used, if mapType = 1 mistag h2 are used
      auto iWP_ = iWP;
      //if(pt < 30. && iWP_ == kLoose){
      //  iWP_ = kMedium;
      //}
      auto& sf_map{sfMapSets[mapType][iWP_]};
      auto& sf_map_SystUncty{sfMapSets_SystUncty[mapType][iWP_]};
      auto& eff_map{effMapSets[mapType][iWP_]};

      int iX{eff_map->GetXaxis()->FindFixBin(pt)};
      if (iX == 0)
        iX = 1;
      else if (iX > eff_map->GetNbinsX())
        iX = eff_map->GetNbinsX();

      int iY{eff_map->GetYaxis()->FindFixBin(eta)};
      if (iY == 0)
        iY = 1;
      else if (iY > eff_map->GetNbinsY())
        iY = eff_map->GetNbinsY();

      // iWP = 0 Tight, 1 Medium, 2 Loose 
      // or iWP = 0 Loose, 1 Medium, 2 Tight
      bool passId = (Jet_puId->At(iJ)) & (1 << iWP_);
      if (passId){
        scalefactor[0] = (sf_map->GetBinContent(iX, iY));
        scalefactor[1] = (sf_map->GetBinContent(iX, iY) + sf_map->GetBinError(iX, iY) + sf_map_SystUncty->GetBinContent(iX, iY));
        scalefactor[2] = (sf_map->GetBinContent(iX, iY) - sf_map->GetBinError(iX, iY) - sf_map_SystUncty->GetBinContent(iX, iY));
      }
      else {
        scalefactor[0] = (1- sf_map->GetBinContent(iX, iY)*eff_map->GetBinContent(iX,iY)) / (1-eff_map->GetBinContent(iX,iY));
        scalefactor[1] = (1- (sf_map->GetBinContent(iX, iY) + sf_map->GetBinError(iX, iY) + sf_map_SystUncty->GetBinContent(iX, iY))*eff_map->GetBinContent(iX,iY)) / (1-eff_map->GetBinContent(iX,iY));
        scalefactor[2] = (1- (sf_map->GetBinContent(iX, iY) - sf_map->GetBinError(iX, iY) - sf_map_SystUncty->GetBinContent(iX, iY))*eff_map->GetBinContent(iX,iY)) / (1-eff_map->GetBinContent(iX,iY));
      }
      // safty for empty histogram bins
      scalefactors[0][iWP] *= scalefactor[0]>0.?scalefactor[0]:1.;
      scalefactors[1][iWP] *= scalefactor[1]>0.?scalefactor[1]:1.;
      scalefactors[2][iWP] *= scalefactor[2]>0.?scalefactor[2]:1.;
    }
  }
  //cout << "SF L norm/up/down: "<< scalefactors[0][kLoose] << " "<<scalefactors[1][kLoose] << " "<<scalefactors[2][kLoose] << endl;
}

void
PUJetIdEventSF::bindTree_(multidraw::FunctionLibrary& _library)
{
  if (currentEntry == -2) {
    currentEntry = -1;

    {
      TDirectory::TContext context;

      //cout << "debug 2-1" << endl;
      auto* source{TFile::Open(filename_.c_str())};
      //cout << "debug 2-2" << endl;
      // Same order of bit to check the Jetid 
      std::string wps16[nWPs] = {"L","M","T"};
      std::string wps1718[nWPs] = {"T","M","L"};

      std::string* wps;

      if (year == "UL2016" || year == "UL2016APV"){
        wps = wps16;
      }
      else{
        wps = wps1718;
      }

      for (unsigned iwp{0}; iwp != nWPs; ++iwp) {

        if(!source->Get(("h2_eff_mc"+year +"_" + wps[iwp]).c_str())){
          cout << ("h2_eff_mc"+year +"_" + wps[iwp]).c_str() << " is not exist!!!!!" << endl;
        }
        if(!source->Get(("h2_mistag_mc"+year +"_" + wps[iwp]).c_str())){
          cout << ("h2_mistag_mc"+year +"_" + wps[iwp]).c_str() << " is not exist!!!!!" << endl;
        }
        if(!source->Get(("h2_eff_sf"+year +"_" + wps[iwp]).c_str())){
          cout << ("h2_eff_sf"+year +"_" + wps[iwp]).c_str() << " is not exist!!!!!" << endl;
        }
        if(!source->Get(("h2_mistag_sf"+year +"_" + wps[iwp]).c_str())){
          cout << ("h2_mistag_sf"+year +"_" + wps[iwp]).c_str() << " is not exist!!!!!" << endl;
        }
        if(!source->Get(("h2_eff_sf"+year +"_" + wps[iwp]+"_SystUncty").c_str())){
          cout << ("h2_eff_sf"+year +"_" + wps[iwp]+"_SystUncty").c_str() << " is not exist!!!!!" << endl;
        }
        if(!source->Get(("h2_mistag_sf"+year +"_" + wps[iwp]+"_SystUncty").c_str())){
          cout << ("h2_mistag_sf"+year +"_" + wps[iwp]+"_SystUncty").c_str() << " is not exist!!!!!" << endl;
        }

        effMapSets[0][iwp].reset(static_cast<TH1*>(source->Get(("h2_eff_mc"+year +"_" + wps[iwp]).c_str())));
        effMapSets[1][iwp].reset(static_cast<TH1*>(source->Get(("h2_mistag_mc"+year +"_" + wps[iwp]).c_str())));
        effMapSets[0][iwp]->SetDirectory(nullptr);
        effMapSets[1][iwp]->SetDirectory(nullptr);
        sfMapSets[0][iwp].reset(static_cast<TH1*>(source->Get(("h2_eff_sf"+year +"_" + wps[iwp]).c_str())));
        sfMapSets[1][iwp].reset(static_cast<TH1*>(source->Get(("h2_mistag_sf"+year +"_" + wps[iwp]).c_str())));
        sfMapSets[0][iwp]->SetDirectory(nullptr);
        sfMapSets[1][iwp]->SetDirectory(nullptr);
        sfMapSets_SystUncty[0][iwp].reset(static_cast<TH1*>(source->Get(("h2_eff_sf"+year +"_" + wps[iwp]+"_SystUncty").c_str())));
        sfMapSets_SystUncty[1][iwp].reset(static_cast<TH1*>(source->Get(("h2_mistag_sf"+year +"_" + wps[iwp]+"_SystUncty").c_str())));
        sfMapSets_SystUncty[0][iwp]->SetDirectory(nullptr);
        sfMapSets_SystUncty[1][iwp]->SetDirectory(nullptr);
      }
      //cout << "debug 2-3" << endl;
      delete source;
    }
    
    _library.bindBranch(nJet, "nJet");
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(Jet_pt, "Jet_pt"); // nanoAOD pT
    //_library.bindBranch(Jet_pt, "Jet_pt_nom"); // JER smeared PT
    _library.bindBranch(Jet_jetId, "Jet_jetId");
    _library.bindBranch(Jet_eta, "Jet_eta");
    _library.bindBranch(Jet_phi, "Jet_phi");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(Jet_genJetIdx, "Jet_genJetIdx");
    _library.bindBranch(Jet_puId, "Jet_puId");

    _library.addDestructorCallback([]() {
        currentEntry = -2;
        nJet = nullptr;
        nLepton = nullptr;
        Jet_pt = nullptr;
        Jet_eta = nullptr;
        Jet_genJetIdx = nullptr;
        Jet_puId = nullptr;
        Jet_phi = nullptr;
        Lepton_eta = nullptr;
        Lepton_phi = nullptr;
        Jet_jetId = nullptr;
        for (auto& sms : sfMapSets) {
          for (auto& sfMap : sms)
            sfMap.reset();
        }
        for (auto& sms_syst : sfMapSets_SystUncty) {
          for (auto& sfMap_syst : sms_syst)
            sfMap_syst.reset();
        }
        for (auto& sms : effMapSets) {
          for (auto& efMap : sms)
            efMap.reset();
        }
      });
  }
}
