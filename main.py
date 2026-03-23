from controle.controle_de_estoque import Produto, Estoque
from controle.controle_de_consumo import Venda
from dados.salvar_dados import salvar_dados, carregar_dados
from dados.gerar_dados import gerar_dados_fake
from datetime import *
from estrutura.estruturas import Lista
from rich.table import Table
from rich import print
from rich.panel import Panel




dados_fake = carregar_dados()

if dados_fake is None:
    dados_fake = gerar_dados_fake()
    salvar_dados(dados_fake)




historico_pagamento = dados_fake

estoque_produtos = Estoque()


estoque_produtos.adicionar_produto(Produto("coxinha", 6, "05/05/22", "06/03/22"))
estoque_produtos.adicionar_produto(Produto("coxinha", 6, "04/05/22", "12/03/22"))
estoque_produtos.adicionar_produto(Produto("coxinha", 6, "03/05/22", "09/03/22"))




print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


inicio = Panel(title="CANTINA FATEC",renderable="Bem vindo(a) a CANTINA FATEC!\n\nPressione ENTER para entrar!",width=40)
print(inicio)
print("\n")
print("\n")
entrar = input()
print("\n")

while True:
    menu = Table(title="Menu", show_lines=True)

    menu.add_column("Produtos",justify="center")
    menu.add_column("Preço",justify="center")
    menu.add_column("Data de Abastecimento",justify="center")
    menu.add_column("Data de Validade",justify="center")
    menu.add_column("Quantidade", justify="center")


    for i in estoque_produtos.ver_items_estoque():
        nome_produto = i[0]
        lista_produtos = i[1]

        if lista_produtos.tamanho() > 0:
            primeiro = lista_produtos.acessar(0)

            preco = primeiro.preco
            data_compra = primeiro.data_compra.strftime("%d/%m/%Y")
            validade = primeiro.validade.strftime("%d/%m/%Y")
            quantidade = lista_produtos.tamanho()

            menu.add_row(
                nome_produto,
                f"R$ {preco:.2f}",
                data_compra,
                validade,
                str(quantidade)
            )
    
    print(menu)
    

    
    print("\n\n1 - Comprar\n2 - Historico de Compras\n0 - Sair")
    
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o seu nome: ")
        curso = input("Digite o seu curso(IA/ESG): ")
        categoria = input("Digite a sua categoria(Aluno/Professor) ")
        produto = input("Digite o nome do produto que deseja comprar: ")
        quantidade = int(input("Digite a quantidade do produto que deseja comprar: "))
        hora = str(datetime.now().strftime('%d/%m/%Y %H:%M'))
        venda = Venda(estoque_produtos.pegar_produto_estoque(produto),nome,categoria,curso,quantidade,hora)

        
        resultado = venda.vender()
        if resultado is not None:
            historico_pagamento.adicionar(resultado)
            salvar_dados(historico_pagamento)



    if opcao == "2":

        historico = Table(title="Histórico de Vendas", show_lines=True)

        historico.add_column("Nome",justify="left")
        historico.add_column("Categoria",justify="center")
        historico.add_column("Curso",justify="center")
        historico.add_column("valor Gasto",justify="center")
        historico.add_column("Data e Hora", justify="center")


        for item in historico_pagamento.percorrer():
            historico.add_row(item.nome,item.categoria,item.curso,f"R$ {item.valor:.2f}",item.data_hora)
        print(historico)
        print("\n")
        voltar = input("Aperte ENTER para voltar")

            
    if opcao == "0":
        break
