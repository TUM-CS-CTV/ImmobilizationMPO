'''This code creates the initial values for the solve_bvp function. When
one initial value fails, other initial values are used.'''
def I_V_2(counter,L_ran, S1o_ran):     
    
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
    globalvar.step3 = 50
    yx = np.linspace(0,L,50)    
    temp = 1/random.uniform(1,99)*500/L**2
    
    a1C = temp
    b1C = -2*a1C*L
    c1C = S10
    
    a2C = -temp/2
    b2C = -2*a2C*L
    c2C = S20
    
    a3C = -temp/2
    b3C = -2*a3C*L
    c3C = S30
    
    if counter <= 1:

    
        Y10i = np.polyval([a1C,b1C,c1C], yx)
        Y11i = np.polyval([2*a1C,b1C], yx)
        Y20i = np.polyval([a2C,b2C,c2C], yx)
        Y21i = np.polyval([2*a2C,b2C], yx)
        Y30i = np.polyval([a3C,b3C,c3C], yx)
        Y31i = np.polyval([2*a3C,b3C], yx)
    
    if counter == 3: 
        Y10i = np.linspace(0,0,50)
        Y11i = np.linspace(0,0,50)  
        Y20i = np.linspace(0,0,50)
        Y21i = np.linspace(0,0,50)  
        Y30i = np.linspace(0,0,50)
        Y31i = np.linspace(0,0,50)  
        
    if counter == 2: 
        T = L/random.uniform(1,10)
        a = 0.2*T
        b = 0.2*T/S10
        
        Y10i = a/(yx+b)
        Y11i = -a/(yx+b)**2  
        Y20i = (S10-a/(yx+b))*0.5
        Y21i = 0.5*a/(yx+b)**2  
        Y30i = (S10-a/(yx+b))*0.5
        Y31i = 0.5*a/(yx+b)**2   
        
    if counter == 4: 
        Y10i = S10*(1-1/(1+np.exp(-25/L*yx)))*2
        Y11i = - (2*S10*25/L*np.exp(-25/L*yx))/((np.exp(25/L*yx)+1))**2
        Y20i = S10*(-1+1/(1+np.exp(-25/L*yx)))
        Y21i = (2*S10*25/L*np.exp(-25/L*yx))/((np.exp(25/L*yx)+1))**2
        Y30i = S10*(-1+1/(1+np.exp(-25/L*yx)))
        Y31i = + (2*S10*25/L*np.exp(-25/L*yx))/((np.exp(25/L*yx)+1))**2
    
    if counter == 5: 
        Y10i = S10*(1-1/(1+np.exp(-25/L*yx)))*2
        Y11i = - (2*S10*25/L*np.exp(-25/L*yx))/((np.exp(25/L*yx)+1))**2
        Y20i = S10*(-1+1/(1+np.exp(-25/L*yx)))
        Y21i = (2*S10*25/L*np.exp(-25/L*yx))/((np.exp(25/L*yx)+1))**2
        Y30i = S10*(-1+1/(1+np.exp(-25/L*yx)))
        Y31i = + (2*S10*25/L*np.exp(-25/L*yx))/((np.exp(25/L*yx)+1))**2    
        
    if counter >= 6: 
        Y10i = np.linspace(0,0,50)
        Y11i = np.linspace(0,0,50)  
        Y20i = np.linspace(0,0,50)
        Y21i = np.linspace(0,0,50)  
        Y30i = np.linspace(0,0,50)
        Y31i = np.linspace(0,0,50)         

    return(Y10i,Y11i,Y20i,Y21i,Y30i,Y31i,a1C,a2C,a3C)