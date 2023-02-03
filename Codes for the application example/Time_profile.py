'''This code simulates the change of the concentrations of the substrates
in the batch reactor. SID alpha'''

def time_profile(EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,i):    
    import numpy as np
    from scipy.integrate import odeint
    import math as mt
    import scipy.optimize as opt
    import pylab
    import time
    import globalvar
    from scipy.integrate import solve_ivp

    Timesec1 = time.time()
    Timesec2 = time.time()+181
    counter = 0
    globalvar.stop = 1 
    solver_name = 'LSODA'
    status_ODE1 = 'ok'
    
    while globalvar.stop != 0 and counter < 4:
        globalvar.stop = 0
        Timesec1 = time.time()
        
        if counter == 10: 
            solver_name = 'LSODA'#'BDF'
        if counter == 20: 
            solver_name = 'LSODA'#'RK45'
    
        import SI_IM_1 as rr1
        import SI_IM_2 as rr2
        import I_V_1   as iv1    
        
        globalvar.Y110i,globalvar.Y111i,globalvar.Y210i,globalvar.Y211i,globalvar.Y220i,globalvar.Y221i,globalvar.Y320i,globalvar.Y321i,a1A,a2A = iv1.I_V_1(counter,L,S1o)
        
        def Material_balances(t,y):        
            S1 = y[0]
            S2 = y[1]
            S3 = y[2]
            v={}
            v[0] = rr1.Reaction_rates(S1,S2,S3,EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,counter)
            v[1] = rr2.Reaction_rates(S1,S2,S3,EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,counter)
            dS1dt = -v[0] 
            dS2dt = +v[0]-v[1] 
            dS3dt = v[1] 
            dSdt = [dS1dt, dS2dt, dS3dt]
            return(dSdt)
        
        Timesec2 = time.time()
        if Timesec2-Timesec1> 10: 
            continue
        
        t = np.linspace(0,tf,200)
        S0 = [S1o, 0.01, 0.01]
        sol = solve_ivp(Material_balances,[0,tf], S0, method=solver_name, t_eval=t)
        S1 = sol.y[0]
        S2 = sol.y[1]
        S3 = sol.y[2]

        results = sol.y[2, -1]
        yield1 = sol.y[2, -1]
        counter = counter + 1 
        pylab.savefig('Si_run{}_'.format(i)+'{}.PNG'.format(counter))
        if counter == 4: 
            status_ODE1 = 'Crashed'
            
        print('S3' ,file = open("si.txt", "w+"))
        print(sol.y[2,:] ,file = open("si.txt", "a"))
    
    return(sol.t,sol.y[0,:],sol.y[1,:],sol.y[2,:])