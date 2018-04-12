# deltapq
Subtract density matrices
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
