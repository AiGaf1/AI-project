import numpy as np

def greedyAlgoVersion1(adj_matrix):

    cur_city = 0 # current city
    route = [0] 
    length = 0
    
   
    for i in range(len(adj_matrix)): #O(n)

        sorted_ind_cities = np.argsort(adj_matrix[cur_city]) #O(nlogn)  

        for next_city in sorted_ind_cities: #O(n)  # searching for the smallest distance 
            if next_city not in route: #O(n)
                route.append(next_city)
                length += adj_matrix[cur_city][next_city]
                cur_city = next_city
                break
    
    length += adj_matrix[route[-1]][0]
    route.append(0)

    return route, length


# n * (n + nlogn) * n 
#n^3 + n^2logn



    


