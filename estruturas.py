
from modelos import Produto


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




class Estoque:
    def __init__(self):
        # O Dicionário armazena: Nome do Produto -> Fila de lotes desse produto
        self._produtos = Dicionario()

    def adicionar_produto(self, produto):
        # Verifica se já existe uma fila para esse produto
        fila_do_produto = self._produtos.buscar(produto.nome)
        
        if fila_do_produto is None:
            fila_do_produto = Fila()
            self._produtos.adicionar(produto.nome, fila_do_produto)
        
        fila_do_produto.enqueue(produto)

    def baixar_estoque(self, nome_produto):
        fila = self._produtos.buscar(nome_produto)
        if fila and not fila.is_empty():
            lote = fila.ver_primeiro()
            lote.quantidade -= 1
            
            # Se o lote zerar, removemos ele da fila
            if lote.quantidade <= 0:
                fila.dequeue()
            return True
        return False




