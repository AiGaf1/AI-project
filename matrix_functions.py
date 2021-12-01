import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import tsplib95 as tsp

def euc_dist(a,b):
  return np.linalg.norm(a-b)

def file_to_df(fileName):
    '''read points from file and trasform them to dataframe'''

    with open('TSP/' + fileName) as f:
        lines = f.readlines()

    read_lines = ['NODE_COORD_SECTION\n', 'DISPLAY_DATA_SECTION\n']

    if any(map(lambda v: v in read_lines, lines)):
        i = 0
        while i < len(lines):
            if lines[i] in read_lines:
                break
            i += 1
  
        N = len(lines) - 1 - i
        coords = lines[-N:]
        coords.pop()

        df = pd.DataFrame(columns=['point', 'x', 'y'])
        for i in range(len(coords)):
            coords[i] = coords[i].strip()
            values = coords[i].split()
            df = df.append({'point': values[0], 'x': values[1], 'y': values[2]}, ignore_index=True)

    return df.apply(pd.to_numeric)

def get_matrix(df_points):
    '''from dataframe of points gets adjacency matrix'''

    adj_matrix = np.zeros((len(df_points), len(df_points)))
    
    for i in range(adj_matrix.shape[0]):
        a = df_points.iloc[i,:].values
        a = np.array((a[1], a[2]))

        for j in range(adj_matrix.shape[1]):
            b = df_points.iloc[j,:].values
            b = np.array((b[1], b[2]))
            res = euc_dist(a,b)
            adj_matrix[i][j] = res

    return adj_matrix

def plotTSP(path, points, ax):

    """
    path: List of lists with the different orders in which the nodes are visited
    points: coordinates for the different nodes
    num_iters: number of paths that are in the path list
    
    """

    # Unpack the primary TSP path and transform it into a list of ordered 
    # coordinates

    x = []; y = []
    for i in path:
        x.append(points[i][1])
        y.append(points[i][2])
    
    ax.plot(x, y, 'co')

    # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
    a_scale = float(max(x))/float(100)

   
    # Draw the primary path for the TSP problem
    ax.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale, 
            color ='g', length_includes_head=True)
    for i in range(0,len(x)-1):
        ax.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = a_scale,
                color = 'g', length_includes_head = True)

    #Set axis too slitghtly larger than the set of x and y
    #ax.xlim(0, max(x)*1.1)
    #ax.ylim(0, max(y)*1.1)
    ax.draw()

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

def x_coord_of_point(D, j):
    return ( D[0,j]**2 + D[0,1]**2 - D[1,j]**2 ) / ( 2*D[0,1] )

def coords_of_point(D, j):
    x = x_coord_of_point(D, j)
    return np.array([x, math.sqrt( D[0,j]**2 - x**2 )])
    
def calculate_positions(D):
    (m, n) = D.shape
    P = np.zeros( (n, 2) )
    tr = ( min(min(D[2,0:2]), min(D[2,3:n])) / 2)**2
    P[1,0] = D[0,1]
    P[2,:] = coords_of_point(D, 2)
    for j in range(3,n):
        P[j,:] = coords_of_point(D, j) 
        if abs( np.dot(P[j,:] - P[2,:], P[j,:] - P[2,:]) - D[2,j]**2 ) > tr:
            P[j,1] = - P[j,1]
    return P 
    






