def uguali(albero1,albero2, is_root_call = True):

    if albero1 is None and albero2 is None:
        return not is_root_call
    
    if albero1 is None or albero2 is None:
        return False

    if albero1.getRootVal() != albero2.getRootVal():
        return False
    
    return uguali(albero1.getLeftChild(), albero2.getLeftChild(), False) and uguali(albero1.getRightChild(), albero2.getRightChild(), False)


