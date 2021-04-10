#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"

#include <iostream>

class TMVAPyKerasDNN : public multidraw::TTreeFunction {
public:
  TMVAPyKerasDNN(std::string fileName);

  char const* getName() const override { return "TMVAPyKerasDNN"; }
  TTreeFunction* clone() const override { return new TMVAPyKerasDNN(std::string fileName); }
  
  void beginEvent(long long) override;
  unsigned getNdata() override { return 1; }
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


  float DNNscore{};
  void setValues();

  std::unique_ptr<ReadDNN> dnn; 
  void readVariableList(std::string fileName);
  std::vector<std::pair<std::string, std::string>> variables{};
  std::map<std::string, FloatValueReader*> mapVariables{};


  std::string fileName_;

};


void
TMVAPyKerasDNN::beginEvent(long long _iEntry)
{
  setValues();
}


TMVAPyKerasDNN::TMVAPyKerasDNN(std::string fileName) :
  TTreeFunction(),
  fileName_{fileName}
{
  readVariableList(fileName);
  initDNN();
}


double
TMVAPyKerasDNN::evaluate(unsigned iJ)
{
  return DNNscore;
}


void
TMVAPyKerasDNN::bindTree_(multidraw::FunctionLibrary& _library)
{

  for(auto &pair : variables){
    if(pair.second == '-'){
      _library.bindBranch(&(mapVariables[pair.first]), pair.first);
    }
    else{ // read aliase
      _library.bindBranch(&(mapVariables[pair.second]), pair.second);
    }
  }
    
  //_library.bindBranch(nCleanJet, "nCleanJet");
  //_library.bindBranch(CleanJet_pt, "CleanJet_pt");
  //_library.bindBranch(CleanJet_eta, "CleanJet_eta");
  //_library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");
  //_library.bindBranch(Jet_pt_nom, "Jet_pt_nom");
  //_library.bindBranch(Jet_btagDeepB, "Jet_btagDeepB");
}


void
TMVAPyKerasDNN::initDNN()
{
  std::vector<std::string> inputVariables;
  for(auto &pair : variables){
    inputVariables.push_back(pair.first)
  }
  dnn = new ReadDNN(inputVariables);
}


void
TMVAPyKerasDNN::setValues()
{
  std::vector<double> inputValues;
  // load ReadDNN from shared obj.
  for(auto &pair : variables){
    if(pair.second == '-'){
      inputValues.push_back(mapVariables[pair.first]);
    }
    else{ // read aliase
      inputValues.push_back(mapVariables[pair.second]);
    }
  }
  DNNscore = dnn->GetMvaValue(inputValues);
}


void
TMVAPyKerasDNN::readVariableList(std::string fileName)
{
    variables.clear();
    std::ifstream inFile(fileName);
    
    std::string variable, aliase;
    while(inFile >> variable >> aliase){
      std::cout << variable << " "<< aliase << std::endl;
      variables.emplace_back(variable, aliase);
    }
}


