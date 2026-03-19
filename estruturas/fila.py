from lista import Lista


class Fila:
    def __init__(self):
        self._fila = Lista()

    def is_empty(self):
        return self._fila.is_empty()

    def ver_primeiro(self):
        if self.is_empty():
            return None
        return self._fila.acessar(0)

    def enqueue(self, item):
        self._fila.adicionar(item)

    def dequeue(self):
        if self.is_empty():
            return None
        
        item = self._fila.acessar(0)
        self._fila.remover(0)
        return item



