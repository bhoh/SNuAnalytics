from HiggsAnalysis.CombinedLimit.PhysicsModel import *


class BRChargedHiggsCB(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        self.modelBuilder.doVar('BR[0,0,0.005]');
        #self.modelBuilder.doVar('BR[0,0,0.05]'); #upper bound constrained from ttbar normalization
        self.modelBuilder.doSet('POI','BR')
        #self.modelBuilder.doVar('sqrtBR[0,0.00001,1]');
        #self.modelBuilder.doSet('POI','sqrtBR')
        isVcbModel = False  # consider H+(80GeV) as W+(80GeV) and find the best fit of Vcb
        self.modelBuilder.factory_('expr::Scaling_BR("@0", BR)')
        #self.modelBuilder.factory_('expr::Scaling_ttCH("(1-@0)*@0 * (2*364.35)", Scaling_BR)')
        if not isVcbModel:
          self.modelBuilder.factory_('expr::Scaling_ttCH("(1-@0)*@0 * (2 * 831.76 * 0.1080 * 3)", Scaling_BR)')
          self.modelBuilder.factory_('expr::Scaling_tt("(1-@0)*(1-@0)", Scaling_BR)')
        else:
          self.modelBuilder.factory_('expr::Scaling_ttCH("@0 * (364.35)", Scaling_BR)')
          self.modelBuilder.factory_('expr::Scaling_ttlj("(1-@0)", Scaling_BR)')
        #self.modelBuilder.factory_('expr::Scaling_tt_bb("(1-@0)*(1-@0)", Scaling_BR)')
        #self.modelBuilder.factory_('expr::Scaling_tt_cc("(1-@0)*(1-@0)", Scaling_BR)')
        #self.modelBuilder.factory_('expr::Scaling_tt_jj("(1-@0)*(1-@0)", Scaling_BR)')


        # Xsec
        #self.modelBuilder.doVar('r[1,0.001,10]'); # Xsec
        #self.modelBuilder.doSet('POI','r')
        #self.modelBuilder.factory_('expr::Scaling_ttCH("@0", r)')
        #self.modelBuilder.factory_('expr::Scaling_tt("(1-@0/(831.76 * 0.1080 * 3))/2+TMath::Sqrt(0.25-0.5*@0/(831.76 * 0.1080 * 3))", r)')


	self.processScaling = {
              'CHToCB_M075':'ttCH',
              'CHToCB_M080':'ttCH',
              'CHToCB_M085':'ttCH',
              'CHToCB_M090':'ttCH',
              'CHToCB_M100':'ttCH',
              'CHToCB_M110':'ttCH',
              'CHToCB_M120':'ttCH',
              'CHToCB_M130':'ttCH',
              'CHToCB_M140':'ttCH',
              'CHToCB_M150':'ttCH',
              'CHToCB_M160':'ttCH',
              'TT+':'tt',
              'TTLJ+':'ttlj',
              #'TT+bb':'tt_bb',
              #'TT+cc':'tt_cc',
              #'TT+jj':'tt_jj',
            }

        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):

        for prefix, model in self.processScaling.iteritems():
            if process.startswith(prefix):
                return 'Scaling_'+model

        return 1

brChargedHiggsCB = BRChargedHiggsCB()

