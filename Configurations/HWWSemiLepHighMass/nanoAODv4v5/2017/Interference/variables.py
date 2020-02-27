
massesModelsFile = "massesModels.py"
if os.path.exists(massesModelsFile) :
  handle = open(massesModelsFile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", massesModelsFile, " does not exist."

#variables['GenRecH_m500'] = {
#    'name' : 'GenH_mass',
#    'range':(50,100, 1000),
#    'xaxis':'1',
#    'fold': 0
#}

variables['I_sigXh0_sigXww'] = {
    'name' : 'I_sigXh0_sigXww',
    'range':(50,-10, 10),
    'xaxis':'1',
    'fold': 0
}
variables['I_sigXh0'] = {
    'name' : 'I_sigXh0',
    'range':(50,-10, 10),
    'xaxis':'1',
    'fold': 0
}

variables['I_sigXww125'] = {
    'name' : 'I_sigXww125',
    'range':(50,-0.5, 0.5),
    'xaxis':'1',
    'fold': 0
}

variables['I_h0Xww'] = {
    'name' : 'I_h0Xww',
    'range':(50,-1, 5),
    'xaxis':'1',
    'fold': 0
}

variables['wwOVsig125'] = {
    'name' : 'wwOVsig125',
    'range':(50,-0.01, 0.2),
    'xaxis':'1',
    'fold': 0
}


variables['h0OVsig'] = {
    'name' : 'h0OVsig',
    'range':(50,-10, 10),
    'xaxis':'1',
    'fold': 0
}


variables['GenRecH_m125'] = {
    'name' : 'GenH_mass',
    'range':(50,10, 300),
    'xaxis':'1',
    'fold': 0
}

variables['GenRecH_m_wide'] = {
    'name' : 'GenH_mass',
    'range':(100,300, 5500),
    'xaxis':'1',
    'fold': 0
}

variables['GenRecH_m900'] = {
    'name' : 'GenH_mass',
    'range':(50,100, 1800),
    'xaxis':'1',
    'fold': 0
}

#variables['GenRecH_m2500'] = {
#    'name' : 'GenH_mass',
#    'range':(50,100, 3500),
#    'xaxis':'1',
#    'fold': 0
#}


variables['GenRecH_m4000'] = {
    'name' : 'GenH_mass',
    'range':(50,500, 5000),
    'xaxis':'1',
    'fold': 0
}

variables['Lep1_pt'] = {
    'name' : 'Lepton_pt[0]',
    'range':(50,0, 50),
    'xaxis':'1',
    'fold': 0
}

variables['Lep1_eta'] = {
    'name' : 'Lepton_eta[0]',
    'range':(50,-3, 3),
    'xaxis':'1',
    'fold': 0
}
variables['Lep2_pt'] = {
    'name' : 'Lepton_pt[1]',
    'range':(50,0, 50),
    'xaxis':'1',
    'fold': 0
}

variables['Lep2_eta'] = {
    'name' : 'Lepton_eta[1]',
    'range':(50,-3, 3),
    'xaxis':'1',
    'fold': 0
}
