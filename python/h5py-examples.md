# h5py Examples
- Example 1 goes over the basics of creating a hdf5 file, `file5.hdf5`, in python and populating some of the information for a dataset. The hdf5 file object generally behaves like a standard python file object and accepts the modes listed in the table below:

| Mode String | File Action |
| ----------- | ----------- |
| r           | Readonly, file must exist |
| r+          | Read/write file must exist |
| w           | Create file, clear if exist |
| w- or x     | Create file, fail if exist |
| a           | Read/write if exist, create otherwise |

- Example 2 goes over a more functional way to access hdf5 files and briefly explores some of the data.
-
