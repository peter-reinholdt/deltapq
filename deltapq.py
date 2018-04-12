#!/usr/bin/env python

import argparse
import horton
import re
import numpy as np
from helpers import to_numpy, from_numpy
from cubic import get_cubic_grid, write_cube


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-i", dest="qm_files_in",  default=[], nargs="+", help="A number of input qm files. Accepted formats are fchk, molden,\
            wfn")
    parser.add_argument("-o", dest="outfile", type=str, default="out.cube", help="Name of output cube file", metavar="out.cube")
    parser.add_argument("--operation", dest="operation", type=str, default="[0] - [1]", help="Use custom elementwise operation instead of default difference. Example: exp([0]) + [1] * [2]")
    parser.add_argument("--cube-buffer", dest="cube_buffer", type=float, default=5.0, help="Size of buffer region to determine box dimensions")
    parser.add_argument("--cube-density", dest="cube_density", type=float, default=4.0, help="Number of points [per bohr] in box")

    args = parser.parse_args()
    if not args.qm_files_in:
        raise ValueError("Missing input QM files")
    if type(args.qm_files_in) == "str":
        infiles = [args.qm_files_in]
    else:
        infiles = args.qm_files_in

    operation = re.sub("\[", "dms[", args.operation)
    operation = re.sub("\]", "][i,j]", operation)
    #get density matrices
    molecules = []
    for filename in infiles:
        print(filename)
        molecules.append(horton.IOData.from_file(filename))
    dms = []
    for mol in molecules:
        dms.append(to_numpy(mol.get_dm_full()))
    
    reference = molecules[0]
    dm = reference.get_dm_full()
    for i in range(reference.obasis.nbasis):
        for j in range(reference.obasis.nbasis):
             dm.set_element(i,j, eval(operation))

    #get cube points
    xyzgrid, origin, npts, spacings = get_cubic_grid(reference, args.cube_buffer, args.cube_density)
    #evaluate real-space density on the cubic grid, using the transformed dm in the basis of the first molecule
    data = reference.obasis.compute_grid_density_dm(dm, xyzgrid)
    #write the transformed real-space density to cube file
    write_cube(args.outfile, reference, data, origin, npts, spacings)
