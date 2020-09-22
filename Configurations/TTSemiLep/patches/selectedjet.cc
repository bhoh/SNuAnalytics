#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class SelectedJet : public multidraw::TTreeFunction {
public:
  SelectedJet(float ptCut, float absEtaCut);

  char const* getName() const override { return "SelectedJet"; }
  TTreeFunction* clone() const override { return new SelectedJet(ptCut_, absEtaCut_); }
  
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
  FloatArrayReader* Jet_btagDeepB{};


  std::vector<unsigned> selected_jet{};
  void setValues();

  float ptCut_{};
  float absEtaCut_{};


};


void
SelectedJet::beginEvent(long long _iEntry)
{
  setValues();
}


SelectedJet::SelectedJet(float ptCut, float absEtaCut) :
  TTreeFunction(),
  ptCut_{ptCut},
  absEtaCut_{absEtaCut}
{
}


double
SelectedJet::evaluate(unsigned iJ)
{
  return selected_jet[iJ];
}


void
SelectedJet::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nCleanJet, "nCleanJet");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");
  _library.bindBranch(Jet_pt_nom, "Jet_pt_nom");
  _library.bindBranch(Jet_btagDeepB, "Jet_btagDeepB");
}


void
SelectedJet::setValues()
{

  unsigned nCJ{*nCleanJet->Get()};

  selected_jet.clear();

  for(unsigned iCJ{0}; iCJ != nCJ; ++iCJ){

    unsigned OrigIdx = CleanJet_jetIdx->At(iCJ);
    // pT, eta cut
	if(Jet_pt_nom->At(OrigIdx) <= ptCut_ || fabs(CleanJet_eta->At(iCJ)) >= absEtaCut_ ){
	  continue;
	}
	selected_jet.push_back(OrigIdx);

  }

}

