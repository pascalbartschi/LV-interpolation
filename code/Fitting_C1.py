# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:29:00 2022

@author: paesc
"""

from scipy import optimize, integrate
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data/C1.csv')
data = data.dropna()
columns = [i for i in data.columns]

x = np.array(data['time (days)'])
liv_algae = data[' algae (10^6 cells/ml)'] * 10**6
liv_rotifer = data[' rotifers (animals/ml)']
dead_rotifer = data[' dead animals (per ml)']
# x = [i for i in zip(x,x)]
y = np.array([i for i in zip(liv_algae, liv_rotifer)], dtype = float)

data1 = pd.DataFrame({'time': x, 'algae (cells(ml)':liv_algae, 'rotifers (cells /ml)':liv_rotifer, 
                     'dead rotifers (cells/ml)': dead_rotifer })

algrot_ratio = liv_algae/liv_rotifer
rot_death_ratio = dead_rotifer/liv_rotifer

# x = [i for i in zip(x,x)]
y = np.array([i for i in zip(y_alg, y_rot)], dtype = float)


    
def lotka_volterra(y, x, ga, da, dr, gr):
    
    
    da_dt = ga * y[0] + da * y[0] * y[1]
    dr_dt = -dr * y[1] + gr * y[1] * y[0]
    
    return da_dt, dr_dt

def fitode(x, ga, da, dr, gr):
    return integrate.odeint(lotka_volterra, (y[0,0],y[0,1]), x, args=(ga,da,dr,gr))



def OLS(true, pred):
    true = np.array(true)
    pred = np.array(pred)
    
    return np.sum((true - pred) ** 2)


# popt, pcov  = optimize.curve_fit(fitode, x, y)

# plotting

# fig, axs = plt.subplots(2,1, figsize = (20,10))

# axs[0].scatter(x, y_alg)
# axs[0].plot(x, y_alg)
# axs[0].set_title('Algae')
# axs[1].scatter(x, y_rot)
# axs[1].plot(x, y_rot)
# axs[1].set_title('Rotifers')

# plt.show()