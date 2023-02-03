'''This code simulates the concentration profiles of the substrates
inside the pore.'''

def Reaction_rates(S1,S2,S3,EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,counter):    
    import numpy as np
    from   scipy.integrate import odeint
    import math as mt
    import scipy.optimize as opt
    import pylab
    from   scipy.integrate import solve_bvp
    import matplotlib.pyplot as plt
    import math
    import globalvar
    import scipy.interpolate as inter
    
    S10 = S1
    S20 = S2 
    S30 = S3
    
    x = np.linspace(0,L,50)
    
    def Differential_equations(x,Y):
        dY110dx = Y[1]
        dY111dx = 1/D1 * EA * Y[0] * kA 
        dYdx = [dY110dx,dY111dx]
        return(dYdx)
    
    def Boundary_conditions(Ybc0,YbcL):      
        Y110_0,Y111_0 = Ybc0
        Y110_L,Y111_L = YbcL
        return(Y110_0-S10,Y111_L)
    
    sol = solve_bvp(Differential_equations, Boundary_conditions, x, [globalvar.Y110i,globalvar.Y111i], max_nodes=1000)
    Y110,Y111 = sol.y
    ya1,ya2 = sol.y
    
    if counter < 10:
        f0 = inter.interp1d(sol.x,sol.y[0,:])
        f1 = inter.interp1d(sol.x,sol.y[1,:])
        globalvar.Y110i = f0(x)
        globalvar.Y111i = f1(x)
    
    if sol.status != 0: 
        globalvar.stop = 1
    
    vI = -A * D1 * Y111[0] * Np  / 2

    return(vI)