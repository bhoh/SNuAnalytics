from HiggsAnalysis.CombinedLimit.PhysicsModel import *


class BRChargedHiggsCB(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        #self.modelBuilder.doVar('BR[0,0.0000000001,0.1]');
        self.modelBuilder.doVar('BR[0,0.0000001,1]');
        self.modelBuilder.doSet('POI','BR')
        #self.modelBuilder.doVar('sqrtBR[0,0.00001,1]');
        #self.modelBuilder.doSet('POI','sqrtBR')

        self.modelBuilder.factory_('expr::Scaling_BR("@0", BR)')
        #self.modelBuilder.factory_('expr::Scaling_ttCH("(1-@0)*@0 * (364.35 + 2*87.31)", Scaling_BR)')
        self.modelBuilder.factory_('expr::Scaling_ttCH("(1-@0)*@0 * (2*364.35)", Scaling_BR)')
        self.modelBuilder.factory_('expr::Scaling_tt("(1-@0)*(1-@0)", Scaling_BR)')
        #???    ((87.310)*2*(1-@0)*@0 + (364.35)*(1-@0)*@0)*(1 pb-1 signal sample)
        # A*(1-BR)*BR = Xsec
        # BR^2-BR+Xsec/A = 0, (BR-1/2)^2 = (1/4-Xsec/A), BR = 1/2 \pm sqrt(1/4-Xsec/A)
        #
        #self.modelBuilder.factory_('expr::Scaling_BR("@0*@0", sqrtBR)')
        #self.modelBuilder.factory_('expr::Scaling_ttCH("2 * (1-(@0))*(@0)", Scaling_BR)')
        #self.modelBuilder.factory_('expr::Scaling_tt("(1-(@0))*(1-(@0))", Scaling_BR)')

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
              'TT':'tt',
              'TT+bb':'tt',
              'TT+cc':'tt',
              'TT+jj':'tt',
            }

        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):

        for prefix, model in self.processScaling.iteritems():
            if process.startswith(prefix):
                return 'Scaling_'+model

        return 1

brChargedHiggsCB = BRChargedHiggsCB()

