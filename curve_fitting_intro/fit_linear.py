# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:30:23 2022

@author: paesc
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so

# input

x = np.linspace(0,20)
y = [i + np.random.normal(0, 2) for i in x] 

# function

def linear(x,a,b):
    return a * x + b

# fit with sp

popt, _ = so.curve_fit(linear, x, y)

a, b = popt

# new values with optimal parameters

y_new = linear(x,a,b)



fig, axs = plt.subplots(1,1,figsize = (10,20))
                        
axs.scatter(x,y)
axs.plot(x, y_new)

plt.show()


