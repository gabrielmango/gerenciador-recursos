from GerenciadorPedidos import GerenciadorPedidos

import os

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
        gerenciador_pedidos.verificar_estoque()
        gerenciador_pedidos.cadastrar_pedido()
        gerenciador_pedidos.cadastrar_entrega()
        gerenciador_pedidos.cadastrar_carrinho_produtos()
        print('Dados do pedido cadastrados no Banco de Dados.')


if __name__ == '__main__':
    main()