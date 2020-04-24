
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
//libCondFormatsJetMETObjects.so
#include "JetMETCorrections/Modules/interface/JetResolution.h"

#include "TKinFitterDriver.h"

#include "TSystem.h"
#include "TROOT.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include "TH1.h"

#include <string>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <array>
#include <string>


class KinematicFitter : public multidraw::TTreeFunction {
public:
  KinematicFitter(char const* yr);

  char const* getName() const override { return "KinematicFitter"; }
  TTreeFunction* clone() const override { return new KinematicFitter(year.c_str()); }

  void beginEvent(long long) override;
  int getMultiplicity() override { return 1; }
  unsigned getNdata() override;
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  static std::string year;

  static long long currentEntry;
  static UIntValueReader*nCleanJetJet;
  static UIntValueReader* nJet;
  static UIntValueReader* nCleanJet;
  static FloatArrayReader* Jet_pt;
  static FloatArrayReader* Jet_pt_nom;
  static FloatArrayReader* Jet_eta;
  static FloatArrayReader* Jet_phi;
  static FloatArrayReader* Jet_mass;
  static FloatArrayReader* Jet_btagDeepB;
  static FloatArrayReader* Lepton_pt;
  static FloatArrayReader* Lepton_eta;
  static FloatArrayReader* Lepton_phi;
  static FloatValueReader* PuppiMET_pt;
  static FloatValueReader* PuppiMET_phi;
  static FloatValueReader* Rho;
  static IntArrayReader* CleanJet_jetIdx;

  static std::vector<unsigned> SelectedJet_jetIdx;
  static std::vector<TLorentzVector> SelectedJet_4vector;
  static std::vector<double> SelectedJet_btagcsv;
  static std::vector<float> SelectedJet_PtResolution;

  static JME::JetResolution jet_resolution;
  static JME::JetResolutionScaleFactor jet_resolution_sf;
  static TKinFitterDriver fitter; // 2018 is dummy variable for now

  static std::vector<std::array<double, 1>> fitterResults; //std::vector<std::array<double, nShiftTypes>>

  static void selectJets(int syst);

  static void setValues(long long);

};

/*static*/
std::string KinematicFitter::year{""};
long long KinematicFitter::currentEntry{-2};
UIntValueReader* KinematicFitter::nJet{};
UIntValueReader* KinematicFitter::nCleanJet{};
FloatArrayReader* KinematicFitter::Jet_pt{};
FloatArrayReader* KinematicFitter::Jet_pt_nom{};
FloatArrayReader* KinematicFitter::Jet_eta{};
FloatArrayReader* KinematicFitter::Jet_phi{};
FloatArrayReader* KinematicFitter::Jet_mass{};
FloatArrayReader* KinematicFitter::Jet_btagDeepB{};
FloatArrayReader* KinematicFitter::Lepton_pt{};
FloatArrayReader* KinematicFitter::Lepton_eta{};
FloatArrayReader* KinematicFitter::Lepton_phi{};
FloatValueReader* KinematicFitter::PuppiMET_pt{};
FloatValueReader* KinematicFitter::PuppiMET_phi{};
FloatValueReader* KinematicFitter::Rho{};
IntArrayReader* KinematicFitter::CleanJet_jetIdx{};

std::vector<unsigned> KinematicFitter::SelectedJet_jetIdx = std::vector<unsigned>();
std::vector<TLorentzVector> KinematicFitter::SelectedJet_4vector = std::vector<TLorentzVector>();
std::vector<double> KinematicFitter::SelectedJet_btagcsv = std::vector<double>();
std::vector<float> KinematicFitter::SelectedJet_PtResolution = std::vector<float>();
JME::JetResolution KinematicFitter::jet_resolution = JME::JetResolution();
JME::JetResolutionScaleFactor KinematicFitter::jet_resolution_sf = JME::JetResolutionScaleFactor();

TKinFitterDriver KinematicFitter::fitter = TKinFitterDriver(2018); // 2018 is dummy variable for now

std::vector<std::array<double, 1>> KinematicFitter::fitterResults = std::vector<std::array<double, 1>>();

KinematicFitter::KinematicFitter(char const* yr) :
  TTreeFunction()
{
  if (year.size() == 0)
    year = yr;
  else if (year != yr)
    throw std::runtime_error("KinematicFitter already set up for " + year);

  //TString BASE_PATH = TString(std::getenv("CMSSW_BASE")) + TString("/src/SNuAnalytics/Configurations/TTSemiLep/patches/KinematicFitter/src/");
  //try{
  //  gROOT->LoadMacro(BASE_PATH + "TAbsFitConstraint.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TAbsFitParticle.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintEp.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintM.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintM2Gaus.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintMGaus.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticleEt.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticleEtEtaPhi.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticleEtPhi.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticlePt.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticlePxPy.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticlePz.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TKinFitter.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TSCorrection.C+"  );
  //  gROOT->LoadMacro(BASE_PATH + "TKinFitterDriver.C+"  );
  //}
  //catch(const runtime_error& error) {
  //  gROOT->LoadMacro(BASE_PATH + "TAbsFitConstraint.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TAbsFitParticle.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintEp.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintM.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintM2Gaus.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitConstraintMGaus.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticleEt.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticleEtEtaPhi.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticleEtPhi.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticlePt.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticlePxPy.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TFitParticlePz.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TKinFitter.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TSCorrection.C++"  );
  //  gROOT->LoadMacro(BASE_PATH + "TKinFitterDriver.C++"  );
  //}
}

void
KinematicFitter::beginEvent(long long _iEntry)
{
  setValues(_iEntry);
}

unsigned
KinematicFitter::getNdata()
{
  return fitterResults.size();
}

double
KinematicFitter::evaluate(unsigned iJ)
{
  return fitterResults[iJ][0]; // no systematic available yet
}

void
KinematicFitter::selectJets(int syst)
{

  SelectedJet_jetIdx.clear();
  SelectedJet_4vector.clear();
  SelectedJet_btagcsv.clear();
  SelectedJet_PtResolution.clear();
  FloatArrayReader* jet_pt_jer_ptr = NULL;

  if(syst==0){
    jet_pt_jer_ptr = Jet_pt_nom;
  }
  else{
    throw std::runtime_error("KinematicFitter syst index is not valid ");
  }

  unsigned nCJ{*nCleanJet->Get()};
  for (unsigned iCJ{0}; iCJ != nCJ; ++iCJ) {
    int iJ{CleanJet_jetIdx->At(iCJ)};
    if(iJ<0){
      throw std::runtime_error("KinematicFitter invalid index in CleanJet_jetIdx");
      break;
    }
    double pt{Jet_pt->At(iJ)};
    double pt_jer{jet_pt_jer_ptr->At(iJ)};
    double eta{Jet_eta->At(iJ)};
    double phi{Jet_phi->At(iJ)};
    double m{Jet_mass->At(iJ)};
    double btagcsv{Jet_btagDeepB->At(iJ)};

    //XXX
    //XXX
    //XXX
    //XXX
    //XXX hard coded cuts !!!!!!!!!!!!!!!!!!!!
    //XXX
    //XXX
    //XXX
    //XXX
    if (pt_jer <= 30. || std::abs(eta) >= 2.5)
      continue;
    SelectedJet_jetIdx.push_back(iJ);
    TLorentzVector tmp_4vector;
    tmp_4vector.SetPtEtaPhiM(pt_jer,eta,phi,m);
    SelectedJet_4vector.push_back(std::move(tmp_4vector));
    SelectedJet_btagcsv.push_back(btagcsv);
    double PtResolution =  jet_resolution.getResolution({{JME::Binning::JetPt, pt}, {JME::Binning::JetEta, eta}, {JME::Binning::Rho, *Rho->Get()}});
    double PtResolution_sf = jet_resolution_sf.getScaleFactor({{JME::Binning::JetPt, pt},{JME::Binning::JetEta, eta}}, Variation::NOMINAL);
    SelectedJet_PtResolution.push_back(PtResolution*PtResolution_sf);
  } 
}

void
KinematicFitter::setValues(long long _iEntry)
{
  if (_iEntry == currentEntry)
    return;

  currentEntry = _iEntry;

  fitterResults.clear();

  selectJets(0);
  TLorentzVector lepton;
  lepton.SetPtEtaPhiM(Lepton_pt->At(0),Lepton_eta->At(0),Lepton_phi->At(0),0.);
  TLorentzVector MET;
  MET.SetPtEtaPhiM(*PuppiMET_pt->Get(), 0., *PuppiMET_phi->Get(), 0.);
  
  double DeepB_WP_M_2018 = 0.4184; //XXX let me hard code this time

  //TKinFitterDriver fitter = TKinFitterDriver(2018); // 2018 is dummy variable for now
  fitter.SetAllObjects(SelectedJet_4vector, SelectedJet_btagcsv, DeepB_WP_M_2018, lepton, MET);
  fitter.SetJetPtResolution(SelectedJet_PtResolution);
  fitter.FindMaxPtHadTopFit(false,true,true);

  std::vector<double> tmp_results = {
    fitter.GetBestInitialDijetMass()             , // 0
    fitter.GetBestInitialDijetMass_high()        , // 1
    fitter.GetBestCorrectedDijetMass()           , // 2
    fitter.GetBestCorrectedDijetMass_high()      , // 3
    fitter.GetBestFittedDijetMass()              , // 4
    fitter.GetBestFittedDijetMass_high()         , // 5
    fitter.GetBestChi2()                         , // 6 
    static_cast<double>( fitter.GetBestStatus()                   ) , // 7
    static_cast<double>( fitter.GetBestDownTypeJetBTagged()       ) , // 8
    static_cast<double>( fitter.GetBestHadronicTopBJetIdx()       ) , // 9
    static_cast<double>( fitter.GetBestLeptonicTopBJetIdx()       ) , // 10
    static_cast<double>( fitter.GetBestHadronicWCHUpTypeJetIdx()  ) , // 11
    static_cast<double>( fitter.GetBestHadronicWCHDownTypeJetIdx()) , // 12
    fitter.GetBestHadronicTopBJetPull()          , // 13
    fitter.GetBestHadronicWCHUptypeJetIdxPull()  , // 14
    fitter.GetBestHadronicWCHDowntypeJetIdxPull(), // 15
    fitter.GetBestHadronicTopMass()              , // 16
    fitter.GetBestLeptonicTopMass()              , // 17
    fitter.GetBestLeptonicWMass()                  // 18
  };
  fitterResults.resize(tmp_results.size());

  for(unsigned iR{0}; iR!=fitterResults.size(); ++iR){
    std::fill_n(fitterResults[iR].begin(),1,tmp_results[iR]);
  }
}

void
KinematicFitter::bindTree_(multidraw::FunctionLibrary& _library)
{
  if (currentEntry == -2) {
    currentEntry = -1;

    {
      TDirectory::TContext context;

      // Will add get jet resolution
      std::string jetPtResolutionPath = "";
      std::string jetPtResolutionSFPath = "";
      std::string BASE_PATH = std::getenv("CMSSW_BASE") + std::string("/src/PhysicsTools/NanoAODTools/data/jme/");
      if(year=="2018"){
        jetPtResolutionPath = BASE_PATH + "Autumn18_V7_MC_PtResolution_AK4PFchs.txt";
        jetPtResolutionSFPath = BASE_PATH + "Autumn18_V7_MC_SF_AK4PFchs.txt";
      }
      else{
        throw std::runtime_error("no configuration for year: " + year);
      }
      jet_resolution = JME::JetResolution( jetPtResolutionPath );
      jet_resolution_sf = JME::JetResolutionScaleFactor( jetPtResolutionSFPath );

    }

    _library.bindBranch(nJet, "nJet");
    _library.bindBranch(nCleanJet, "nCleanJet");
    _library.bindBranch(Jet_pt, "Jet_pt");
    _library.bindBranch(Jet_pt_nom, "Jet_pt_nom");
    _library.bindBranch(Jet_eta, "Jet_eta");
    _library.bindBranch(Jet_phi, "Jet_phi");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(Jet_btagDeepB, "Jet_btagDeepB");
    _library.bindBranch(Lepton_pt,  "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(PuppiMET_pt, "PuppiMET_pt");
    _library.bindBranch(PuppiMET_phi, "PuppiMET_phi");
    _library.bindBranch(Rho, "fixedGridRhoFastjetAll");
    _library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");

    _library.addDestructorCallback([]() {
        currentEntry = -2;
        nJet = nullptr;
        nCleanJet = nullptr;
        Jet_pt = nullptr;
        Jet_pt_nom = nullptr;
        Jet_eta = nullptr;
        Jet_phi = nullptr;
        Jet_mass = nullptr;
        Jet_btagDeepB = nullptr;
        Lepton_pt = nullptr;
        Lepton_eta = nullptr;
        Lepton_phi = nullptr;
        PuppiMET_pt = nullptr; 
        PuppiMET_phi = nullptr;
        Rho = nullptr;
        CleanJet_jetIdx = nullptr;
        jet_resolution =  JME::JetResolution();
        jet_resolution_sf = JME::JetResolutionScaleFactor();
      });
  }
}
