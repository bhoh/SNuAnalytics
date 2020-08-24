import os
import sys
sys.path.insert(0, os.getcwd()+"/../MassPoints")
sys.path.insert(0, os.getcwd()+"/../")
##--signal Mass points--##
from List_MX import *
from List_MX_VBF import *
from WPandCut2016 import Year

List_MX_common=list(set(List_MX).intersection(List_MX_VBF))

##--bkg--##
#BKG=[ 'DY', 'WZZ', 'WWZ','WWW','ZZZ', 'ZZ', 'WZ', 'WW', 'WpWmJJ_EWK_QCD_noHiggs', 'top', 'Wjets0j', 'Wjets1j', 'Wjets2j','vbfHWWlnuqq_M125','ggHWWlnuqq_M125'] + ['QCD_MU','QCD_EM','QCD_bcToE']
#BKG=[ 'DY', 'MultiV', 'WpWmJJ_EWK_QCD_noHiggs', 'top', 'Wjets0j', 'Wjets1j', 'Wjets2j','vbfHWWlnuqq_M125','ggHWWlnuqq_M125']# +['QCD_MU','QCD_EM','QCD_bcToE']
#BKG=[ 'DY', 'MultiV', 'WpWmJJ_EWK_QCD_noHiggs', 'top', 'Wjets','vbfHWWlnuqq_M125','ggHWWlnuqq_M125']# +['QCD_MU','QCD_EM','QCD_bcToE']
#BKG=[ 'DY', 'MultiV', 'qqWWqq', 'top', 'Wjets','ggWW','h125','QCD','HTT']# +['QCD_MU','QCD_EM','QCD_bcToE']
BKG=[ 'DY', 'MultiV', 'qqWWqq', 'top', 'Wjets','ggWW','ggHWWlnuqq_M125','QCD','HTT']# +['QCD_MU','QCD_EM','QCD_bcToE']
if Year=='2016':
    BKG.append('vbfHWWlnuqq_M125')




###---Make samples dictionary---##
#handle=open('../sample_2016.py','r')
#exec(handle)
#handle.close()

##---Make samples file for plotting nad Runcard
#f=open()
#for s in samples:##
#    f.write('samples["'+s+'"]={}\n')


#List_SampleTemplate=['samples_2016limit_MassTemplate_ele.py','samples_2016limit_MassTemplate_mu.py']
#List_StructureTemplate=['structure_MassTemplate_ele.py','structure_MassTemplate_mu.py']





print "-----sampleFile-----"
for MX in List_MX_common:
    for flv in ['ele','mu']:
        print MX
        ##SampleTemplate
        for rg in ['SR','TOP','SB']:
            f=open('samples_limit_M'+str(MX)+'_'+flv+'.py','w') ##samples_limit_M
            for s in BKG:
                f.write('samples["'+s+'"]={}\n')
            f.write('samples["DATA"]={}\n')

            f.write('samples["ggHWWlnuqq_M'+str(MX)+'_S"]={}\n')        
            f.write('samples["vbfHWWlnuqq_M'+str(MX)+'_S"]={}\n')
            f.write('samples["ggHWWlnuqq_M'+str(MX)+'_SBI"]={}\n')        
            f.write('samples["vbfHWWlnuqq_M'+str(MX)+'_SBI"]={}\n')
            
            f.close()

print "------structure File------"
for MX in List_MX_common:
    for flv in ['ele','mu']:
        print MX
        ##SampleTemplate
        for rg in ['SR','TOP','SB']:
            f=open('structure_M'+str(MX)+'_'+flv+'.py','w')
            for s in BKG:
                f.write('structure["'+s+'"]={\n\
                "isSignal" : 0,\n\
                "isData"   : 0 ,\n\
                }\n')
            
            f.write('structure["DATA"]={\n\
            "isSignal" : 0,\n\
            "isData"   : 1 ,\n\
            }\n')

            f.write('structure["ggHWWlnuqq_M'+str(MX)+'_S"]={\n\
            "isSignal" : 1,\n\
            "isData"   : 0 ,\n\
            }\n')        
            f.write('structure["vbfHWWlnuqq_M'+str(MX)+'_S"]={\n\
            "isSignal" : 1,\n\
            "isData"   : 0 ,\n\
            }\n')
        
            f.write('structure["ggHWWlnuqq_M'+str(MX)+'_SBI"]={\n\
            "isSignal" : 1,\n\
            "isData"   : 0 ,\n\
            }\n')        
            f.write('structure["vbfHWWlnuqq_M'+str(MX)+'_SBI"]={\n\
            "isSignal" : 1,\n\
            "isData"   : 0 ,\n\
            }\n')
            
            f.close()
    
##---Make Final Nuisance
#nuisances['dynorm']['sample']
defaultNuisanceFile='../nuisances.py'
f=open(defaultNuisanceFile,'r')
fnew=open('nuisance.py','w')
lines=f.readlines()

for line in lines:
    fnew.write(line)

fnew.write(
    '''
for n in nuisances:
      for s in sorted(nuisances[n]['samples']):
        if '_S' in s:
          sbi=s.replace('_S','_SBI')
          nuisances[n]['samples'][sbi]=nuisances[n]['samples'][s]

    '''
)

fnew.close()

os.system('cp nuisance.py nuisance_Boosted.py')
os.system('cp nuisance.py nuisance_Resolved.py')
