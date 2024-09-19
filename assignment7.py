#!/usr/bin/env python
# coding: utf-8

# # Assignment 7
# 
# In [Assignment 6](http://nbviewer.jupyter.org/github/PGE323M-Fall2018/assignment6/blob/master/assignment6.ipynb) we wrote our own implementation of least squares curve fititng functions using Numpy data structures and operations.  Of course, least squares curve fitting is a very common task in scientific computing and there are several robust curve fitting utilities in the [SciPy](https://www.scipy.org/) software suite.
# 
# Complete the class below by implementing the functions `fit`, and `fit_through_zero`. Use the [`scipy.optimize.curve_fit`](`https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#scipy.optimize.curve_fit) function.  This function takes a *function* as its first argument.  Use a `lambda` function defined within `fit` and `fit_through_zero`.  For the `fit` function, the `lambda` function will have the form
# 
# $$
# f(\phi, \kappa_0, m) = \kappa_0 + m \frac{\phi^3}{(1 - \phi)^2}
# $$
# 
# where $\phi$ is the independent variable and $\kappa_0$ and $m$ are the fitting parameters.  This function will need to be modified slighty for the `fit_through_zero` implementation.

# In[1]:


import numpy as np
import pandas as pd
import scipy.optimize

class KozenyCarmen():
    
    def __init__(self, filename):
        
        #This reads a filename that is passed as an argument during
        #class instantiation and stores the columns of the data as
        #class attributes porosity and permeability
        self.df = pd.read_csv(filename)
        
        return
    
    def fit(self):
        #This function should implement a lambda function defining the form
        #of the function to curve fit, then return the estimated parameters
        #of both the \kappa_0 and m
        f = lambda phi, kappa0, m: kappa0 + m * (phi ** 3 / (1 - phi) ** 2)
        
        popt, pcov = scipy.optimize.curve_fit(f, self.df['porosity'], self.df['permeability']) 
        return popt
    
    def fit_through_zero(self):
        #This function should implement a lambda function defining the form
        #of the function to curve fit, then return the estimated parameter m
        f = lambda phi, m: m * (phi ** 3 / (1 - phi) ** 2)
        
        popt, pcov = scipy.optimize.curve_fit(f, self.df['porosity'], self.df['permeability']) 
        return popt

