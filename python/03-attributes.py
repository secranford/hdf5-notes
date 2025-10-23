#!/usr/bin/env python3
# Example to demonstrate basic attribute information and creation
import h5py
import numpy as np

with h5py.File("attr.hdf5", "w") as f:  # Clear attr.hdf5 if it exists
    dset = f.create_dataset("my dataset", (10, 10), dtype="i")  # dataset created
    for i in range(10):
        for j in range(10):
            dset[i, j] = i + j  # give dataset some values

    # In practice, it might be better to place these definitions again after assigment
    # to avoid conflicts
    attr = dset.attrs
    akeys = attr.keys()
    avals = attr.values()
    aitems = attr.items()

    # No attributes have been assigned so they are blank, and most of its
    # elements only give a view and must instead be placed in a list or iterated to see
    print(f"Ouput from testing attribute before assigning: {attr}")
    # Now lets populate the dataset with some attributes
    dset.attrs["Creation Date"] = "10-22-2025"
    dset.attrs["Creator"] = "secranford"
    dset.attrs["Elem Sum"] = np.sum(dset)
    # Now check the attribute info
    print("------------------")
    print(f"Output from testing attribute after assigning: {attr}")
    print(f"Attribute keys: {list(akeys)}")
    print(f"Attribute values: {list(avals)}")
    print(f"Attribute items: {list(aitems)}")
    print("Listing the key - values together:")
    for k, v in aitems:
        print(f"{k} = {v}")

    # Let's overwrite an attribute
    attr["Creator"] = "BATMAN"
    print("------------------")
    print(f"attribute after rewrite: {list(aitems)}")

    # delete an attribute
    del attr["Elem Sum"]
    print("------------------")
    print("Listing the key - values together after rewrite and deletion:")
    for k, v in aitems:
        print(f"{k} = {v}")
