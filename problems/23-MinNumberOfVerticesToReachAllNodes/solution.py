def minimum_vertices(edges, n):
    in_degree = [0] * n
    for start, end in edges:
        in_degree[end] += 1
    print([i for i, degree in enumerate(in_degree) if degree == 0])
    
minimum_vertices([[0,1],[0,2],[2,5],[3,4],[4,2]], 6)

minimum_vertices([[0,1],[3,1],[2,1],[1,4],[2,4]], 5)