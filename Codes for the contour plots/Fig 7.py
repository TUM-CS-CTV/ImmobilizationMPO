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
xlist = np.logspace(-2.10,2.10, num = 500) 
ylist = np.logspace(-2.05,2.05, num = 500) 
m1, m2 = np.meshgrid(xlist, ylist) 

# definition of the algebraic equations 
R = (1-np.exp(-m1)-(m1/(m2-m1))*(np.exp(-m1)-np.exp(-m2)))/(1-np.exp(-np.sqrt(2)*m1)-(m1**2/(m2**2-m1**2))*(np.exp(-np.sqrt(2)*m1)-np.exp(-np.sqrt(2)*m2)))

Ybeta = (1-np.exp(-np.sqrt(2)*m1)-(m1**2/(m2**2-m1**2))*(np.exp(-np.sqrt(2)*m1)-np.exp(-np.sqrt(2)*m2)))

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
levels = [0.2, 0.4, 0.6, 0.8]
cp = ax.contourf(m1, m2, R, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], vmin = 0.0, vmax=1.0, cmap=cmap.reversed())
cp2 = ax.contour(m1, m2, Ybeta,  levels=levels, colors = 'white', linestyles = 'dashed', linewidths = 1.5)
manual_locations = [(2*10**(1),1.5*10**(-1)),(2*10**(1),4*10**(-1)),(2*10**(1),6*10**(-1)),(2*10**(1),4*10**(0))]
fig.colorbar(cp, label='$R_{\mathrm{α}/\mathrm{β}}$ / (mol/mol)')
ax.clabel(cp2, levels, inline=1, fmt='%1.1f', fontsize=20, manual=manual_locations)
ax.yaxis.set_tick_params(width=1.4, length = 5)
ax.xaxis.set_tick_params(width=1.4, length = 5)
ax.tick_params(axis='y', which='minor', colors='black', left=True, length = 3, width=1.2)
ax.tick_params(axis='x', which='minor', colors='black', bottom=True, length = 3, width=1.2)
ax.tick_params(axis="x", direction="out")
ax.set_xlabel('$\mu_1$ / (-)')
ax.set_ylabel('$\mu_2$ / (-)')
ax.set_xlim(10**(-2), 10**(2))
ax.set_ylim(10**(-2), 10**(2))
plt.yticks([10**(-2), 10**(-1), 10**(0), 10**(1), 10**(2)])
plt.xticks([10**(-2), 10**(-1), 10**(0), 10**(1), 10**(2)])
locmin = klp.ticker.LogLocator(base=10.0,subs=(0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=8)
ax.xaxis.set_minor_locator(locmin)
ax.xaxis.set_minor_formatter(klp.ticker.NullFormatter())
plt.savefig('Fig7.png', bbox_inches='tight')  
plt.savefig('Fig7.pdf', bbox_inches='tight')   
plt.show()