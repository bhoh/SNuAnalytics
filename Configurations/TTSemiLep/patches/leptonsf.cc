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

class LeptonSF : public multidraw::TTreeFunction {
public:
  LeptonSF(char const* fileName, char const* histName);

  char const* getName() const override { return "LeptonSF"; }
  TTreeFunction* clone() const override { return new LeptonSF(fileName_.Data(), histName_.Data()); }
  
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
  double GetBinContent4SF(TH2* hist, double valx, double valy, double sys);

  TString fileName_{};
  TString histName_{};

  TFile* rootFile{};
  TH2F* histLeptonSF{};


};


void
LeptonSF::beginEvent(long long _iEntry)
{
  setValues();
}


LeptonSF::LeptonSF(char const* fileName, char const* histName) :
  TTreeFunction(),
  fileName_{fileName},
  histName_{histName}
{
  // read SF, from txt file.
  // list up lepton SFs (RECO, ID, Trigger) on the txt file.
  // read SFs in map<TString, TH2D>

  rootFile = new TFile(fileName_);
  histLeptonSF = (TH2F*)rootFile->Get(histName_);
}


double
LeptonSF::evaluate(unsigned iJ)
{
  // leptonSF[0] : central, leptonSF[1] : up, leptonSF[2] : down
  return leptonSF[iJ];
}


void
LeptonSF::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_electronIdx, "Lepton_electronIdx");
  _library.bindBranch(Electron_deltaEtaSC, "Electron_deltaEtaSC");
}


void
LeptonSF::setValues()
{

  leptonSF.clear();
  double lepEta{Lepton_eta->At(0)}; //TODO will use scEta for electron
  double lepPt{Lepton_pt->At(0)};
  leptonSF.push_back(this->GetBinContent4SF(histLeptonSF, lepEta, lepPt, 0));
  //TODO push back up/down systematic

}


double LeptonSF::GetBinContent4SF(TH2* hist, double valx, double valy, double sys){
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
    
double LeptonSF::GetBinContent4SF(TH1* hist, double valx, double sys){
  double xmin=hist->GetXaxis()->GetXmin();
  double xmax=hist->GetXaxis()->GetXmax();
  if(xmin>=0) valx=fabs(valx);
  if(valx<xmin) valx=xmin+0.001;
  if(valx>xmax) valx=xmax-0.001;
  return hist->GetBinContent(hist->FindBin(valx)) + sys*hist->GetBinError(hist->FindBin(valx));
}

