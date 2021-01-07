def binary_search(array, item):
	first = 0
	last = len(array)-1
	index = None
	while( first<=last and not index):
		mid = (first + last)//2
		if array[mid] == item :
			index = mid
		else:
			if item < array[mid]:
				last = mid - 1
			else:
				first = mid + 1
	if index:
	    return index
	else:
	    return "Not found"
	    
arr = [ 2, 3, 4, 10, 40 ] 
x = [10, 15, 4]

for item in x:
    print(binary_search(arr, item))