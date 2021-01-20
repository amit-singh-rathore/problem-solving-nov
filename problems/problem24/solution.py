def kClosest(points, K):
    if K < 1:
        raise Exception('Invalid k')
    points.sort(key= lambda x : (x[0])**2+ (x[1])**2)
    return points[:K]
    
print(kClosest([[1,3],[-2,2]], 1))