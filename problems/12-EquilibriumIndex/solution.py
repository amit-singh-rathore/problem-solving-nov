def equilibrium_index(array):
    if len(array)<3:
        return "Not enough elemnts for Equilibirium check"
    left_sum = array[0]
    total_sum = sum(array)
    for idx, item in enumerate(array[1:]):
        if left_sum == total_sum - (item + left_sum):
            return idx+1
        else:
            left_sum += item
    
    return "No equilibrium Index found"
    
	    
array = [-7, 1, 5, 2, -4, 3, 0]

print(equilibrium_index(array))