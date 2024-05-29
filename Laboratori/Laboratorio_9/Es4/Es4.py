def massimo(albero):
    if albero == None:
        return 0
    
    root_val = albero.getRootVal()

    left_max = massimo(albero.getLeftChild())
    right_max=massimo(albero.getRightChild())

    return max(int(root_val),left_max,right_max)
                
                


    
