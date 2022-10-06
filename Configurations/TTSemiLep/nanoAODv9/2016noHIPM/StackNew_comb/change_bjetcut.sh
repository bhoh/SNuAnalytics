#sed -i 's/(nBJets_WP_M + nBJets_WP_M_20to30)/(nBJets_WP_M)/g' cuts*.py QCD_ABCD/cuts*.py
#sed -i 's/(nBJets_WP_M)/(nBJets_WP_M + nBJets_WP_M_20to30)/g' cuts*.py QCD_ABCD/cuts*.py
#sed -i 's/(nCleanJet30_2p4+nCleanJet20to30_2p4_PU_M)/(nCleanJet30_2p4)/g' cuts*.py QCD_ABCD/cuts*.py
#sed -i 's/(status_nom==0)/(status_nom>=0 \&\& chi2_nom<50.)/g' variables*.py QCD_ABCD/variables*.py
sed -i 's/(status_nom>=0 \&\& chi2_nom<50.)/(status_nom==0)/g' variables*.py QCD_ABCD/variables*.py
