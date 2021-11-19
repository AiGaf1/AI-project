import numpy as np


def initial_bound(A):
    sum = 0
    for i in range(A.shape[0]):
        a, b = sorted(A[i])[:2]
        sum += (a + b)
    return sum / 2


def branchAndBound_recursive(A, nodes, current_path, current_bound, current_cost, level, visited):
    global best_path, best_cost
    N = len(nodes)

    if level == N:

        path_cost = current_cost + A[current_path[level-1]][current_path[0]]

        if path_cost < best_cost:
            current_path[N] = 0
            best_path = current_path.copy()
            best_cost = path_cost

        return best_path, best_cost

    for i in range(N):

        x = current_path[level - 1]
        y = i

        if (A[current_path[level - 1]][i] != np.inf and visited[i] == False):

            temporal = current_bound
            current_cost += A[x][y]

            if level == 1:
                current_bound -= ( np.min(A[x]) + np.min(A[y]) ) / 2
            else:
                _, a = sorted(A[x])[:2]
                current_bound -= ( a + np.min(A[y]) ) / 2

            if current_bound + current_cost < best_cost:
                current_path[level] = i
                visited[i] = True
                branchAndBound_recursive(A, nodes, current_path, current_bound, current_cost, level+1, visited)

            current_cost -= A[current_path[level - 1]][i]
            current_bound = temporal

            visited = [False] * len(visited)
            for j in range(level):
                if current_path[j] != -1:
                    visited[current_path[j]] = True


def branchAndBound(dist_matrix):

    N = len(dist_matrix)
    startPoint = 0
    nodes = list(range(startPoint, N))

    current_path = [-1] * (N + 1)
    visited = [False] * N

    init_bound = initial_bound(dist_matrix)

    current_path[0] = 0
    visited[0] = True

    branchAndBound_recursive(dist_matrix, nodes, current_path, init_bound, 0, 1, visited)
    
    return best_path, best_cost