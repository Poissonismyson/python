class BinaryTree:
	## Inizializzazione di un albero
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

	## Inserimento di un nuovo nodo come figlo sinistro
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            ## Il nuovo valore sostituisce il vecchio
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

	## Inserimento di un nuovo nodo come figlo destro
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            ## Il nuovo valore sostituisce il vecchio
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


