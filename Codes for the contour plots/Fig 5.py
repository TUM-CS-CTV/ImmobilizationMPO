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

# Imports packages 
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib as klp
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# defines grid for the contour plots
xlist = np.logspace(0, 3, 1000)
ylist = np.logspace(-8,-5, 1000)
X, Y = np.meshgrid(xlist, ylist) 

# gives values to the non-varied parameters
D1            = 5*10**(-6)         # dm^2 min^-1
D2            = Y                  # dm^2 min^-1
kA            = 1000               # dm^2 μmol^-1 min^-1
kB            = 998                # dm^2 μmol^-1 min^-1
L             = 5*10**(-4)         # dm 
A             = 10**(-13)          # dm^2
N_alpha_A     = 5*10**(12) / 2     # -
N_alpha_B     = 5*10**(12) / 2     # -
N_beta        = 5*10**(12)         # -
tf            = X                  # min
EA_alpha_A    = 6                  # μmol dm^-2
EB_alpha_B    = 6                  # μmol dm^-2
EA_beta       = 6/2                # μmol dm^-2
EB_beta       = 6/2                # μmol dm^-2

# definition of the algebraic equations 
m1_alpha_A = np.sqrt(kA*EA_alpha_A/D1)

m1_beta = np.sqrt(kA*EA_beta/D1)

m2_alpha_B = np.sqrt(kB*EB_alpha_B/D2)

m2_beta = np.sqrt(kB*EB_beta/D2)

p1_alpha_A = A * D1 * N_alpha_A * m1_alpha_A * np.tanh(m1_alpha_A*L)

p1_beta = A * D1 * N_beta * m1_beta * np.tanh(m1_beta*L)

p2_alpha_B = A * D2 * N_alpha_B * m2_alpha_B * np.tanh(m2_alpha_B*L)

p2_beta = A * D2 * N_beta * m2_beta * np.tanh(m2_beta*L)

p3_beta = A * D1 * N_beta * m1_beta**2 * m2_beta**2 /(m1_beta**2-m2_beta**2) * (np.tanh(m2_beta*L)/m2_beta - np.tanh(m1_beta*L)/m1_beta)

R =  (1-np.exp(-p1_alpha_A*tf)-(p1_alpha_A)/(p2_alpha_B-p1_alpha_A)*(np.exp(-p1_alpha_A*tf)-np.exp(-p2_alpha_B*tf)) ) / (1-np.exp(-p1_beta*tf)-(p1_beta-p3_beta)/(p2_beta-p1_beta)*(np.exp(-p1_beta*tf)-np.exp(-p2_beta*tf)))

Ybeta = (1-np.exp(-p1_beta*tf)-(p1_beta-p3_beta)/(p2_beta-p1_beta)*(np.exp(-p1_beta*tf)-np.exp(-p2_beta*tf)))

# plotting
fig,ax=plt.subplots(figsize=(6.1, 5))
plt.rcParams['font.size'] = 20
plt.rcParams['axes.linewidth'] = 1.4 
plt.yscale("log")
plt.xscale("log")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.setp(ax.spines.values(), linewidth=1.4)
cmap = plt.cm.Blues(np.linspace(0,1.1,35))
cmap = klp.colors.ListedColormap(cmap[8:,:-1])
cp = ax.contourf(X, Y, R, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], vmin = 0.0, vmax=1.0, cmap=cmap.reversed())
levels = [0.2, 0.4, 0.6, 0.8]
cp2 = ax.contour(X, Y, Ybeta,  levels=levels, colors = 'white', linestyles = 'dashed', linewidths = 1.5)
fig.colorbar(cp, label='$R_{\mathrm{α}/\mathrm{β}}$ / (mol/mol)') # Add a colorbar to a plot
ax.clabel(cp2, levels, inline=True, fmt='%1.1f', fontsize=20, manual=[(4*10**(0),10**(-7)),(10**(1),10**(-7)),(1.95*10**(1),10**(-7)),(3.0*10**(1),10**(-7))])
ax.yaxis.set_tick_params(width=1.4, length = 5)
ax.xaxis.set_tick_params(width=1.4, length = 5)
ax.tick_params(axis='y', which='minor', colors='black', left=True, length = 3, width=1.2)
ax.tick_params(axis='x', which='minor', colors='black', bottom=True, length = 3, width=1.2)
ax.tick_params(axis="x", direction="out")
ax.set_xlabel('$t$ / (min)')
ax.set_ylabel('$D_2$ / (dm$^2$ min$^{-1}$)')
plt.savefig('Fig5.png', bbox_inches='tight')  
plt.savefig('Fig5.pdf', bbox_inches='tight')  
plt.show()
