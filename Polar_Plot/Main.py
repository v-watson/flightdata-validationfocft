# -*- coding: utf-8 -*-
"""
Polar Plot - Concept to filter for points of interest
Created on Fri Aug 19 21:12:15 2016
@author: Viruben
"""

import numpy as np
import matplotlib.pyplot as plt

N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2 * np.random.rand(N)
colors = theta

ax = plt.subplot(111, polar = True)
c = plt.scatter(theta, r, c = colors, s = area, cmap = plt.cm.hsv)
c.set_alpha(0.75)

plt.show()