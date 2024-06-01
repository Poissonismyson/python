
def contaOccorrenze(s,c):

    if not s:
        return 0

    if s[0] != c:
        return contaOccorrenze(s[1:],c)
    if s[0] == c:
        return 1 + contaOccorrenze(s[1:],c)

