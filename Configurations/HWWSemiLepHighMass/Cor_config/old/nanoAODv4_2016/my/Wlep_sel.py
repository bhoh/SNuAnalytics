Mw='(80.4)'
mu='(pow('+Mw+',2)/2'+'Lepton_pt[0]*MET_pt*cos(MET_phi-Lepton_phi[0]))'
Lepton_pz='(Lepton_pt[0]*sinh(Lepton_eta[0]))'
lepton_E ='(Lepton_pt[0]*cosh(Lepton_eta[0]))'
Wlep_pz_1='('+mu+'*'+Lepton_pz+'/pow(Lepton_pt[0],2))'
Wlep_pz_2='(sqrt(   (pow('+mu+'*'+Lepton_pz+'/(pow(Lepton_pt[0],2)),2 ) -  (pow('+lepton_E+'*'+'MET_pt,2)-'+mu+')/pow(Lepton_pt[0],2) )      ))'

sol1='('+Wlep_pz_1+'+'+Wlep_pz_2+')'
sol2='('+Wlep_pz_1+'-'+Wlep_pz_2+')'
sol1small='('+sol1+'<'+sol2+')'
sol2small='('+sol1+'>'+sol2+')'
Wlep_pz='('+sol1small+'*'+sol1+'+'+sol2small+'*'+sol2+')'



