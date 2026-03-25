from estrutura.estruturas import Lista

class Pagamento:
    def __init__(self, nome,categoria,curso,valor, data_hora,produto_nome):
        self.nome = nome
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data_hora = data_hora
        self.produto_nome = produto_nome 
    
    def __repr__(self):
        return f"nome: {self.nome} | curso: {self.curso} | categoria: {self.categoria} | Gastou: {self.valor} | Data: {self.data_hora} | Produto: {self.produto_nome}\n"

