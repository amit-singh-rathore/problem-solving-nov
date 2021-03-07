from collections import deque

def canReach( arr, start):
    deque_ = deque([start])
    visited = set()
    
    while deque_:
        source_idx = deque_.popleft()
        if arr[source_idx] == 0:
            return True
            
        visited.add(source_idx)
        
        for idx in [source_idx+arr[source_idx], source_idx-arr[source_idx]]:
            if 0 <= idx < len(arr) and idx not in visited:
                deque_.append(idx)
                visited.add(idx)
        
    
    return False
        

print(canReach([4,2,3,0,3,1,2], 5))
