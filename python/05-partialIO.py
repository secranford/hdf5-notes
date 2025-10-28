#!/usr/bin/env python3
# Example to demonstrate basics of partial IO in hdf5
import h5py
import numpy as np
import random

example_data = np.arange(100).reshape((10, 10))  # 2D array with values from 0 to 99
# type and shape of actual array
print(f"Example data shape and type: {example_data.shape} {type(example_data)}")

with h5py.File("partial.h5", "w") as f:

    dset = f.create_dataset("numbers", data=example_data)  # create a dataset from
    # existing data
    print(f"Dataset type: {type(dset)}")  # notice that the type is diff from the array
    # however, it behaves like a numpy array:
    extr = dset[4,5]
    print(f"Data extraction and type: {extr} {type(extr)}")

    # array slicing is faster than individual element calls
    extr = dset[0,::2] # first row, every 2nd element starting at the first elem
    # works well and easily for data that is contiguous in memory, can be adapted for
    # more unstructured, random, or specific retrival or data


