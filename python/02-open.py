#!/usr/bin/env python3
# Example on opening an hdf5 file in python and checking data information
import h5py

with h5py.File("file5.hdf5","r") as f:
    k = list(f.keys()) # what are the named datasets?
    dset = f["my dataset"] # retrieve our dataset
    sh = dset.shape
    ty = dset.dtype
    val = dset[0,0]
    print(f"The datasets are: {k}")
    print(f"The shape of our dataset is: {sh}")
    print(f"The type of our dataset is: {ty}")
    print(f"The value of the 0,0 elem is: {val}")
#f.close() # no need for close opening file in this way


