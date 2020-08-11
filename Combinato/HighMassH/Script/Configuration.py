##--
import os
import sys


##----Configurations
def LoadCardPath(): 
    #CMSSW=os.getenv('CMSSW_BASE')
    cardpath={
        '2016':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2016/Datacards_2016',
        '2017':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2017/Datacards_2017',
        '2018':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2018/Datacards_2018',

    }
    return cardpath
def LoadCutPath():
    cutspath={
        'Boosted':CMSSW+'/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/templates_jhchoi/cuts_Boosted_template.py',
        'Resolved':CMSSW+'/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/templates_jhchoi/cuts_Resolved_template.py',
    }
    return cutspath
def LoadMXPath():
    MXPath={
        'GGF':{
        '2016':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2016/MassPoints/List_MX.py',
        '2017':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2017/MassPoints/List_MX.py',
        '2018':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2018/MassPoints/List_MX.py',
        },
        'VBF':{
        '2016':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2016/MassPoints/List_MX_VBF.py',
        '2017':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2017/MassPoints/List_MX_VBF.py',
        '2018':'/cms/ldap_home/jhchoi/HWW_Analysis/slc7/ForShape/CMSSW_10_2_19/src/SNuAnalytics/Configurations/HWWSemiLepHighMass/Full_v6Production/ForAN/Final/DeepAK8WP2p5/2018/MassPoints/List_MX_VBF.py',
        }
    }
    return MXPath


def LoadConfiguration():

    variableForCR='Event'
    variableForSR='WW_mass'

    config={
        
        'Boosted':{
            'TOP':{
                'variable':variableForCR,
                'cuts':[
                    'eleCH__BoostedGGF__TOP__METOver40__PtOverM04__MEKDTAG___',
                    'eleCH__BoostedGGF__TOP__METOver40__PtOverM04__UNTAGGED___',
                    'eleCH__BoostedVBF__TOP__METOver40__PtOverM04___',
                    'muCH__BoostedGGF__TOP__METOver40__PtOverM04__MEKDTAG___',
                    'muCH__BoostedGGF__TOP__METOver40__PtOverM04__UNTAGGED___',
                    'muCH__BoostedVBF__TOP__METOver40__PtOverM04___',
                ],
            },
            'SB':{
                'variable':variableForCR,
                'cuts':[
                    'eleCH__BoostedGGF__SB__METOver40__PtOverM04__MEKDTAG___',
                    'eleCH__BoostedGGF__SB__METOver40__PtOverM04__UNTAGGED___',
                    'eleCH__BoostedVBF__SB__METOver40__PtOverM04___',
                    'muCH__BoostedGGF__SB__METOver40__PtOverM04__MEKDTAG___',
                    'muCH__BoostedGGF__SB__METOver40__PtOverM04__UNTAGGED___',
                    'muCH__BoostedVBF__SB__METOver40__PtOverM04___',
                    
                ],
            },             
            'SR':{
                'variable':variableForSR,
                'cuts':[
                    'eleCH__BoostedGGF__SR__METOver40__PtOverM04__MEKDTAG___',
                    'eleCH__BoostedGGF__SR__METOver40__PtOverM04__UNTAGGED___',
                    'eleCH__BoostedVBF__SR__METOver40__PtOverM04___',
                    'muCH__BoostedGGF__SR__METOver40__PtOverM04__MEKDTAG___',
                    'muCH__BoostedGGF__SR__METOver40__PtOverM04__UNTAGGED___',
                    'muCH__BoostedVBF__SR__METOver40__PtOverM04___',
                ],
            }
            
        },
        
        'Resolved':{
            'TOP':{
                'variable':variableForCR,
                'cuts':[
                    'eleCH__ResolvedGGF__TOP__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__MEKDTAG',
                    'eleCH__ResolvedGGF__TOP__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__UNTAGGED',
                    'eleCH__ResolvedVBF__TOP__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL',
                    'muCH__ResolvedGGF__TOP__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__MEKDTAG',
                    'muCH__ResolvedGGF__TOP__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__UNTAGGED',
                    'muCH__ResolvedVBF__TOP__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL',
                ],

            },
            'SB':{
                'variable':variableForCR,
                'cuts':[
                    'eleCH__ResolvedGGF__SB__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__MEKDTAG',
                    'eleCH__ResolvedGGF__SB__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__UNTAGGED',
                    'eleCH__ResolvedVBF__SB__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL',
                    'muCH__ResolvedGGF__SB__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__MEKDTAG',
                    'muCH__ResolvedGGF__SB__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__UNTAGGED',
                    'muCH__ResolvedVBF__SB__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL',
],
            },
            'SR':{
                'variable':variableForSR,
                'cuts':[
                    'eleCH__ResolvedGGF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__MEKDTAG',
                    'eleCH__ResolvedGGF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__UNTAGGED',
                    'eleCH__ResolvedVBF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL',
                    'muCH__ResolvedGGF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__MEKDTAG',
                    'muCH__ResolvedGGF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL__UNTAGGED',
                    'muCH__ResolvedVBF__SR__METOver30__PtOverM035__WlepMtOver50__WWMtOver60__ScoreALL',],
            }
        }
        
    }


    

    return config
###-----------------Function

def GetGGFMXList(Year):
    Year=str(Year)
    MXPath=LoadMXPath()
    handle=open(MXPath['GGF'][Year],'r')
    exec(handle)
    handle.close()
    return List_MX

def GetVBFMXList(Year):
    Year=str(Year)
    MXPath=LoadMXPath()
    handle=open(MXPath['VBF'][Year],'r')
    exec(handle)
    handle.close()
    return List_MX_VBF

#combineCards.py -S ${ARGUMENT}
if __name__ == '__main__':
    SetConfiguration()
