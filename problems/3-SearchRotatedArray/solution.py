def search(array, start_idx, end_idx, key):
    if start_idx> end_idx:
        return -1
    
    mid_idx = (start_idx + end_idx) // 2
    if array[mid_idx] == key: 
        return mid_idx
    
    if array[mid_idx] >= array[end_idx]:
        if key >= array[start_idx] and key <= array[mid_idx]: 
            return search(array, start_idx, mid_idx-1, key) 
        return search(array, mid_idx + 1, end_idx, key)
    
    if key >= array[mid_idx] and key <= array[end_idx]: 
        return search(array, mid_idx + 1, end_idx, key) 
    return search(array, start_idx, mid_idx-1, key) 
    
def binary_search_rotated(array, key):
    return search(array, 0, len(array)-1, key)