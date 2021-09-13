import os
import argparse
import collections
from datacards import datacards



masses = ['075','080','080_yield','085','090','100','110','120','130','140','150','160']
mass_points = [("CH090",90),("CH100",100),("CH110",110),("CH120",120),("CH130",130),("CH140",140),("CH150",150),("CH160,160")]
dirBase={}
dirBase['2016'] = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2016/StackNew_comb/'
dirBase['2017'] = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2017/StackNew_comb/'
dirBase['2018'] = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/nanoAODv7/2018/StackNew_comb/'
variableName = ['fitted_dijet_M','fitted_dijet_M_high','Bins']

base_dir = '/cms/ldap_home/bhoh/latinos/CMSSW_10_6_4/src/SNuAnalytics/Configurations/TTSemiLep/scripts/'

class LimitCalc():

    def __init__(self,StatOnly, Ch, Year, Method, Options, Batch, Run, Snapshot, Seed='12345'):
      if StatOnly==True:
          self.StatOnlyLabel = "stat_only"
          self.StatOnly = '-S 0'
      elif StatOnly==False:
          self.StatOnlyLabel = ""
          self.StatOnly = ''
      else:
          raise RuntimeError("no such args: %s"%StatOnly)

      if Ch == "All":
        self.Ch = ['sng_4j_muCH_2b', 'sng_4j_eleCH_2b','sng_4j_muCH_3b', 'sng_4j_eleCH_3b']
        #self.Ch = ['sng_4j_muCH_2b', 'sng_4j_eleCH_2b']
        #self.Ch = ['sng_4j_muCH_3b', 'sng_4j_eleCH_3b']
        #2j2b,    3j2b,    >=4j2b,    3j3b(sensitive to ttbj),    >=4j3b(sensitive to ttcc),    >=4j4b(sensitive to ttbb)
        self.Ch += ['dbl_2j_ee','dbl_2j_mm','dbl_2j_em','dbl_2j_me']
      elif Ch in ['sngCH']:
        self.Ch = ['sng_4j_muCH', 'sng_4j_eleCH']
      else:
        print 'There is no channel like',Ch, 'Exiting....'
        exit()

      if Year == "All":
        self.Year = ['2016','2017','2018']
        #self.Year = ['2018']
        #self.Year = ['2017']
        #self.Year = ['2016']
        #self.Year = ['2017','2018']
      elif Year in ['2016','2017','2018']:
        self.Year    = [Year]
      else:
        print 'there is no year like',Year,'Exiting....'
        exit()


      if Run !='':
        self.Run = '--run '+Run
        self.RunLabel = Run
      else:
        self.Run =''
        self.RunLabel = ''
      
      self.masses = masses
      
      self.tags = datacards

      self.Method = Method
      self.Options = Options
      self.Batch = Batch

      self.Snapshot = Snapshot

      self.Seed = Seed

      self.combinedCards = []
      self.workspaceFile = []


      print 'Configuration for Combination ========================='
      print 'Stat only'.ljust(20),    self.StatOnlyLabel
      print 'Channel'.ljust(20),    self.Ch
      print 'Year'.ljust(20),        self.Year
      print 'Run'.ljust(20),        self.Run
      print 'Method'.ljust(20),    self.Method

    def SetMass(self, mass):
      if mass in masses:
        self.masses = [mass]
      else:
        raise Exception('SetMass to %s'%mass)

    #def CombineCards(self, doRun):
    #  if not os.path.isdir(base_dir + 'combinedCards'):
    #    os.mkdir(base_dir + 'combinedCards')
    #  for mass in self.masses:
    #    cards = collections.OrderedDict()
    #    combName= base_dir + 'combinedCards/M' + mass
    #    for year in self.Year:
    #      combName = combName + 'Y'+year
    #      for ch in self.Ch:
    #        #combName += ch
    #        processName = 'Y'+year+'__'+ch
    #        if 'dbl' in ch:
    #          tmp_variableName = variableName[2]
    #        elif (mass > "125" and "3b" in ch):
    #          tmp_variableName = variableName[1]
    #        else:
    #          tmp_variableName = variableName[0]
    #        if '3b' in ch and 'dbl' not in ch:
    #          tmp_variableName += '_down_type_jet_b_tagged'
    #        cardDir = dirBase[year]+'/Datacards'+'/'+ch+'/'+tmp_variableName
    #        if 'dbl' in ch:
    #          mass_suffix = ''
    #        else:
    #          mass_suffix = '_CHToCB_M{MASS}'.format(MASS=mass)
    #        cardName= '{DIR}/datacard{SUFFIX}.txt'.format(DIR=cardDir,SUFFIX=mass_suffix)
    #        #print processName
    #        #print cardName
    #        cards[processName]=cardName
    #    cmd = 'combineCards.py '
    #    for process in cards:
    #      #print process, cards[process]
    #      cmd = cmd + ' ' + process + '=' + cards[process]
    #    cmd += ' > ' + combName + '.txt'
    #    if doRun:
    #      print 'cmd', cmd
    #      os.system(cmd)
    #    else:
    #      print 'cmd', cmd
    #      
    #    self.combinedCards.append(combName+'.txt')
                    
    def CombineCards(self, tag, mass, doRun):
      self.combinedCards = []
      if not os.path.isdir(base_dir + 'combinedCards'):
        os.mkdir(base_dir + 'combinedCards')
      if not os.path.isdir(base_dir + 'combinedCards/' + tag) and tag in self.tags:
        os.mkdir(base_dir + 'combinedCards/' + tag)
      cards = collections.OrderedDict()
      combName= base_dir + 'combinedCards/' + tag + '/M' + mass
      for year in self.tags[tag][mass]:

        if year not in self.Year:
          continue
        for data_card in self.tags[tag][mass][year]:
          ch = data_card.split('/')[-3]
          var = data_card.split('/')[-2]
          if 'not_b_tagged' in var:
            processName = 'Y'+year+'__'+ch+'__'+'Hplus_0b'
          else:
            processName = 'Y'+year+'__'+ch
          if 'Y'+year not in combName:
            combName    += 'Y'+year
          cards[processName]=data_card

      cmd = 'combineCards.py '
      for process in cards:
        #print process, cards[process]
        cmd += ' ' + process + '=' + cards[process]
      cmd += ' > ' + combName + '.txt'
      if doRun:
        print 'cmd', cmd
        os.system(cmd)
      else:
        print 'cmd', cmd
        
      self.combinedCards.append(combName+'.txt')

    #def Text_to_Workspace(self, doRun=False):
    #  if not os.path.isdir(base_dir + 'workspace'):
    #    os.mkdir(base_dir + 'workspace')

    #  for card in self.combinedCards:
    #    for mass in self.masses:
    #      if 'M'+mass in card:
    #        massf = int(float(mass))
    #        print 'making workspace for',card,'mass', massf
    #        #example:
    #        #text2workspace.py CHToCB_datacard_CH090_0.35_0.40.txt -P HiggsAnalysis.CombinedLimit.ChargedHiggs:brChargedHiggsCB -o ../workspace/mu_90_0.35_0.40_stat.root -m 90
    #        command_template = "text2workspace.py %s -P %s -o %s -m %i"
    #        arg1 = card
    #        arg2 = "HiggsAnalysis.CombinedLimit.ChargedHiggsCB:brChargedHiggsCB"
    #        arg3 = base_dir + 'workspace/' + card.split('combinedCards/')[-1] + '.root'
    #        arg4 = massf
    #        command = command_template%(arg1,arg2,arg3,arg4)
    #    #### scaling constraint
    #    #command += " --X-rescale-nuisance 'CMS*' 0.5"
    #    self.workspaceFile.append(arg3)
    #    if doRun:
    #          os.system(command)
    #    else:
    #          print 'cmd',command

    def Text_to_Workspace(self, tag, mass, doRun):
      self.workspaceFile = []
      if not os.path.isdir(base_dir + 'workspace'):
        os.mkdir(base_dir + 'workspace')
      if not os.path.isdir(base_dir + 'workspace/' + tag) and tag in self.tags:
        os.mkdir(base_dir + 'workspace/' + tag)

      for card in self.combinedCards:
        if 'M'+mass in card:
          massf = int(float(mass.replace('_yield','')))
          print 'making workspace for',card,'mass', massf
          #example:
          #text2workspace.py CHToCB_datacard_CH090_0.35_0.40.txt -P HiggsAnalysis.CombinedLimit.ChargedHiggs:brChargedHiggsCB -o ../workspace/mu_90_0.35_0.40_stat.root -m 90
          command_template = "text2workspace.py %s -P %s -o %s -m %i --channel-masks"
          arg1 = card
          arg2 = "HiggsAnalysis.CombinedLimit.ChargedHiggsCB:brChargedHiggsCB"
          arg3 = base_dir + 'workspace/'+ tag + '/' + card.split('combinedCards/' + tag +'/')[-1] + '.root'
          arg4 = massf
          command = command_template%(arg1,arg2,arg3,arg4)
        #### scaling constraint
        #command += " --X-rescale-nuisance 'CMS*' 0.5"
        self.workspaceFile.append(arg3)
        if doRun:
              os.system(command)
        else:
              print 'cmd',command



    #def Combine(self,doRun=False):
    #  if not os.path.isdir(base_dir + 'combine'):
    #    os.mkdir(base_dir + 'combine')
    #  #example:
    #  #combine ../workspace/mu_90_0.35_0.40_stat.root -M AsymptoticLimits  --cminDefaultMinimizerType Minuit2 --rAbsAcc 0.000001 --mass 90 --name CHlimit_mu_90_0.35_0.40 | tee res_mu_90_0.35_0.40_stat.out
    #  #command_template = "combine %s --mass %d --name %s "
    #  command_template = "combine -d %s --mass %d --name %s "
    #  #FIXME
    #  #command_template = "combine harvest install %s --mass %d --name %s "
    #  for workspace in self.workspaceFile:
    #    for mass in self.masses:
    #      if 'M'+mass in workspace:
    #        print workspace
    #        arg1 = workspace
    #        arg2 = float(mass)
    #        name = workspace.split('/')[-1]
    #        name = name.split('.txt.root')[0]
    #        if ' --singlePoint ' in self.Options:
    #          name += '.r' + self.Options.split(' --singlePoint ')[1].split(' ')[0]
    #        print name
    #        arg3 =name
    #        if self.StatOnly != '':
    #          arg3 += '_' + self.StatOnlyLabel
    #        if self.RunLabel != '':
    #          arg3 += '_' + self.RunLabel
    #        if self.Snapshot:
    #          snapshot_option = '{BASE_DIR}/combine/higgsCombine{NAME}.MultiDimFit.mH{MASS}.root'.format(BASE_DIR=base_dir,NAME=name,MASS=int(mass)) 
    #          snapshot_option += ' --snapshotName "MultiDimFit"' 
    #          command = command_template%(snapshot_option,arg2,arg3)
    #        else:
    #          command = command_template%(arg1,arg2,arg3)
    #        #########
    #        #options = "-M FitDiagnostics --plots --saveShapes"
    #        #options = "-M FitDiagnostics --plots --saveShapes --saveWithUncertainties"
    #        #options += " -t -1 --expectSignal 0"
    #        #--cminDefaultMinimizerTolerance arg (=0.10000000000000001)
    #        #options += " --cminPoiOnlyFit"
    #        #options += " --stepSize 0.01 --maxFailedSteps 10"
    #        #options += " --cminDefaultMinimizerTolerance 0.1"
    #        #options += " --robustHesse 1"
    #        #options += " --cminPreScan --cminPreFit 1"
    #        #options += " --keepFailures --saveNLL" 
    #        #options += " --preFitValue 0"
    #        #options += " --cminPreScan --cminSingleNuisFit "
    #        #########
    #        #options = "-M ChannelCompatibilityCheck"
    #        #########
    #        #options = '-M HybridNew --LHCmode LHC-limits'
    #        #method = '-M '+self.Method
    #        # --rAbsAcc arg (=0.00050000000000000001)
    #        # --rRelAcc arg (=0.0050000000000000001)
    #        #options +=' --rAbsAcc 0.1 --rRelAcc 0.005000000000000001'
    #        #options += " --cminPreScan --cminSingleNuisFit "
    #        #options += ' -t -1 '
    #        #options += ' --toysFrequentist'
    #        #########
    #        #options = "-M MultiDimFit --robustFit=1 "
    #        #########
    #        command += '-M ' +  self.Method + ' ' + self.Options + ' '+ self.Batch.format(MASS=mass)
    #        command += ' -s ' + self.Seed
    #        if ' -t ' in self.Options:
    #          pipe_line = "| tee %s/combine/res_%s.%s.mH%s.out"%(base_dir,name,self.Method,str(arg2).split('.0')[0]+'.{SEED}'.format(SEED=self.Seed))
    #        else:
    #          pipe_line = "| tee %s/combine/res_%s.%s.mH%s.out"%(base_dir,name,self.Method,str(arg2).split('.0')[0])
    #        command += pipe_line
    #        if doRun:
    #          os.system(command)
    #        else:
    #          print(command)
    #          print arg3
    #        #higgsCombineM090Y2017Mu2b3bEl2b3b.AsymptoticLimits.mH90.root
    #        rootFileName = 'higgsCombine'+arg3+'.'+self.Method+'.mH'+str(arg2).split('.0')[0]+'.{SEED}'.format(SEED=self.Seed)+'.root'
    #        #print rootFileName
    #        os.system('mv '+rootFileName +' %s/combine/'%base_dir)
    #        if self.Method=='FitDiagnostics':
    #          os.system('mv %s %s/combine/'%('fitDiagnostics'+arg3+'.root',base_dir))

    def Combine(self, tag, mass, doRun):
      if not os.path.isdir(base_dir + 'combine/' + tag):
        os.mkdir(base_dir + 'combine/' + tag)
      #example:
      #combine ../workspace/mu_90_0.35_0.40_stat.root -M AsymptoticLimits  --cminDefaultMinimizerType Minuit2 --rAbsAcc 0.000001 --mass 90 --name CHlimit_mu_90_0.35_0.40 | tee res_mu_90_0.35_0.40_stat.out
      #command_template = "combine %s --mass %d --name %s "
      command_template = "combine -d %s --mass %d --name %s "
      #FIXME
      #command_template = "combine harvest install %s --mass %d --name %s "
      for workspace in self.workspaceFile:
        if 'M'+mass in workspace:
          print workspace
          arg1 = workspace
          arg2 = float(mass.replace('_yield',''))
          name = workspace.split('/')[-1]
          name = name.split('.txt.root')[0]
          if ' --singlePoint ' in self.Options:
            name += '.r' + self.Options.split(' --singlePoint ')[1].split(' ')[0]
          print name
          arg3 =name
          if self.StatOnly != '':
            arg3 += '_' + self.StatOnlyLabel
          if self.RunLabel != '':
            arg3 += '_' + self.RunLabel
          if self.Snapshot:
            snapshot_option = '{BASE_DIR}/combine/'+tag+'/higgsCombine{NAME}.MultiDimFit.mH{MASS}.root'.format(BASE_DIR=base_dir,NAME=name,MASS=int(mass)) 
            snapshot_option += ' --snapshotName "MultiDimFit"' 
            command = command_template%(snapshot_option,arg2,arg3)
          else:
            command = command_template%(arg1,arg2,arg3)
          #########
          #options = "-M FitDiagnostics --plots --saveShapes"
          #options = "-M FitDiagnostics --plots --saveShapes --saveWithUncertainties"
          #options += " -t -1 --expectSignal 0"
          #--cminDefaultMinimizerTolerance arg (=0.10000000000000001)
          #options += " --cminPoiOnlyFit"
          #options += " --stepSize 0.01 --maxFailedSteps 10"
          #options += " --cminDefaultMinimizerTolerance 0.1"
          #options += " --robustHesse 1"
          #options += " --cminPreScan --cminPreFit 1"
          #options += " --keepFailures --saveNLL" 
          #options += " --preFitValue 0"
          #options += " --cminPreScan --cminSingleNuisFit "
          #########
          #options = "-M ChannelCompatibilityCheck"
          #########
          #options = '-M HybridNew --LHCmode LHC-limits'
          #method = '-M '+self.Method
          # --rAbsAcc arg (=0.00050000000000000001)
          # --rRelAcc arg (=0.0050000000000000001)
          #options +=' --rAbsAcc 0.1 --rRelAcc 0.005000000000000001'
          #options += " --cminPreScan --cminSingleNuisFit "
          #options += ' -t -1 '
          #options += ' --toysFrequentist'
          #########
          #options = "-M MultiDimFit --robustFit=1 "
          #########
          command += '-M ' +  self.Method + ' ' + self.Options + ' '+ self.Batch.format(MASS=mass)
          command += ' -s ' + self.Seed
          if doRun:
            os.system(command)
          else:
            print(command)
            print arg3
          #higgsCombineM090Y2017Mu2b3bEl2b3b.AsymptoticLimits.mH90.root
          rootFileName = 'higgsCombine'+arg3+'.'+self.Method+'.mH'+str(arg2).split('.0')[0]+'.{SEED}'.format(SEED=self.Seed)+'.root'
          #print rootFileName
          os.system('mv '+rootFileName +' %s/combine/%s'%(base_dir,tag))
          if self.Method=='FitDiagnostics':
            os.system('mv %s %s/combine/%s'%('fitDiagnostics'+arg3+'.root',base_dir,tag))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TrueOrNotTrue')
    parser.add_argument('-StatOnly',help="False or True", default=False, type=bool)
    parser.add_argument('-Ch',help="Mu of El", default='All')
    parser.add_argument('-Year',help="Which year to use", default='All')
    parser.add_argument('-combineCards',help="combine data cards", action='store_true')
    parser.add_argument('-text2workspace',help="run text2workspace script", action='store_true')
    parser.add_argument('-M',help="Method to use", default='AsymptoticLimits')
    parser.add_argument('-options',help="options to use", default=' ')
    parser.add_argument('-batch',help="options to use", default=' ')
    parser.add_argument('-run',help="blind?", default='')
    parser.add_argument('-snapshot',help="using snapshot", action='store_true')

    args = parser.parse_args()
    StatOnly=args.StatOnly
    Ch=args.Ch
    Year=args.Year
    combineCards = args.combineCards
    text2workspace = args.text2workspace
    Method=args.M
    Options=args.options
    Batch=args.batch
    Run=args.run
    Snapshot=args.snapshot

    print 'Set up parameters =========================================='
    print 'StatOnly:'.ljust(20),StatOnly
    print 'Lepton Flavor:'.ljust(20),Ch
    print 'Year:'.ljust(20),Year
    print 'Method:'.ljust(20),Method
    print 'Run:'.ljust(20),Run

    s = LimitCalc(StatOnly,Ch,Year,Method,Options,Batch,Run,Snapshot)
    s.CombineCards(combineCards)
    s.Text_to_Workspace(text2workspace)
    s.Combine(True)
