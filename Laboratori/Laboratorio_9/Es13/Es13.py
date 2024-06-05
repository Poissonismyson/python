def ricercaBinaria(l, left, right, v):
    
    if left > right:
        return -1
    
    mid = (left + right)//2

    if l[mid] == v:
        return mid
    elif l[mid] > v:
        return ricercaBinaria(l,left,mid - 1,v)
    elif l[mid] < v:
        return ricercaBinaria(l,mid+1,right,v)


