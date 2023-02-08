'''This code is used to plot the results. First import your results from the txt file in a excel file named "Results.xlsx".
Then save everything in the same directory and run this code. 

Make sure that the correct columns are selected in lines 14 to 16 of this code. 

Also, you have to add any modulus you want to color-code yourself in column U of the excel file.'''

from matplotlib import pyplot as plt, colors
import numpy as np
import pandas as pd
import xlwings as xw
import pandas as pd
import matplotlib.patches as mpatches

ws = xw.Book("Results.xlsx").sheets['Sheet1']
x = ws.range("S3:S1999").value
y = ws.range("T3:T1999").value
c = ws.range("U3:U1999").value

plt.rcParams["figure.figsize"] = [6.5, 5]
plt.rcParams["figure.autolayout"] = True
plt.rcParams.update({'font.size': 18})
plt.rcParams['axes.linewidth'] = 1.25 

df = pd.DataFrame({"x": x, "y": y, "c": c})
fig, ax = plt.subplots()
cmap = plt.cm.Blues



ax.xaxis.set_tick_params(width=1.25)
ax.yaxis.set_tick_params(width=1.25)
plt.plot([0,1],[0,1], transform=ax.transAxes,c='midnightblue')
norm = colors.LogNorm(vmin=10**(-2), vmax=10**(2))
ax.scatter(df.x, df.y, marker = 'o', edgecolor = '0.2', lw = 0.5 ,color=cmap(norm(df.c.values)))

ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.xlim(0, 1)
plt.ylim(0, 1)


sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
cbara = fig.colorbar(sm, label ="$ f_{\mathrm{FOK}} $ / (-)")
cbara.ax.tick_params(width=1.5, which="major")
cbara.ax.tick_params(width=1, which="minor")
plt.tight_layout()
plt.xlabel("$Y_{\mathrm{δ}_{.}}$ / (-)")
plt.ylabel("$Y_{\mathrm{γ}_{.}}$ / (-) ")

plt.savefig('md.png')
plt.savefig('md.pdf')
