from modelos import Pagamento
from estruturas import Estoque, Lista, Dicionario

class Cantina:
    def __init__(self):
        
        self.estoque = Estoque()
        self.historico_pagamentos = Lista() 
        
        self.consumo_por_cliente = Dicionario()

    def realizar_venda(self, nome_cliente, categoria, curso, nome_produto, valor_pago, data_hora):
       
        sucesso = self.estoque.baixar_estoque(nome_produto)
        
        if sucesso:
            
            novo_pagamento = Pagamento(nome_cliente, categoria, curso, valor_pago, data_hora)
            self.historico_pagamentos.adicionar(novo_pagamento)
            
            # 3. Atualiza o controle de quem consumiu o quê [cite: 18]
            self._registrar_consumo(nome_cliente, nome_produto)
            return True, "Venda realizada com sucesso!"
        
        return False, "Produto esgotado ou não encontrado."

    def _registrar_consumo(self, cliente, produto):
        # Método interno para organizar o relatório de consumo [cite: 24]
        consumo_atual = self.consumo_por_cliente.buscar(cliente)
        if consumo_atual is None:
            consumo_atual = Lista()
            self.consumo_por_cliente.adicionar(cliente, consumo_atual)
        consumo_atual.adicionar(produto)

    def gerar_relatorio_vendas(self):
        print("--- RELATÓRIO DE VENDAS ---")
        for i in range(self.historico_pagamentos.tamanho()):
            pgto = self.historico_pagamentos.acessar(i)
            # Em vez de print(pgto), você acessa os atributos:
            print(f"Nome: {pgto.nome_pagador} - Valor: {pgto.valor}")
