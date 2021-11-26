import networkx as nx
import time
import numpy as np

def matrix_to_graph(A):
  
  G=nx.Graph()

  for i in range(A.shape[0]):
    for j in range(len(A[i])):
      if A[i][j] != np.inf:
        G.add_edge(i, j, weight=A[i][j])

  return G


def prism_algo(G,A):

  # initialization
  mstSet = []
  mst = nx.Graph()
  mst_cost = 0
  nodes = sorted(G.nodes)
  vertices = dict.fromkeys(nodes, np.inf)
  vertices[nodes[0]] = 0

  while len(mstSet) < len(nodes):

    rem_nodes = [node for node in nodes if node not in mstSet]
    remaining = {key: vertices[key] for key in rem_nodes}

    #print(remaining)

    minval = np.amin(list(remaining.values()))
    res = [k for k, v in remaining.items() if v==minval]
    new = res[0]
    mstSet.append(new)
    mst.add_node(new)

    if len(mstSet) > 1:
      aux = A[new]
      neighbor = np.where(aux == minval)
      mst.add_edge(new,neighbor[0][0], weight=minval)

    mst_cost += vertices[new]

    for n in G.neighbors(new):
      if G[new][n]["weight"] < vertices[n]:
        vertices[n] = G[new][n]["weight"]
    #print(vertices)

  #print(mstSet)

  return mst, mstSet, mst_cost


def mst_tsp(G,A):

  mst, mstSet, mst_cost = prism_algo(G,A)

  # preorder trasversal of mst
  solution = list(nx.dfs_preorder_nodes(mst, source=mstSet[0]))
  solution.append(mstSet[0])
  
  # cost of tour
  cost = 0
  for n in range(len(solution)):
    if n < len(solution)-1:
      i = solution[n]
      j = solution[n+1]
      cost += A[i][j]

  return solution, cost

def run_MNS(dist_matrix):

    G = matrix_to_graph(dist_matrix)
    path, distance = mst_tsp(G,dist_matrix)

    return path, distance
