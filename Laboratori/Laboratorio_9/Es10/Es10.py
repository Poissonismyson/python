def valutaEspressione(albero):
    if albero is None:
        return 0
    
    if albero.getLeftChild() is None and albero.getRightChild() is None:
        return int(albero.getRootVal())
    else:

    
        operatore = albero.getRootVal()

        left_val = valutaEspressione(albero.getLeftChild())

        right_val = valutaEspressione(albero.getRightChild())

        if operatore == '+':
            return left_val + right_val
        elif operatore == '-':
            return left_val - right_val
        elif operatore == '/':
            return left_val / right_val
        elif operatore == '*':
            return left_val * right_val
        
                
                


    
