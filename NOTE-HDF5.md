# HDF5 Notes

## The HDF5 Data format

- HDF5: Hierarchical Data Format
- HDF5 is a binary data format that allows you to handle large datasets. It is a self describing data format meaning it contains metadata describing the data within. It allows you to store multiple data format types together with context and ways to access the data in different ways.
- Partial I/O. HDF5 supports partial input/output for data, meaning you don't need to load the entire file to memory to be able to extract or write the data that you want. This makes I/O more efficient.

## Resources for learning HDF5

- The official HDF5 Group [website][hdf5] is a good resource to learn more about hdf5 and see available resources or tutorials on handling the data format. Many programming languages such as python, Fortran, and Matlab have a way to handle hdf5 files. The HDF5 Group even has a visual tool for handling the file format, [HDFView][hdfview]. There is also a [browser][myhdf5] application, which can be helpful for exploring the data format.
- There is also a github for [@HDF5 Group][hdf5_git] and a [forum][hdforum] to post and read commonly asked questions
- The HDF5 Group has put out this [youtube][hdf5yt] tutorial playlist for learning about hdf5 and practicing in python. They also released this [tutorial][hdf5tut] video and accompanying [github][hdf5tut_git] repo.

## HDF5 in python

- To handle hdf5 files in python, use the `h5py` library. The best resource for the library are the [html docs][h5py_doc].
- [hdf5]: https://www.hdfgroup.org/
  [hdfview]: https://www.hdfgroup.org/download-hdfview/
  [myhdf5]: https://myhdf5.hdfgroup.org/
  [hdf5yt]: https://youtu.be/S74Kc8QYDac?si=20HfSIq7xQBjiItB
  [hdf5tut]: https://youtu.be/3ndbhId2vuY?si=tWEDAtwbOT0of3Xq
  [hdf5tut_git]: https://github.com/HDFGroup/hdf5-tutorial#
  [hdf5_git]: https://github.com/HDFGroup
  [hdforum]: https://forum.hdfgroup.org/
  [h5py_doc]: https://forum.hdfgroup.org/
