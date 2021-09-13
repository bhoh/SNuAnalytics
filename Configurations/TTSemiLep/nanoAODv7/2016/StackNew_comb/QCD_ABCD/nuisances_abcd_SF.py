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

mc = [skey for skey in samples if skey != 'DATA']
samples_key = [skey for skey in samples]

ABCD_SF_1l =  '(nLooseLep==1)*((eleCH || muCH || MET_CHToCB_pt_nom<=20)*1 + (muCH_noTight  && (nBJets_WP_M + nBJets_WP_M_20to30 == 2) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_mu_2b[0]) + (muCH_noTight  && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_mu_3b[0]) + (eleCH_noTight && (nBJets_WP_M + nBJets_WP_M_20to30 == 2) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_ele_2b[0]) + (eleCH_noTight && ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3) && (MET_CHToCB_pt_nom>20))*(OTF_ABCD_SF_ele_3b[0]))'
#ABCD_SF_2l =  '(nLooseLep==2)*((isOSpair || MET_CHToCB_pt_nom<=40)*1 + (!isOSpair && MET_CHToCB_pt_nom>40)*((nBJets_WP_M + nBJets_WP_M_20to30 == 2)*((eeCH)*OTF_ABCD_SF_ee_2b[0] + (emCH)*OTF_ABCD_SF_em_2b[0] + (meCH)*OTF_ABCD_SF_me_2b[0] + (mmCH)*OTF_ABCD_SF_mm_2b[0]) + ((nBJets_WP_M + nBJets_WP_M_20to30) >= 3)*((eeCH)*OTF_ABCD_SF_ee_3b[0] + (emCH)*OTF_ABCD_SF_em_3b[0] + (meCH)*OTF_ABCD_SF_me_3b[0] + (mmCH)*OTF_ABCD_SF_mm_3b[0])))'
ABCD_SF_2l =  '(nLooseLep==2)*(1)'

ABCD_SF      = '(%s+%s)'%(ABCD_SF_1l, ABCD_SF_2l)


##for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
#for shift in ['lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
#    btag_up, btag_down = '(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift
#
#    name = 'btag_%s' % shift
#    if 'stats' in shift:
#        name += '_2016'
#    ABCD_SF_syst_up   = ABCD_SF.replace('[0]',name+'[1]')
#    ABCD_SF_syst_down = ABCD_SF.replace('[0]',name+'[2]')
#    btag_up, btag_down = '(%s)*%s/%s'%(btag_up,ABCD_SF_syst_up,ABCD_SF), '(%s)*%s/%s'%(btag_down,ABCD_SF_syst_down,ABCD_SF)
#    btag_syst = ['({var}<9999?{var}:1.)'.format(var=btag_up),'({var}<9999?{var}:1.)'.format(var=btag_down)]
#
#    samples_dict = dict((skey, btag_syst) for skey in mc)
#    samples_dict.update({ 'DATA' : ['%s/%s'%(ABCD_SF_syst_up,ABCD_SF),'%s/%s'%(ABCD_SF_syst_down,ABCD_SF)]})
#    nuisances['btag_shape_%s' % shift] = {
#        'name': name,
#        'kind': 'weight',
#        'type': 'shape',
#        'samples': samples_dict,
#        'group': 'experimental',
#    }
#
#for syst in ['ttbb','ttcc','ttXsec']:
#    ABCD_SF_syst_up   = ABCD_SF.replace('[0]',syst+'[1]')
#    ABCD_SF_syst_down = ABCD_SF.replace('[0]',syst+'[2]')
#    nuisances['ABCD_SF'+syst] = {
#        'name': syst,
#        'kind': 'weight',
#        'type': 'shape',
#        'samples': { key : ['%s/%s'%(ABCD_SF_syst_up,ABCD_SF),'%s/%s'%(ABCD_SF_syst_down,ABCD_SF)] for key in samples_key },
#        'group': 'theory',
#    } 
#for syst in ['binningVar']: #one-side
for syst in ['iso',]:
    ABCD_SF_syst_up   = ABCD_SF.replace('[0]',syst+'[1]').replace('_noTight','_noTight_isoUp')
    ABCD_SF_syst_down = ABCD_SF.replace('[0]',syst+'[2]').replace('_noTight','_noTight_isoDown')
    nuisances['ABCD_SF'+syst] = {
        'name': syst,
        'kind': 'weight',
        'type': 'shape',
        'samples': { key : ['%s/%s'%(ABCD_SF_syst_up,ABCD_SF),'%s/%s'%(ABCD_SF_syst_down,ABCD_SF)] for key in samples_key },
        'group': 'theory',
    } 

