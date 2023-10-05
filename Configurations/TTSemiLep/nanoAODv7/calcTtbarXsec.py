
def TtbarXsec_by_mass():
  m_ref = 172.5
  a1 = -0.715324
  a2 =  0.175732
  
  #arXiv:1303.6254.
  m_t   = 173.5
  Xsec_scale = ((m_ref/m_t)**4)*(1+a1*(m_t-m_ref)/(m_ref)+a2*((m_t-m_ref)/(m_ref))**2)
  print(Xsec_scale)
  m_t   = 171.5
  Xsec_scale = ((m_ref/m_t)**4)*(1+a1*(m_t-m_ref)/(m_ref)+a2*((m_t-m_ref)/(m_ref))**2)
  print(Xsec_scale)

def TtbarXsec_by_genTtbarId():
  import ROOT
  BASE_DIR = '/xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7'
  t = ROOT.TChain("Events")
  t.Add(BASE_DIR+'/nanoLatino_TTToSemiLeptonic__part*.root')
  t.Add(BASE_DIR+'/nanoLatino_TTTo2L2Nu__part*.root')
  print("Step1")
  nEntries = t.GetEntries()
  t.SetBranchStatus("*",0)
  t.SetBranchStatus("genTtbarId",1)
  t.SetBranchStatus("genWeight",1)
  print("Step2")
  nTt, nTtbb, nTtbj, nTtcc, nTtjj = 0, 0, 0, 0, 0
  for i in range(nEntries):
    t.GetEntry(i)
    if i%100000 == 1:
      print('i : %d'%i, 
            "ttbbXsec: %f"%((364.35+87.310)*nTtbb/nTt),
            "ttbjXsec: %f"%((364.35+87.310)*nTtbj/nTt),
            "ttccXsec: %f"%((364.35+87.310)*nTtcc/nTt),
            "ttjjXsec: %f"%((364.35+87.310)*nTtjj/nTt))
    genWeight = t.genWeight
    nTt += genWeight
    genTtbarId = t.genTtbarId
    if genTtbarId%100 >= 53 and genTtbarId%100 <= 55 :
      nTtbb+=genWeight
    elif genTtbarId%100 == 51 or genTtbarId%100 == 52 :
      nTtbj+=genWeight
    elif genTtbarId%100 >= 41 and genTtbarId%100 <= 45 :
      nTtcc+=genWeight
    else:
      nTtjj+=genWeight
  print("nTt", nTt)
  print("nTtbb", nTtbb)
  print("nTtbj", nTtbj)
  print("nTtcc", nTtcc)
  print("nTtjj", nTtjj)
  

if __name__ == '__main__':
  TtbarXsec_by_genTtbarId()
