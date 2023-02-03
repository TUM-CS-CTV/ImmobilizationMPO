'''This code creates the initial values for the solve_bvp function. When
one initial value fails, other initial values are used.'''

def I_V_1(counter,L_ran, S1o_ran):     
    
    import numpy as np
    from scipy.integrate import odeint
    import math as mt
    import scipy.optimize as opt
    import pylab
    import globalvar
    import random
    
    L = L_ran
    S10 = S1o_ran
    S20 = 0.01
    S30 = 0.01
    globalvar.step1 = 50
    globalvar.step2 = 50
    zx = np.linspace(0,L,50)   
    temp = 1/random.uniform(1,99)*500/L**2
    
    a1A = temp
    b1A = -2*a1A*L
    c1A = S10
    
    a2A = -temp
    b2A = -2*a2A*L
    c2A = S20     
    
    if counter <= 1:
        Y110i = np.polyval([a1A,b1A,c1A], zx)
        Y111i = np.polyval([2*a1A,b1A], zx)
        Y210i = np.polyval([a2A,b2A,c2A], zx)
        Y211i = np.polyval([2*a2A,b2A], zx)
         
        Y220i = np.polyval([0], zx)
        Y221i = np.polyval([0], zx)
        Y320i = np.polyval([0], zx)
        Y321i = np.polyval([0], zx)
        
    if counter == 3: 
        Y110i = np.linspace(0,0,50)
        Y111i = np.linspace(0,0,50)  
        Y210i = np.linspace(0,0,50)
        Y211i = np.linspace(0,0,50)  
        Y220i = np.linspace(0,0,50)
        Y221i = np.linspace(0,0,50)  
        Y320i = np.linspace(0,0,50)
        Y321i = np.linspace(0,0,50)  
          
    if counter == 2: 
        T = L/random.uniform(1,10)
        a = 0.2*T
        b = 0.2*T/S10 
        Y110i = a/(zx+b)
        Y111i = -a/(zx+b)**2 
        Y210i = S10-a/(zx+b)
        Y211i = a/(zx+b)**2 
        Y220i = np.linspace(0,0,50)
        Y221i = np.linspace(0,0,50)  
        Y320i = np.linspace(0,0,50)
        Y321i = np.linspace(0,0,50) 
        
    if counter == 4: 
        Y110i=S10*(1-1/(1+np.exp(-25/L*zx)))*2
        Y111i = - (2*S10*25/L*np.exp(-25/L*zx))/((np.exp(25/L*zx)+1))**2
        Y210i= S10*(-1+1/(1+np.exp(-25/L*zx)))*2
        Y211i = (2*S10*25/L*np.exp(-25/L*zx))/((np.exp(25/L*zx)+1))**2
        Y220i = np.linspace(0,0,50)
        Y221i = np.linspace(0,0,50)  
        Y320i = np.linspace(0,0,50)
        Y321i = np.linspace(0,0,50) 
        
    if counter ==5: 
        Y110i=S10*(1-1/(1+np.exp(-25/L*zx)))*2
        Y111i = - (2*S10*25/L*np.exp(-25/L*zx))/((np.exp(25/L*zx)+1))**2
        Y210i = S10*(-1+1/(1+np.exp(-25/L*zx)))*2
        Y211i = (2*S10*25/L*np.exp(-25/L*zx))/((np.exp(25/L*zx)+1))**2
        Y220i = np.linspace(0,0,50)
        Y221i = np.linspace(0,0,50)  
        Y320i = np.linspace(0,0,50)
        Y321i = np.linspace(0,0,50)       
           
    if counter >=6: 
        Y110i = np.linspace(0,0,50)
        Y111i = np.linspace(0,0,50)  
        Y210i = np.linspace(0,0,50)
        Y211i = np.linspace(0,0,50)  
        Y220i = np.linspace(0,0,50)
        Y221i = np.linspace(0,0,50)  
        Y320i = np.linspace(0,0,50)
        Y321i = np.linspace(0,0,50)     

    return(Y110i,Y111i,Y210i,Y211i,Y220i,Y221i,Y320i,Y321i,a1A,a2A)