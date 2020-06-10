from ROOT import TFile, TTree
import os, math

base_dir  = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb/scripts/combine/'
file_name = 'higgsCombineM120Y2016muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2017muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2018muCH4j2b__HEMveto4j3b__HEMvetoeleCH4j2b__HEMveto4j3b__HEMveto.r0.00000000000002to0.00996005996002.AsymptoticLimits.mH120.12345.root'
f = TFile(base_dir + file_name,'READ')
limit = f.Get('limit')

def GetMedian(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

def Get2SigmaMedian(lst):
    n = len(lst)
    s = sorted(lst, key=lambda x : x[0])
    #hi95 = int(min(n-1, math.ceil(0.975  * n)))
    #lo95 = int(min(n-1, math.floor(0.025 * n)))
    hi68 = int(min(n-1, math.ceil(0.84  * n)))
    lo68 = int(min(n-1, math.floor(0.16 * n)))
    try:
        #return lst[lo95:hi95]
        return lst[lo68:hi68]
    except TypeError:
        print lst



out_file = TFile("test.root","RECREATE")
out_file.mkdir('toys')
out_tree = limit.CloneTree(0)

nEntries = limit.GetEntries()



valid_range_entries = []
grid = {}
for i in range(nEntries/6):
    # 6 quantile
    # to validate cls value,
    # if minimization quailty is not good, cls value become 0.5 or 1 or very small value
    valid_cls_range=[]
    for j in range(6):
      limit.GetEntry(i*6+j)
      limit_ = limit.limit
      r_     = limit.r
      valid_cls_range += [ 0 < limit_ < 0.45 ]
      if r_ not in grid:
          grid[r_]  = [(limit_, i, j)]
      else:
          grid[r_] += [(limit_, i, j)] #j : quantile

    if sum(valid_cls_range) == 6:
        valid_range_entries += [i*6+j for j in range(6)]

exclude_entries = []
for key in grid:
    ele1, ele2, ele3 = grid[key][0], grid[key][1], grid[key][2]
    if not ele3 == 5: # 5 is obs.
        continue
    if ele2*6+ele3 not in valid_range_entries:
        continue
    median_ = Get2SigmaMedian( grid[key] )

    if ele1 not in median_:
        exclude_entries += [ele2*6+j for j in range(6)]
 

for i in valid_range_entries:
    if i in exclude_entries:
        continue
    limit.GetEntry(i)
    out_tree.Fill()

out_file.cd()
out_tree.Write()
out_file.Close()

