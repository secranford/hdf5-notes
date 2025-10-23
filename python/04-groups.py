#!/usr/bin/env python3
# Example to demonstrate basic groups information and creation
import h5py
import numpy as np
import random

with h5py.File("groups.h5", "w") as f:

    dset = f.create_dataset("Square", (3, 3), "i")  # create a dataset
    for i in range(3):
        dset[i, i] = i + 1

    grp = f.create_group("first_group")  # create a group
    subgrp = grp.create_group("sub group")  # create sub group
    sdset = subgrp.create_dataset("Random", (2, 2), "f")  # dataset in sub group
    sdset[:, :] = random.random()

    # Create a sub grouped dataset using the posix style naming
    pdset = f.create_dataset("f/s/posix_data", (5,), "i")
    pdset[:] = pdset.shape[0]

    dset.attrs["Data Info"] = "A 3x3 matrix with sequential diagonal values"
    sdset.attrs["Data Info"] = "A 2x2 matrix filled with the same random value"
    pdset.attrs["Data Info"] = "A 1D array of length 5 with the same value as its shape"
    print(f"The name attribute gives a valid path for a dataset or group: {grp.name}")

    print(15 * "-")
    print("Lets list all the names of the different groups and datasets:")
    print()
    def printname(name):
        print(name)

    f.visit(printname)

    # lets grab just the datasets so we can explore it's values and attributes.
    # theres probably a better way to do this, but this is practice
    def find_data(name, obj):
        if isinstance(obj, h5py.Dataset):
            print()
            print(f"Dataset: {name}")
            aitems = obj.attrs.items()
            print("Attribute key - values:")
            for k, v in aitems:
                print(f"{k} = {v}")
            print(f"Data: \n{obj[...]}")

    print(15 * "-")
    print("Now lets grab just the datasets and list the attributes and data: ")
    f.visititems(find_data)
