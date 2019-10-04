{
  TFile f("nanoLatino_GluGluHToWWToLNuQQ_M900__part1_Skim.root");
  //TFile f("nanoLatino_GluGluHToWWToLNuQQ_M2500__part0_Skim.root");
  //TFile f("nanoLatino_GluGluHToWWToLNuQQ_M4000__part6_Skim.root");
  f.ls();
  gSystem->Exec("mkdir CtrPlots");
  Events->Draw("IsFatSig");
  c1->SaveAs("CtrPlots/IsFatSig.png");

  Events->Draw("HlnFat_mass","IsFatSig && !IsFatTop");
  c1->SaveAs("CtrPlots/HlnFat_mass_sig.png");

  Events->Draw("WptOvHfatM","WptOvHfatM>0 && WptOvHfatM<1");
  c1->SaveAs("CtrPlots/WptOvHfatM.png");

  Events->Draw("WptOvHak4M","WptOvHak4M>0 && WptOvHak4M<1");
  c1->SaveAs("CtrPlots/WptOvHak4M.png");

  Events->Draw("Whad_mass","Whad_mass>50 && Whad_mass<250");
  c1->SaveAs("CtrPlots/Whad_mass.png");

  Events->Draw("Wlep_pt_PF","Wlep_pt_PF>100 && Wlep_pt_PF<1000");
  c1->SaveAs("CtrPlots/Wlep_pt_PF.png");

  Events->Draw("CleanFatJet_pt[0]","CleanFatJet_pt[0]>200 && CleanFatJet_pt[0]<1000");
  c1->SaveAs("CtrPlots/CleanFatJet_pt.png");

  Events->Draw("CleanFatJet_mass[0]","CleanFatJet_mass[0]>50 && CleanFatJet_mass[0]<250");
  c1->SaveAs("CtrPlots/CleanFatJet_mass.png");

  Events->Draw("Hlnjj_mass","IsJjSig && !IsJjTop");
  c1->SaveAs("CtrPlots/Hlnjj_mass_sig.png");

  Events->Draw("Wlep_mt","Wlep_mt >50 && Wlep_mt< 160");
  c1->SaveAs("CtrPlots/Wlep_mt.png");
  Events->Draw("Hlnjj_mt","Hlnjj_mt >50 && Hlnjj_mt< 2000");
  c1->SaveAs("CtrPlots/Hlnjj_mt.png");

}

