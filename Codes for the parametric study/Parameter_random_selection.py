'''This code defines the parameter values.'''
def Random_parameters():  
    import random
    import Time_profile as tp
    import Time_profile2 as tp2
    import numpy as np
    import math
    S1o_ran   = 10**(random.uniform(math.log10(1), math.log10(1000))) #mΜ 
    tf_ran    = 10**(random.uniform(math.log10(1), math.log10(2000))) #min
    EA_ran    = 10**(random.uniform(math.log10(1), math.log10(10))) #μΜ 
    EB_ran    = 10**(random.uniform(math.log10(1), math.log10(10))) #μΜ 
    Np_ran   = 10**(random.uniform(math.log10(10**12), math.log10(10**16))) #pores/particle
    L_ran     = 10**(random.uniform(math.log10(10**(-6)), math.log10(10**(-3)))) #dm 
    A_ran     = 10**(random.uniform(math.log10(3*10**(-16)), math.log10(2*10**(-13)))) #dm
    D1_ran    = 10**(random.uniform(math.log10(10**(-8)), math.log10(10**(-5)))) #dm^2 min-1
    D2_ran    = 10**(random.uniform(math.log10(10**(-8)), math.log10(10**(-5)))) #dm^2 min-1
    D3_ran    = 10**(random.uniform(math.log10(10**(-8)), math.log10(10**(-5)))) #dm^2 min-1
    kA_ran   = 10**(random.uniform(math.log10(0.1), math.log10(1000))) #mΜ 
    kB_ran   = 10**(random.uniform(math.log10(0.1), math.log10(1000))) #mΜ 
    return(S1o_ran,tf_ran,EA_ran,EB_ran,Np_ran,L_ran,A_ran,D1_ran,D2_ran,D3_ran,kA_ran,kB_ran)

