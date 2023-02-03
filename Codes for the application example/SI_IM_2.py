'''This code simulates the concentration profiles of the substrates
inside the pore.'''

def Reaction_rates(S1,S2,S3,EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,counter):    
    import numpy as np
    from scipy.integrate import odeint
    import math as mt
    import scipy.optimize as opt
    import pylab
    from scipy.integrate import solve_bvp
    import matplotlib.pyplot as plt
    import math
    import globalvar
    import scipy.interpolate as inter

    S10 = S1
    S20 = S2 
    S30 = S3
    
    x = np.linspace(0,L,50)

    def Differential_equations(x,Y):
        dY220dx = Y[1]
        dY221dx = 1/D2 * EB * Y[0] * kB 
        dYdx = [dY220dx,dY221dx]
        return(dYdx)
    
    def Boundary_conditions(Ybc0,YbcL):      
        Y220_0,Y221_0 = Ybc0
        Y220_L,Y221_L = YbcL
        return(Y220_0-S20,Y221_L)
    
    sol = solve_bvp(Differential_equations, Boundary_conditions, x, [globalvar.Y220i,globalvar.Y221i], max_nodes=1000)
    
    Y220,Y221 = sol.y
    
    if counter < 10:
        f4 = inter.interp1d(sol.x,sol.y[0,:])
        f5 = inter.interp1d(sol.x,sol.y[1,:])
        globalvar.Y220i = f4(x)
        globalvar.Y221i = f5(x)

    if sol.status != 0: 
        globalvar.stop = 1

    vII = -A * D2 * Y221[0] * Np / 2

    return(vII)