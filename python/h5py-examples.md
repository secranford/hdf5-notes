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
