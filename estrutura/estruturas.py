

class Lista:
    def __init__(self):
        self._dados = []

    def is_empty(self):
        return len(self._dados) == 0

    def adicionar(self, item):
        self._dados.append(item)

    def inserir(self,index,produto):
        self._dados.insert(index,produto)

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
    







class Dicionario:
    def __init__(self):
        self._dados = {}  # dict interno (resolve chave rápido)

    def adicionar(self, chave, valor):
        # aqui você pode decidir o tipo do valor
        self._dados[chave] = valor

    def buscar(self, chave):
        return self._dados.get(chave, None)

    def remover(self, chave):
        return self._dados.pop(chave, None)

    def ver_items(self):
        itens = Lista()
        for chave, valor in self._dados.items():
            itens.adicionar((chave, valor))
        return itens.percorrer()

    def is_empty(self):
        return len(self._dados) == 0