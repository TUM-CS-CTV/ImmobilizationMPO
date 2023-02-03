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

'''This code simulates and compares the yields achieved with three different 
spatial immobilization strategies. It also plots the results and saves the 
plot in a pdf. Please save all codes in the same directory and run this code.'''

import Parameters as rps
import Time_profile as tp
import Time_profile2 as tp2
import Time_profile_b as tp_b
import Time_profile2_b as tp2_b
import numpy as np
import math
import matplotlib.pyplot as plt
import pylab
global Y110i,Y111i,Y210i,Y211i,Y220i,Y221i,Y320i,Y321i,Y10i,Y11i,Y20i,Y21i,Y30i,Y31i
from matplotlib.ticker import FormatStrFormatter

print('Results', file = open("Overview3.txt", "w+"))
print('alpha','beta','gamma','delta',file = open("Overview3.txt", "a"))

Ea = np.linspace(0.001,9.999,250) 
Storage = {}

Yalphas = []
Ybetas = []
Ygamas = []
Ydeltas = []
EAs = []

for i in Ea:
    EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np = rps.Parameters(i)
    t,S1alpha,S2alpha,S3alpha = tp.time_profile(EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,i)
    t,S1beta,S2beta,S3beta = tp2.time_profile2(EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,i)
    t,S1delta,S2delta,S3delta = tp_b.time_profile_b(EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,i)
    t,S1gama,S2gama,S3gama = tp2_b.time_profile2_b(EA,kA,EB,kB,A,D1,D2,D3,L,S1o,tf,Np,i)
    print(i)
    print(i, S3alpha[-1]/S1o,S3beta[-1]/S1o,S3gama[-1]/S1o,S3delta[-1]/S1o,file = open("Overview3.txt", "a"))
    EAs.append(i)
    Yalphas.append(S3alpha[-1]/S1o)
    Ybetas.append(S3beta[-1]/S1o)
    Ygamas.append(S3gama[-1]/S1o)
    Ydeltas.append(S3delta[-1]/S1o)    

fig = plt.figure(figsize=(5.5,5))
ax1 = fig.add_subplot(111)
ax1.plot(EAs, Yalphas,'b', label='Single immobilization (α)')
ax1.plot(EAs, Ygamas,'m', label='Co-immobilization, heterogeneous, A first (γ)')
ax1.plot(EAs, Ydeltas,'c', label='Co-immobilization, heterogeneous, B first (δ)')
#ax1.plot(8.290798994974875, 0.8525150847272743, 'k*', markersize=15)
ax1.set_ylim(0,1)
ax1.set_xlim(0,10)
ax2 = ax1.twiny()
ax2.set_xticks(ax1.get_xticks())
ax2.set_xbound(ax1.get_xbound())
ax2.set_xticklabels([10 - int(x) for x in ax1.get_xticks()])
ax2.set_xlabel('X', rotation=0, labelpad=12)
ax1.set_xlabel('$\it{E}_A^{\mathrm{max}}$ / ($\mu$mol dm$^{-2}$)', fontsize=20)
ax1.set_ylabel('$\it{Y}$$_\mathrm{m}$ / (-)', fontsize=20)
ax2.set_xlabel('$\it{E}_B^{\mathrm{max}}$ / ($\mu$mol dm$^{-2}$)', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=20)
ax2.tick_params(axis='both', which='major', labelsize=20)
pylab.savefig('optimization.pdf', bbox_inches='tight')
