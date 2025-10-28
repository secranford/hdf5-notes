#!/usr/bin/env python3
# Create 128 megabyte hdf5 file
import h5py
import numpy as np

d = np.ones((400,400,400),dtype=np.int16) # large array

with h5py.File("128MB_test.h5", "w") as f:
    dset = f.create_dataset("Ones",data=d)
