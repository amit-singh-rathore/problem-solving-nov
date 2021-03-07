def valid_mountain_array(array):
    if len(array)<3:
        return False
    idx = 1
    while idx < len(array) and array[idx]>array[idx-1]:
        idx += 1
    
    if idx==1 or idx==len(array):
        return False
    
    while idx < len(array) and array[idx]<array[idx-1]:
        idx += 1
    
    if idx == len(array):
        return True
    else:
        return False