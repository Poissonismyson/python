
class Vertex:
## Crea un oggetto di classe Vertex, dato l'identificatore del vertice (stringa)
    def addNeigbor(self,key):
        self.id = key
        self.connectedTo = {}

## Aggiunge nbr ai vicini del vertice corrente
def addNeighbor(self,nbr,weight=1):
    self.connectedTo[nbr] = weight

## Rappresentazione in stringa di un oggetto di tipo Vertex
def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

## Restituisce una lista contenente gli identificatori dei vicini del vertice corrente

def getConnections(self):
    return self.connectedTo.keys()

## Restituisce l'identificatore di *questo* vertice
def getId(self):
    return self.id

## restituisce il peso dell'arco tra *questo* vertice e il vertice nbr