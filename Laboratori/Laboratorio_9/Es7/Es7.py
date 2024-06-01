def checkPieno(albero):

    if not albero:
        return False

    if albero.getLeftChild() is None and albero.getRightChild() is None:
        return True
    
    if albero.getLeftChild() is not None and albero.getRightChild() is not None:
        return checkPieno(albero.getLeftChild()) and  checkPieno(albero.getRightChild())

    
    return False

    
