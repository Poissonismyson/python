def restituiscistringa(m,n):
	ret = ''
	for i in range(len(m)):
		if (i+1) % n == 0:
			for j in range(len(m[i])):
				ret += str(m[i][j])
			ret += " "

		
	return ret.rstrip(' ')
	

