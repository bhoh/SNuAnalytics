import os

print "run the significance plots from the TMVA out test tree"
#P_ggfh_points = ["400"]
P_ggfh_points = ["400","1500"]
#mass_points = ["200"]
mass_points = ["200","400","800","1000","1500","2000","3000","4000","5000"]
#W_reco = ["Bst"]
W_reco = ["Bst", "Res"]
for P_point in P_ggfh_points:
  print P_point
  for Wreco in W_reco:
    print Wreco
    for mass in mass_points:
      print "For mass:",mass
      label_bgEW  = Wreco+'P'+P_point+'mh'+mass+"bgEW"
      label_bgVbf = Wreco+'P'+P_point+'mh'+mass+"bgVbf"
      EWDirName  = "TMVAClassification_"+label_bgEW
      VbfDirName = "TMVAClassification_"+label_bgVbf

      # rm old directories
      os.system("rm -rf TMVAClassification")


      
      # For EW background
      #rmCmd = "rm -rf "+EWDirName
      #os.system(rmCmd)
      #mkdirCmd = 'mkdir -p TMVAClassification/plots'
      #os.system(mkdirCmd)
      #cmd_EW  = "root -l -q 'mvaeffscxxMod.C("+'"",'+'"Out_Roots_kd/out_train_2017_'+Wreco+"_Pggfh"+P_point+'_GgfM'+mass+'vsEW0p1.root",50,1)'+"'"
      ##cmd_EW  = "root -l -q 'mvaeffscxxMod.C("+'"",'+'"Out_Roots_Allp400p1500/out_train_2017_'+Wreco+"_Pggfh"+P_point+'_GgfM'+mass+'vsEW0p1.root",50,0.001)'+"'"
      #os.system(cmd_EW)
      #mvCmd = 'mv TMVAClassification '+EWDirName
      #os.system(mvCmd)

      ## For Vbf background
      rmCmd = "rm -rf "+VbfDirName
      os.system(rmCmd)
      mkdirCmd = 'mkdir -p TMVAClassification/plots'
      os.system(mkdirCmd)
      cmd_Vbf = "root -l -q 'mvaeffscxxMod.C("+'"",'+'"Out_Roots_kd/out_train_2017_'+Wreco+"_Pggfh"+P_point+'_GgfM'+mass+'vsVbfM'+mass+'.root",50,1)'+"'"
      #cmd_Vbf = "root -l -q 'mvaeffscxxMod.C("+'"",'+'"Out_Roots_Allp400p1500/out_train_2017_'+Wreco+"_Pggfh"+P_point+'_GgfM'+mass+'vsVbfM'+mass+'.root",50,0.001)'+"'"
      os.system(cmd_Vbf)
      mvCmd = 'mv TMVAClassification '+VbfDirName
      os.system(mvCmd)

