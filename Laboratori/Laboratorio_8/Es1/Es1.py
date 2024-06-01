def prodotto(s1,s2):
    if not s1 or not s2:
        return 0
    s = max(s1) * max(s2)
    d = min(s1) * min(s2)
    return (s-d)
