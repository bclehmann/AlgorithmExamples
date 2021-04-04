def pow(a, b):
	if b == 0:
		return 1
	
	if b == 1:
		return a
	
	tmp = pow(a, b // 2)
	tmp *= tmp
	
	if b % 2 == 1:
		tmp *= a
	
	return tmp
