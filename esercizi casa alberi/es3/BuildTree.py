from BinaryTree import BinaryTree

def costruisci_albero(file):
    f = open(file,'r',encoding='utf-8')
    f.readline()
    tree = None
    '''
        Un dizionario viene usato per avere la corrispondenza
        fra l'identificativo di un nodo (radice di sottoalbero)
        e il riferimento all'oggetto corrispondente
    ''' 
    dtree = {} 
    for riga in f:
        comp = riga.strip().split()
        nodo = comp[0]
        figli = comp[1].split(',')
        fsx = figli[0]
        fdx = figli[1]
        if not tree:
	    ## Radice del albero
            tree = BinaryTree(nodo)
            dtree[nodo] = tree 
            
        t = dtree[nodo]
       
        if fsx != '-':
	    ## Inserimento del figlio sinistro ed aggiornamento del dizionario
            t.insertLeft(fsx)
            dtree[fsx] = t.getLeftChild()
        if fdx != '-':
	    ## Inserimento del figlio destro ed aggiornamento del dizionario
            t.insertRight(fdx)
            dtree[fdx] = t.getRightChild()
        
    f.close()
    return tree
