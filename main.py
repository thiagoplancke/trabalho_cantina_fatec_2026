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

while True:
    inicio = Panel(
        "[bold green]Bem vindo(a) a CANTINA FATEC![/bold green]\n\n"
        "[cyan]1[/cyan] → Entrar como ADM\n"
        "[cyan]2[/cyan] → Entrar como cliente\n"
        "[red]0[/red] → Sair",
        title="[bold yellow]🍔 CANTINA FATEC[/bold yellow]",
        border_style="bright_blue",
        width=50)

    print(inicio)
    print("\n")
    print("\n")
    entrar = str(input(">>> "))
    if entrar == "1":
        senha = "1234"
        usersenha = input("Digite a sua senha: ")
        if usersenha == senha:
            while True:
                tela = Panel(
                    "[bold green]Bem vindo(a) ADM[/bold green]\n\n"
                    "[cyan]1[/cyan] → Histórico de compras\n"
                    "[cyan]2[/cyan] → Relatório\n"
                    "[cyan]3[/cyan] → Adicionar Produto\n"
                    "[red]0[/red] → Sair",
                    title="[bold yellow]🔐 ÁREA ADMIN[/bold yellow]",
                    border_style="bright_magenta",
                    width=50)

                print(tela)
                opcao = str(input(">>> "))
                if opcao == "1":
                    historico = Table(
                        title="📜 Histórico de Vendas",
                        show_lines=True,
                        header_style="bold magenta"
                    )

                    historico.add_column("Nome", justify="left", style="cyan")
                    historico.add_column("Categoria", justify="center", style="green")
                    historico.add_column("Curso", justify="center", style="blue")
                    historico.add_column("Produto", justify="center", style="yellow")
                    historico.add_column("Valor", justify="center", style="bold green")
                    historico.add_column("Data", justify="center", style="white")

                    print(historico_pagamento)
                    for item in historico_pagamento.percorrer():
                        historico.add_row(item.nome,item.categoria,item.curso,item.produto_nome,f"R$ {item.valor:.2f}",item.data_hora)
                    print(historico)
                    print("\n")
                    voltar = input("Aperte ENTER para voltar")

                if opcao == "2":
                    total = 0
                    quantidade_vendas = 0
                    total_aluno = 0
                    total_professor = 0

                    for item in historico_pagamento.percorrer():
                        total += item.valor
                        quantidade_vendas += 1

                        if item.categoria.lower() == "aluno":
                            total_aluno += item.valor
                        elif item.categoria.lower() == "professor":
                            total_professor += item.valor

                    ticket_medio = 0
                    if quantidade_vendas > 0:
                        ticket_medio = total / quantidade_vendas

                    relatorio = Table(
                        title="📊 Relatório Geral",
                        show_lines=True,
                        header_style="bold yellow"
                    )

                    relatorio.add_column("Métrica", justify="left", style="cyan")
                    relatorio.add_column("Valor", justify="center", style="bold green")

                    relatorio.add_row("Total Faturado", f"R$ {total:.2f}")
                    relatorio.add_row("Quantidade de Vendas", str(quantidade_vendas))
                    relatorio.add_row("Ticket Médio", f"R$ {ticket_medio:.2f}")
                    relatorio.add_row("Faturamento Alunos", f"R$ {total_aluno:.2f}")
                    relatorio.add_row("Faturamento Professores", f"R$ {total_professor:.2f}")

                    print(relatorio)
                    input("\nAperte ENTER para voltar")

                
                if opcao == "3":
                    quant = int(input("Quantos produtos deseja armazenar: "))
                    nome_p = input("Digite o nome do produto: ")
                    valor = float(input("Digite o valor a ser vendido do produto: "))
                    data_a = str(input("digite a data de abastecimento em dd/mm/aa: "))
                    data_co = str(input("Digite a data de validade do(s) produto(s) em dd/mm/aa: "))

                    if quant > 1:
                        for _ in range(quant):
                            estoque_produtos.adicionar_produto(Produto(nome_p, valor,data_a , data_co))
                    if quant == 1:
                        estoque_produtos.adicionar_produto(Produto(nome_p, valor,data_a , data_co))



                
                if opcao == "0":
                    break


    if entrar == "2":
        while True:
            menu = Table(
                title="🍽️ Cardápio",
                show_lines=True,
                header_style="bold blue"
            )

            menu.add_column("Produto", justify="center", style="yellow")
            menu.add_column("Preço", justify="center", style="green")
            menu.add_column("Abastecimento", justify="center", style="cyan")
            menu.add_column("Validade", justify="center", style="red")
            menu.add_column("Qtd", justify="center", style="magenta")

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
            

            
            print("\n\n1 - Comprar\n0 - Sair")
            
            opcao = input("Digite uma opção: ")

            if opcao == "1":
                produto = input("Digite o nome do produto que deseja comprar: ")
                quantidade = int(input("Digite a quantidade do produto que deseja comprar: "))
                nome = input("Digite o seu nome: ")
                curso = input("Digite o seu curso(IA/ESG): ")
                categoria = input("Digite a sua categoria(Aluno/Professor) ")
                hora = str(datetime.now().strftime('%d/%m/%Y %H:%M'))
                venda = Venda(estoque_produtos.pegar_produto_estoque(produto),nome,categoria,curso,quantidade,hora,produto)

                
                resultado = venda.vender()
                if resultado is not None:
                    historico_pagamento.adicionar(resultado)
                    salvar_dados(historico_pagamento)


                    
            if opcao == "0":
                break

    if entrar == "0":
        break
