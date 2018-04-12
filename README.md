# deltapq
A small script that can be used to manipulate density matrices and output cube-files.
A common usage is subtracting two density matrices of structures with slightly different geometry.

## Usage
```
usage: deltapq.py [-h] [-i QM_FILES_IN [QM_FILES_IN ...]] [-o out.cube]
                  [--operation OPERATION] [--cube-buffer CUBE_BUFFER]
                  [--cube-density CUBE_DENSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i QM_FILES_IN [QM_FILES_IN ...]
                        A number of input qm files. Accepted formats are fchk,
                        molden, wfn
  -o out.cube           Name of output cube file
  --operation OPERATION
                        Use custom elementwise operation instead of default
                        difference. Example: exp([0]) + [1] * [2]
  --cube-buffer CUBE_BUFFER
                        Size of buffer region to determine box dimensions
  --cube-density CUBE_DENSITY
                        Number of points [per bohr] in box
```
By default, `deltapq` operates on two qm-files and takes the elementwise difference of the density matrix, but custom operations can be defined through the `--operation` option. For example, to evaluate the `sin()` of a single density matrix, use `--operation sin([0])`.

## Installation
The script depends on numpy and on the horton program. 
Install the depedencies and clone the repository.
```
git clone 
https://github.com/peter-reinholdt/deltapq.git
```

### Installing dependencies with conda
```
conda install numpy
conda install -c theochem horton
```
