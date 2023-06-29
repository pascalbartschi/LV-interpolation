# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:37:57 2022

@author: paesc
"""


import matplotlib.pyplot as plt
import numpy as np





def odeSolver(t0, y0, dfFunc, h, nSteps, solverStepFunc):

    """This is a general ODE solver that takes the
    derivative df/dt (dfFunc) and the algorithm for one time
    step (solverStepFunc) as function arguments.
	t0 = Initial time
	y0 = Initial function values (array)
	nSteps = Total number of integration steps
	solverStepFunc = Euler Method, Midpoint RK or RK4
    """

    yn = y0
    tn = t0
    tlist = [t0]
    ylist = [y0]
    for n in range(nSteps):

        yn1 = solverStepFunc(tn, yn, h, dfFunc)
        tn1 = tn + h
        tlist.append(tn1)
        ylist.append(yn1)
        tn = tn1
        yn = yn1

    return (np.array(tlist), np.array(ylist))

	

def eulerStep(tn, yn, h, dfdt):
    """forward Euler step solving method"""
    dy = h * dfdt(tn, yn)
    yn1 = yn + dy

    return yn1



def midPointRK2Step(tn, yn, h, dfdt):
    """Rk2 step solving method"""
    yn1 = eulerStep(tn,yn,h/2,dfdt)
    dy = dfdt(tn+h/2,yn1)
    yn2 = yn + h * dy
    return yn2



def rK4Step(tn, yn, h, dfdt):
    """Rk4 step solving method"""
    k1 = h * dfdt(tn,yn)
    k2 = h * dfdt(tn+h/2, yn+k1/2)
    k3 = h * dfdt(tn+h/2, yn+k2/2)
    k4 = h * dfdt(tn+h, yn+k3)
    yn1 = yn + k1/6 + k2/3 + k3/3 + k4/6

    return yn1



def lotkaVolterra(t, y):
    """Implements the Lotka Volterra System dm/dt and dfox/dt
    where y=(m,fox), dy/dt=(dm/dt, dfox/dt)"""
    m = y[0]
    f = y[1]
    km = 2
    kmf = 0.02
    kfm = 0.01
    kf = 1.06
    dmdt = (km * m) - (kmf * f * m)
    dfoxdt =(kfm * f * m) - (kf * f)

    return np.array([dmdt, dfoxdt])


def plotSol(dfFunc, initialCond, solverStepFunc):
    """Call ODEsolver for all methods in list with the given starting conditions
    and plot them in one plot"""

    t0, y0, nSteps, h = initialCond

    fig,ax = plt.subplots(nrows=len(solverStepFunc),ncols=2)

    name = dfFunc.__name__

    fig.suptitle(f"ODE: {name} with t0={t0}, y0={y0}, nSteps={nSteps}, h={h}", size=20)

    for i,m in enumerate(solverStepFunc):

        t,y = odeSolver(t0,y0,dfFunc,h,nSteps,m)
        ax[i][0].plot(t, y[:,0])
        ax[i][0].plot(t,y[:,1])
        ax[i][0].set_title(f"{m.__name__}")
        ax[i][0].set_ylabel("Pop Size")

        ax[i][1].set_title(f"{m.__name__}")
        ax[i][1].plot(y[:,0], y[:,1], color="violet")
        ax[i][1].set_ylabel("foxes")

        if i == 0:
            ax[i][0].set_title(f"Population Plot: {m.__name__}")
            ax[i][1].set_title(f"Phase Plot: {m.__name__}")

        if i == len(solverStepFunc)-1:

            ax[i][0].set_xlabel("Time")
            plt.xlabel('mice')


# h = 0.1
# nSteps = 600
# t0 = 0
# y0 = np.array([100, 15])
#
# odeSolver(t0, y0, LotakVolterra, h, nSteps, eulerStep)

# Main__________________________________________________________________________

def main():
    """Solve and plot the Lotka Volterra Equation with different step solving methods and differend
    starting conditions"""
    h = 0.1
    nSteps = 600
    t0 = 0
    y0 = np.array([100, 15])
    plotSol(lotkaVolterra, [t0,y0,nSteps,h], [eulerStep,midPointRK2Step,rK4Step])


    h = 0.01
    nSteps = 6000
    t0 = 0
    y0 = np.array([100, 15])
    # plotSol(lotkaVolterra, [t0,y0,nSteps,h], [eulerStep,midPointRK2Step,rK4Step])


    h = 0.01
    nSteps = 6000
    t0 = 0
    y0 = np.array([10, 150])
    # plotSol(lotkaVolterra, [t0,y0,nSteps,h], [eulerStep,midPointRK2Step,rK4Step])

    h = 0.01
    nSteps = 6000
    t0 = 0
    y0 = np.array([3, 1])
    # plotSol(lotkaVolterra, [t0,y0,nSteps,h], [eulerStep,midPointRK2Step,rK4Step])


if __name__== "__main__":

    main()
