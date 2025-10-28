# HDF5 Notes

## The HDF5 Data format

- HDF5: Hierarchical Data Format
- HDF5 is a binary data format that allows you to handle large datasets. It is a self describing data format meaning it contains metadata describing the data within and there is no need to write special parsers for the data (i.e. checking headers and character delemiters). It allows you to store multiple data format types together with context and ways to access the data in different ways. You should also not store data info in the file name and instead store it in the data's metadata (i.e. don't name your file something like BOLT-DNS-GRID2-v4.h5).
- Partial I/O. HDF5 supports partial input/output for data, meaning you don't need to load the entire file to memory to be able to extract or write the data that you want. This makes I/O more efficient.
- The hdf5 data format is also platform independent meaning you can create and access the data across different machines and environments.
- You can compress hdf5 data, i.e. for archival storage or transfer.
- The hdf5 data format consists of only three data structures: **Datasets**, **Attributes**, and **Groups**. Datasets are equivalent to multidimensional arrays. Attributes are the key-value metadata information that gets attached to datasets. Groups are containers that function similar to file folders and allow you to group datasets and even other groups together and organize them.
- Datasets have a single defined datatype (i.e. 64 bit float) and a prescribed shape (i.e. 2 by 2 array) and can be sliced meaning you can partially access the data within the dataset. There is not a practical size limit to how large a dataset can be.
- Attributes are stored with datasets as key-value pairs to help give context to the data they are attached to. This is a large part of what makes the hdf5 format self describing, you don't need separate files or notes to explain what your data is or how it is stored. Attributes themselves do not support partial I/O.
- Groups represent the relationship between your different datasets and allow you to organize multiple datasets of different datatypes all within the same file. The folder like structure provides more context to the data and helps make it self describing. Groups act as containers holding links. A link can point to a dataset or another group. Through this, a dataset can belong to multiple groups within your file.
- Datasets or Groups are often referred to as objects within the context of an hdf5 file.
- Paths help identify objects by the links traversed to retrieve them, similar to the full file name of a file on your computer. An object being able to have multiple groups means there can be multiple paths leading to it. You can create a group(s) or dataset(s) anywhere within your file and are not restricted to a specific structure. 

## Resources for learning HDF5

- The official HDF5 Group [website][hdf5] is a good resource to learn more about hdf5 and see available resources or tutorials on handling the data format. Many programming languages such as python, Fortran, and Matlab have a way to handle hdf5 files. The HDF5 Group even has a visual tool for handling the file format, [HDFView][hdfview]. There is also a [browser][myhdf5] application, which can be helpful for exploring the data format.
- There is also a github for [@HDF5 Group][hdf5_git] and a [forum][hdforum] to post and read commonly asked questions
- The HDF5 Group has put out this [youtube][hdf5yt] tutorial playlist for learning about hdf5 and practicing in python. They also released this [tutorial][hdf5tut] video and accompanying [github][hdf5tut_git] repo.

## HDF5 in python

- To handle hdf5 files in python, use the `h5py` library. The best resource for the library are the [html docs][h5py_doc].
- python is particularly useful for learning hdf5 or as a standalone hdf5 file handler since it is a dynamically typed language and it's hdf5 library interfaces well with python's intrinsically robust datatypes and classes. This makes it easy to play around and learn with. For standalone post processing of hdf5 files, it is also very useful and easy to intuitively generalize functions and classes based on your dataset (i.e. a custom us3d post processor). For internal reading/writing of hdf5 files for use within your scientific codes, it is probably best to use the library specific to the language your code is written in (i.e. Fortran, c++, etc.).
- [hdf5]: https://www.hdfgroup.org/
  [hdfview]: https://www.hdfgroup.org/download-hdfview/
  [myhdf5]: https://myhdf5.hdfgroup.org/
  [hdf5yt]: https://youtu.be/S74Kc8QYDac?si=20HfSIq7xQBjiItB
  [hdf5tut]: https://youtu.be/3ndbhId2vuY?si=tWEDAtwbOT0of3Xq
  [hdf5tut_git]: https://github.com/HDFGroup/hdf5-tutorial#
  [hdf5_git]: https://github.com/HDFGroup
  [hdforum]: https://forum.hdfgroup.org/
  [h5py_doc]: https://forum.hdfgroup.org/
