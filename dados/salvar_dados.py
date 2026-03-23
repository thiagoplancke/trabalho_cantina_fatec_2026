import pickle
import os

ARQUIVO = "dados/dados.pkl"


def salvar_dados(historico):
    with open(ARQUIVO, "wb") as f:
        pickle.dump(historico, f)


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return None
    
    with open(ARQUIVO, "rb") as f:
        return pickle.load(f)