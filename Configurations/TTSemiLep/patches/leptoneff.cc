#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>
#include <map>

#include "TVector2.h"
#include "TString.h"
#include "TFile.h"
#include "TH2.h"
#include "TH2F.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class LeptonEff : public multidraw::TTreeFunction {
public:
  LeptonEff(char const* fileNameEle, char const* fileNameMu, char const* histNameEle, char const* histNameMu, char const* binningEle, char const* binningMu);

  char const* getName() const override { return "LeptonEff"; }
  TTreeFunction* clone() const override { return new LeptonEff(fileNameEle_.Data(), fileNameMu_.Data(), histNameEle_.Data(), histNameMu_.Data(), binningEle_.Data(), binningMu_.Data()); }
  
  void beginEvent(long long) override;
  unsigned getNdata() override { return leptonEff.size(); }
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  IntArrayReader*   Lepton_isTightElectron_POGTight{};
  IntArrayReader*   Lepton_isTightMuon_cut_Tight_POG{};
  IntArrayReader*   Lepton_pdgId{};
  IntArrayReader*   Lepton_electronIdx{};
  UIntValueReader*  nLepton{};
  FloatArrayReader* Electron_deltaEtaSC{};
  FloatArrayReader* Electron_eCorr{};
  FloatArrayReader* Lepton_rochesterSF{};


  std::vector<double> leptonEff{};
  void setValues();
  double GetBinContent4SF(TH1* hist, double valx, double sys);
  double GetBinContent4SF(TH2* hist, double valx, double valy, double sys);

  TString fileNameEle_{};
  TString fileNameMu_{};
  TString histNameEle_{};
  TString histNameMu_{};
  TString binningEle_{};
  TString binningMu_{};

  TFile* rootFileEle{};
  TFile* rootFileMu{};
  TH2F* histLeptonEffEle{};
  TH2F* histLeptonEffMu{};


};


void
LeptonEff::beginEvent(long long _iEntry)
{
  setValues();
}


LeptonEff::LeptonEff(char const* fileNameEle, char const* fileNameMu, char const* histNameEle, char const* histNameMu, char const* binningEle, char const* binningMu) :
  TTreeFunction(),
  fileNameEle_{fileNameEle},
  fileNameMu_{fileNameMu},
  histNameEle_{histNameEle},
  histNameMu_{histNameMu},
  binningEle_{binningEle},
  binningMu_{binningMu}
{
  // read SF, from txt file.
  // list up lepton SFs (RECO, ID, Trigger) on the txt file.
  // read SFs in map<TString, TH2D>

  rootFileEle = new TFile(fileNameEle_);
  rootFileMu  = new TFile(fileNameMu_);

  if(!rootFileEle){
    throw std::runtime_error("file not exist: " + fileNameEle_);
  }
  if(!rootFileMu){
    throw std::runtime_error("file not exist: " + fileNameMu_);
  }

  histLeptonEffEle = (TH2F*)rootFileEle->Get(histNameEle_);
  histLeptonEffMu = (TH2F*)rootFileMu->Get(histNameMu_);

  if(!histLeptonEffEle){
    throw std::runtime_error("hist not exist: " + histNameEle_);
  }
  if(!histLeptonEffMu){
    throw std::runtime_error("hist not exist: " + histNameMu_);
  }
}


double
LeptonEff::evaluate(unsigned iJ)
{
  // leptonEff[0] : central, leptonEff[1] : ele up, leptonEff[2] : ele down, leptonEff[3] : mu up, leptonEff[4] : mu down
  return leptonEff[iJ];
}


void
LeptonEff::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_isTightElectron_POGTight,  "Lepton_isTightElectron_POGTight");
  _library.bindBranch(Lepton_isTightMuon_cut_Tight_POG, "Lepton_isTightMuon_cut_Tight_POG");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_electronIdx, "Lepton_electronIdx");
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Electron_deltaEtaSC, "Electron_deltaEtaSC");
  _library.bindBranch(Electron_eCorr, "Electron_eCorr");
  _library.bindBranch(Lepton_rochesterSF, "Lepton_rochesterSF");
}


void
LeptonEff::setValues()
{

  leptonEff.clear();
  // lepton loop
  std::array<double, 5> eff_minus_1_total = {1., 1., 1., 1., 1.};
  std::array<double, 5> eff_minus_1 = {1., 1., 1., 1., 1.};

  unsigned nL{*nLepton->Get()};

  for(unsigned iL{0}; iL!=nL; iL++){
  //for(unsigned iL{0}; iL!=1; iL++){

    // is tight
    if(Lepton_isTightElectron_POGTight->At(iL)<0.5 && Lepton_isTightMuon_cut_Tight_POG->At(iL)<0.5){
      continue;
    }

    double lepEta{Lepton_eta->At(iL)};
    double lepDeltaEtaSC{0.};
    double lepeCorr{1.};
    int lepFlav{abs(Lepton_pdgId->At(iL))};
    if(lepFlav==11){
      lepDeltaEtaSC = Electron_deltaEtaSC->At(Lepton_electronIdx->At(iL));
      lepeCorr      = Electron_eCorr->At(Lepton_electronIdx->At(iL));
    }
    else if(lepFlav==13){
      lepeCorr = Lepton_rochesterSF->At(iL);
    }

    double lepPt{Lepton_pt->At(iL)};
    lepPt /=lepeCorr;

    double xvar, yvar;
    TH2F* histLeptonEff;

    //binning info. by lepton flavour
    TString binning_{""};
    if(lepFlav==11){
      binning_ = binningEle_;
      histLeptonEff = histLeptonEffEle;
    }
    else if(lepFlav==13){
      binning_ = binningMu_;
      histLeptonEff = histLeptonEffMu;
    }
    else{
      std::cout << "lepton flavour" << std::endl;
      exit(1);
    }

    // set xvar, yvar
    if(binning_=="pteta"){
      xvar = lepPt;
      yvar = lepEta+lepDeltaEtaSC;
    }
    else if(binning_=="etapt"){
      xvar = lepEta+lepDeltaEtaSC;
      yvar = lepPt;
    }
    else{
      std::cout << "binning should be pteta or etapt" << std::endl;
      exit(1);
    }

    eff_minus_1.at(0) = 1. - this->GetBinContent4SF(histLeptonEff, xvar, yvar, 0.);
    eff_minus_1.at(1) = 1. - this->GetBinContent4SF(histLeptonEff, xvar, yvar, lepFlav==11?1.:0.);
    eff_minus_1.at(2) = 1. - this->GetBinContent4SF(histLeptonEff, xvar, yvar, lepFlav==11?-1.:0.);
    eff_minus_1.at(3) = 1. - this->GetBinContent4SF(histLeptonEff, xvar, yvar, lepFlav==13?1.:0.);
    eff_minus_1.at(4) = 1. - this->GetBinContent4SF(histLeptonEff, xvar, yvar, lepFlav==13?-1.:0.);

    // eff. minus 1.
    eff_minus_1_total.at(0) *= eff_minus_1.at(0);
    eff_minus_1_total.at(1) *= eff_minus_1.at(1);
    eff_minus_1_total.at(2) *= eff_minus_1.at(2);
    eff_minus_1_total.at(3) *= eff_minus_1.at(3);
    eff_minus_1_total.at(4) *= eff_minus_1.at(4);
  }

  eff_minus_1_total.at(0) = 1-eff_minus_1_total.at(0);
  eff_minus_1_total.at(1) = 1-eff_minus_1_total.at(1);
  eff_minus_1_total.at(2) = 1-eff_minus_1_total.at(2);
  eff_minus_1_total.at(3) = 1-eff_minus_1_total.at(3);
  eff_minus_1_total.at(4) = 1-eff_minus_1_total.at(4);

  leptonEff.push_back(eff_minus_1_total.at(0));
  leptonEff.push_back(eff_minus_1_total.at(1));
  leptonEff.push_back(eff_minus_1_total.at(2));
  leptonEff.push_back(eff_minus_1_total.at(3));
  leptonEff.push_back(eff_minus_1_total.at(4));

}


double LeptonEff::GetBinContent4SF(TH2* hist, double valx, double valy, double sys){
  double xmin=hist->GetXaxis()->GetXmin();
  double xmax=hist->GetXaxis()->GetXmax();
  double ymin=hist->GetYaxis()->GetXmin();
  double ymax=hist->GetYaxis()->GetXmax();
  if(xmin>=0) valx=fabs(valx);
  if(valx<xmin) valx=xmin+0.001;
  if(valx>xmax) valx=xmax-0.001;
  if(ymin>=0) valy=fabs(valy);
  if(valy<ymin) valy=ymin+0.001;
  if(valy>ymax) valy=ymax-0.001;
  return hist->GetBinContent(hist->FindBin(valx,valy))+sys*hist->GetBinError(hist->FindBin(valx,valy));
}
    
double LeptonEff::GetBinContent4SF(TH1* hist, double valx, double sys){
  double xmin=hist->GetXaxis()->GetXmin();
  double xmax=hist->GetXaxis()->GetXmax();
  if(xmin>=0) valx=fabs(valx);
  if(valx<xmin) valx=xmin+0.001;
  if(valx>xmax) valx=xmax-0.001;
  return hist->GetBinContent(hist->FindBin(valx)) + sys*hist->GetBinError(hist->FindBin(valx));
}

