import json

class GeradorNotaEntrega:
    def __init__(self, caminho_arquivo):
        self._arquivo = self.abrir_arquivo(caminho_arquivo)


    def abrir_arquivo(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError as e:
            raise e

    def criar_nota_entrega(self):
        dados_pedido = self._arquivo
        with open('nota_de_entrega.txt', 'w', encoding='utf-8') as arquivo:
            pedido = dados_pedido[0]['pedido']
            entrega = dados_pedido[0]['entrega']
            produtos = dados_pedido[0]['produtos']
            cliente = dados_pedido[0]['cliente']
            
            arquivo.write("Detalhes do Pedido:\n")
            arquivo.write(f"Código do Pedido: {pedido['codigo']}\n")
            arquivo.write(f"Data do Pedido: {pedido['data_pedido']}\n")
            arquivo.write(f"Total do Pedido: R${pedido['total_pedido']:.2f}\n")
            arquivo.write(f"Método de Pagamento: {pedido['pagamento']['metodo']}\n")
            arquivo.write(f"Observação: {pedido['observacao']}\n\n")
            
            arquivo.write("Detalhes de Entrega:\n")
            arquivo.write(f"Valor do Frete: R${entrega['frete']:.2f}\n")
            arquivo.write(f"Previsão de Entrega: {entrega['previsao']}\n")
            arquivo.write(f"Endereço de Entrega: {entrega['endereco_entrega']['endereco']}, {entrega['endereco_entrega']['numero']}\n")
            arquivo.write(f"Bairro: {entrega['endereco_entrega']['bairro']}\n")
            arquivo.write(f"Cidade: {entrega['endereco_entrega']['cidade']}\n")
            arquivo.write(f"Estado: {entrega['endereco_entrega']['estado']}\n")
            arquivo.write(f"Responsável pela Entrega: {entrega['responsavel']}\n")
            arquivo.write(f"Telefone Fixo: {entrega['contato']['telefone_fixo']}\n")
            arquivo.write(f"Celular: {entrega['contato']['celular']}\n")
            arquivo.write(f"WhatsApp: {'Sim' if entrega['contato']['whatsapp'] else 'Não'}\n")
            arquivo.write(f"Observação de Entrega: {entrega['observacao']}\n\n")
            
            arquivo.write("Produtos:\n")
            for produto in produtos:
                arquivo.write(f"Nome: {produto['nome']}")
                arquivo.write("\n")
            
            arquivo.write("Informações do Cliente:\n")
            arquivo.write(f"Cliente Cadastrado: {'Sim' if cliente['cliente_cadastrado'] else 'Não'}\n")
            arquivo.write(f"Nome Completo: {cliente['nome_completo']}\n")
            arquivo.write(f"Endereço de Entrega: {cliente['endereco'][0]['endereco']}, {cliente['endereco'][0]['numero']}\n")
            arquivo.write(f"Bairro: {cliente['endereco'][0]['bairro']}\n")
            arquivo.write(f"Cidade: {cliente['endereco'][0]['cidade']}\n")
            arquivo.write(f"Estado: {cliente['endereco'][0]['estado']}\n")
            


