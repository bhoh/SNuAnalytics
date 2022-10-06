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
  treeBaseDir = "/xrootd/store/user/bhoh/Latino/HWWNano/"

def CalcLenBranch(samples,branch):

    passes={}

    for s in samples:
      print "---",s,"---"
      if len(samples[s]['name'])==0:continue
      FirstFile=samples[s]['name'][0].replace("###","")
      print FirstFile
      f=ROOT.TFile.Open(FirstFile)
      tree=f.Get("Events")
      if tree.GetListOfBranches().FindObject(branch):
        print 'Length$("%s")'%branch
        tree.Draw('Length$(%s)'%branch)
        htemp=ROOT.gPad.GetPrimitive("htemp")
        n= int(htemp.GetMean())
        print n
        if not n in passes:
          passes[n]=[]
        passes[n].append(s)
      f.Close()

    return passes


#CalcLenBranch
nMember_sample=CalcLenBranch(samples,'LHEPdfWeight') ## {33:[DY,Wjets...]}
PDF4LHC15_nnlo_30_pdfas={}
NNPDF={}
PDF_ALL={}
for n in nMember_sample:
  if n==33:
    for s in nMember_sample[n]:
      PDF4LHC15_nnlo_30_pdfas[s]=['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(n)]
      #PDF4LHC15_nnlo_30_pdfas
  elif n>=100:
    for s in nMember_sample[n]:
      NNPDF[s]=['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(n)]
PDF_ALL.update(PDF4LHC15_nnlo_30_pdfas)
PDF_ALL.update(NNPDF)
#PDF_ALL.update({'TT' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TT+jj' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TT+cc' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TT+bb' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TT+bj' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLJ' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLJ_jj' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLJ_bb' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLJ_bj' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLJ_cc' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLL' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLL_jj' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLL_bb' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLL_bj' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'TTLL_cc' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'Others' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })
#PDF_ALL.update({'QCD' :['LHEPdfWeight[%s]/LHEPdfWeight[0]'%i for i in range(100)] })

mc = [skey for skey in samples if skey != 'DATA' and 'QCD' not in skey]
mc += ['TT','TT+bb','TT+bj','TT+cc','TT+jj','Others']
mc += ['TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
#ttmc_syst = ['TTLJ+bb','TTLJ+bj','TTLJ+cc','TTLJ+jj','TTLL+bb','TTLL+bj','TTLL+cc','TTLL+jj']
ttmc_syst = ['TTLJ','TTLJ_jj','TTLJ_cc','TTLJ_bb','TTLJ_bj','TTLL','TTLL_jj','TTLL_cc','TTLL_bb','TTLL_bj']
ttmc_syst += ['TT','TT+bb','TT+bj','TT+cc','TT+jj']
ttmc = [ skey for skey in ttmc_syst ]
ttmc += ['CHToCB_M%s'%mass for mass in ['075','080','085','090','100','110','120','130','140','150','160']]
qcdmc = ['QCD_EM','QCD_bcToE','QCD_MU']
qcdmc += ['QCD']

from pprint import pprint

for key, var in PDF_ALL.iteritems():
    print("key: %s, \t\t\t %d"%(key,len(var)))



include_mva = False

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}


