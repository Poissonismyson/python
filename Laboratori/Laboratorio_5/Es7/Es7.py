def verificalista(l,i):
	for r in range(len(l)):
		if r % 2 == 0:
			somma = sum(l[r])
			if somma != i:
				return False
	return True

	return None
