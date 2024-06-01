def contaFoglie(albero):
    if albero is None:
        return 0
    
    if albero.getLeftChild() is None and albero.getRightChild() is None:
        return 1
    
    return contaFoglie(albero.getLeftChild()) + contaFoglie(albero.getRightChild())
    
    

                
                


    
