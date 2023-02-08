# ----------------------------------------------------------------------------
# This code supplements the following paper: 
#
# "Mechanistic modeling. parametric study, and optimization of immobilization 
#                of enzymatic cascades in porous particles"
#
# Authors: Leandros Paschalidis, Sara Arana-Pena, Volker Sieber, Jakob Burger
# 
#
# The paper was submited to: Reaction Chemistry & Engineering.
# ----------------------------------------------------------------------------

import Parameter_random_selection as rps
import Time_profile as tp
import Time_profile2 as tp2
import math
global Y110i,Y111i,Y210i,Y211i,Y220i,Y221i,Y320i,Y321i,Y10i,Y11i,Y20i,Y21i,Y30i,Y31i
print('Results', file = open("Overview.txt", "w+"))
print('counter','S1o_ran','tf_ran','EA_ran','EB_ran','Np_ran','L_ran','A_ran','D1_ran','D2_ran','D3_ran','kA_ran','kB_ran','results1/results2','results1','results2','Status1','Status2','Yield1','Yield2',file = open("Overview.txt", "a"))
i = 0 
Storage = {}
while i < 3:
    S1o_ran,tf_ran,EA_ran,EB_ran,Np_ran,L_ran,A_ran,D1_ran,D2_ran,D3_ran,kA_ran,kB_ran = rps.Random_parameters()
    results1,a1A,a2A,a3A,status_ODE1,yield1 = tp.time_profile(S1o_ran,tf_ran,EA_ran,EB_ran,Np_ran,L_ran,A_ran,D1_ran,D2_ran,D3_ran,kA_ran,kB_ran,i)
    results2,a1C,a2C,a3C,status_ODE2,yield2 = tp2.time_profile2(S1o_ran,tf_ran,EA_ran,EB_ran,Np_ran,L_ran,A_ran,D1_ran,D2_ran,D3_ran,kA_ran,kB_ran,i)
    print('Iteration', i, 'Ratio', yield1/yield2)
    print(i,S1o_ran,tf_ran,EA_ran,EB_ran,Np_ran,L_ran,A_ran,D1_ran,D2_ran,D3_ran,kA_ran,kB_ran,results1/results2,results1,results2,status_ODE1,status_ODE2,yield1,yield2,file = open("Overview.txt", "a"))
    i=i+1