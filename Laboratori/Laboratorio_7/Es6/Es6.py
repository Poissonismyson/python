class Dizionario:

        def __init__(self,d):
                self.d = d


        def size(self):
                
                return len(self.d)

        def isEmpty(self):
                
                return not self.d

        def find(self,k):
                if k in self.d:
                        return True
                else:
                        return False

        def insert(self,k,v):
                l = [k]
                if k in self.d:
                        l.append(self.d[k])
                        
                else:
                        l.append(v)
                
                self.d[k]= v
                return tuple(l)

                
        def remove(self,k):
                t = tuple()
                if k in self.d:
                        
                        t = (k, self.d.pop(k))
                        return t
                return t

        def keys(self):
                l = [k for k in self.d.keys()]
                return l
        
        def values(self):
                l = [v for v in self.d.values()]
                return l

        def pairs(self):
                l = [p for p in self.d.items()]
                return l

        def sort(self):
                l = self.pairs()
                return sorted(l)

