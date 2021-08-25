class Options(object):
    def __init__(self, **kwargs):
        self.basis = kwargs.pop('basis', "cc-pVDZ")
        self.calc = kwargs.pop('calc',True)
        self.cartCoords = kwargs.pop('cartCoords', "Bohr")
        self.cartInsert = kwargs.pop('cartInsert',-1)
        self.charge = kwargs.pop('charge', 0)
        self.coords = kwargs.pop('coords', "ZMAT")
        self.disp = kwargs.pop('disp', 0.01)
        self.dispCheck = kwargs.pop('dispCheck',False)
        self.dispTol = kwargs.pop('dispTol',0.0)
        self.energyRegex = kwargs.pop('energyRegex','')
        self.geomCheck = kwargs.pop('geomCheck',False)
        self.mode_coupling_check = kwargs.pop('mode_coupling_check', False)
        self.nslots = kwargs.pop("nslots", 1)
        self.off_diag = kwargs.pop('off_diag', False)
        self.off_diag_bands = kwargs.pop('off_diag_bands', 1)
        self.off_diag_limit = kwargs.pop('off_diag_limit', False) 
        self.printout_rel_e = kwargs.pop('printout_rel_e', True)
        self.program = kwargs.pop('program', "molpro@2010.1.67+mpi")
        self.projTol = kwargs.pop('projTol',1.0e-14)
        self.queue = kwargs.pop("queue", "gen4.q")
        self.reducedDisp = kwargs.pop('reducedDisp',False)
        self.spin = kwargs.pop('spin', 1)
        self.successRegex = kwargs.pop('successRegex','')
        self.tightDisp = kwargs.pop('tightDisp',False)
        self.tol = kwargs.pop('tol',1.0e-14)
        self.units = kwargs.pop('units','HartreeBohr')
        ## These options may be helpful in the future for porting over to Sapelo
        # self.cluster = kwargs.pop("cluster", "").upper()
        # self.wait_time = kwargs.pop("wait_time", None)
        # self.time_limit = kwargs.pop("time_limit", None)
