'''This code defines the parameter values.'''

def Parameters(i):  
    import random
    import Time_profile as tp
    import Time_profile2 as tp2
    import numpy as np
    S1o     = 1000        # mΜ  
    tf      = 480         # min 
    EA      = i           # μmol dm^-2 
    EB      = 10-i        # μmol dm^-2   
    Np      = 5*10**14    # - 
    L       = 2*10**(-4)  # dm 
    A       = 8*10**(-15) # dm^2
    D1      = 10**(-8)    # dm^2 min-1 
    D2      = 5*10**(-6)  # dm^2 min-1 
    D3      = 5*10**(-6)  # dm^2 min-1 
    kA      = 30          # dm^2 μmol^-1 min^-1   
    kB      = 80          # dm^2 μmol^-1 min^-1 
    return(EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np)