from BinaryTree import *

from BuildTree import *

#Funzione che calcola l'altezza di un albero binario

def trovaAltezza(tree):
    if tree is None:
        return 0
    if tree.getLeftChild() is None and tree.getRightChild() is None:
        return 0
    h_sin = 1 + trovaAltezza(tree.getLeftChild())
    h_des = 1 + trovaAltezza(tree.getRightChild())
    return max(h_sin, h_des)

#Funzione che verifica se un valore corrisponde all'identificativo di un nodo oppure no

def trovaValore(tree, v):
    if tree is None:
        return False
    if tree.getRootVal() == v:
        return True
    x = trovaValore(tree.getLeftChild(), v)
    y = trovaValore(tree.getRightChild(), v)
    return trovaValore(tree.left, v) or trovaValore(tree.right, v)
