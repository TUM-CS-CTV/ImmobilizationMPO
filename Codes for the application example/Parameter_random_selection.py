def Random_parameters(i):  
    import random
    import Time_profile as tp
    import Time_profile2 as tp2
    import numpy as np
    S1o_ran  = 1000 #mΜ  
    tf_ran   = 480 #min 
    zPA_ran  = 1 #particles/liter
    E_ran1    = i #μΜ 
    E_ran2    = 10-i #μΜ  
    zPO_ran  = 5*10**14 #pores/particle
    L_ran    = 2*10**(-4) #dm 
    A_ran    = 8*10**(-15) #dm
    D_ran1    = 10**(-8) #dm^2 min-1 
    D_ran2    = 5*10**(-6) #dm^2 min-1 
    D_ran3    = 5*10**(-6) #dm^2 min-1 
    Vmax_ran1 = 1 #mM/min/μΜ 
    Km_ran1   = 30 #mΜ 
    Vmax_ran2 = 1 #mM/min/μΜ 
    Km_ran2   = 80 #mΜ 
    return(E_ran1,Vmax_ran1,Km_ran1,E_ran2,Vmax_ran2,Km_ran2,A_ran,D_ran1,D_ran2,D_ran3,L_ran,S1o_ran,tf_ran,zPO_ran,zPA_ran)