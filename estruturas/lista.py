class Lista:
    def __init__(self):
        self._dados = []

    def is_empty(self):
        return len(self._dados) == 0

    def adicionar(self, item):
        self._dados.append(item)

    def remover(self, index=None):
        if self.is_empty():
            return None
        
        if index is None:
            return self._dados.pop()
        
        if index < 0 or index >= len(self._dados):
            return None
        
        return self._dados.pop(index)

    def acessar(self, index):
        if self.is_empty():
            return None
        
        if index < 0 or index >= len(self._dados):
            return None
        
        return self._dados[index]

    def tamanho(self):
        return len(self._dados)

    def percorrer(self):
        return self._dados
    

