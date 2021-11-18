import itertools
def brute_force(m):
    #holds the possible paths
    possiblePaths=[]
    #the starting point of the journey
    startPoint=0
    #list of nodes
    nodes= list(range(startPoint+1, len(m)))
    #length of array-1
    L=len(m)-1

    #calculating the possible paths
    for subset in itertools.permutations(nodes, L):
        list1=list(subset)
        list1.insert(0,startPoint)
        list1.append(0)
        possiblePaths.append(list1)
  #print the Hamilton Circuits
  #print("Hamilton Circuits:",possiblePaths)

  #list of Weights
        listOfWeights=[]

  #calculating the weights of the paths
    for j in range(len(possiblePaths)):
        l=[]
        for i in range(len(possiblePaths[j])-1):
            l.append(m[possiblePaths[j][i]][possiblePaths[j][i+1]])
        listOfWeights.append(sum(l))
  #print the weights of the Hamilton Ciruits
  #print("Weights:", listOfWeights)

  #finding the minimum weight
    min_value=min(listOfWeights)
    min_index = listOfWeights.index(min_value)

    return possiblePaths[min_index], min_value