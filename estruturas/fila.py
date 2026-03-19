class Fila():
    def __init__(self):
        self.fila = []
    

    def is_empty(self):
        return len(self._fila) == 0


    def ver_primeiro(self):
        if self.is_empty():
            return None
        return self.fila[0]
        
    def enqueue(self,item):
        self.fila.append(item)

        

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.fila[0]
        self.fila.pop(0)
        
        return item



