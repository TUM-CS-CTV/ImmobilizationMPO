'''This code simulates the change of the concentrations of the substrates
in the batch reactor. SID gamma'''

def time_profile(S1o_ran,tf_ran,EA_ran,EB_ran,Np_ran,L_ran,A_ran,D1_ran,D2_ran,D3_ran,kA_ran,kB_ran,i):    
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
    
        import C_IM2 as rr2
        import I_V_1   as iv2    
    
        globalvar.Y10i,globalvar.Y11i,globalvar.Y20i,globalvar.Y21i,globalvar.Y30i,globalvar.Y31i,a1C,a2C,a3C = iv2.I_V_1(counter,L_ran,S1o_ran)
        
        def Material_balances2(t,y):        
            X1 = y[0]
            X2 = y[1]
            X3 = y[2]
            v = rr2.Reaction_rates2(X1,X2,X3,S1o_ran,tf_ran,EA_ran,EB_ran,Np_ran,L_ran,A_ran,D1_ran,D2_ran,D3_ran,kA_ran,kB_ran,counter)
            dX1dt = -v[0] 
            dX2dt = +v[0]-v[1] 
            dX3dt = v[1] 
            dXdt = [dX1dt, dX2dt, dX3dt]
            return(dXdt)
       
        Timesec4 = time.time()
        if Timesec4-Timesec3> 10: 
            continue
        
        t = np.linspace(0,tf_ran,200)
        S0 = [S1o_ran, 0.01, 0.01]
        sol = solve_ivp(Material_balances2,[0,tf_ran], S0, method=solver_name, t_eval=t)
        S1 = sol.y[0]
        S2 = sol.y[1]
        S3 = sol.y[2]
        
        #"""    
        import matplotlib.pyplot as plt
        plt.figure(figsize=(9,8))
        plt.plot(sol.t,sol.y[0,:] ,'b', label='S$_1$')
        plt.plot(sol.t,sol.y[1,:] ,'r', label='S$_2$')
        plt.plot(sol.t,sol.y[2,:] ,'g', label='S$_3$')
        plt.xlabel('$\it{t}$ / (min)', fontsize=17)
        plt.ylabel('$\it{S}$$_i$ / (mM)', fontsize=17)
        plt.grid(False)
        plt.xticks(fontsize=17)
        plt.yticks(fontsize=17)
        plt.legend()
        plt.title('Co-immobilization ci-B/A: Iteration ' + str(i))
        if globalvar.stop == 1: 
           plt.title('Co-immobilization: CRASHED, WILL BE REPEATED, Iteration: '  + str(i))        
        #"""         
        counter = counter+1
        pylab.savefig('bCo_run{}_'.format(i)+'{}.PNG'.format(counter))
        plt.show()

        results = sol.y[2, -1]
        yield2 = sol.y[2, -1]
        Timesec4 = time.time()
        print(counter)
        
        if counter == 4: 
            status_ODE2 = 'Crashed'        
        
    return(results,a1C,a2C,a3C,status_ODE2,yield2)