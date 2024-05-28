def verificadiagonale(m):
	if not m:
		return False
	
	for i in range(len(m)):
		for j in range(len(m[i])):
			if i != j:
				if m[i][j] != 0:
					return False
			

	return True
