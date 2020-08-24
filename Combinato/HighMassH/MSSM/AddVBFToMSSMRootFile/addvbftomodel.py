#import CombineHarvester.CombineTools.plotting as plot
#import os
import ROOT
import math
import os
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)

# This script is used to add VBF cross sections to given MSSM scenario root files.

modfile = "mh125_13.root"
newfile = "mh125_13_VBF.root"

os.system('cp '+modfile+' '+newfile)

file1 = ROOT.TFile(modfile, 'r')
histo = file1.Get('xs_gg_H')
file1.Close
histo.SetName("xs_vbf_H")
file = ROOT.TFile(newfile, 'UPDATE')

Hxsec = {60:6.924, 65:6.603, 70:6.301, 75:6.016, 80:5.748, 85:5.496, 90:5.258, 95:5.034, 100:4.822, 105:4.623, 110:4.434, 115:4.255, 120:4.086, 125:3.925, 130:3.773, 135:3.629, 140:3.492, 145:3.362, 150:3.239, 160:3.010, 170:2.802, 180:2.612, 190:2.440, 200:2.282, 210:2.138, 220:2.006, 230:1.884, 240:1.772, 250:1.669, 260:1.573, 270:1.485, 280:1.403, 290:1.326, 300:1.256, 310:1.190, 320:1.128, 330:1.071, 340:1.017, 350:0.9666, 360:0.9194, 370:0.8752, 380:0.8337, 390:0.7947, 400:0.7580, 410:0.7235, 420:0.6909, 430:0.6602, 440:0.6312, 450:0.6038, 460:0.5778, 470:0.5533, 480:0.5301, 490:0.5081, 500:0.4872, 550:0.3975, 600:0.3274, 650:0.2719, 700:0.2275, 750:0.1915, 800:0.1622, 850:0.1380, 900:0.1180, 950:0.1013, 1000:0.08732, 1050:0.07551, 1100:0.06550, 1150:0.05698, 1200:0.04970, 1250:0.04345, 1300:0.03807, 1350:0.03343, 1400:0.02941, 1450:0.02592, 1500:0.02288, 1550:0.02023, 1600:0.01791, 1650:0.01588, 1700:0.01410, 1750:0.01253, 1800:0.01115, 1850:0.009926, 1900:0.008849, 1950:0.007896, 2000:0.007052, 2050:0.006303, 2100:0.005638, 2150:0.005046, 2200:0.004520, 2250:0.004051, 2300:0.003633, 2350:0.003259, 2400:0.002925, 2450:0.002627, 2500:0.002360, 2550:0.002122, 2600:0.001908, 2650:0.001717, 2700:0.001545} # VBF Xsecs for BSM 13GeV, from YR4

mZ=91.1876
# Pi = acos(-1)
for x in xrange(1,histo.GetXaxis().GetNbins()+1):
  for y in xrange(1,histo.GetYaxis().GetNbins()+1):
    mA = histo.GetXaxis().GetBinCenter(x)
    beta = math.atan(histo.GetYaxis().GetBinCenter(y))
    try:
      mh = math.sqrt( 0.5*(mA*mA+mZ*mZ - math.sqrt( (mA*mA-mZ*mZ)*(mA*mA-mZ*mZ) + 4*mA*mA*mZ*mZ*math.sin(2*beta)*math.sin(2*beta) )) )
    except ValueError:
      mh = 0
    mH = math.sqrt( 0.5*(mA*mA+mZ*mZ + math.sqrt( (mA*mA-mZ*mZ)*(mA*mA-mZ*mZ) + 4*mA*mA*mZ*mZ*math.sin(2*beta)*math.sin(2*beta) )) )



    alpha = math.atan( -1.0*(mA*mA+mZ*mZ)*math.sin(2*beta) /( (mZ*mZ-mA*mA)*math.cos(2*beta)+math.sqrt( (mA*mA-mZ*mZ)*(mA*mA-mZ*mZ) + 4*mA*mA*mZ*mZ*math.sin(2*beta)*math.sin(2*beta) ) ) )

    ### This is used specifically for hMSSM
    #alpha = -1*math.atan( ( (mZ*mZ+mA*mA)*math.cos(beta)*math.sin(beta) ) / ( mZ*mZ*math.cos(beta)*math.cos(beta)+mA*mA*math.sin(beta)*math.sin(beta)-125*125 ) )


    if mH in Hxsec:
      Hx = Hxsec[mH]
    else:
      for i in sorted(Hxsec):
        if i > mH:
          Hx = Hxsec[i]+(Hxsec[j]-Hxsec[i])*(1-(mH-j)/(i-j))
          break
        j = i

    Hx = Hx*math.cos(beta-alpha)*math.cos(beta-alpha)
    if histo.GetBinContent(x,y) != 0: histo.SetBinContent(x,y,Hx) #for hMSSM: Small area at low mA/low tanb is not defined in this scenario.

histo.Write()
file.Close
print "Done!"
exit(0)
