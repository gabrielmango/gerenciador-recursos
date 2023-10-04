from GerenciadorPedidos import GerenciadorPedidos
from database.GerenciadorBancoDados import GerenciadorBancoDados

import os
from pprint import pprint

def existe_pedidos(caminho_pasta):
    arquivos_pasta = os.listdir(caminho_pasta)

    for arquivo in arquivos_pasta:
        if arquivo.endswith('.json'):
            return os.path.join(caminho_pasta, arquivo)
    return False

def main():

    PEDIDOS_PATH = 'entrada_pedidos'

    if existe_pedidos(PEDIDOS_PATH):
        gerenciador_pedidos = GerenciadorPedidos(existe_pedidos(PEDIDOS_PATH))
        gerenciador_pedidos.cadastrar_cliente()
        gerenciador_pedidos.cadastrar_pedido()


if __name__ == '__main__':
    main()