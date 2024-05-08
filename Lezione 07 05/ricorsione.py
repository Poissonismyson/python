class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

def insertLeft(self,newNode):
    if self.leftChild == None:
        self.leftChild = BinaryTree(newNode)
    else:
        t = BinaryTree(newNode)
        t.leftChild = self.leftChild
        self.leftChild = t

def GetLeftChild(self):
    return self.leftChild

def GetRightChild(self):
    return self.rightChild

def SetRootVal(self,obj):
    self.key = obj

def preordine(tree):
    if tree:
        print(tree.key)
        preordine(tree.leftChild)
        preordine(tree.rightChild)

def postordine(tree):
    if tree:
        postordine(tree.leftChild)
        postordine(tree.rightChild)
        print(tree.key)

def simmetrica(tree):
    if tree:
        simmetrica(tree.leftChild)
        print(tree.key)
        simmetrica(tree.rightChild)





