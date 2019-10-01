{
  TFile f("nanoLatino_GluGluHToWWToLNuQQ_M4000__part6_Skim.root");
  f.ls();
  gSystem->Exec("mkdir CtrPlots");
  Events->Draw("IsFatSig");
  c1->SaveAs("CtrPlots/IsFatSig.png");
  Events->Draw("HlnFat_mass","IsFatSig && !IsFatTop");
  c1->SaveAs("CtrPlots/HlnFat_mass_sig.png");


}

