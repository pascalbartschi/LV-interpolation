# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:52:36 2022

@author: paesc
"""

import scipy.optimize as so
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
data = pd.read_csv(url, header = None)

x,y = data[4], data[6]

## linear fit

def linear(x, a, b):
    return a * x + b

# optimize

parlin, _ = so.curve_fit(linear, x, y)
a, b = parlin

# for plotting fitted line

x_line = np.arange(min(x), max(x), 1)
y_line1 = linear(x_line, a,b)

## polynomial fit 

def polynomial(x,a,b,c):
    return a * x**2 + b * x + c

parpoly, _ = so.curve_fit(polynomial, x, y)
a,b,c = parpoly

y_line2 = polynomial(x_line,a,b,c)

## fifth degree polynomial fit

def poly_5(x, a, b, c, d, e, f):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

parpoly5, _ = so.curve_fit(poly_5 , x, y)
a,b,c,d,e,f = parpoly5

y_line3 = poly_5(x_line,a,b,c,d,e,f)

## sine fit

def sine(x, a, b, c, d):
	return a * np.sin(b - x) + c * x**2 + d

parsine, _ = so.curve_fit(sine, x, y)
a,b,c,d = parsine

y_line4 = sine(x_line,a,b,c,d)

## plotting

fig, axs = plt.subplots(2,2, figsize = (10,20), sharex = True, sharey = True)

axs[0,0].scatter(x,y)
axs[0,0].plot(x_line, y_line1, '--', color = 'red')
axs[0,0].set_title('Linear')

axs[0,1].scatter(x,y)
axs[0,1].plot(x_line, y_line2, '--', color = 'red')
axs[0,1].set_title('Polynomial 2nd degree')


axs[1,0].scatter(x,y)
axs[1,0].plot(x_line, y_line3, '--', color = 'red')
axs[1,0].set_title('Polynomial 5th degree')


axs[1,1].scatter(x,y)
axs[1,1].plot(x_line, y_line4, '--', color = 'red')
axs[1,1].set_title('Sine')



plt.show()