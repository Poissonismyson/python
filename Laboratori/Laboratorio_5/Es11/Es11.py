def trasposta(m):
	
	ret = []
	
	if len(m) == 0:
		return ret
	
	for i in range(len(m[0])):
		a = []
		for j in range(len(m)):
			a.append(m[j][i])
			
		ret.append(a)

	return ret
	