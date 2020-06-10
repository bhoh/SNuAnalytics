
##--signal Mass points--##
from List_MX import *
from List_MX_VBF import *


List_MX_common=list(set(List_MX).intersection(List_MX_VBF))

##--bkg--##
#BKG=[ 'DY', 'WZZ', 'WWZ','WWW','ZZZ', 'ZZ', 'WZ', 'WW', 'WpWmJJ_EWK_QCD_noHiggs', 'top', 'Wjets0j', 'Wjets1j', 'Wjets2j','vbfHWWlnuqq_M125','ggHWWlnuqq_M125'] + ['QCD_MU','QCD_EM','QCD_bcToE']
#BKG=[ 'DY', 'MultiV', 'WpWmJJ_EWK_QCD_noHiggs', 'top', 'Wjets0j', 'Wjets1j', 'Wjets2j','vbfHWWlnuqq_M125','ggHWWlnuqq_M125']# +['QCD_MU','QCD_EM','QCD_bcToE']
BKG=[ 'DY', 'MultiV', 'WpWmJJ_EWK_QCD_noHiggs', 'top', 'Wjets','vbfHWWlnuqq_M125','ggHWWlnuqq_M125']# +['QCD_MU','QCD_EM','QCD_bcToE']

import os


###---Make samples dictionary---##
#handle=open('../sample_2017.py','r')
#exec(handle)
#handle.close()

##---Make samples file for plotting nad Runcard
#f=open()
#for s in samples:##
#    f.write('samples["'+s+'"]={}\n')


#List_SampleTemplate=['samples_2017limit_MassTemplate_ele.py','samples_2017limit_MassTemplate_mu.py']
#List_StructureTemplate=['structure_MassTemplate_ele.py','structure_MassTemplate_mu.py']





print "-----sampleFile-----"
for MX in List_MX_common:
    for flv in ['ele','mu']:
        print MX
        ##SampleTemplate
        f=open('samples_2017limit_M'+str(MX)+'_'+flv+'.py','w')
        for s in BKG:
            f.write('samples["'+s+'"]={}\n')
        if 'ele' in flv:
            f.write('samples["QCD_EM"]={}\n')
            f.write('samples["QCD_bcToE"]={}\n')
        if 'mu' in flv:
           f.write('samples["QCD_MU"]={}\n')
        f.write('samples["DATA"]={}\n')
        f.write('samples["ggHWWlnuqq_M'+str(MX)+'"]={}\n')        
        f.write('samples["vbfHWWlnuqq_M'+str(MX)+'"]={}\n')

        f.close()

print "------structure File------"
for MX in List_MX_common:
    for flv in ['ele','mu']:
        print MX
        ##SampleTemplate
        f=open('structure_M'+str(MX)+'_'+flv+'.py','w')
        for s in BKG:
            f.write('structure["'+s+'"]={\n\
            "isSignal" : 0,\n\
            "isData"   : 0 ,\n\
            }\n')
        if 'ele' in flv:
            f.write('structure["QCD_EM"]={\n\
            "isSignal" : 0,\n\
            "isData"   : 0 ,\n\
            }\n')
            f.write('structure["QCD_bcToE"]={\n\
            "isSignal" : 0,\n\
            "isData"   : 0 ,\n\
            }\n')
        if 'mu' in flv:
            f.write('structure["QCD_MU"]={\n\
            "isSignal" : 0,\n\
            "isData"   : 0 ,\n\
            }\n')
        f.write('structure["DATA"]={\n\
        "isSignal" : 0,\n\
        "isData"   : 1 ,\n\
        }\n')
        f.write('structure["ggHWWlnuqq_M'+str(MX)+'"]={\n\
        "isSignal" : 1,\n\
        "isData"   : 0 ,\n\
        }\n')        
        f.write('structure["vbfHWWlnuqq_M'+str(MX)+'"]={\n\
        "isSignal" : 1,\n\
        "isData"   : 0 ,\n\
        }\n')

        f.close()
    
