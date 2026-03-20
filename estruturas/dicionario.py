from lista import Lista


class Dicionario:
    def __init__(self):
        self._dados = Lista()

    def adicionar(self, chave, valor):
        for i in range(self._dados.tamanho()):
            par = self._dados.acessar(i)
            if par[0] == chave:
                self._dados.remover(i)
                self._dados.adicionar((chave, valor))
                return
        
        self._dados.adicionar((chave, valor))

    def buscar(self, chave):
        for i in range(self._dados.tamanho()):
            par = self._dados.acessar(i)
            if par[0] == chave:
                return par[1]
        return None

    def remover(self, chave):
        for i in range(self._dados.tamanho()):
            par = self._dados.acessar(i)
            if par[0] == chave:
                return self._dados.remover(i)
        return None

    def is_empty(self):
        return self._dados.is_empty()