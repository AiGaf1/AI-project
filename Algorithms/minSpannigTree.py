import networkx as nx
import time
import numpy as np

def calculate_cost(path,A):
  cost = 0
  for n in range(len(path)):
    if n < len(path)-1:
      i = path[n]
      j = path[n+1]
      cost += A[i][j]
  return cost

def matrix_to_graph(A):
  
  G=nx.Graph()

  for i in range(A.shape[0]):
    for j in range(len(A[i])):
      if A[i][j] != np.inf:
        G.add_edge(i, j, weight=A[i][j])

  return G

def dfs(mst, mstSet):

  results = []

  # we try all possible combinations with every node as the source of the dfs
  for node in mstSet:
    dfs = list(nx.algorithms.traversal.edgedfs.edge_dfs(mst,source=node,orientation='ignore'))

    dfs_list = []
    tsp = []

    for tpl in dfs:
      dfs_list.append(tpl[0])
      dfs_list.append(tpl[1])

    for node in dfs_list:
      if node not in tsp:
        tsp.append(node)
    results.append(tsp)

  return results


def prism_algo(G,A):

  # initialization
  mstSet = []
  mst = nx.Graph()
  mst_cost = 0
  nodes = sorted(G.nodes)
  vertices = dict.fromkeys(nodes, np.inf)
  vert_map = dict.fromkeys(nodes, 0)
  mst.add_node(0)
  vertices[nodes[0]] = 0

  while len(mstSet) < len(nodes):

    rem_nodes = [node for node in nodes if node not in mstSet]
    remaining = {key: vertices[key] for key in rem_nodes}

    minval = np.amin(list(remaining.values()))
    res = [k for k, v in remaining.items() if v==minval]
    new = res[0]
    mstSet.append(new)

    if len(mstSet) > 1:
      aux = A[new]
      neighbor = np.where(aux == minval)
      mst.add_node(new)
      mst.add_node(vert_map[new])
      mst.add_edge(vert_map[new],new, weight=minval)

    mst_cost += vertices[new]

    for n in G.neighbors(new):
      if (n not in mstSet) and G[new][n]["weight"] < vertices[n]:
        vertices[n] = G[new][n]["weight"]
        vert_map[n] = new

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

  return solution,cost

def run_MNS(dist_matrix):

    G = matrix_to_graph(dist_matrix)
    path, distance = mst_tsp(G,dist_matrix)

    return path, distance
