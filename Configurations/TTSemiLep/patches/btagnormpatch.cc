/*
  Temporary on-the-fly btag SF calculator for nanoLatino trees nAODv5_2016/2017/2018v5 or earlier.
*/

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "CondTools/BTau/test/BTagCalibrationStandalone.h"

#include "TSystem.h"
#include "TFile.h"
#include "TH2D.h"
#include "TString.h"

#include <string>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <map>
#include <array>
#include <string>

class BTagReshapeNormReader;

class BtagReshapeNorm : public multidraw::TTreeFunction {
public:
  BtagReshapeNorm(char const* filename, char const* samplename,char const* shift = "central", char const* algo = "deepcsv");

  char const* getName() const override { return "BtagReshapeNorm"; }
  TTreeFunction* clone() const override { return new BtagReshapeNorm(filename_.c_str(), samplename_.c_str(), shiftStr_.c_str(), algo_.c_str()); }

  void beginEvent(long long) override;
  int getMultiplicity() override { return 1; }
  unsigned getNdata() override;
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  enum ShiftType {
    kCentral,
    kJESUp,
    kJESDown,
    kHFUp,
    kHFDown,
    kLFUp,
    kLFDown,
    kHFStats1Up,
    kHFStats1Down,
    kHFStats2Up,
    kHFStats2Down,
    kLFStats1Up,
    kLFStats1Down,
    kLFStats2Up,
    kLFStats2Down,
    kCFErr1Up,
    kCFErr1Down,
    kCFErr2Up,
    kCFErr2Down,
    nShiftTypes
  };

  std::string filename_{};
  std::string samplename_{};

  std::string shiftStr_{};
  unsigned shift_{nShiftTypes};

  std::string algo_{};

  static long long currentEntry;
  static UIntValueReader* nJet;
  static FloatArrayReader* Jet_pt;
  static FloatArrayReader* Jet_eta;
  static IntArrayReader* Jet_hadronFlavour;
  //static FloatArrayReader* Jet_btag;

  typedef std::array<std::unique_ptr<BTagReshapeNormReader>, 3> Readers;
  static Readers readers;
  static std::string readerFilename;
  static std::string readerAlgo;

  static void setValues(long long);

  static std::vector<std::array<double, nShiftTypes>> scalefactors;

  static std::array<std::string, nShiftTypes> shiftNames;
  static std::array<std::vector<unsigned>, 3> relevantShifts;
};

class BTagReshapeNormReader{
public:
  BTagReshapeNormReader(std::string central, std::vector<std::string> shifts, std::string samplename);
  ~BTagReshapeNormReader();

  double eval_auto_bounds(std::string syst, int flav, float absEta, float pt);
  void load(std::string fileName, std::string algo, int flav);
protected:
  std::string central_;
  std::string algo_;
  TString samplename_;
  int flav_;
  std::vector<std::string> shifts_;
  TFile *tfile;
  std::map<std::string, TH2D*> mapNorm;
  //
};

/*static*/
BtagReshapeNorm::Readers BtagReshapeNorm::readers{};
std::string BtagReshapeNorm::readerFilename{};
std::string BtagReshapeNorm::readerAlgo{};
long long BtagReshapeNorm::currentEntry{-2};
UIntValueReader* BtagReshapeNorm::nJet{};
FloatArrayReader* BtagReshapeNorm::Jet_pt{};
FloatArrayReader* BtagReshapeNorm::Jet_eta{};
IntArrayReader* BtagReshapeNorm::Jet_hadronFlavour{};
//FloatArrayReader* BtagReshapeNorm::Jet_btag{};
std::vector<std::array<double, BtagReshapeNorm::nShiftTypes>> BtagReshapeNorm::scalefactors{};

std::array<std::string, BtagReshapeNorm::nShiftTypes> BtagReshapeNorm::shiftNames{{
  "central",
  "up_jes",
  "down_jes",
  "up_hf",
  "down_hf",
  "up_lf",
  "down_lf",
  "up_hfstats1",
  "down_hfstats1",
  "up_hfstats2",
  "down_hfstats2",
  "up_lfstats1",
  "down_lfstats1",
  "up_lfstats2",
  "down_lfstats2",
  "up_cferr1",
  "down_cferr1",
  "up_cferr2",
  "down_cferr2"
}};

std::array<std::vector<unsigned>, 3> BtagReshapeNorm::relevantShifts{};

BtagReshapeNorm::BtagReshapeNorm(char const* filename, char const* samplename, char const* shift/* = "central"*/, char const* algo/* = "deepcsv"*/) :
  TTreeFunction(),
  filename_{filename},
  samplename_{samplename},
  shiftStr_{shift},
  shift_{static_cast<unsigned>(std::find(shiftNames.begin(), shiftNames.end(), shiftStr_) - shiftNames.begin())},
  algo_{algo}
{
  if (shift_ == nShiftTypes)
    throw std::invalid_argument("Unknown shift name " + shiftStr_);
}

void
BtagReshapeNorm::beginEvent(long long _iEntry)
{
  setValues(_iEntry);
}

unsigned
BtagReshapeNorm::getNdata()
{
  return scalefactors.size();
}

double
BtagReshapeNorm::evaluate(unsigned iJ)
{
  return scalefactors[iJ][shift_];
}

void
BtagReshapeNorm::setValues(long long _iEntry)
{
  if (_iEntry == currentEntry)
    return;

  currentEntry = _iEntry;

  scalefactors.clear();

  unsigned nJ{*nJet->Get()};
  scalefactors.resize(nJ);
  
  for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    BTagEntry::JetFlavor jf;
  
    switch (Jet_hadronFlavour->At(iJ)) {
    case 5:
      jf = BTagEntry::FLAV_B; // = 0
      break;
    case 4:
      jf = BTagEntry::FLAV_C; // = 1
      break;
    default:
      jf = BTagEntry::FLAV_UDSG; // = 2
      break;
    }

    double central{readers[jf]->eval_auto_bounds("central", jf, std::abs(Jet_eta->At(iJ)), Jet_pt->At(iJ))};

    // set all shifts to central first
    std::fill_n(scalefactors[iJ].begin(), nShiftTypes, central);

    // then fill the actual shift values for relevant types
    for (auto s : relevantShifts[jf])
      scalefactors[iJ][s] = readers[jf]->eval_auto_bounds(shiftNames[s], jf, std::abs(Jet_eta->At(iJ)), Jet_pt->At(iJ));
  }
}

void
BtagReshapeNorm::bindTree_(multidraw::FunctionLibrary& _library)
{
  if (currentEntry == -2) {
    std::cout << "Loading data for " << algo_ << " from " << filename_ << std::endl;

    relevantShifts[BTagEntry::FLAV_B] = {kJESUp, kJESDown, kLFUp, kLFDown, kHFStats1Up, kHFStats1Down, kHFStats2Up, kHFStats2Down};
    relevantShifts[BTagEntry::FLAV_C] = {kCFErr1Up, kCFErr1Down, kCFErr2Up, kCFErr2Down};
    relevantShifts[BTagEntry::FLAV_UDSG] = {kJESUp, kJESDown, kHFUp, kHFDown, kLFStats1Up, kLFStats1Down, kLFStats2Up, kLFStats2Down};

    readerFilename = filename_;
    readerAlgo = algo_;

    for (auto flav : {BTagEntry::FLAV_B, BTagEntry::FLAV_C, BTagEntry::FLAV_UDSG}) {
      std::vector<std::string> shiftsToRead;
      for (auto s : relevantShifts[flav])
        shiftsToRead.push_back(shiftNames[s]);
      readers[flav].reset(new BTagReshapeNormReader("central", shiftsToRead, samplename_));
      readers[flav]->load(filename_, algo_, flav);
    }

    std::cout << "  done." << std::endl;

    currentEntry = -1;
    _library.bindBranch(nJet, "nJet");
    _library.bindBranch(Jet_pt, "Jet_pt");
    _library.bindBranch(Jet_eta, "Jet_eta");
    _library.bindBranch(Jet_hadronFlavour, "Jet_hadronFlavour");
    //if (algo_ == "deepcsv")
    //  _library.bindBranch(Jet_btag, "Jet_btagDeepB");
    //else if (algo_ == "csvv2")
    //  _library.bindBranch(Jet_btag, "Jet_btagCSVV2");
    //else if (algo_ == "deepjet")
    //  _library.bindBranch(Jet_btag, "Jet_btagDeepFlavB");

    _library.addDestructorCallback([]() {
        currentEntry = -2;
        nJet = nullptr;
        Jet_pt = nullptr;
        Jet_eta = nullptr;
        Jet_hadronFlavour = nullptr;
        //Jet_btag = nullptr;
        for (auto& reader : readers)
          reader.reset();
      });
  }
  else if (readerFilename != filename_ || readerAlgo != algo_) {
    std::cerr << "BtagReshapeNorm module configured for " << readerFilename << " and " << readerAlgo << " already." << std::endl;
    std::cerr << "You cannot create an instance for " << filename_ << " and " << algo_ << " because the module is" << std::endl;
    std::cerr << "written in a hacky way using static global variables." << std::endl;
    throw std::invalid_argument(filename_ + "/" + algo_);
  }
}


/////////////////////////////////////////////////////////////////////


BTagReshapeNormReader::BTagReshapeNormReader(std::string central, std::vector<std::string> shifts, std::string samplename):
  central_{central},
  shifts_{shifts},
  samplename_{samplename}
  
{
  //
}


BTagReshapeNormReader::~BTagReshapeNormReader()
{
  for(auto &norm : mapNorm){
    delete norm.second;
  }
  delete tfile;
}


double BTagReshapeNormReader::eval_auto_bounds(std::string syst, int flav, float absEta, float pt)
{
  //only central value avaliable
  double out=1.;
  TH2D* hist2D=NULL;
  if(flav == BTagEntry::FLAV_B){
    hist2D = mapNorm["b"];
  }
  else if(flav == BTagEntry::FLAV_C){
    hist2D = mapNorm["c"];
  }
  else if(flav == BTagEntry::FLAV_UDSG){
    hist2D = mapNorm["udsg"];
  }
  if(!hist2D){
    std::cout << "BTagReshapeNormReader::eval_auto_bounds :  hist2D is NULL pointer " << std::endl;
    exit(EXIT_FAILURE);
  }
  int binx=-1, biny=-1;
  if(pt>=20. && pt<1000. && absEta<2.5){
    binx = hist2D->GetXaxis()->FindBin(pt);
    biny = hist2D->GetYaxis()->FindBin(absEta);
    out = hist2D->GetBinContent(binx,biny);

  }
  //std::cout << "pt : " << pt << std::endl;
  //std::cout << "ptbin : " << binx << std::endl;
  //std::cout << "absEta : " << absEta << std::endl;
  //std::cout << "absEtabin : " << biny << std::endl;
  //std::cout << "flav : " << flav << std::endl;
  //std::cout << "out : " << out << std::endl;
  return out;
}


void BTagReshapeNormReader::load(std::string fileName, std::string algo, int flav)
{
  std::cout << "load fileName : " << fileName << std::endl;
  std::cout << "         algo : " << algo << std::endl;
  std::cout << "         flav : " << flav << std::endl;
  tfile = new TFile(fileName.c_str(),"READ");
  if(flav == BTagEntry::FLAV_B){
    mapNorm["b"] = (TH2D*)(tfile->Get(samplename_+"/b"));
  }
  else if(flav == BTagEntry::FLAV_C){
    mapNorm["c"] = (TH2D*)(tfile->Get(samplename_+"/c"));
  }
  else if(flav == BTagEntry::FLAV_UDSG){
    mapNorm["udsg"] = (TH2D*)(tfile->Get(samplename_+"/udsg"));
  }
  return;
}


