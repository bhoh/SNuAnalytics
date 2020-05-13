// 
// LatinoAnalysis/Gardener/python/variables/melaHighMassKDwCalc.C
//
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include "TMath.h"
#include "TLorentzVector.h"
#include "TLorentzRotation.h"
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include "TString.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include <ZZMatrixElement/MELA/interface/Mela.h>
#include <MelaAnalytics/CandidateLOCaster/interface/MELACandidateRecaster.h>

class MelaHighMassKDwCalc{
  public:
  MelaHighMassKDwCalc(double com, double mpole, double width);
  //MelaHighMassKDwCalc(double com, double mpole, double width, TVar::CandidateDecayMode mode=TVar::CandidateDecay_WW);
  ~MelaHighMassKDwCalc();

  void setCandidateDecayMode(TVar::CandidateDecayMode mode);
  
  void setMelaHiggsMassWidth(double mpole, double wpole);

  void resetMCFM_EWKParameters(double Gf=1.16639E-05, double alphaEW=1./128., double mW=80.399, double mZ=91.1876, double sin2thetaW=0.23119);

  void setIsVbfProd(bool IsVbf){_isVBF = IsVbf; return;};
  float computeDecP( TVar::Process, TVar::MatrixElement, bool resetInputEvent );
  float computeProdP(TVar::Process, TVar::MatrixElement, bool resetInputEvent );
  

  void setupDaughters(
           bool isVBF,
           const std::vector<int>& daughter_ids,   const std::vector<TLorentzVector>& daughter_4Vs,
           const std::vector<int>& associate_ids, const std::vector<TLorentzVector>& associate_4Vs, 
           const std::vector<int>& mother_ids,    const std::vector<TLorentzVector>& mother_4Vs,
	   bool isGenLevel);

  void setupDaughtersNoMom(
           bool isVBF,
           const std::vector<int>& daughter_ids,   const std::vector<TLorentzVector>& daughter_4Vs,
           const std::vector<int>& associate_ids, const std::vector<TLorentzVector>& associate_4Vs, 
	   bool isGenLevel);

  void setCurrentCandidateFromIndex(int idx){_mela->setCurrentCandidateFromIndex( idx ); };
                      
  private:

  bool recast();

  double _com;
  double _mpole;
  double _width;
  MELACandidate* _candModified;

  Mela* _mela;
  MELACandidateRecaster * _recaster;
  SimpleParticleCollection_t* _daughters;
  SimpleParticleCollection_t* _associated;
  SimpleParticleCollection_t* _mothers;
  bool _isVBF;
  bool _isGenLevel;

};

MelaHighMassKDwCalc::MelaHighMassKDwCalc(double com, double mpole, double width ):
_com(com),
_mpole(mpole),
_width(width),
_daughters(new SimpleParticleCollection_t()),
_associated(new SimpleParticleCollection_t()),
_mothers(new SimpleParticleCollection_t())
{
  //TVar::VerbosityLevel verbosity = TVar::DEBUG;
  TVar::VerbosityLevel verbosity = TVar::SILENT;
  //TVar::VerbosityLevel verbosity = TVar::ERROR;
  _mela =  new Mela(com, mpole, verbosity);
  _mela->setCandidateDecayMode(TVar::CandidateDecay_WW);
  // Should be called per-ME -- U. Sarica
  //_mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //_mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //_mela->selfDHzzcoupl[0/1][0][0]=1; // You need this.
  //_mela->selfDHwwcoupl[0/1][0][0]=1; // You need this as well.
  //_mela->selfDHggcoupl[0/1][0][0]=1;
  //Gf=1.16639E-05, alphaEW=1./128., mW=80.399, mZ=91.1876, sin2thetaW=0.23119
  //resetMCFM_EWKParameters(); // No need to call for default arguments; they are already set -- U. Sarica
  //TVar::Production candScheme=TVar::JJVBF;
  //_recaster =  new MELACandidateRecaster(candScheme);
  //_candModified = 0;
}

MelaHighMassKDwCalc::~MelaHighMassKDwCalc(){
  delete _daughters;
  delete _mela;
  delete _associated;
}
void MelaHighMassKDwCalc::setCandidateDecayMode(TVar::CandidateDecayMode mode){
  _mela->setCandidateDecayMode(mode);
}

void MelaHighMassKDwCalc::setMelaHiggsMassWidth(double mpole, double wpole){
  _mela->setMelaHiggsMassWidth(mpole, wpole, 0);
  _mpole = mpole;
  _width = wpole;
}

void MelaHighMassKDwCalc::resetMCFM_EWKParameters(double Gf, double alphaEW, double mW, double mZ, double sin2thetaW){
  _mela->resetMCFM_EWKParameters(Gf, alphaEW, mW, mZ, sin2thetaW);
}

bool MelaHighMassKDwCalc::recast(){
  if (_candModified)
    delete _candModified;
  MELACandidate* melaCand = _mela->getCurrentCandidate();
  _recaster->copyCandidate(melaCand, _candModified);
  _recaster->reduceJJtoQuarks(_candModified);
  _mela->setCurrentCandidate(_candModified);
  if (std::isnan(_candModified->getSortedDaughter(0)->t()))
    return false;
  return true;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

float MelaHighMassKDwCalc::computeDecP(TVar::Process process, TVar::MatrixElement MEgen, bool resetEvt){    

  float me;
  if(process == TVar::bkgWW){
    //cout<<"bkgWW case"<<endl;
    _mela->setProcess(process, MEgen, _isVBF ? TVar::JJEW : TVar::ZZQQB);
    //_mela->setProcess(process, MEgen, _isVBF ? TVar::JJEW : TVar::ZZGG);
  }else{
    _mela->setProcess(process, MEgen, _isVBF ? TVar::JJVBF : TVar::ZZGG);
  }
  //_mela->setProcess(TVar::HSMHiggs, TVar::MCFM, _isVBF ? TVar::JJVBF : TVar::ZZGG);
  // Added here -- U. Sarica
  //cout<<"setting mass and width "<<_mpole<<" "<<_width<<endl;
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //_mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  if (!_isVBF)
    _mela->computeP(me, !_isGenLevel);//useConstant: if isGen=true when calling setInputEvent, this argument will be disregarded. recon useConstant = true
  else
    _mela->computeProdDecP(me, !_isGenLevel); // only with MCFM

  if(resetEvt)
    _mela->resetInputEvent(); // clean up 

  return me;
}


float MelaHighMassKDwCalc::computeProdP(TVar::Process process, TVar::MatrixElement MEgen, bool resetEvt){    

  float me;
  if(process == TVar::bkgWW){
    _mela->setProcess(process, MEgen, _isVBF ? TVar::JJEW : TVar::ZZQQB);
    //_mela->setProcess(process, MEgen, _isVBF ? TVar::JJEW : TVar::ZZGG);
  }else{
    _mela->setProcess(process, MEgen, _isVBF ? TVar::JJVBF : TVar::ZZGG);
  }
  //_mela->setProcess(TVar::HSMHiggs, TVar::MCFM, _isVBF ? TVar::JJVBF : TVar::ZZGG);
  // Added here -- U. Sarica
  //_mela->setMelaHiggsMassWidth(_mpole, _width, 0);
  //_mela->setMelaHiggsMassWidth(125., 4.07e-3, 1);
  //
  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);

  _mela->computeProdP(me, !_isGenLevel);//useConstant: if isGen=true when calling setInputEvent, this argument will be disregarded. recon useConstant = true

  if(resetEvt)
    _mela->resetInputEvent(); // clean up 

  return me;
}

//TODO maybe
//float MelaHighMassKDwCalc::computeBgP(){    
//  float me;
//  _mela->setProcess(TVar::bkgWW_SMHiggs, TVar::MCFM, _isVBF ? TVar::JJEW : TVar::ZZGG);
//  // Added here -- U. Sarica
//  _mela->setMelaHiggsMassWidth(_mpole, _width, 0);
//  //
//  if (!_isVBF)
//    _mela->computeP(me, false);
//  else
//    _mela->computeProdDecP(me, false);
//  
//  _mela->resetInputEvent();  
//  return me;
//}


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void MelaHighMassKDwCalc::setupDaughters(
    bool isVBF,
    const std::vector<int>& daughter_ids,   const std::vector<TLorentzVector>& daughter_4Vs,
    const std::vector<int>& associate_ids, const std::vector<TLorentzVector>& associate_4Vs, 
    const std::vector<int>& mother_ids,    const std::vector<TLorentzVector>& mother_4Vs,
    bool isGenLevel){
                    
 
  _isVBF    = isVBF;
  _isGenLevel = isGenLevel;

  _daughters->clear();
  for (unsigned i(0); i < daughter_4Vs.size(); ++i){
    _daughters->push_back(SimpleParticle_t(daughter_ids[i], daughter_4Vs[i]));
  }
  _associated->clear();
  for (unsigned int i = 0; i < associate_4Vs.size(); ++i){
    _associated->push_back(SimpleParticle_t(associate_ids[i], associate_4Vs[i]));
  }
  _mothers->clear();
  bool hasOneGluon = false;
  if( !mother_4Vs.empty() ){
    for (unsigned int i = 0; i < mother_4Vs.size(); ++i){
      _mothers->push_back(SimpleParticle_t(mother_ids[i], mother_4Vs[i]));
      if (mother_ids[i] == 21)
        hasOneGluon = true;
    }
  }

  if (_candModified != 0){
    delete _candModified;
    _candModified = 0;
  }

  _mela->resetInputEvent(); // clean up
  if( mother_4Vs.empty() ){
    _mela->setInputEvent(_daughters, _associated, 0,        _isGenLevel); 
  }else{
    _mela->setInputEvent(_daughters, _associated, _mothers, _isGenLevel); 
  }

}
void MelaHighMassKDwCalc::setupDaughtersNoMom(
    bool isVBF,
    const std::vector<int>& daughter_ids,  const std::vector<TLorentzVector>& daughter_4Vs,
    const std::vector<int>& associate_ids, const std::vector<TLorentzVector>& associate_4Vs, 
    bool isGenLevel){
  _isVBF    = isVBF;
  _isGenLevel = isGenLevel;

  _daughters->clear();
  //cout<<"daughters ------------"<<endl;
  for (unsigned i(0); i < daughter_4Vs.size(); ++i){
    //cout<<"da_id "<<daughter_ids[i]<<" 4v "<<daughter_4Vs[i].Pt()<<" "<<daughter_4Vs[i].Eta()<<" "<<daughter_4Vs[i].Phi()<<" "<<daughter_4Vs[i].M()<<endl;
    _daughters->push_back(SimpleParticle_t(daughter_ids[i], daughter_4Vs[i]));
  }
  _associated->clear();
  for (unsigned int i = 0; i < associate_4Vs.size(); ++i){
    //cout<<"ass_id "<<associate_ids[i]<<" 4v "<<associate_4Vs[i].Pt()<<" "<<associate_4Vs[i].Eta()<<" "<<associate_4Vs[i].Phi()<<" "<<associate_4Vs[i].M()<<endl;
    _associated->push_back(SimpleParticle_t(associate_ids[i], associate_4Vs[i]));
  }

  _mela->resetInputEvent(); // clean up
  _mela->setInputEvent(_daughters, _associated, 0,        _isGenLevel); 
  //std::vector<int> mother_ids;
  //std::vector<TLorentzVector> mother_4Vs;
  //setupDaughters( isVBF,
//	daughter_ids, daughter_4Vs,
////	associate_ids, associate_4Vs,
//	mother_ids, mother_4Vs,
//	isGenLevel);

}
