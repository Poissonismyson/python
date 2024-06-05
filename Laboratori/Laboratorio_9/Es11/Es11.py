def massimo(l):
<<<<<<< HEAD
    if len(l) == 0:
        return 0
    
    if len(l) == 1:
        return l[0]
    
    else:
        return max(l[0], massimo(l[1:]))
=======
    if len(l) < 1:
        return 0
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0],massimo(l[1:]))
>>>>>>> d18414897a74660b83bb9cca78ecc9891bf09a2a
