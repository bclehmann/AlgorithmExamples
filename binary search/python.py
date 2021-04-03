def binary_search(array, target):
	low = 0
	high = len(array) - 1
	
	while high >= low:
		mid = (high + low) // 2
		
		if array[mid] > target:
			high = mid - 1
		elif array[mid] < target:
			low = mid + 1
		else:
			return mid
	
	return -1
