#hadd.root:/sng_4j_A_muCH_2b/EleSCEta
#hadd.root:/sng_4j_A_muCH_2b/MuonEta
#hadd.root:/sng_4j_A_muCH_2b/Event
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_down_type_jet_b_tagged
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high_down_type_jet_b_tagged
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high_had_top_pt_gt_120_down_type_jet_b_tagged
#hadd.root:/sng_4j_A_muCH_2b/fitted_dijet_M_high_had_top_pt_gt_80_down_type_jet_b_tagged
#QCD_MU, QCD_EM, QCD_bcToE
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os,sys
import numpy as np
import copy


usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)

parser.add_option('--tag'                , dest='tag'               , help='Tag used for the shape file name'           , default=None)
parser.add_option('--shapeFile'                , dest='shapeFile'               , help='original shape file path'           , default=None)
      
# read default parsing options as well
hwwtools.addOptions(parser)
hwwtools.loadOptDefaults(parser)
(opt, args) = parser.parse_args()

sys.argv.append( '-b' )
#ROOT.gROOT.SetBatch()


print " configuration file = ", opt.pycfg

if not opt.debug:
  pass
elif opt.debug == 2:
  print 'Logging level set to DEBUG (%d)' % opt.debug
  logging.basicConfig( level=logging.DEBUG )
elif opt.debug == 1:
  print 'Logging level set to INFO (%d)' % opt.debug
  logging.basicConfig( level=logging.INFO )

ROOT.TH1.SetDefaultSumw2(True)
  
## load the samples
#samples = {}
#if os.path.exists(opt.samplesFile) :
#  handle = open(opt.samplesFile,'r')
#  exec(handle)
#  handle.close()

## load the cuts
cuts = {}
if os.path.exists(opt.cutsFile) :
  handle = open(opt.cutsFile,'r')
  exec(handle)
  handle.close()

## load the variables
variables = {}
if os.path.exists(opt.variablesFile) :
  handle = open(opt.variablesFile,'r')
  exec(handle)
  handle.close()

###
fileName='rootFile_%s/hadd.root'%opt.tag

outFileName = 'rootFile_%s/ABCD_data_driven_shape.root'%opt.tag
outFile =  ROOT.TFile(outFileName,'RECREATE')


#histo_DATA
#histo_DY
#histo_ST
#histo_TTLJ_jj
#histo_TTLJ_cc
#histo_TTLJ_bj
#histo_TTLJ_bb
#histo_TTLL_jj
#histo_TTLL_cc
#histo_TTLL_bj
#histo_TTLL_bb
#histo_TTWjets
#histo_TTZjets
#histo_Wjets
#histo_WW
#histo_WZ
#histo_ZZ     

samples = [
         'histo_DATA',
         'histo_DY',
         'histo_ST',
         'histo_TTLJ_jj',
         'histo_TTLJ_cc',
         'histo_TTLJ_bj',
         'histo_TTLJ_bb',
         'histo_TTLL_jj',
         'histo_TTLL_cc',
         'histo_TTLL_bj',
         'histo_TTLL_bb',
         'histo_TTWjets',
         'histo_TTZjets',
         'histo_Wjets',
         'histo_WW',
         'histo_WZ',
         'histo_ZZ',
     ]

input_dict = {
  '' : {
    'input'    : fileName,
    'chennels' : {}
    }
  }

for cut in cuts:
  if 'iso' in cut:
    continue
  cutName = cut
  fullCutNames = []
  if 'categories' in cuts[cut]:
    for scut in cuts[cut]['categories']:
      fullCutNames.append((cutName,scut))
  else:
    fullCutNames.append((cutName,))

  for fullCutName_tuple in fullCutNames:
    ## fill cut and sample name string
    if len(fullCutName_tuple)==1:
      fullCutName = fullCutName_tuple[0]
    elif len(fullCutName_tuple)==2:
      fullCutName = fullCutName_tuple[0] + "_" + fullCutName_tuple[1]
    ##
    input_dict['']['chennels'][fullCutName] = {}
    for variable in variables:
      if 'cuts' in variables[variable]:
        if fullCutName_tuple[0] in variables[variable]['cuts']:
          input_dict['']['chennels'][fullCutName][variable] = copy.deepcopy(samples)
        else:
          pass
      else:
        input_dict['']['chennels'][fullCutName][variable] = copy.deepcopy(samples)




nuisances_btag = [
        'btag_lfUp',
        'btag_lfDown',
        'btag_hfUp',
        'btag_hfDown',
        'btag_hfstats1_2016Up',
        'btag_hfstats1_2016Down',
        'btag_hfstats2_2016Up',
        'btag_hfstats2_2016Down',
        'btag_lfstats1_2016Up',
        'btag_lfstats1_2016Down',
        'btag_lfstats2_2016Up',
        'btag_lfstats2_2016Down',
        'btag_cferr1Up',
        'btag_cferr1Down',
        'btag_cferr2Up',
        'btag_cferr2Down',
        ]

nuisances_tt_hf = [
        'ttbbUp',
        'ttbbDown',
        'ttccUp',
        'ttccDown',
        ]

nuisances_others = [
        'ttXsecUp',
        'ttXsecDown',
        'isoUp',
        'isoDown', #dumy
        'binningVarUp',
        'binningVarDown', #dumy
        ]
hist_path_dict = {}
hist_path_dict['mu_2b']  = 'sng_4j_muCH_2b/MuonEta/histo_TF_data_driven'
hist_path_dict['mu_3b']  = 'sng_4j_muCH_3b/MuonEta/histo_TF_data_driven'
hist_path_dict['ele_2b'] = 'sng_4j_eleCH_2b/EleSCEta/histo_TF_data_driven'
hist_path_dict['ele_3b'] = 'sng_4j_eleCH_3b/EleSCEta/histo_TF_data_driven'
for syst in ['mu_2b', 'mu_3b','ele_2b','ele_3b']:
  # i th bin syst
  hist_source = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/ABCD_SF/ABCD_data_driven_SF_2016.root' % os.getenv('CMSSW_BASE')
  f = ROOT.TFile(hist_source,"READ")
  h = f.Get(hist_path_dict[syst])
  Nbins = h.GetNbinsX()
  for i in range(1,Nbins+1):
    name = "ABCD_SF_%s_bins%d_2016"%(syst,int(i))
    nuisances_others.append(name+"Up")
    nuisances_others.append(name+"Down")

#nuisances = nuisances_btag + nuisances_tt_hf + nuisances_others
nuisances = [
            'isoUp',
            'isoDown', #dumy
        ]

for nuisance in nuisances:
  input_dict[nuisance] = copy.deepcopy(input_dict[''])

  if 'iso' in nuisance:
    #rename ch
    for ch in input_dict[nuisance]['chennels']:
      if 'iso' in ch:
        continue
      ch_new = ch.replace("_D_","_%s_D_"%nuisance)
      input_dict[nuisance]['chennels'][ch_new] = input_dict[nuisance]['chennels'].pop(ch)

  for ch in input_dict[nuisance]['chennels']:
    for var in input_dict[nuisance]['chennels'][ch]:
      for i, histo_name in enumerate(input_dict[nuisance]['chennels'][ch][var]):
        histo_name_nuis = histo_name + '_' + nuisance
        input_dict[nuisance]['chennels'][ch][var][i] = histo_name_nuis

from pprint import pprint
pprint(input_dict)

#bins = {
#   'sng_4j_eleCH_2b' : np.array([-2.5, -1.479, 0, 1.479, 2.5]),
#   'sng_4j_eleCH_3b' : np.array([-2.5, 2.5]),
#   'sng_4j_muCH_2b'  : np.array([-2.4, -1.2, -0.9, 0, 0.9, 1.2, 2.4]),
#   'sng_4j_muCH_3b'  : np.array([-2.4, -0.9, 0, 0.9, 2.4]),
#}

def GetHisto(f_, ch, var, histoNameList, rebin):

  histo_rebinned = None
  for histoName in histoNameList:
    print('%s/%s/%s'%(ch,var,histoName))
    histo_ = f_.Get('%s/%s/%s'%(ch,var,histoName))
    histo = histo_.Clone('_'.join([ch,var,histoName]))

    if histo_rebinned == None:
      if 'histo_DATA' not in histoName:
        raise Exception('first entry should be histo_DATA')
      histo_rebinned = histo.Clone()
    else:
      if 'histo_DATA' in histoName:
        raise Exception('histo_DATA is entered for the negative summation')
      # scale ttbar samples
      if 'histo_TTLL_' in histoName or 'histo_TTLJ_' in histoName:
        if '_bb' in histoName or '_bj' in histoName:
          if '_ttbbUp' in histoName:
            scale = 1.5
          elif '_ttbbDown' in histoName:
            scale = 1.
          else:
            scale = 1.2
        elif '_cc' in histoName:
          if '_ttccUp' in histoName:
            scale = 1.2
          elif '_ttccDown' in histoName:
            scale = 1./1.2
          else:
            scale = 1.0
        elif '_jj' in histoName:
          if '_ttbbUp' in histoName:
            scale = 1.0
            #scale = 0.98745 #((364.35-1.5*(1.433+6.782)-1.0*28.21)/(327.93))
          elif '_ttbbDown' in histoName:
            scale = 1.0
            #scale = 1.0058  #((364.35-(1./1.3)*(1.433+6.782)-1.0*28.21)/(327.93))
          elif '_ttccUp' in histoName:
            scale = 1.0
            #scale = 0.95697 #((364.35-1.0*(1.433+6.782)-1.5*28.21)/(327.93))
          elif '_ttccDown' in histoName:
            scale = 1.0
            #scale = 1.0198  #((364.35-1.0*(1.433+6.782)-(1./1.3)*28.21)/(327.93))
          else:
            scale = 1.0 
        else:
          raise Exception('unsupported ttbar category')
        # ttXsec scale
        if '_ttXsecUp' in histoName:
          scale = 1.06114
        elif '_ttXsecDown' in histoName:
          scale = 1./1.06114

        histo.Scale(scale)

      histo_rebinned.Add(histo, -1)

  return histo_rebinned

def SuppressZeros(histo):
  nBinsX = histo.GetNbinsX()
  for i in range(nBinsX):
    content = histo.GetBinContent(i+1)
    error   = histo.GetBinError(i+1)
    if content < 0:
      if content+error < 0:
        histo.SetBinContent(i+1,0)
        histo.SetBinError(i+1,0)
      else:
        histo.SetBinContent(i+1,0)
        histo.SetBinError(i+1,content+error)

def SetToZeros(histo):
  nBinsX = histo.GetNbinsX()
  for i in range(nBinsX):
    histo.SetBinContent(i+1,0)
    histo.SetBinError(i+1,1.)

def AppendForEnvelop(histos_envelop, ch, var, histoD):
  if ch not in histos_envelop:
    histos_envelop[ch] = {}
  if var not in histos_envelop[ch]:
    histos_envelop[ch][var] = []
  histos_envelop[ch][var].append(histoD)

def WriteEnvelop(histos_envelop, suffix, ch, var):
  histo_list = histos_envelop[ch][var]
  nBinsX = histo_list[0].GetNbinsX()
  bins_cont_up, bins_err_up     = [0.]*nBinsX, [0.]*nBinsX
  bins_cont_down, bins_err_down = [999999999999999999999999999999]*nBinsX, [999999999999999999999999999999]*nBinsX

  for i_histo, histo in enumerate(histo_list):
    # if sum is below zero, skip this histo
    sum_binc = sum([histo.GetBinContent(i+1) for i in range(nBinsX)])
    if i_histo>0 and sum_binc <= 1e-7:
      continue
    #

    for i in range(nBinsX):
      bin_content = histo.GetBinContent(i+1)
      bin_error = histo.GetBinError(i+1)
      if bins_cont_up[i] < bin_content:
        bins_cont_up[i] = bin_content
        bins_err_up[i]  = bin_error
      elif bins_cont_down[i] > bin_content:
        bins_cont_down[i] = bin_content
        bins_err_down[i]  = bin_error
      
  histo_envelop_up   = histo_list[0].Clone('histo_QCD_data_driven_qcd_envelop_%sUp'%suffix)
  histo_envelop_down = histo_list[0].Clone('histo_QCD_data_driven_qcd_envelop_%sDown'%suffix)

  for i in range(nBinsX):
    histo_envelop_up.SetBinContent(i+1,bins_cont_up[i])
    histo_envelop_up.SetBinError(i+1,bins_err_up[i])
    histo_envelop_down.SetBinContent(i+1,bins_cont_down[i])
    histo_envelop_down.SetBinError(i+1,bins_err_down[i])

  outFile.cd(ch+'/'+var)
  histo_envelop_up.Write('histo_QCD_data_driven_qcd_envelop_%sUp'%suffix)
  histo_envelop_down.Write('histo_QCD_data_driven_qcd_envelop_%sDown'%suffix)


histos_envelop = {}
histos_envelop_btag = {}
histos_envelop_tt_hf   = {}

outFile.cd()

exclude_3b = False

for tag_key, tag in input_dict.iteritems():
  f = ROOT.TFile(tag['input'],'READ')
  chennels = tag['chennels']
  for ch in chennels:
    outFile.mkdir(ch)
    outFile.cd(ch)
    for var in chennels[ch]:
      outFile.mkdir(ch+'/'+var)
      outFile.cd(ch+'/'+var)
  
      histoNameD = chennels[ch][var]
      rebin      = None
  
      print(histoNameD)
  
      histoD = GetHisto(f, ch, var, histoNameD, rebin)
      SuppressZeros(histoD)
      if exclude_3b and '_3b' in ch:
        SetToZeros(histoD)

      outHistName = 'histo_QCD_data_driven'
      if tag_key == '':
        pass
      elif 'iso' in tag_key:
        if 'eleCH' in ch or 'eleORmuCH' in ch:
          new_histo_suffix = 'antiiso_ele'
        elif 'muCH' in ch:
          new_histo_suffix = 'antiiso_mu'
        new_histo_suffix += tag_key.replace('iso','') # for Up/Down suffix
        outHistName += '_' + new_histo_suffix
      elif 'binning' in tag_key:
        ch_ = ch.replace('sng_4j_D_','').replace('eleCH','e').replace('muCH','m')
        year = '2016'
        new_histo_suffix = 'binning_%s_%s%s'%(ch_,year,tag_key.replace('binningVar',''))
        outHistName += '_' + new_histo_suffix
      else:
        outHistName += '_' + tag_key
      histoD.Write(outHistName)

      if tag_key in nuisances_btag or tag_key=='':
        AppendForEnvelop(histos_envelop_btag, ch, var, histoD)
      if tag_key in nuisances_tt_hf or tag_key=='':
        AppendForEnvelop(histos_envelop_tt_hf, ch, var, histoD)

for ch in input_dict['']['chennels']:
  for var in input_dict['']['chennels'][ch]:
    WriteEnvelop(histos_envelop_btag,  'btag', ch, var)
    WriteEnvelop(histos_envelop_tt_hf, 'tt_hf', ch, var)

outFile.Close()
