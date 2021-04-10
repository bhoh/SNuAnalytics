import os

SITE=os.uname()[1]


xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

elif  'sdfarm' in SITE:
  xrootdPath = 'root://cms-xrdr.private.lo:2094'
  treeBaseDir = "/xrootd/store/user/jhchoi/Latino/HWWNano/"

samples_key = [skey for skey in samples]
mc = [skey for skey in samples if skey != 'DATA']

ABCD_SF_1l =  '(nLooseLep==1)*((eleCH || muCH || MET_CHToCB_pt_nom<=20)*1 + (muCH_noTight  && (nBJets_WP_M + nBJets_WP_M_20to30 == 2) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_mu_2b[0]) + (muCH_noTight  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_mu_3b[0]) + (eleCH_noTight && (nBJets_WP_M + nBJets_WP_M_20to30 == 2) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_ele_2b[0]) + (eleCH_noTight && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_ele_3b[0]))'
#ABCD_SF_2l =  '(nLooseLep==2)*((isOSpair || MET_CHToCB_pt_nom<=40)*1 + (!isOSpair && MET_CHToCB_pt_nom>40)*((nBJets_WP_M + nBJets_WP_M_20to30 == 2)*((eeCH)*OTF_ABCD_SF_ee_2b[0] + (emCH)*OTF_ABCD_SF_em_2b[0] + (meCH)*OTF_ABCD_SF_me_2b[0] + (mmCH)*OTF_ABCD_SF_mm_2b[0]) + ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)*((eeCH)*OTF_ABCD_SF_ee_3b[0] + (emCH)*OTF_ABCD_SF_em_3b[0] + (meCH)*OTF_ABCD_SF_me_3b[0] + (mmCH)*OTF_ABCD_SF_mm_3b[0])))'
ABCD_SF_2l =  '(nLooseLep==2)*(1)'
ABCD_SF      = '(%s+%s)'%(ABCD_SF_1l, ABCD_SF_2l)


#for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_up, btag_down = '(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift

    name = 'btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'
    ABCD_SF_syst_up   = ABCD_SF.replace('[0]',name+'[1]')
    ABCD_SF_syst_down = ABCD_SF.replace('[0]',name+'[2]')
    btag_up, btag_down = '(%s)*%s/%s'%(btag_up,ABCD_SF_syst_up,ABCD_SF), '(%s)*%s/%s'%(btag_down,ABCD_SF_syst_down,ABCD_SF)
    btag_syst = ['({var}<9999?{var}:1.)'.format(var=btag_up),'({var}<9999?{var}:1.)'.format(var=btag_down)]

    samples_dict = dict((skey, btag_syst) for skey in mc)
    samples_dict.update({ 'DATA' : ['%s/%s'%(ABCD_SF_syst_up,ABCD_SF),'%s/%s'%(ABCD_SF_syst_down,ABCD_SF)]})
    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': samples_dict,
        'group': 'experimental',
    }

for syst in ['ttbb','ttcc','ttXsec']:
    ABCD_SF_syst_up   = ABCD_SF.replace('[0]',syst+'[1]')
    ABCD_SF_syst_down = ABCD_SF.replace('[0]',syst+'[2]')
    nuisances['ABCD_SF'+syst] = {
        'name': syst,
        'kind': 'weight',
        'type': 'shape',
        'samples': { key : ['%s/%s'%(ABCD_SF_syst_up,ABCD_SF),'%s/%s'%(ABCD_SF_syst_down,ABCD_SF)] for key in samples_key },
        'group': 'theory',
    }
for syst in ['isoVar','binningVar']: #one-side
    ABCD_SF_syst_up   = ABCD_SF.replace('[0]',syst+'[1]')
    nuisances['ABCD_SF'+syst] = {
        'name': syst,
        'kind': 'weight',
        'type': 'shape',
        'samples': { key : ['%s/%s'%(ABCD_SF_syst_up,ABCD_SF),'1.'] for key in samples_key },
        'group': 'theory',
    }
hist_path_dict = {}
hist_path_dict['mu_2b']  = 'sng_4j_muCH_2b/MuonEta/histo_TF_data_driven'
hist_path_dict['mu_3b']  = 'sng_4j_muCH_3b/MuonEta/histo_TF_data_driven'
hist_path_dict['ele_2b'] = 'sng_4j_eleCH_2b/EleSCEta/histo_TF_data_driven'
hist_path_dict['ele_3b'] = 'sng_4j_eleCH_3b/EleSCEta/histo_TF_data_driven'
for syst in ['mu_2b', 'mu_3b','ele_2b','ele_3b']:
  # i th bin syst
  hist_source = '%s/src/SNuAnalytics/Configurations/TTSemiLep/patches/ABCD_SF/ABCD_data_driven_SF_2017.root' % os.getenv('CMSSW_BASE')
  f = ROOT.TFile(hist_source,"READ")
  h = f.Get(hist_path_dict[syst])
  Nbins = h.GetNbinsX()
  for i in range(1,Nbins+1): 
    ABCD_SF_syst_up   = ABCD_SF.replace('%s[0]'%syst,'%s[%d]'%(syst,int(2*i-1)))
    ABCD_SF_syst_down = ABCD_SF.replace('%s[0]'%syst,'%s[%d]'%(syst,int(2*i)))
    name = "ABCD_SF_%s_bins%d_2017"%(syst,int(i))
    nuisances[name] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': { key : ['%s/%s'%(ABCD_SF_syst_up,ABCD_SF),'%s/%s'%(ABCD_SF_syst_down,ABCD_SF)] for key in samples_key },
        'group': 'experiment',
    }

