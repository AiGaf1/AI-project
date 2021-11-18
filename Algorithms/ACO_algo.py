import numpy as np
import random

NUMANT = 2
NUMITER = 2
ALPHA = 1
BETA = 2
RHO = 0.3
LEFT = 2
Q = 1

def updateTau(tau_matrix, deltaTau):

    for i in range(len(tau_matrix)):
        for j in range(len(tau_matrix)):

            tau_matrix[i][j] = (1.0 - RHO) * tau_matrix[i][j] + deltaTau[i][j]

    return tau_matrix


def getDeltaTauPerAnt(deltaTauColony, route, length):

    for i in range(len(route) - 1):
        cur_city = route[i]
        next_city = route[i + 1]
        deltaTauColony[cur_city][next_city] = deltaTauColony[next_city][cur_city] =+ Q/length

    return deltaTauColony

def selectNextCity(adj_matrix, cur_city, tau_matrix):

    n_cities = len(adj_matrix)
    city_lst = [i for i in range(n_cities)]

    heurist_matrix = [[ dist ** -1 if dist != 0 else 0 for dist in lst ] for lst in adj_matrix] #heurist_matrix = adj_matrix ** -1

    
    
    prob_dict = {}
    denomin = 0

    for city in range(len(city_lst)):
        if city in city_lst:
            prob = tau_matrix[cur_city][city] ** ALPHA * \
                heurist_matrix[cur_city][city] ** BETA
            prob_dict[city] = prob
            denomin += prob

    next_city = -1




    if len(prob_dict) == 1:
        next_city = list(prob_dict.keys())[0]
    else:
        sumSelect = 0
        generatedProbab = random.uniform(0, 1)

        for i in prob_dict: # i = city index

            prob_dict[i] /= denomin
            sumSelect += prob_dict[i]

            if sumSelect >= generatedProbab:
                next_city = i
                break

        next_city if next_city != -1 else list(prob_dict.keys())[-1]
    return next_city


def makeRoute(adj_matrix, length, tau_matrix):

    cur_city = 0
    route = [0]
    
    while len(adj_matrix) != len(route):
        next_city = selectNextCity(adj_matrix, cur_city, tau_matrix)
        route.append(next_city)

        length += adj_matrix[cur_city][next_city]
        cur_city = next_city
    
    length += adj_matrix[cur_city][0]

    return route, length

def ACO(adj_matrix):

    n_cities = len(adj_matrix)
    best_length = float('inf')
    tau_matrix = np.ones((n_cities, n_cities))

    for colony in range(NUMITER):
        deltaTauColony = np.zeros((n_cities, n_cities))
        
        for ant in range(NUMANT):
            cur_length = 0

            cur_route, cur_length = makeRoute(adj_matrix, cur_length, tau_matrix)
            deltaTauColony = getDeltaTauPerAnt(deltaTauColony, cur_route, cur_length)

            if best_length > cur_length:
                best_length = cur_length
                best_route = cur_route

        tau_matrix = updateTau(tau_matrix, deltaTauColony)

    return best_route, best_length




