
def find_major_element(array):
    
    # below block of code finds a majority element
    major_element = array[0]
    count = 0
    for i in range(len(array)):
        if array[i] == major_element:
            count += 1
        else:
            count -= 1
        
        if count <=0:
            major_element = array[i]
            count = 1
    
    # below block of verifies if majority element occures more than or equal n/2 times    

    if array.count(major_element)>=(len(array)/2):
        return major_element
        
    return -1

print(find_major_element([ 3, 10, 3, 2, 3, 5, 3, 1, 3, 4, 3, 10, 5, 3]))