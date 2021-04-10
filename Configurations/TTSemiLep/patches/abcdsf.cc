#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>
#include <map>

#include "TVector2.h"
#include "TString.h"
#include "TFile.h"
#include "TH2.h"
#include "TH2F.h"
#include "TH1.h"
#include "TH1F.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class ABCDSF : public multidraw::TTreeFunction {
public:
  ABCDSF(char const* fileName, char const* histName, char const* systName, char const* binning);

  char const* getName() const override { return "ABCDSF"; }
  TTreeFunction* clone() const override { return new ABCDSF(fileName_.Data(), histName_.Data(), systName_.Data(), binning_.Data()); }
  
  void beginEvent(long long) override;
  unsigned getNdata() override { return leptonSF.size(); }
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  IntArrayReader*   Lepton_pdgId{};
  IntArrayReader*   Lepton_electronIdx{};
  FloatArrayReader* Electron_deltaEtaSC{};


  std::vector<double> leptonSF{};
  void setValues();
  double GetBinContent4SF(TH1* hist, double valx, double sys);
  double GetBinContent4SF(TH1* hist, double valx, double sys, int stat_bin);
  double GetBinContent4SF(TH2* hist, double valx, double valy, double sys);

  TString fileName_{};
  TString histName_{};
  TString systName_{};
  TString binning_{};

  TFile* rootFile{};
  TH1F* histABCDSF{};
  TH1F* histABCDSF_syst_up{};
  TH1F* histABCDSF_syst_down{};


};


void
ABCDSF::beginEvent(long long _iEntry)
{
  setValues();
}


ABCDSF::ABCDSF(char const* fileName, char const* histName, char const* systName, char const* binning) :
  TTreeFunction(),
  fileName_{fileName},
  histName_{histName},
  systName_{systName},
  binning_{binning}
{
  // read SF, from txt file.
  // list up lepton SFs (RECO, ID, Trigger) on the txt file.
  // read SFs in map<TString, TH2D>

  rootFile = new TFile(fileName_);
  histABCDSF = (TH1F*)rootFile->Get(histName_);
  if(systName_==""){
    histABCDSF_syst_up   = histABCDSF;
    histABCDSF_syst_down = histABCDSF;
  }
  else if(systName_.Contains("Var")){
    histABCDSF_syst_up   = (TH1F*)rootFile->Get(histName_+"_"+systName_);
    histABCDSF_syst_down = (TH1F*)rootFile->Get(histName_+"_"+systName_);
  }
  else{
    histABCDSF_syst_up   = (TH1F*)rootFile->Get(histName_+"_"+systName_+"Up");
    histABCDSF_syst_down = (TH1F*)rootFile->Get(histName_+"_"+systName_+"Down");
  }

  if(!histABCDSF){
    std::cout << histName_ << std::endl;
    exit(1);
  }
  if(!histABCDSF_syst_up){
    std::cout <<histName_+"_"+systName_+"(Up)" << std::endl;
    exit(1);
  }
  if(!histABCDSF_syst_down){
    std::cout <<histName_+"_"+systName_+"(Down)" << std::endl;
    exit(1);
  }
}


double
ABCDSF::evaluate(unsigned iJ)
{
  // leptonSF[0] : central, leptonSF[1] : up, leptonSF[2] : down
  return leptonSF[iJ];
}


void
ABCDSF::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_electronIdx, "Lepton_electronIdx");
  _library.bindBranch(Electron_deltaEtaSC, "Electron_deltaEtaSC");
}


void
ABCDSF::setValues()
{

  leptonSF.clear();
  double lepEta{Lepton_eta->At(0)}; //TODO will use scEta for electron
  double lepDeltaEtaSC{0.};
  if(abs(Lepton_pdgId->At(0))==11){
    lepDeltaEtaSC = Electron_deltaEtaSC->At(Lepton_electronIdx->At(0));
  }

  double xvar;
  xvar = lepEta+lepDeltaEtaSC;

  leptonSF.push_back(this->GetBinContent4SF(histABCDSF,          xvar,  0));
  if(systName_==""){
    for(int i(1); i<=histABCDSF->GetNbinsX(); i++){
      leptonSF.push_back(this->GetBinContent4SF(histABCDSF,         xvar,   1, i));
      leptonSF.push_back(this->GetBinContent4SF(histABCDSF,         xvar,  -1, i));
    }
    std::cout << "//////////////////////////////////////////" << std::endl;
    for(auto& x : leptonSF){
      std::cout << x << std::endl;
    }
    std::cout << "//////////////////////////////////////////" << std::endl;
  }
  else{
    leptonSF.push_back(this->GetBinContent4SF(histABCDSF_syst_up,   xvar,  0));
    leptonSF.push_back(this->GetBinContent4SF(histABCDSF_syst_down, xvar,  0));
  }

}


double ABCDSF::GetBinContent4SF(TH2* hist, double valx, double valy, double sys){
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

double ABCDSF::GetBinContent4SF(TH1* hist, double valx, double sys){
  double xmin=hist->GetXaxis()->GetXmin();
  double xmax=hist->GetXaxis()->GetXmax();
  if(xmin>=0) valx=fabs(valx);
  if(valx<xmin) valx=xmin+0.001;
  if(valx>xmax) valx=xmax-0.001;
  return hist->GetBinContent(hist->FindBin(valx)) + sys*hist->GetBinError(hist->FindBin(valx));
}

double ABCDSF::GetBinContent4SF(TH1* hist, double valx, double sys, int stat_bin){
  double xmin=hist->GetXaxis()->GetXmin();
  double xmax=hist->GetXaxis()->GetXmax();
  if(xmin>=0) valx=fabs(valx);
  if(valx<xmin) valx=xmin+0.001;
  if(valx>xmax) valx=xmax-0.001;
  int bin_index = hist->FindBin(valx);
  if(stat_bin != bin_index){
    sys = 0.;
  }
  return std::max(1e-10, hist->GetBinContent(bin_index) + sys*hist->GetBinError(bin_index));
}

