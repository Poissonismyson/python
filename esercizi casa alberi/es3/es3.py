import BinaryTree, BuildTree

albero = BuildTree.costruisci_albero("albero.txt")

def somma_sottrazione(albero):
    if albero is None:
        return 0
    
    val = int(albero.getRootVal())
    
    if albero.getLeftChild() is not None or albero.getRightChild() is not None:
        return val+somma_sottrazione(albero.getRightChild()) + somma_sottrazione(albero.getRightChild())
     