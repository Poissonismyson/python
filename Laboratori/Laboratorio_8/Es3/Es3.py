class Insieme:

    def __init__(self,s):
        self.s = s
        pass

    def size(self):
        
        return len(self.s)
    
    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def svuota(self):
        self.s = set()
        return self.s
        
    def find(self,e):
        return e in self.s

    def insert(self,e):
        if e not in self.s:
            self.s.add(e)
            return 1
        else:
            return -1

    def remove(self,e):
        if e in self.s:
            self.s.remove(e)
            return 1
        else:
            return -1

    def sottoinsieme(self,s2):
        return self.s.issubset(s2)

    def soprainsieme(self,s2):
        return self.s.issuperset(s2)
