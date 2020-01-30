
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

variables['I_H_w_hBkkk'] = {
    'name' : 'I_H_w_hB',
    'range':(50,-10, 10),
    'xaxis':'1',
    'fold': 0
}
variables['I_H_w_B'] = {
    'name' : 'I_H_w_B',
    'range':(50,-10, 10),
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
