
































import sys
sys.path.insert(0, "MassPoints")
from List_melaKDmass import *

for MX in List_melaKDmass:
  variables['P_BstGF'+str(MX)]={
      'name' : 'PrbBstGF' + str(MX),
      'range':(50,0,1),
      'xaxis':'Prob. GF_{Boost}',
      'fold':3
  }
  variables['P_RsvGF'+str(MX)]={
      'name' : 'PrbRsvGF' + str(MX),
      'range':(50,0,1),
      'xaxis':'Prob. GF_{Resol}',
      'fold':3
  }
  variables['meP'+str(MX) +'_BstNoT_ggf_S']={
      'name' : 'meP' + str(MX) + '_BstNoT_ggf_S*1e9',
      'range':(50,0,1e-3),
      'xaxis':'Prob. GF_{Boost}',
      'fold':3
  }
  variables['meP'+str(MX) +'_BstNoT_ggf_B']={
      'name' : 'meP' + str(MX) + '_BstNoT_ggf_B*1e9',
      'range':(50,0,1e-3),
      'xaxis':'Prob. GF_{Boost}',
      'fold':3
  }
  variables['meP'+str(MX)+'_ResNoT_ggf_S']={
      'name' : 'meP'+str(MX)+'_ResNoT_ggf_S*1e9',
      'range':(50,0,1e-3),
      'xaxis':'Prob. GF_{Resol}',
      'fold':3
  }
  variables['meP'+str(MX)+'_ResNoT_ggf_B']={
      'name' : 'meP'+str(MX)+'_ResNoT_ggf_B*1e9',
      'range':(50,0,1e-3),
      'xaxis':'Prob. GF_{Resol}',
      'fold':3
  }



#variables['CleanFatJetPassMBoostedSR_HlnFat_mass']={
#    'name' : 'CleanFatJetPassMBoostedSR_HlnFat_mass[0]',
#    #'range':(80,0,4000),
#    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000,6000],),
#    'xaxis':'m_{lnJ} [GeV]',
#    'divideByBinWidth':1,
#    'fold':0
#}
#
#
#
#
#variables['LnJJ_mass']={
#    'name': 'Hlnjj_mass',
#    'range':([0,200,210,230,250,300,350,400,450,500,550,600,650,700,750,800,900,1000,1500,2000,2500,3000,4000,5000,6000],),
#    'xaxis':'m_{lnjj} [GeV]',
#    'divideByBinWidth':1,
#    'fold':0
#}
#
#
#variables['events']={
#    'name': '1',
#    'range':(1,0,2),
#    'xaxis':'event',
#    'fold':3
#}


