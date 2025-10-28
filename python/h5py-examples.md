# h5py Examples
- Example 1 goes over the basics of creating a hdf5 file, `file5.hdf5`, in python and populating some of the information for a dataset. The hdf5 file object generally behaves like a standard python file object and accepts the modes listed in the table below:

| Mode String | File Action |
| ----------- | ----------- |
| r           | Readonly, file must exist |
| r+          | Read/write file must exist |
| w           | Create file, clear if exist |
| w- or x     | Create file, fail if exist |
| a           | Read/write if exist, create otherwise. Does not clear file, appends|

- Example 2 goes over a more functional way to access hdf5 files and briefly explores some of the data. You must run Example 1 first to have created `file5.hdf5`.
- Example 3 gives an intro to accessing and creating hdf5 attributes.
- Example 4 gives an intro to create and accessing groups in hdf5. Note that both create_dataset and create_group are not restricted to the File object and can instead be applied to any group. This is what allows you to nest datasets and groups within a folder like structure. Using a POSIX style dataset name allows you to group a dataset upon creation.
- Example 5 gives an intro to partial IO in hdf5. In the example data extract, hdf5 located the requested element on disk and loads it into memory. It then performs the necessary type conversion needed to match one of numpy's data types. A numpy value is created and returned to the python caller. This is sometimes referred to as "lazy loading" since the data stays on disk until you need it. This type conversion also makes actions such as iterating over elements in a dataset very slow as the conversion and calls are done individually at each iteration. You should instead use numpy array slicing to get a speed up in both grabbing the data and the conversion between hdf5 and python so you minimize calls.
- Example 6 is similar to example 5. Run the `create-128mb.py` script to create the larger hdf5 file before testing the example. Putting what we learned from example 5 together, we can load and use an entire dataset without loading all the data at once; which, depending on our machine and the size of our data, might be impossible. This example could take a few minutes to run. Look at `06-output.txt` if you want to just see the performance benefit on my laptop. It is clear that slicing methods alone bring tremendous speed up, but so does partial IO.
