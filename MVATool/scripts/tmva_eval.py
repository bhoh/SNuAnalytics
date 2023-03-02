import ROOT
from ROOT import TMVA, TFile, TString, TH1D, TCanvas
from array import array

from variables import *

# example
# https://root.cern.ch/doc/master/ApplicationClassificationKeras_8py.html

TMVA.PyMethodBase.PyInitialize()

branches = {}
def addVariables(tmvaReader):
    for branchName in variables:
        branches[branchName] = array('f', [-999])
        tmvaReader.AddVariable(branchName, branches[branchName])


def setBranchAddress(tmvaTree):
    for branchName in variables:
        tmvaTree.SetBranchAddress(branchName, branches[branchName])

    if "XSWeight" not in branches:
        branches["XSWeight"] = array('f', [-999])
    tmvaTree.SetBranchAddress("XSWeight", branches["XSWeight"])


def bookMethods(tmvaReader):
    xmlPath_DNN = 'TMVAClassification_CHToCB_year_comb/weights_CHToCB_year_comb/TMVAClassification_DNN.weights.xml'
    xmlPath_BDT = 'TMVAClassification_CHToCB_year_comb/weights_CHToCB_year_comb/TMVAClassification_BDT.weights.xml'
    tmvaReader.BookMVA('PyKeras::DNN',TString(xmlPath_DNN))
    tmvaReader.BookMVA('BDT::BDT',TString(xmlPath_BDT))


def normWeights(mvaWeights, scale=1.):
    return map(lambda w: w*scale, mvaWeights)


def fillMVAvector(ttree, mvaMethod, variable="random_label"):
    mvaValues  = []
    mvaWeights = []

    if variable=="reco_mass_hish":
      mass_label = lambda : min( max(75., ttree.fitted_dijet_M_high_nom), 160.)
    elif variable=="reco_mass_low":
      mass_label = lambda : min( max(75., ttree.fitted_dijet_M_nom), 160.)
    elif variable=="fixed_label_high":
      mass_label = lambda : 150.
    elif variable=="fixed_label_low":
      mass_label = lambda : 110.
    else:
      mass_label = None

    entries = ttree.GetEntries()
    for i in range(entries):
      ttree.GetEntry(i)
      if mass_label != None:
        branches["mass_label"][0] = mass_label()
      mvaValue = reader.EvaluateMVA(mvaMethod)
      mvaValues.append(mvaValue)
      mvaWeights.append(branches["XSWeight"][0])

    #normalize weight by sample
    sumW = float(sum(mvaWeights))
    mvaWeights = normWeights(mvaWeights, 1./sumW)

    return mvaValues, mvaWeights


def getMVApdf(histName, mva_values_sig, mva_weights_sig, binning=(200, 0.0, 1.0)):

    if type(binning) == tuple:
        pdf = TH1D(histName, histName, *binning)
    elif type(binning) == list:
        bin_array = array('f', binning)
        pdf = TH1D(histName, histName, bin_array.size, bin_array)

    for i, val in enumerate(mva_values_sig):
        pdf.Fill(val, mva_weights_sig[i])

    return pdf


def getEff(hist):
    hist_cloned = hist.Clone(hist.GetName() + "_cloned")
    integral = hist_cloned.Integral()
    hist_cloned.Scale(1./integral)

    eff  = hist_cloned.GetCumulative(ROOT.kFALSE)

    return eff


# load sig. and bkg. trees.


# assign branches

#book method
# case 1) 1 PyKeras, 2 BDT
# case 2) multiple method with different hyperparameters


# eval mva values
reader = TMVA.Reader("Color:!Silent")
addVariables(reader)
bookMethods(reader)


mva_values_dict = {}
mva_weights_dict = {}

file_names = {}
#file_names = {
#        ('2016', 'TTLJ_powheg', 'Train') : '/cms_scratch/bhoh/mva_TTLJ_powheg_2016_Train.root',
#        ('2016', 'TTLJ_powheg', 'Test') : '/cms_scratch/bhoh/mva_TTLJ_powheg_2016_Test.root',
#        ('2016', 'TTLJ_powheg', 'Val') : '/cms_scratch/bhoh/mva_TTLJ_powheg_2016_Val.root',
#        
#        
#        }

#for year in ['2016HIPM', '2016noHIPM', '2017', '2018']:
for year in ['2017']:
    for sample in ['TTLJ_powheg', 'CHToCB_M075', 'CHToCB_M080', 'CHToCB_M085', 'CHToCB_M090', 'CHToCB_M100', 'CHToCB_M110', 'CHToCB_M120', 'CHToCB_M130', 'CHToCB_M140', 'CHToCB_M150', 'CHToCB_M160']:
        for label in ['Train', 'Test', 'Val']:
            key = (year, sample, label)
            inputFileName = "/cms_scratch/bhoh/mva_{}_{}_{}.root".format(sample,year,label)
            file_names[key] = inputFileName

#mva_pdf_dict   = {}
#for mva_model in ['DNN']:
#    for key in fine_names:
#        for variable in ['random_label', 'fixed_label_high', 'fixed_label_low', 'reco_mass_high', 'reco_mass_low']:
#            for binning in ['finebin','twobin']:
#                mva_pdf_dict[mva_model, *key, variable, binning] = 


for key in file_names:
    year, sample, label = key
    outFileName      = "/cms_scratch/bhoh/mva_%s_%s.root"%(sample,year)
    outFileNameTrain = "/cms_scratch/bhoh/mva_%s_%s_Train.root"%(sample,year)
    outFileNameTest = "/cms_scratch/bhoh/mva_%s_%s_Test.root"%(sample,year)
    print(outFileNameTrain, file_names[key])
    print(outFileNameTest, file_names[key])

    data_Train = TFile.Open(outFileNameTrain)
    tree_Train = data_Train.Get("Events")
    data_Test = TFile.Open(outFileNameTest)
    tree_Test = data_Test.Get("Events")

    setBranchAddress(tree_Train)
    setBranchAddress(tree_Test)


    mva_values_train, mva_weights_train = fillMVAvector(tree_Train, 'PyKeras::DNN', True)
    mva_values_test, mva_weights_test = fillMVAvector(tree_Test,  'PyKeras::DNN', True)

    mva_values_dict[year, sample+"_Train"]  = mva_values_train
    mva_weights_dict[year, sample+"_Train"] = mva_weights_train
    mva_values_dict[year, sample+"_Test"]  = mva_values_test
    mva_weights_dict[year, sample+"_Test"] = mva_weights_test


#mva_values_bkg_train  = mva_values_dict ["2016", "TTLJ_powheg_Train"]
#mva_weights_bkg_train = mva_weights_dict["2016", "TTLJ_powheg_Train"]
#
#mva_values_bkg_test  = mva_values_dict ["2016", "TTLJ_powheg_Test"]
#mva_weights_bkg_test = mva_weights_dict["2016", "TTLJ_powheg_Test"]
#
#mva_values_sig_train  = mva_values_dict ["2016", "CHToCB_M140_Train"]
#mva_weights_sig_train = mva_weights_dict["2016", "CHToCB_M140_Train"]
#mva_values_sig_train  .extend( mva_values_dict ["2016", "CHToCB_M150_Train"] )
#mva_weights_sig_train .extend( mva_weights_dict["2016", "CHToCB_M150_Train"] )
#mva_values_sig_train  .extend( mva_values_dict ["2016", "CHToCB_M160_Train"] )
#mva_weights_sig_train .extend( mva_weights_dict["2016", "CHToCB_M160_Train"] )
#
#mva_values_sig_test  = mva_values_dict ["2016", "CHToCB_M140_Test"]
#mva_weights_sig_test = mva_weights_dict["2016", "CHToCB_M140_Test"]
#mva_values_sig_test  .extend( mva_values_dict ["2016", "CHToCB_M150_Test"] )
#mva_weights_sig_test .extend( mva_weights_dict["2016", "CHToCB_M150_Test"] )
#mva_values_sig_test  .extend( mva_values_dict ["2016", "CHToCB_M160_Test"] )
#mva_weights_sig_test .extend( mva_weights_dict["2016", "CHToCB_M160_Test"] )




#normalize by category
#default xsec in signal 364.35 pb
training_fraction = None
n_bkgs   = 1000000.
num_mass = 3.
br = 0.001
mva_weights_bkg = normWeights(mva_weights_bkg, n_bkgs * (1-br) * (1-br))
mva_weights_sig = normWeights(mva_weights_sig, n_bkgs * 2 * br * (1-br) / num_mass)

mvaBpdf = getMVApdf("mvaB", mva_values_bkg, mva_weights_bkg)
mvaSpdf = getMVApdf("mvaS", mva_values_sig, mva_weights_sig)

mvaBeff = getEff(mvaBpdf)
mvaSeff = getEff(mvaSpdf)

rocCalc  = TMVA.ROCCalc.ROCCalc(mvaSpdf, mvaBpdf)
h_roc            = rocCalc.GetROC()
ref_cut          = rocCalc.GetSignalReferenceCut()


nStot, nBtot     = int(sum(mva_weights_sig)), int(sum(mva_weights_bkg))
print(nStot, nBtot)
h_significance   = rocCalc.GetSignificance(nStot, nBtot)  # S / sqrt(S+B)
h_purity         = rocCalc.GetPurity(nStot, nBtot)        # S / (S+B)

best_sig_cut     =  h_significance.GetMaximumBin() * h_significance.GetBinWidth(1)
best_sig_Beff    =  mvaBeff.GetBinContent(h_significance.GetMaximumBin())
best_sig_Seff    =  mvaSeff.GetBinContent(h_significance.GetMaximumBin())

mvaBpdf_2bin = getMVApdf("mvaB", mva_values_bkg, mva_weights_bkg, [0., best_sig_cut, 1.])
mvaSpdf_2bin = getMVApdf("mvaS", mva_values_sig, mva_weights_sig, [0., best_sig_cut, 1.])



auc = rocCalc.GetROCIntegral()
print("AUC:             " + str(auc)            )
print("ref. cut:        " + str(ref_cut)        )
print("best sig. cut:   " + str(best_sig_cut)   )
print("best sig. Seff:  " + str(best_sig_Seff))
print("best sig. Beff:  " + str(best_sig_Beff))


c1 = TCanvas("c1","c1", 800, 600)
c2 = TCanvas("c2","c2", 800, 600)
c3 = TCanvas("c3","c3", 800, 600)

c1.cd()
h_roc.Draw()


c2.cd()
# set 0 for last bin
h_significance.SetBinContent( h_significance.GetNbinsX(), 0.)
h_significance.Draw()

c3.cd()
# set 0 for last bin
h_purity.SetBinContent( h_purity.GetNbinsX(), 0.)
h_purity.Draw()



#TMVA::ROCCurve::ROCCurve( const std::vector<Float_t>&  mvaSignal,
#                          const std::vector<Float_t>&  mvaBackground,
#                          const std::vector<Float_t>&  mvaSignalWeights,
#                          const std::vector<Float_t>&  mvaBackgroundWeights 
#                        )


