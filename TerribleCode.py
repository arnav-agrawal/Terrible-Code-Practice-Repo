#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:42:08 2020

@author: arnav
"""

'''
Code for trial documentation-sprint, to learn how to use Sphinx and NumPy. 
'''

import numpy as np


#function that calculates roots for ax^2 + b^x + c = 0

def quadratic_formula(a,b,c):
    """
    Uses the quadratic formula to calculate roots for a quadratic equation

    Parameters
    ----------
    a : float
        Coefficient of the second-order term.
    b : float
        Coefficient of the first-order term.
    c : float
        Coefficient of the constant term.

    Raises
    ------
    ValueError
        If the equation has no real solutions.

    Returns
    -------
    sol : list
        A list containing 1 or 2 solutions.
    """
    
    d = b**2-4*a*c # discriminant

    if d < 0:
        raise ValueError("This equation has no real solution")
    elif d == 0:
        x = (-b+np.sqrt(b**2-4*a*c))/2*a
        sol = [x]
        return sol
    else:
        x1 = (-b+np.sqrt(b**2-4*a*c))/2*a
        x2 = (-b-np.sqrt(b**2-4*a*c))/2*a
        sol = [x1, x2]
        return sol


# simple numerical integration of f(x) over an interval x: [x_lower, x_upper] using composite trapezoid rule.

def simple_integrate(f, x):
    """
    Numerical integration of a function over an interval x using compositve trapezoid rule

    Parameters
    ----------
    f : list
        Function that is defined over the interval x, and is valued at the upper and lower bounds of x.
    x : list
        List that defines the interval of integration, x: [x_lower, x_upper].

    Returns
    -------
    int_sum : int
        The integral of the function over the interval.
    """
    
    int_sum = 0

    for i in range(x.size-1):
        int_sum += 0.5*(x[i+1] - x[i])*(f[i] + f[i+1])
    
    return int_sum


# function for nth Fibonacci number 
  
def fibonacci(n): 
    """
    Recursive function that return the nth Fibonacci number in the sequence

    Parameters
    ----------
    n : int
        The element of the Fibonacci sequence that is desired.

    Raises
    ------
    ValueError
        If n <= 0.

    Returns
    -------
    int
        The value of the nth element of the Fibonacci sequence.   
    """
    
    if n<=0: 
        raise ValueError("Input cannot be less than 1") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)  



# convert time in seconds to hours, minutes and seconds

def get_hms(t_sec):
    """
    Convert a time given in seconds to hours, minutes, and seconds

    Parameters
    ----------
    t_sec : int
        Time in seconds.

    Returns
    -------
    h : int
        The hours portion of the time.
    m : int
        The minutes portion of the time.
    s : int
        The seconds portion of the time.
    """

    h = t_sec//3600

    m = (t_sec - h*3600)//60

    s = t_sec%60

    return h,m,s