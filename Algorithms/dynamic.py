import itertools

def dynamProg(matrix):
    startPoint=0
    n = len(matrix)
    C = {}

    
    #initial cost
    for k in range(1, n):
        C[(2**k, k)] = (matrix[0][k], 0)
    #print(C[(1, 1)])
    
    #iterate through subsets
    for s in range(2, n):
        for S in itertools.combinations(range(1, n), s):
            b = 0
            for i in S:
              b +=2**i
              
            #find the minimum weight
            for k in S:
                p =b& ~(2**k)
                r = []
                for m in S:
                    if m == 0 or m == k:
                        continue
                    r.append((C[(p, m)][0] + matrix[m][k], m))  
                C[(b, k)] = min(r)

    
    #optimal cost
    r = []
    for k in range(1, n):
        r.append((C[(b, k)][0] + matrix[k][0], k))
    opt, beg= min(r)
    

    #backtack full path
    path = []
    for i in range(n - 1):
        path.append(beg)
        ne = b&~(2**beg)
        empty, beg = C[(b, beg)]
        b = ne
    

    path.append(0)
    path.insert(0,startPoint)

    return path, opt