import numpy as np

def greedyAlgoVersion2(adj_matrix):

    
    best_length = np.inf
    best_route = []

    city_lst = [i for i in range(len(adj_matrix))]
    
    for cur_city in city_lst: #n
        route = [cur_city] 
        length = 0

        for _ in range(len(adj_matrix)):
            sorted_ind_cities = np.argsort(adj_matrix[cur_city]) # n * log(n)     

            for next_city in sorted_ind_cities: #n  # searching for the smallest distance  
                if next_city not in route: # 1 * n
                    route.append(next_city)
                    length += adj_matrix[cur_city][next_city]
                    cur_city = next_city
                    break
        
        length += adj_matrix[route[0]][cur_city]
        route.append(route[0])

        if best_length > length:
            best_length = length
            best_route =  route

    return best_route, best_length


#n^3 *  log(n)



