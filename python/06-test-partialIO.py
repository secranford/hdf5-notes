#!/usr/bin/env python3
# Example to demonstrate partial IO on larger file
import h5py
import numpy as np
import time

with h5py.File("128MB_test.h5", "r") as f:
    k = list(f.keys())[0]  # grab dataset key
    print(f"File has dataset key: {k}")
    dset = f[k]  # lazy load, not on memory yet
    print("> Loading dataset through multiple methods...")
    # method 1, loading everthing into memory at once by looping
    t0 = time.perf_counter()
    i, j, k = dset.shape  # i know it has 3 dimensions
    
    # the comments below are specifically for python2, in python3, range has been
    # updated to behave like xrange and xrange has been removed.

    # range creates a list of numbers that get loaded to memory
    # xrange is like a lazy load version of range, it creates the iterator one at a
    # time and so is more efficient for large number of iterations
    for ii in range(i):
        for jj in range(j):
            for kk in range(k):
                dset[
                    ii, jj, kk
                ]  # I am accessing the element which loads it into memory
    t1 = time.perf_counter()

    print("> Done with method 1, moving to method 2")

    # method 2, loading everthing into memory with slicing
    t2 = time.perf_counter()
    dset[:]
    t3 = time.perf_counter()

    print("> Done with method 2, moving to method 3")
    # method 3, loading slices of the dataset into memory with slicing
    t4 = time.perf_counter()
    for ii in range(i):
        dset[ii, :, :]  # now only loading slices of the dataset at a time
    t5 = time.perf_counter()

    print()
    print(f"Method 1 took: {(t1-t0)*1e3} milliseconds")
    print(f"Method 2 took: {(t3-t2)*1e3} milliseconds")
    print(f"Method 3 took: {(t5-t4)*1e3} milliseconds")
