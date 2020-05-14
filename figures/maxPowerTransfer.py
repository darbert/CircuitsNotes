# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:14:37 2019

@author: jdh03d
"""
import matplotlib.pyplot  as pyplot

rl = [0.01*r for r in range(0,1000)] #relative to R_s
p = [r/(r+1)**2 for r in rl]

pyplot.plot(rl, p, color='blue', lw=2)
pyplot.ylim((0, 0.35))
pyplot.xlim((0,3))
pyplot.xticks([])
pyplot.yticks([])
pyplot.xlabel("R$_{L}$", family='Verdana', size=26)
pyplot.ylabel("P$_L$", family='Verdana', size=26)
pyplot.show()