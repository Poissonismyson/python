def preordine(tree):
    if tree is None:
        return
    ## In generale, invece di stampare il valore si fa qualcosa di più utile
    print(tree.getRootVal())
    preordine(tree.getLeftChild())
    preordine(tree.getRightChild())

def postordine(tree):
    if tree is None:
        return
    postordine(tree.getLeftChild())
    postordine(tree.getRightChild())
    ## In generale, invece di stampare il valore si fa qualcosa di più utile
    print(tree.getRootVal())

def simmetrica(tree):
    if tree is None:
        return
    simmetrica(tree.getLeftChild())
    ## In generale, invece di stampare il valore si fa qualcosa di più utile
    print(tree.getRootVal())
    simmetrica(tree.getRightChild())


import BuildTree, BinaryTree

albero = BuildTree.costruisci_albero("albero.txt") #cambiare il nome del file per cambiare albero in input
print("Visita in preordine:")
preordine(albero)
print()
print("Visita in postordine:")
postordine(albero)
print()
print("Visita in ordine simmetrico:")
simmetrica(albero)
