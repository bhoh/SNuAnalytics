# Use: python importPars.py <card to make workspace and manipulate> <file1 with fit result> <file2 with fit result> ...
# Example: python importPars.py /path/to/SRfit/card.txt /path/to/CRfit/fitDiagnostics.root 

import sys, subprocess, ROOT

def importPars(incard,fitresult,toDrop,mass):
    # First convert the card
    outFileName = "morphedWorkspace_fitDiagnostics{}.root".format(str(mass))
    origFileName = "origWorkspace_fitDiagnostics{}.root".format(str(mass))
    subprocess.call(['cp {} {}'.format(incard, outFileName)],shell=True)
    subprocess.call(['cp {} {}'.format(incard, origFileName)],shell=True)

    # Open new workspace
    w_f = ROOT.TFile.Open(outFileName, 'UPDATE')
    w = w_f.Get('w')

    print ('Importing '+fitresult+' ...')
    # Open fit result we want to import
    fr_f = ROOT.TFile.Open(fitresult)
    fr = fr_f.Get('fit_b') # b-only fit result (fit_s for s+b)
    myargs = fr.floatParsFinal()

    for i in range(myargs.getSize()):
        var = myargs.at(i)
        #if var.GetName() in toDrop: continue
        #if 'prop_bin' in var.GetName(): continue

        print (var.GetName())

        if not w.allVars().contains(var):
            print ('WARNING: Could not find %s'%var.GetName())
        else:
            var_to_change = w.var(var.GetName())
            print ('\tBefore:    %.2f +/- %.2f (%.2f,%.2f)'%(var_to_change.getValV(),var_to_change.getError(),var_to_change.getMin(),var_to_change.getMax()))
            var_to_change.setMin(var.getMin())
            var_to_change.setMax(var.getMax())
            var_to_change.setVal(var.getValV())
            var_to_change.setError(var.getError())
            
            print ('\tChange to: %.2f +/- %.2f (%.2f,%.2f)'%(var.getValV(),var.getError(),var.getMin(),var.getMax()))
            print ('\tAfter:     %.2f +/- %.2f (%.2f,%.2f)'%(var_to_change.getValV(),var_to_change.getError(),var_to_change.getMin(),var_to_change.getMax()))

    w_f.WriteTObject(w,'w',"Overwrite")
    w_f.Close()

if __name__ == "__main__":
    incard = sys.argv[1]
    fit_result = sys.argv[2]
    toDrop = sys.argv[3].split(',')
    mass = sys.argv[4]
    importPars(incard,fit_result,toDrop,mass)
