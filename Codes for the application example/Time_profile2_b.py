'''This code simulates the change of the concentrations of the substrates
in the batch reactor. SID gamma'''

def time_profile2_b(EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,i):    
    import numpy as np
    from scipy.integrate import odeint
    import math as mt
    import scipy.optimize as opt
    import pylab
    import time
    import globalvar
    from scipy.integrate import solve_ivp

    Timesec3 = time.time()
    Timesec4 = time.time()+181
    counter = 0
    globalvar.stop = 1
    solver_name = 'LSODA'
    status_ODE2 = 'ok'
    
    while globalvar.stop != 0 and counter < 4:
        globalvar.stop = 0
        Timesec3 = time.time()
    
        if counter == 10: 
            solver_name = 'LSODA'#'BDF'
        if counter == 20: 
            solver_name = 'LSODA'#'RK45'   
    
        import C_IM_b as rr2
        import I_V_2_b   as iv2    
    
        globalvar.Y10i,globalvar.Y11i,globalvar.Y20i,globalvar.Y21i,globalvar.Y30i,globalvar.Y31i,a1C,a2C,a3C = iv2.I_V_2(counter,L,S1o)
        
        def Material_balances2(t,y):        
            X1 = y[0]
            X2 = y[1]
            X3 = y[2]
            v = rr2.Reaction_rates2(X1,X2,X3,EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,counter)
            dX1dt = -v[0] 
            dX2dt = +v[0]-v[1] 
            dX3dt = v[1] 
            dXdt = [dX1dt, dX2dt, dX3dt]
            return(dXdt)
       
        Timesec4 = time.time()
        if Timesec4-Timesec3> 10: 
            continue
        
        t = np.linspace(0,tf,200)
        S0 = [S1o, 0.01, 0.01]
        sol = solve_ivp(Material_balances2,[0,tf], S0, method=solver_name, t_eval=t)
        S1 = sol.y[0]
        S2 = sol.y[1]
        S3 = sol.y[2]
        
        counter = counter+1
        pylab.savefig('aCo_run{}_'.format(i)+'{}.PNG'.format(counter))

        results = sol.y[2, -1]
        yield2 = sol.y[2, -1]
        Timesec4 = time.time()
        
        if counter == 4: 
            status_ODE2 = 'Crashed'       
            
        print('S3' ,file = open("ci_AB.txt", "w+"))
        print(sol.y[2,:] ,file = open("ci_AB.txt", "a"))
        
    return(sol.t,sol.y[0,:],sol.y[1,:],sol.y[2,:])