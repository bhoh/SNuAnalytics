OnlySignal=True##for PDF,QCDscale
DoPDF=True
DoQCDscale=True
DoPS=True

import os




samples={}
handle=open('samples_2016.py','r')
exec(handle)
handle.close()


from MakeSampleDict import *



#PSWeight
if DoPDF:
  ###----PDF
  os.system('mkdir -p PDF')
  f=open('PDF/nuisance_pdf.py','w')
  nMember_sample=CaclLenBranch(samples,'LHEPdfWeight')
  #print "nMember_sample={}"
  f.write("nMember_sample={}\n")
  for n in nMember_sample:
    #print "# of member->",n
    if int(n)==0:continue
    mylist=[]
    for s in nMember_sample[n]:
      mylist.append(s)
      #print "nMember_sample["+str(n)+"]=",mylist
    f.write("nMember_sample["+str(n)+"]=[")
    for s in mylist:
      if OnlySignal:
        if 'ggHWWlnuqq_M' in s or 'vbfHWWlnuqq_M' in s:
          f.write('"'+s+'"'+',')
    f.write(']\n')
    #pdfAccept[s]=["abs(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0]) < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)] ## outlyer in top sample
  f.close()

###---QCDscale

if DoQCDscale:
  os.system('mkdir -p QCDscale')
  f=open('QCDscale/nuisance_QCDscale.py','w')
  nMember_sample=CaclLenBranch(samples,'LHEScaleWeight')
  f.write("nMember_sample={}\n")
  for n in nMember_sample:
    #print "# of member->",n
    if int(n)==0:continue
    mylist=[]
    for s in nMember_sample[n]:
      mylist.append(s)
    #print "nMember_sample["+str(n)+"]=",mylist
    f.write("nMember_sample["+str(n)+"]=[")
    for s in mylist:
      if OnlySignal:
        if 'ggHWWlnuqq_M' in s or 'vbfHWWlnuqq_M' in s:
          f.write('"'+s+'"'+',')
    f.write(']\n')
    #pdfAccept[s]=["abs(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0]) < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)] ## outlyer in top sample
  f.close()


##--PS
if DoPS:##PSWeight
  os.system('mkdir -p PS')
  f=open('PS/nuisance_PS.py','w')
  nMember_sample=CaclLenBranch(samples,'PSWeight')
  f.write("nMember_sample={}\n")
  for n in nMember_sample:
    #print "# of member->",n
    #for s in nMember_sample[n]:
    #  print s
    if int(n)!=4:continue
    mylist=[]
    for s in nMember_sample[n]:
      mylist.append(s)
    #print "nMember_sample["+str(n)+"]=",mylist 
    f.write("nMember_sample["+str(n)+"]=[")
    for s in mylist:
      f.write('"'+s+'"'+',')
    f.write(']\n')
    #pdfAccept[s]=["abs(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0]) < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)] ## outlyer in top sample
  f.close()


'''
nuisances['QCDscaleAccept'] = {
    'name': 'QCDscaleAccept',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': 'samples': dict((skey, variations) for skey in mc),
}
'''

#"abs(LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0]) < 10 ? LHEPdfWeight["+str(i)+"]/LHEPdfWeight[0] : 1.0" for i in range(n)
#samples_value=MakeSampleDict(samples,'LHEScaleWeight',"LHEScaleWeight[0]")
#print samples_value

#nuisances['QCDscaleAccept'] = {
#    'name': 'QCDscaleAccept',
#    'kind': 'weight_envelope',
#    'type': 'shape',
#    'samples': samples_value,
#}



#CaclLenBranch
#nMember_sample=CaclLenBranch(samples,'LHEPdfWeight') ## {33:[DY,Wjets....]}
