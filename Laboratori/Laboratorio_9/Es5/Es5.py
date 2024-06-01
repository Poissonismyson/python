def mischiaStringhe(s1,s2):
    if len(s1) != len(s2):
        return ''
    if not s1 and not s2:
        return ''
    else:
        return s1[0] + s2[-1] + mischiaStringhe(s1[1:],s2[:len(s2)-1])

