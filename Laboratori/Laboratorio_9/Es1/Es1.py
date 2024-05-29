def uguali(s1,s2):
    if not s1 and not s2:
        return True
    elif not s1 or not s2:
        return False
    elif s1[0] != s2[0]:
        return False
    else:
        return uguali(s1[1:],s2[1:])


