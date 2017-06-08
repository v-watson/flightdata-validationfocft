# -*- coding: utf-8 -*-
"""
SHOL Power Plot
Created on Fri Aug 19 22:28:41 2016
@author: Viruben
"""
import matplotlib.pylab as plt
from matplotlib.path import Path
import matplotlib.patches as patches

verts = [
         (0, 0),
         (0, 1),
         (1, 1),
         (1, 0),
         (0, 0),]
         
codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY]

path = Path(verts, codes)
c = patches.Circle((0.5, 0.5), 0.25, facecolor="none",
edgecolor="black", linewidth=2)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
patch = patches.PathPatch(path, facecolor='none', lw=2)
ax.add_patch(patch)
plt.gca().add_patch(c)
plt.show()         