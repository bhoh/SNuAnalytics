/*
  Temporary on-the-fly btag SF calculator for nanoLatino trees nAODv5_2016/2017/2018v5 or earlier.
*/

#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "CondTools/BTau/test/BTagCalibrationStandalone.h"

#include "TSystem.h"

#include <string>
#include <unordered_map>
#include <iostream>
#include <vector>
#include <array>
#include <string>

class BtagSF : public multidraw::TTreeFunction {
public:
  //BtagSF(char const* filename, char const* shift = "central", char const* algo = "deepcsv");
  BtagSF(char const* filename, char const* shift = "central", char const* year = "-1", char const* algo = "deepjet");

  char const* getName() const override { return "BtagSF"; }
  TTreeFunction* clone() const override { return new BtagSF(filename_.c_str(), shiftStr_.c_str(), year_.c_str(), algo_.c_str()); }

  void beginEvent(long long) override;
  int getMultiplicity() override { return 1; }
  unsigned getNdata() override;
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  enum ShiftType {
    kCentral,
    //kJESUp,
    //kJESDown,
    //kJESAbsolute_2018Up,
    //kJESAbsolute_2018Down,
    //kJESBBEC1_2018Up,
    //kJESBBEC1_2018Down,
    //kJESEC2_2018Up,
    //kJESEC2_2018Down,
    //kJESHF_2018Up,
    //kJESHF_2018Down,
    //kJESRelativeSample_2018Up,
    //kJESRelativeSample_2018Down,
    //kJESAbsolute_2017Up,
    //kJESAbsolute_2017Down,
    //kJESBBEC1_2017Up,
    //kJESBBEC1_2017Down,
    //kJESEC2_2017Up,
    //kJESEC2_2017Down,
    //kJESHF_2017Up,
    //kJESHF_2017Down,
    //kJESRelativeSample_2017Up,
    //kJESRelativeSample_2017Down,
    //kJESAbsolute_2016Up,
    //kJESAbsolute_2016Down,
    //kJESBBEC1_2016Up,
    //kJESBBEC1_2016Down,
    //kJESEC2_2016Up,
    //kJESEC2_2016Down,
    //kJESHF_2016Up,
    //kJESHF_2016Down,
    //kJESRelativeSample_2016Up,
    //kJESRelativeSample_2016Down,
    //kJESAbsoluteUp,
    //kJESAbsoluteDown,
    //kJESBBEC1Up,
    //kJESBBEC1Down,
    //kJESEC2Up,
    //kJESEC2Down,
    //kJESFlavorQCDUp,
    //kJESFlavorQCDDown,
    //kJESHFUp,
    //kJESHFDown,
    //kJESRelativeBalUp,
    //kJESRelativeBalDown,

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

  std::string shiftStr_{};
  unsigned shift_{nShiftTypes};

  std::string algo_{};
  std::string year_{};

  static long long currentEntry;
  static UIntValueReader* nCleanJet;
  static FloatArrayReader* CleanJet_pt;
  static FloatArrayReader* CleanJet_eta;
  static IntArrayReader* CleanJet_jetIdx;
  static IntArrayReader* Jet_hadronFlavour;
  static FloatArrayReader* Jet_btag;

  typedef std::array<std::unique_ptr<BTagCalibrationReader>, 3> Readers;
  static Readers readers;
  static std::string readerFilename;
  static std::string readerAlgo;

  static void setValues(long long);

  static std::vector<std::array<double, nShiftTypes>> scalefactors;

  static std::array<std::string, nShiftTypes> shiftNames;
  static std::array<std::vector<unsigned>, 3> relevantShifts;

};

/*static*/
BtagSF::Readers BtagSF::readers{};
std::string BtagSF::readerFilename{};
std::string BtagSF::readerAlgo{};
long long BtagSF::currentEntry{-2};
UIntValueReader* BtagSF::nCleanJet{};
FloatArrayReader* BtagSF::CleanJet_pt{};
FloatArrayReader* BtagSF::CleanJet_eta{};
IntArrayReader* BtagSF::CleanJet_jetIdx{};
IntArrayReader* BtagSF::Jet_hadronFlavour{};
FloatArrayReader* BtagSF::Jet_btag{};
std::vector<std::array<double, BtagSF::nShiftTypes>> BtagSF::scalefactors{};

std::array<std::string, BtagSF::nShiftTypes> BtagSF::shiftNames{{
  "central",
  //"up_jes",
  //"down_jes",
  //"up_jesAbsolute_2018",
  //"down_jesAbsolute_2018",
  //"up_jesBBEC1_2018",
  //"down_jesBBEC1_2018",
  //"up_jesEC2_2018",
  //"down_jesEC2_2018",
  //"up_jesHF_2018",
  //"down_jesHF_2018",
  //"up_jesRelativeSample_2018",
  //"down_jesRelativeSample_2018",
  //"up_jesAbsolute_2017",
  //"down_jesAbsolute_2017",
  //"up_jesBBEC1_2017",
  //"down_jesBBEC1_2017",
  //"up_jesEC2_2017",
  //"down_jesEC2_2017",
  //"up_jesHF_2017",
  //"down_jesHF_2017",
  //"up_jesRelativeSample_2017",
  //"down_jesRelativeSample_2017",
  //"up_jesAbsolute_2016",
  //"down_jesAbsolute_2016",
  //"up_jesBBEC1_2016",
  //"down_jesBBEC1_2016",
  //"up_jesEC2_2016",
  //"down_jesEC2_2016",
  //"up_jesHF_2016",
  //"down_jesHF_2016",
  //"up_jesRelativeSample_2016",
  //"down_jesRelativeSample_2016",
  //"up_jesAbsolute",
  //"down_jesAbsolute",
  //"up_jesBBEC1",
  //"down_jesBBEC1",
  //"up_jesEC2",
  //"down_jesEC2",
  //"up_jesFlavorQCD",
  //"down_jesFlavorQCD",
  //"up_jesHF",
  //"down_jesHF",
  //"up_jesRelativeBal",
  //"down_jesRelativeBal",

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

std::array<std::vector<unsigned>, 3> BtagSF::relevantShifts{};

BtagSF::BtagSF(char const* filename, char const* shift/* = "central"*/, char const* year, char const* algo/* = "deepcsv"*/) :
  TTreeFunction(),
  filename_{filename},
  shiftStr_{shift},
  year_{year},
  shift_{static_cast<unsigned>(std::find(shiftNames.begin(), shiftNames.end(), shiftStr_) - shiftNames.begin())},
  algo_{algo}
{
  if (shift_ == nShiftTypes)
    throw std::invalid_argument("Unknown shift name " + shiftStr_);
}

void
BtagSF::beginEvent(long long _iEntry)
{
  setValues(_iEntry);
}

unsigned
BtagSF::getNdata()
{
  return scalefactors.size();
}

double
BtagSF::evaluate(unsigned iJ)
{
  return scalefactors[iJ][shift_];
}

void
BtagSF::setValues(long long _iEntry)
{
  if (_iEntry == currentEntry)
    return;

  currentEntry = _iEntry;

  scalefactors.clear();

  unsigned nJ{*nCleanJet->Get()};
  scalefactors.resize(nJ);
  
  for (unsigned iJ{0}; iJ != nJ; ++iJ) {
    BTagEntry::JetFlavor jf;
    unsigned origJet_idx = CleanJet_jetIdx->At(iJ);
    switch (Jet_hadronFlavour->At(origJet_idx)) {
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

    double central{readers[jf]->eval_auto_bounds("central", jf, std::abs(CleanJet_eta->At(iJ)), CleanJet_pt->At(iJ), Jet_btag->At(origJet_idx))};

    // set all shifts to central first
    std::fill_n(scalefactors[iJ].begin(), nShiftTypes, central);

    // then fill the actual shift values for relevant types
    for (auto s : relevantShifts[jf]){
      scalefactors[iJ][s] = readers[jf]->eval_auto_bounds(shiftNames[s], jf, std::abs(CleanJet_eta->At(iJ)), CleanJet_pt->At(iJ), Jet_btag->At(origJet_idx));
      //std::cout << "BHO bebug: btagsfpatch 3" << std::endl;

    }
  }
}

void
BtagSF::bindTree_(multidraw::FunctionLibrary& _library)
{
  if (currentEntry == -2) {
    std::cout << "Loading data for " << algo_ << " from " << filename_ << std::endl;

    //relevantShifts[BTagEntry::FLAV_B] = {kJESUp, kJESDown, kLFUp, kLFDown, kHFStats1Up, kHFStats1Down, kHFStats2Up, kHFStats2Down};
    // to avoid : Every otherSysType should only be given once. Duplicate: for kJESUp, kJESDown
    relevantShifts[BTagEntry::FLAV_B] = {kLFUp, kLFDown, kHFStats1Up, kHFStats1Down, kHFStats2Up, kHFStats2Down};
    relevantShifts[BTagEntry::FLAV_C] = {kCFErr1Up, kCFErr1Down, kCFErr2Up, kCFErr2Down};
    //relevantShifts[BTagEntry::FLAV_UDSG] = {kJESUp, kJESDown, kHFUp, kHFDown, kLFStats1Up, kLFStats1Down, kLFStats2Up, kLFStats2Down};
    relevantShifts[BTagEntry::FLAV_UDSG] = {kHFUp, kHFDown, kLFStats1Up, kLFStats1Down, kLFStats2Up, kLFStats2Down};

    std::string year_not_include1;
    std::string year_not_include2;

    if(year_ == "2018"){
      year_not_include1 = "_2017";
      year_not_include2 = "_2016";
    }
    else if(year_ == "2017"){
      year_not_include1 = "_2018";
      year_not_include2 = "_2016";
    }
    else if(year_ == "2016"){
      year_not_include1 = "_2018";
      year_not_include2 = "_2017";
    }


    // add regrouped jec sources
    for(unsigned i(0); i < nShiftTypes; i++){
      // not include not relevant years
      if(shiftNames[i].find("_jes") == std::string::npos || (shiftNames[i].find(year_not_include1) != std::string::npos || shiftNames[i].find(year_not_include2) != std::string::npos)){
        continue;
      }
      relevantShifts[BTagEntry::FLAV_B].push_back(static_cast<ShiftType>(i));
      relevantShifts[BTagEntry::FLAV_UDSG].push_back(static_cast<ShiftType>(i));
      std::cout << "regrouped JEC sources for " << year_ << " : " << shiftNames[i] << std::endl;
    }


    readerFilename = filename_;
    readerAlgo = algo_;

    //std::cout << "BHO bebug: btagsfpatch 0" << std::endl;
    BTagCalibration calib(algo_, filename_);
    //std::cout << "BHO bebug: btagsfpatch 1" << std::endl;
    for (auto flav : {BTagEntry::FLAV_B, BTagEntry::FLAV_C, BTagEntry::FLAV_UDSG}) {
      std::vector<std::string> shiftsToRead;
      for (auto s : relevantShifts[flav])
        shiftsToRead.push_back(shiftNames[s]);
      readers[flav].reset(new BTagCalibrationReader(BTagEntry::OP_RESHAPING, "central", shiftsToRead));
      readers[flav]->load(calib, flav, "iterativefit");
      //std::cout << "BHO bebug: btagsfpatch 2" << std::endl;
    }

    std::cout << "  done." << std::endl;

    currentEntry = -1;
    _library.bindBranch(nCleanJet, "nCleanJet");
    _library.bindBranch(CleanJet_pt, "CleanJet_pt");
    _library.bindBranch(CleanJet_eta, "CleanJet_eta");
    _library.bindBranch(CleanJet_jetIdx, "CleanJet_jetIdx");
    _library.bindBranch(Jet_hadronFlavour, "Jet_hadronFlavour");
    if (algo_ == "deepcsv")
      _library.bindBranch(Jet_btag, "Jet_btagDeepB");
    else if (algo_ == "csvv2")
      _library.bindBranch(Jet_btag, "Jet_btagCSVV2");
    else if (algo_ == "deepjet")
      _library.bindBranch(Jet_btag, "Jet_btagDeepFlavB");

    _library.addDestructorCallback([]() {
        currentEntry = -2;
        nCleanJet = nullptr;
        CleanJet_pt = nullptr;
        CleanJet_eta = nullptr;
        CleanJet_jetIdx = nullptr;
        Jet_hadronFlavour = nullptr;
        Jet_btag = nullptr;
        for (auto& reader : readers)
          reader.reset();
      });
  }
  else if (readerFilename != filename_ || readerAlgo != algo_) {
    std::cerr << "BtagSF module configured for " << readerFilename << " and " << readerAlgo << " already." << std::endl;
    std::cerr << "You cannot create an instance for " << filename_ << " and " << algo_ << " because the module is" << std::endl;
    std::cerr << "written in a hacky way using static global variables." << std::endl;
    throw std::invalid_argument(filename_ + "/" + algo_);
  }
}
