def optimized_sequential_search(array, target):
	for i in range(len(array)):
		if array[i] == target:
			return i
		
		if array[i] > target:
			return -1
	
	return -1
