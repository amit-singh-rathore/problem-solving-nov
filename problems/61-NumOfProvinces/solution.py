def findCircleNum(isConnected):
    province_count = 0
    n = len(isConnected)
    
    connections = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i!=j and isConnected[i][j] == 1:
                connections[i].append(j)
    
    if len(connections) < n:
        province_count = n-len(connections)
        
    processed = set()
    for source in connections:
        if source not in processed:
            province_count+= 1
            stack = [source]
            processed.add(source)
            while stack:
                popped = stack.pop()
                for dest in connections[popped]:
                    if dest not in processed:
                        stack.append(dest)
                        processed.add(dest)
    return province_count
        