
Sites = {

  'iihe' : { 
              'lsCmd'       : 'ls' ,
              'mkDir'       : False , 
              'xrootdPath'  : 'dcap://maite.iihe.ac.be/' ,
              'srmPrefix'   : 'srm://maite.iihe.ac.be:8443' ,
              'treeBaseDir' : '/pnfs/iihe/cms/store/user/xjanssen/HWWNano/' ,
              'batchQueues' : ['localgrid@cream02']
           } ,

  'cern' : {
              'lsCmd'       : 'ls' ,
              'mkDir'       : True ,
              'xrootdPath'  : 'root://eoscms.cern.ch/' ,
              'treeBaseDir' : '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/' ,
              'batchQueues' : ['8nh','1nd','2nd','1nw']
           } ,

  'sdfarm' : {
              'lsCmd'       : 'ls' ,
              'slc_ver'     :  7,
              'mkDir'       : False ,
	      'xrootdPath'  : 'root://cms-xrdr.private.lo:2094/',
              'treeBaseDir' : '/xrootd/store/user/bhoh/Latino/HWWNano/',
             } ,
              #'lsCmd'       : 'xrdfs cms-xrdr.sdfarm.kr ls' ,
              #'xrootdPath'  : 'root://cms-xrdr.private.lo:2094/', inside of Korean farm
	      #'xrootdPath'  : 'root://cms-xrdr.sdfarm.kr:1094/', outside of Korean farm
              #'treeBaseDir' : '/xrd/store/user/jhchoi/Latino/HWWNano/', condor access
              #'treeBaseDir' : '/xrootd/store/user/jhchoi/Latino/HWWNano/', prompt access


  'ifca' : {
              'lsCmd'       : 'ls' ,
              'mkDir'       : True ,
              'xrootdPath'  : '' ,
              'srmPrefix'   : 'srm://srm01.ifca.es' ,
              'treeBaseDir' : '/gpfs/projects/tier3data/LatinosSkims/RunII/Nano/' ,
             }

}
