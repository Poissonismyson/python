def verificaCrescenza(file):
    f = open(file, "r")
    l1 = f.readline().rstrip().split(",")
    l2 = f.readline().rstrip().split(",")

    if len(l1) == 0 or len(l2) == 0 or len(l1) != len(l2):
        return False
    
    else:
        return check(l1,l2)
    

def check(l1,l2):
    if len(l1) == 0:
        return True
    if int(l2[0]) > int(l1[0]) and int(l2[0]) % int(l1[0]) == 0:
        return check(l1[1:], l2[1:])
    else:
        return False
