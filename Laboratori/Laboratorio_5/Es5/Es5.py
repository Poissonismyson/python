def validatriangolareinferiore(m):
	for i in m:
		if len(i) != len(m):
			return False
		
	for i in range(len(m)):	
		for j in range(i+1,len(m)):
			if m[i][j] != 0:
				return False
	return True

