# Importações necessárias dos módulos
from GerenciadorPedidos import GerenciadorPedidos
from GeradorNotaEntrega import GeradorNotaEntrega
import schedule  # Biblioteca para agendar tarefas periódicas
import os  # Biblioteca para operações relacionadas ao sistema de arquivos

# Função para verificar se existem arquivos de pedidos na pasta especificada
def existe_pedidos(caminho_pasta):
    arquivos_pasta = os.listdir(caminho_pasta)

    for arquivo in arquivos_pasta:
        if arquivo.endswith('.json'):
            return os.path.join(caminho_pasta, arquivo)
    return False

def main():
    # Caminho da pasta onde os arquivos de pedidos estão localizados
    PEDIDOS_PATH = 'entrada_pedidos'

    # Verifica se existem arquivos de pedidos na pasta especificada
    if existe_pedidos(PEDIDOS_PATH):
        # Cria uma instância do Gerenciador de Pedidos com o arquivo de pedidos encontrado
        gerenciador_pedidos = GerenciadorPedidos(existe_pedidos(PEDIDOS_PATH))
        # Cria uma instância do Gerador de Nota de Entrega com o arquivo de pedidos encontrado
        gerador_nota_entrega = GeradorNotaEntrega(existe_pedidos(PEDIDOS_PATH))

        # Realiza várias etapas de processamento de pedidos
        gerenciador_pedidos.cadastrar_cliente()
        gerenciador_pedidos.verificar_estoque()
        gerenciador_pedidos.cadastrar_pedido()
        gerenciador_pedidos.cadastrar_entrega()
        gerenciador_pedidos.cadastrar_carrinho_produtos()
        
        # Imprime uma mensagem indicando que os dados do pedido foram cadastrados no Banco de Dados
        print('Dados do pedido cadastrados no Banco de Dados.')

        # Cria a nota de entrega com base nos dados do pedido
        gerador_nota_entrega.criar_nota_entrega()

if __name__ == '__main__':
    # Agendamento da função 'main' para ser executada todos os dias às 10:30
    schedule.every().day.at("10:30").do(main)
