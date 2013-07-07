# coding: utf-8

""" Demonstration of the built-in multiprocessing package """

from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Standard library
import multiprocessing

# Define a 'task' or 'worker' function -- something function that you
#   need to call over and over and over
def task(x):
    return x**2
    
if __name__ == "__main__":
    # a pool is like a magical box that knows how to execute things on
    #   multiple CPUs
    pool = multiprocessing.Pool(processes=4)
    
    # this will run the function task() on all values in range(10000)
    result = pool.map(task, range(10000))
    print(result)