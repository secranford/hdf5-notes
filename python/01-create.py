#!/usr/bin/env python3
# Example on creating a minimal hdf5 file in python
import h5py

f = h5py.File("file5.hdf5","w") # hdf5 file created
# better:
#with h5py.File("file.hdf5","w") as f:
#    dset = f.create_dataset("my dataset", (10,10),dtype='f') # dataset created

# hdf5 datasets need 3 things: a name, a shape (dimension), and a prescribed datatype
dset = f.create_dataset("my dataset", (10,10),dtype='f') # dataset created
dset[0,0] = 2.1
f.close()
