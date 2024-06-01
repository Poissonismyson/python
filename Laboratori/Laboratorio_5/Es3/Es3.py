def scambiarighe(m,i1,i2):
	ret = []
	if len(m) != 0 and validamatrice(m) and i2 < len(m) and i1 < len(m) and i2 > -1 and i1 > -1:
		for i in range(len(m)):
			riga = []
			for j in range(len(m[0])):
				if i == i1:
					riga.append(m[i2][j])
				elif i == i2:
					riga.append(m[i1][j])
				else:
					riga.append(m[i][j])
			ret.append(riga)
		return ret
	else:
		return m
	


def validamatrice(l):
	lunghezza = len(l[0])
	for i in range(1,len(l)):
		if len(l[i]) != lunghezza:
			return False
	return True