# -*- coding: utf-8 -*-
"""
SHOL Power Plot
Created on Fri Aug 19 22:28:41 2016
@author: Viruben
"""
import matplotlib.pylab as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-70, 70)
ax.set_ylim(-70, 70)

# Draw SHOL circular axes (speeds)
for x in range(2, 9):
    r = 5 * x
    c = patches.Circle((0, 0), r, facecolor="none", edgecolor="black", linewidth=1)
    plt.gca().add_patch(c)

# Draw horizontal and vertical SHOL axes (azimuths)
verts = [
         (0, 10),
         (0, 40),
         (0, -10),
         (0, -40),
         (-10, 0),
         (-40, 0),
         (10, 0),
         (40, 0)]
         
codes = [Path.MOVETO,
         Path.LINETO,
         Path.MOVETO,
         Path.LINETO,
         Path.MOVETO,
         Path.LINETO,
         Path.MOVETO,
         Path.LINETO]

path = Path(verts, codes)
patch = patches.PathPatch(path, facecolor='none', lw=1)
ax.add_patch(patch)

# Draw azimuths to fill gaps in between horiz and vert azimuths
for a in range(1, 9):
    theta = a * 10
    radius_start = 10
    radius_end = 40
    x_comp_start = radius_start * np.sin(np.deg2rad(theta))
    x_comp_start_lft = -radius_start * np.sin(np.deg2rad(theta))
    y_comp_start = radius_start * np.cos(np.deg2rad(theta))
    y_comp_start_bottom = -radius_start * np.cos(np.deg2rad(theta))
    x_comp_end = radius_end * np.sin(np.deg2rad(theta))
    x_comp_end_lft = -radius_end * np.sin(np.deg2rad(theta))
    y_comp_end = radius_end * np.cos(np.deg2rad(theta))
    y_comp_end_bottom = -radius_end * np.cos(np.deg2rad(theta))
    verts_azi = [
         (x_comp_start, y_comp_start),
         (x_comp_end, y_comp_end),
         (x_comp_start_lft, y_comp_start),
         (x_comp_end_lft, y_comp_end),
         (x_comp_start_lft, y_comp_start_bottom),
         (x_comp_end_lft, y_comp_end_bottom),
         (x_comp_start, y_comp_start_bottom),
         (x_comp_end, y_comp_end_bottom)]
         
    codes_azi = [Path.MOVETO,
         Path.LINETO,
         Path.MOVETO,
         Path.LINETO,
         Path.MOVETO,
         Path.LINETO,
         Path.MOVETO,
         Path.LINETO]
         
         
    path_azi = Path(verts_azi, codes_azi)
    patch_azi = patches.PathPatch(path_azi, facecolor='none', lw=1)
    ax.add_patch(patch_azi)

plt.show()