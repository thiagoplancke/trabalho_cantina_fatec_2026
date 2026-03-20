from logica import Cantina
from modelos import Produto
from datetime import datetime




fatec_cantina = Cantina()


p1 = Produto("Coxinha", 3.00, 6.00, "2026-03-20", "2026-03-22", 10)
p2 = Produto("Suco", 2.00, 5.00, "2026-03-20", "2026-04-20", 20)

fatec_cantina.estoque.adicionar_produto(p1)
fatec_cantina.estoque.adicionar_produto(p2)

 
print("--- Bem-vindo à Cantina FATEC Rio Claro ---") 
nome = input("Nome do aluno: ")
item = input("O que deseja comprar? ")


sucesso, msg = fatec_cantina.realizar_venda(
    nome_cliente=nome,
    categoria="aluno", 
    curso="IA",        
    nome_produto=item,
    valor_pago=6.00,   
    data_hora=datetime.now()
)

print(msg)


fatec_cantina.gerar_relatorio_vendas()