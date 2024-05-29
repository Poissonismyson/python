def aggrega(s1,s2,s3):
    if not s1 or not s2 or not s3:
        return set()
    s = s1.union(s2)

    return (s-s3)
