import os

base_dir  = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv5/2017/StackNew_comb/scripts/combine/'
hadd_target = 'higgsCombineM{MASS}Y2016muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2017muCH4j2b__4j3b__eleCH4j2b__4j3b__Y2018muCH4j2b__HEMveto4j3b__HEMvetoeleCH4j2b__HEMveto4j3b__HEMveto.r{POINT}.AsymptoticLimits.mH{MASS}.12345.root'
masses    = ['120']
nPoints = 1000
points = [0.00000000000001+0.00000000000001*i*i*i*i for i in range(nPoints)] # from 0.00001 to 500 points with 0.00005 steps
nCore     = 4

for mass in masses:
    path = base_dir + hadd_target.format(POINT='*',MASS=int(mass))

    #hadd_commend = 'mkdir {BASE_DIR}/tmp; hadd -f -j {N_CORE} -d {BASE_DIR}/tmp {BASE_DIR}/{OUT_NAME} {TARGETS}'
    hadd_commend = 'hadd -f {BASE_DIR}/{OUT_NAME} {TARGETS}'
    out_name = hadd_target.format(POINT='%.14fto%.14f'%(points[1],points[-1]),MASS=int(mass))
    hadd_commend = hadd_commend.format(BASE_DIR=base_dir,N_CORE=nCore,OUT_NAME=out_name,TARGETS=path)
    #print hadd_commend
    os.system(hadd_commend)
