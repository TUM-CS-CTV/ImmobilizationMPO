'''This code simulates the concentration profiles of the substrates
inside the pore.'''

def Reaction_rates2(S1,S2,S3,EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,counter):  
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
        dY10dx = Y[1]
        dY11dx = 1/D1 * (EA/L * x)  * Y[0] * kA 
        dY20dx = Y[3]
        dY21dx = 1/D2 * (-EB/L * x + EB)  * Y[2] * kB   - 1/D2 * (EA/L * x)  * Y[0] * kA 
        dY30dx = Y[5]
        dY31dx = - 1/D3 * (-EB/L * x + EB) * Y[2] * kB 
        dYdx = [dY10dx, dY11dx, dY20dx, dY21dx, dY30dx, dY31dx]
        return(dYdx)
    
    def Boundary_conditions(Ybc0,YbcL):      
        Y10_0,Y11_0,Y20_0,Y21_0,Y30_0,Y31_0 = Ybc0
        Y10_L,Y11_L,Y20_L,Y21_L,Y30_L,Y31_L = YbcL
        return(Y10_0-S10,Y11_L,Y20_0-S20,Y21_L,Y30_0-S30,Y31_L)
    
    sol = solve_bvp(Differential_equations, Boundary_conditions, x, [globalvar.Y10i,globalvar.Y11i,globalvar.Y20i,globalvar.Y21i,globalvar.Y30i,globalvar.Y31i], max_nodes=1000)  
    
    Y10,Y11,Y20,Y21,Y30,Y31 = sol.y
    
    if counter < 5:
        f8 = inter.interp1d(sol.x,sol.y[0,:])
        f9 = inter.interp1d(sol.x,sol.y[1,:])
        f10 = inter.interp1d(sol.x,sol.y[2,:])
        f11 = inter.interp1d(sol.x,sol.y[3,:])
        f12 = inter.interp1d(sol.x,sol.y[4,:])
        f13 = inter.interp1d(sol.x,sol.y[5,:])
        globalvar.Y10i = f8(x)
        globalvar.Y11i = f9(x)
        globalvar.Y20i = f10(x)
        globalvar.Y21i = f11(x)
        globalvar.Y30i = f12(x)
        globalvar.Y31i = f13(x)
    
    if sol.status != 0: 
        globalvar.stop = 1

    vI = -A * D1 * Y11[0] * Np
    vII = A * D3 * Y31[0] * Np 

    return(vI,vII)