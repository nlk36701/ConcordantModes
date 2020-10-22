import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

"""
    This class may be used to convert a cartesian F-matrix to an internal F-Matrix,
    and vice versa. 
"""

class F_conv(object):
    def __init__(self, F, s_vec, zmat, coord, Print):
        self.F = F
        self.s_vec = s_vec
        self.zmat = zmat
        self.coord = coord
        self.Print = Print
        """ 
            This constant is from:
            https://physics.nist.gov/cgi-bin/cuu/Value?hr 
            If this link dies, find the new link on NIST
            for the Hartree to Joule conversion and pop
            it in there.
            There is a standard uncertainty of 0.0000000000085
            to this value.
        """
        self.mdyne_Hart = 4.3597447222071
        """
            Standard uncertainty of 0.00000000080
        """
        self.Bohr_Ang = 0.529177210903

    def run(self):
        """
            First construct the transpose of the A matrix. This could potentially be passed into the TransDisp.py
            class, rather than recomputing the A matrix. Or perhaps I could make the A-matrix its own module, 
            so that in the future intensities could be computed.
        """
        if self.coord.lower() == "internal":
            """ 
                So, the force constants must have the proper units off the bat to convert properly. 
                Moving from carts to internals, the cartesians must be in units of mdyn/Ang, which
                is then converted to Hartree/bohr^2
            """ 
            # self.F /= self.Bohr_Ang**2
            # self.F *= self.mdyne_Hart
            G = np.dot(self.s_vec.B,self.s_vec.B.transpose())
            self.A_T = np.dot(inv(G),self.s_vec.B)
            self.F = np.einsum('ia,jb,ab->ij',self.A_T,self.A_T,self.F)
            if self.Print:
                self.N = len(self.zmat.atomList)*3 - 6
                self.Print_const()
        elif self.coord.lower() == "cartesian":
            self.F = np.einsum('ai,bj,ab->ij',self.s_vec.B,self.s_vec.B,self.F)
            """ These force constants are converted from Hartree/bohr^2 to mdyne/Ang """
            # self.F /= self.Bohr_Ang**2
            # self.F *= self.mdyne_Hart
            if self.Print:
                self.N = len(self.zmat.atomList)*3
                self.Print_const()
        
    def Print_const(self):
        FC_output = ''
        FC_output += '{:5d}{:5d}\n'.format(len(self.zmat.atomList),self.N)
        self.F_print = self.F.copy()
        self.F_print = self.F_print.flatten()
        for i in range(len(self.F_print)//3):
            FC_output += '{:20.10f}'.format(self.F_print[3*i])
            FC_output += '{:20.10f}'.format(self.F_print[3*i+1])
            FC_output += '{:20.10f}'.format(self.F_print[3*i+2])
            FC_output += '\n'
        if len(self.F_print)%3:
            for i in range(len(self.F_print)%3):
                FC_output += '{:20.10f}'.format(self.F_print[3*(len(self.F_print)//3) + i])
            FC_output += '\n'
        with open('output.default.hess','w') as file:
            file.write(FC_output)
                




