import BinaryTree, BuildTree

#Funzione che calcola l'altezza di un albero binario

def trovaAltezza(tree):
    if tree is None:
        return 0
    if tree.getLEftChild() is None and tree.getRightChild() is None:
        return 0
    h_sin = 1 + trovaAltezza(tree.getLEftChild())
    h_des = 1 + trovaAltezza(tree.getRightChild())
    return max(h_sin, h_des)

#Funzione che verifica se un valore corrisponde all'identificativo di un nodo oppure no

def trovaValore(tree, v):
    if tree == None:
        return False
    elif tree.info == v:
        return True
    else:
        return trovaValore(tree.left, v) or trovaValore(tree.right, v)
