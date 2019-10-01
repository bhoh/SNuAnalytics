{
  TFile f("nanoLatino_nanoLatino_GluGluHToWWToLNuQQ_M2500__part0__HiMaSemiLep2017_MC.root");
  f.ls();
  Events->Draw("GenEvtFlag");
  c1->SaveAs("HiMassCtlPlots/GenEvtFlag.png");

  Events->Draw("GenDrAk8Lept","GenEvtFlag==1 && GenDrAk8Lept<5");
  c1->SaveAs("HiMassCtlPlots/GenDrAk8Lept_Flag1.png");

  Events->Draw("GenDrAk8Ak4","GenEvtFlag==1&&GenDrAk8Ak4<5");
  c1->SaveAs("HiMassCtlPlots/GenDrAk8Ak4_Flag1.png");

  Events->Draw("GenW_Ak8_mass","GenEvtFlag==1&&GenW_Ak8_mass<300");
  c1->SaveAs("HiMassCtlPlots/GenW_Ak8_mass_Flag1.png");

  Events->Draw("GenW_Lept_mass","GenEvtFlag==1&&GenW_Lept_mass<150");
  c1->SaveAs("HiMassCtlPlots/GenW_Lept_Flag1.png");

  Events->Draw("GenH_mass","GenEvtFlag==1");
  c1->SaveAs("HiMassCtlPlots/GenH_mass_Flag1.png");

  Events->Draw("GenW_Ak4_mass","GenEvtFlag==2&&GenW_Ak4_mass<500");
  c1->SaveAs("HiMassCtlPlots/GenW_Ak4_mass_Flag2.png");

  Events->Draw("GenW_Lept_mass","GenEvtFlag==2&&GenW_Lept_mass<150");
  c1->SaveAs("HiMassCtlPlots/GenW_Lept_Flag2.png");

  Events->Draw("GenH_mass","GenEvtFlag==2");
  c1->SaveAs("HiMassCtlPlots/GenH_mass_Flag2.png");

}

