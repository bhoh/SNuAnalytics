#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class SelectedBJet : public multidraw::TTreeFunction {
public:
  SelectedBJet();
  SelectedBJet(float ptCut, float absEtaCut, float csvCut, bool leading4jets);

  char const* getName() const override { return "SelectedBJet"; }
  TTreeFunction* clone() const override { return new SelectedBJet(ptCut_, absEtaCut_, csvCut_, leading4jets_); }
  
  void beginEvent(long long) override;
  unsigned getNdata() override { return selected_jet.size(); }
  int getMultiplicity() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  
  UIntValueReader* nCleanJet{};
  FloatArrayReader* CleanJet_pt{};
  FloatArrayReader* CleanJet_eta{};
  IntArrayReader* CleanJet_jetIdx{};

  FloatArrayReader* Jet_pt_nom{};
  static FloatArrayReader* Jet_btagDeepFlavB;


  std::vector<unsigned> selected_jet{};
  void setValues();

  float ptCut_{};
  float absEtaCut_{};
  float csvCut_{};
  bool  leading4jets_{};

  static bool bdisc_comparing(unsigned i, unsigned j);
};

FloatArrayReader* SelectedBJet::Jet_btagDeepFlavB{};

void
SelectedBJet::beginEvent(long long _iEntry)
{
  setValues();
}


SelectedBJet::SelectedBJet(float ptCut, float absEtaCut, float csvCut, bool leading4jets) :
  TTreeFunction(),
  ptCut_{ptCut},
  absEtaCut_{absEtaCut},
  csvCut_{csvCut},
  leading4jets_{leading4jets}
{
}


double
SelectedBJet::evaluate(unsigned iJ)
{
  return selected_jet[iJ];
}


void
SelectedBJet::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nCleanJet, "nCleanJet");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");
  _library.bindBranch(Jet_pt_nom, "Jet_pt_nom");
  _library.bindBranch(Jet_btagDeepFlavB, "Jet_btagDeepFlavB");
}


void
SelectedBJet::setValues()
{

  unsigned nCJ{*nCleanJet->Get()};

  selected_jet.clear();

  for(unsigned iCJ{0}; iCJ != nCJ; ++iCJ){

    unsigned OrigIdx = CleanJet_jetIdx->At(iCJ);
    // pT, eta, cut
	if(Jet_pt_nom->At(OrigIdx) <= ptCut_ ||
       fabs(CleanJet_eta->At(iCJ)) >= absEtaCut_
      ){
	  continue;
	}
	selected_jet.push_back(OrigIdx);

  }

  if(leading4jets_ && ( selected_jet.size() > 3) ){
    // assume that jet vectore is ordered in pT
    std::sort(selected_jet.begin(),selected_jet.begin()+4,bdisc_comparing);
  }
  else{
    std::sort(selected_jet.begin(),selected_jet.end(),bdisc_comparing);
  }

}

bool SelectedBJet::bdisc_comparing(unsigned i, unsigned j){
 return Jet_btagDeepFlavB->At(i) > Jet_btagDeepFlavB->At(j);
}
