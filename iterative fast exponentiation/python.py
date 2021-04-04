def pow(a, b):
	if b == 0:
		return 1
	
	prod = 1
	
	while b > 0:
		if b % 2 == 1:
			prod *= a
		
		a *= a
		b //= 2
	
	return prod
