#!/usr/bin/env python
import numpy as np

def to_numpy(matrix):
    out = np.zeros((matrix.nbasis, matrix.nbasis))
    for i in range(matrix.nbasis):
        for j in range(matrix.nbasis):
            out[i,j] = matrix.get_element(i,j)
    return out

def from_numpy(matrix, array):
    for i in range(matrix.nbasis):
        for j in range(matrix.nbasis):
            matrix.set_element(i,j, array[i,j])
    return matrix


