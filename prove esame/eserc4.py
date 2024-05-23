
def A_Ex4(albero,x):
    if albero is None:
        return 0
    
    val = albero.getRootVal()
    if val == x:
        val = 0
    
    return val + A_Ex4(albero.getLeftChild(),x) + A_Ex4(albero.getRightChild(),x)
