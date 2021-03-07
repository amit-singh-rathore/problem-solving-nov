def zeros_to_left(array):
    if len(array) < 1:
        return array
    
    non_zero_idx = zero_idx = len(array)-1
    
    while non_zero_idx > 0:
        if array[zero_idx]==0:
            non_zero_idx -= 1
        if array[non_zero_idx] !=0:
            array[zero_idx], array[non_zero_idx] = array[non_zero_idx], array[zero_idx]
        if array[zero_idx]!=0:
            zero_idx -= 1
    return array
