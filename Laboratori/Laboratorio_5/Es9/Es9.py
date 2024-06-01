def simmetrica_quadrata(m):

	if not m: #controllo se la matrice è vuota
		return False 
	

	for r in m:
		if len(r) != len(m): #controllo se la matrice è quadrata
			return False

	

	for i in range(len(m)):
		for j in range(i,len(m)): #ottimizzo per verificare solo il triangolo superiore
			if m[i][j] != m[j][i]: #controllo simmetria
				return False
	
	return True




