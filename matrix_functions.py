import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import tsplib95 as tsp

def get_coord(filename):

    # load an instance
    instance = tsp.loaders.load(filename)
# get the node coords from an instance
    coords = instance.node_coords
    return list(coords.values())

def get_adj_matrix(filepath):

    instance = tsp.loaders.load(filepath)
    coords = instance.node_coords

    matrix = np.zeros((len(coords), len(coords)))

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            res = float(tsp.distances.euclidean(coords[i+1], coords[j+1]))
            if i==j:
                matrix[i][j] = np.inf
            else:
                matrix[i][j] = res
    return matrix

# def x_coord_of_point(D, j):
#     return ( D[0,j]**2 + D[0,1]**2 - D[1,j]**2 ) / ( 2*D[0,1] )

# def coords_of_point(D, j):
#     x = x_coord_of_point(D, j)
#     return np.array([x, math.sqrt( D[0,j]**2 - x**2 )])
    
# def calculate_positions(D):
#     (m, n) = D.shape
#     P = np.zeros( (n, 2) )
#     tr = ( min(min(D[2,0:2]), min(D[2,3:n])) / 2)**2
#     P[1,0] = D[0,1]
#     P[2,:] = coords_of_point(D, 2)
#     for j in range(3,n):
#         P[j,:] = coords_of_point(D, j) 
#         if abs( np.dot(P[j,:] - P[2,:], P[j,:] - P[2,:]) - D[2,j]**2 ) > tr:
#             P[j,1] = - P[j,1]
#     return P 
    






