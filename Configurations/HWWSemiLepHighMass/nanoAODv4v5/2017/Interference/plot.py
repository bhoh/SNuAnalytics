
import os
import glob


#massesModelsFile = "massesModels.py"
#if os.path.exists(massesModelsFile) :
#  handle = open(massesModelsFile,'r')
#  exec(handle)
#  handle.close()
#else:
#  print "!!! ERROR file ", massesModelsFile, " does not exist."
#
#for MX in List_MX:
#  mass = str(MX)
#
#  plot['ggHWW_I_h_'+mass+'M'] = {
#                        'nameHR' : 'IHh'+mass,
#			'isSignal' : 1,
#			'color'    : 4,
#			'isData'   : 0,
#			'samples'  : ['ggHWW_I_h_'+mass+'M'],
#			'scale'    : 1,
#			}
#
#
#  plot['ggHWW_'+mass+'M'] = {
#                        'nameHR' : 'M'+mass,
#			'isSignal' : 1,
#			'color'    : 2,
#			'isData'   : 0,
#			'samples'  : ['ggHWW_'+mass+'M'],
#			'scale'    : 1,
#			}
#
#  plot['ggHWW_I_B_'+mass+'M'] = {
#                        'nameHR' : 'IHB'+mass,
#			'isSignal' : 1,
#			'color'    : 3,
#			'isData'   : 0,
#			'samples'  : ['ggHWW_I_B_'+mass+'M'],
#			'scale'    : 1,
#			}
#
#

plot['ggh125LNuQQ'] = {
                      'nameHR' : 'ggh0lnqq',
      		'isSignal' : 1,
      		'color'    : 1,
      		'isData'   : 0,
      		'samples'  : ['ggh125LNuQQ'],
      		'scale'    : 1,
      		}

plot['ggh125LNuQQ_SI'] = {
                      'nameHR' : 'ggh0lnqq_SandI',
      		'isSignal' : 1,
      		'color'    : 2,
      		'isData'   : 0,
      		'samples'  : ['ggh125LNuQQ_SI'],
      		'scale'    : 1,
      		}

plot['ggh125LNuQQ_I'] = {
                      'nameHR' : 'ggh0lnqq_I',
      		'isSignal' : 1,
      		'color'    : 3,
      		'isData'   : 0,
      		'samples'  : ['ggh125LNuQQ_I'],
      		'scale'    : 1,
      		}


plot['ggWW'] = {
                      'nameHR' : 'ggWW',
      		'isSignal' : 1,
      		'color'    : 4,
      		'isData'   : 0,
      		'samples'  : ['ggWW'],
      		'scale'    : 1,
      		}


legend['lumi'] = 'L = 41.5/fb'
#legend['lumi'] = 'Simulation'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
