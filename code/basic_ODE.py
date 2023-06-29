# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:53:03 2022

@author: paesc
"""

# -*- coding: utf-8 -*-

"""

Created on Wed Apr 27 13:56:24 2022



@author: paesc

"""



import numpy as np

import matplotlib.pyplot





def lotka_volterra(y0, params):
    '''
    

    Parameters
    ----------
    y0 : inital population,
        A: algae
        R: Rotifers
    params :
        ga: growing rate of algae without occurence of rotifer
        da: dying rate of algae due to rotifer consumption
        gr: growing rate of rotifer depending on occuring algae
        dr: dying rate of rotifer without algae occurance

    Returns
    -------
    numpy array of delta algae population, delta rotifer population

    '''

    

    A, R = y0

    ga, da, gr, dr = params

    

    da_dt = (ga * A) - (da * A * R)

    dr_dt = (gr * R * A) - (dr * R)

    

    return np.array([da_dt, dr_dt])





def RK4solver(time, y0, dfdt, params):
    '''
    

    Parameters
    ----------
    time : pandas Series of timepoints
    y0 : tuple of initial population of  (prey, predator)
    dfdt : differential equation system used
    params : parameters of differential equation system

    Returns
    -------
    numpy array of population sizes over simulated timepoints

    '''



    yn = y0

    ylist = [y0]
    
    time = np.array(time) # conversion into array


    for i in range(len(time)):
        
        # if decision for that dt doesn't get to high due to index - 1
        if i == 0:
            dt = time[i]
            
        else:
            dt = time[i] - time[i-1]  
            

        k1 = dt * dfdt(yn, params)

        k2 = dt * dfdt(yn + k1/2.,  params)

        k3 = dt * dfdt(yn + k2/2., params)

        k4 = dt * dfdt(yn + k3, params)

            

        yn1 = yn + 1/6 * (k1 + k2/2. + k3/2. + k4)

        yn = yn1

        ylist.append(yn)

        

    return np.array(ylist)



time = np.linspace(1,1000,10000)

y0 = (100,3)

params = (0.5,0.002,0.005,0.1)



p = RK4solver(time, y0, lotka_volterra, params)



matplotlib.pyplot.figure(1)

matplotlib.pyplot.plot(p)

matplotlib.pyplot.show()



# exit(0)

