from database.GerenciadorBancoDados import GerenciadorBancoDados
from database.Modals import Cliente, Endereco, Contato, InformacoesPagamento, Documentos, Pedido, EntregaPedido, ProdutoPedido, Estoque

import json
from datetime import datetime
from time import sleep


class GerenciadorPedidos:
    def __init__(self, caminho_arquivo):
        """
        Inicializa a classe GerenciadorPedidos.

        Args:
            caminho_arquivo (str): O caminho para o arquivo JSON contendo os dados do pedido.
        """
        self._caminho_arquivo = caminho_arquivo
        self._arquivo = self.abrir_arquivo(self._caminho_arquivo)
        self.database = GerenciadorBancoDados()  # Cria uma instância da classe GerenciadorBancoDados.
        self.padronizacao = PadronizaDados()  # Cria uma instância da classe PadronizaDados.


    def abrir_arquivo(self, caminho_arquivo):
        """
        Abre e carrega um arquivo JSON.

        Args:
            caminho_arquivo (str): O caminho para o arquivo JSON a ser carregado.

        Returns:
            dict: Um dicionário contendo os dados carregados do arquivo JSON.
        
        Raises:
            FileNotFoundError: Se o arquivo especificado não for encontrado.
        """
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError as e:
            raise e
    

    def cliente_cadastrado(self):
        """
        Verifica se o cliente está cadastrado.

        Returns:
            bool: True se o cliente estiver cadastrado, False caso contrário.
        """
        return self._arquivo[0]['cliente']['cliente_cadastrado']


    def _lista_dados_cliente(self):
        """
        Retorna um dicionário contendo os dados do cliente.

        Returns:
            dict: Um dicionário com os dados do cliente, incluindo informações de cliente, endereço,
                  documentos, contato e informações de pagamento.
        """
        return {
            'cliente': self._arquivo[0]['cliente'],
            'endereco': self._arquivo[0]['cliente']['endereco'],
            'documentos': self._arquivo[0]['cliente']['documentos'],
            'contato': self._arquivo[0]['cliente']['contato'],
            'info_pagamento': self._arquivo[0]['cliente']['info_pagamento'],
        }


    def verificar_estoque(self):
        """
        Função que verifica o estoque de produtos em um carrinho de compras e atualiza o estoque se a quantidade for suficiente.

        Esta função percorre os produtos no carrinho de compras, consulta o estoque de cada produto no banco de dados
        e, se a quantidade no estoque for suficiente para a compra, atualiza o estoque subtraindo a quantidade do carrinho.
        Caso contrário, o produto é adicionado a uma lista de produtos com estoque insuficiente.

        Args:
            self: A instância da classe que possui a função.
        
        Returns:
            None

        Exemplo:
            Para usar essa função, você deve tê-la em uma classe que tenha acesso a um banco de dados de produtos.
            Em seguida, basta chamá-la para verificar e atualizar o estoque dos produtos no carrinho de compras.
        """
        lista_produtos = []
        carrinho_produtos = self._arquivo[0]['produtos']
        for produto in carrinho_produtos:
            id_produto = self.database.consulta_id_produto(produto['nome'].upper())
            quantidade_estoque = self.database.consulta_estoque(id_produto)
            if quantidade_estoque - produto['quantidade'] > 0:
                self.database.atualiza_estoque(Estoque, id_produto, {
                    'quantidade': quantidade_estoque - produto['quantidade']
                    })
            else:
                lista_produtos.append(produto['nome'])
        for produtos in lista_produtos:
            print(f'O produto {produtos} não possui quantidade suficiente no estoque!')


    def cadastrar_cliente(self):
        """
        Função para cadastrar um cliente no sistema.

        Verifica se o cliente já está cadastrado e, se não estiver, insere seus dados
        pessoais, de endereço, de contato, informações de pagamento e documentos no banco de dados.

        Args:
            self: A instância atual do objeto que possui esse método.

        Returns:
            None
        """
        if not self.cliente_cadastrado():

            dados = self._lista_dados_cliente()
            dados_cliente = dados['cliente']
            self.database.inserir_dados(Cliente, {
                'nome_completo': self.padronizacao.formatar_texto(dados_cliente['nome_completo']),
                'data_nascimento': self.padronizacao.formatar_data_nascimento(dados_cliente['data_nascimento']),
                'sexo': self.padronizacao.formatar_sexo(dados_cliente['sexo']),
                'data_criacao': datetime.now(),
                'data_alteracao': None
            })
            sleep(1)

            id_cliente = self.database.consulta_id_cliente(dados_cliente['nome_completo'])

            dados_endereco = dados['endereco']
            for dado in dados_endereco:
                self.database.inserir_dados(Endereco, {
                    'id_cliente': id_cliente,
                    'cep': self.padronizacao.formatar_numero_identificacao(dado['cep']),
                    'rua': self.padronizacao.formatar_texto(dado['endereco']),
                    'numero': dado['numero'],
                    'bairro': self.padronizacao.formatar_texto(dado['bairro']),
                    'cidade': self.padronizacao.formatar_texto(dado['cidade']),
                    'estado': self.padronizacao.formatar_texto(dado['estado']),
                    'data_criacao': datetime.now(),
                    'data_alteracao': None
                })

            dados_contato = dados['contato']
            self.database.inserir_dados(Contato, {
                'id_cliente': id_cliente,
                'email': dados_contato['email'],
                'telefone': self.padronizacao.formatar_numero_contato(dados_contato['telefone_fixo']),
                'celular': self.padronizacao.formatar_numero_contato(dados_contato['celular']),
                'whatsapp': dados_contato['whatsapp'],
                'data_criacao': datetime.now(),
                'data_alteracao': None
            })

            dados_info_pagamento = dados['info_pagamento']
            for dado in dados_info_pagamento:
                self.database.inserir_dados(InformacoesPagamento, {
                    'id_cliente': id_cliente,
                    'bandeira': self.padronizacao.formatar_texto(dado['bandeira']),
                    'numero_cartao': dado['numero_cartao'],
                    'data_validade': self.padronizacao.formatar_data_nascimento(dado['data_validade']),
                    'data_criacao': datetime.now(),
                    'data_alteracao': None
                })

            dados_documentos = dados['documentos']
            for chave, valor in dados_documentos.items():
                if chave == 'cpf':
                    self.database.inserir_dados(Documentos, {
                        'id_cliente': id_cliente,
                        'numero': self.padronizacao.formatar_numero_identificacao(valor),
                        'tipo': 'CPF',
                        'data_criacao': datetime.now(),
                        'data_alteracao': None
                    })
                elif chave == 'rg':
                    self.database.inserir_dados(Documentos, {
                        'id_cliente': id_cliente,
                        'numero': self.padronizacao.formatar_numero_identificacao(valor),
                        'tipo': 'IDENTIDADE',
                        'data_criacao': datetime.now(),
                        'data_alteracao': None
                    })


    def cadastrar_pedido(self):
        """
        Método para cadastrar um pedido no sistema.

        Este método realiza as seguintes etapas:
        1. Consulta o ID do cliente com base no nome completo do cliente no arquivo.
        2. Consulta o ID das informações de pagamento com base no número do cartão no arquivo.
        3. Insere os dados do pedido na tabela 'Pedido' do banco de dados.
        
        Parâmetros:
        - self: A instância atual da classe que contém este método.

        Retorno:
        Nenhum retorno explícito. O método insere os dados do pedido no banco de dados.

        Exemplo de Uso:
        instancia.cadastrar_pedido()
        """

        id_cliente = self.database.consulta_id_cliente(self._arquivo[0]['cliente']['nome_completo'])
        id_infopagamento = self.database.consulta_id_infopagamento(self._arquivo[0]['pedido']['pagamento']['numero_cartao'])

        self.database.inserir_dados(Pedido, {
            'id_cliente': id_cliente,
            'id_info_pagamento':id_infopagamento,
            'status': 'PROCESSANDO PEDIDO',
            'codigo': self._arquivo[0]['pedido']['codigo'],
            'data_pedido': self.padronizacao.formatar_data_nascimento(self._arquivo[0]['pedido']['data_pedido']),
            'total_pedido': self._arquivo[0]['pedido']['total_pedido'],
            'observacao': self._arquivo[0]['pedido']['observacao'],
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })
    

    def cadastrar_entrega(self):
        """Função para cadastrar uma entrega relacionada a um pedido.

        Esta função realiza o cadastro de informações sobre a entrega associada a um pedido,
        incluindo detalhes como ID do pedido, ID do contato, ID do endereço, frete, previsão
        de entrega, responsável pelo recebimento e observações.

        Args:
            self: A referência ao objeto que chama o método.

        Returns:
            None
        """
        id_cliente = self.database.consulta_id_cliente(self._arquivo[0]['cliente']['nome_completo'])

        id_pedido = self.database.consulta_id_pedido(self._arquivo[0]['pedido']['codigo'])
        id_contato = self.database.consulta_id_contato(id_cliente)
        id_endereco = self.database.consulta_id_endereco(id_cliente)

        self.database.inserir_dados(EntregaPedido, {
            'id_pedido': id_pedido,
            'id_contato': id_contato,
            'id_endereco': id_endereco,
            'frete': self._arquivo[0]['entrega']['frete'],
            'previsao_entrega': self.padronizacao.formatar_data_nascimento(self._arquivo[0]['entrega']['previsao']),
            'responsavel_recebimento': self.padronizacao.formatar_texto(self._arquivo[0]['entrega']['responsavel']),
            'observacao': self.padronizacao.formatar_texto(self._arquivo[0]['entrega']['observacao']),
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })

    
    def cadastrar_carrinho_produtos(self):
        """
        Esta função é responsável por cadastrar os produtos de um carrinho de compras em um banco de dados.

        Ela recupera os dados dos produtos do carrinho a partir de um arquivo, consulta o ID do pedido associado
        ao carrinho no banco de dados e, em seguida, insere os dados de cada produto no banco de dados.

        Args:
            self: A referência para a instância da classe que chama a função.

        Returns:
            None

        Raises:
            (Coloque aqui quaisquer exceções que esta função possa gerar, se aplicável)
        """
        dados = self._arquivo[0]['produtos']
        id_pedido = self.database.consulta_id_pedido(self._arquivo[0]['pedido']['codigo'])

        for dado in dados:
            id_produto = self.database.consulta_id_produto(dado['nome'].upper())

            self.database.inserir_dados(ProdutoPedido, {
                'id_produto': id_produto,
                'id_pedido': id_pedido,
                'quantidade': dado['quantidade'],
                'subtotal': dado['subtotal'],
                'data_criacao': datetime.now(),
                'data_alteracao': None
            })

class PadronizaDados:
    def valida_texto(self, texto):
        """
        Função para validar se o texto é vazio ou 'nan'.

        Args:
            texto (str): O texto a ser validado.

        Returns:
            bool: Retorna True se o texto for vazio ou 'nan', False caso contrário.
        """
        texto = texto
        if texto == 'nan' or texto == '' or texto == ' ':
            return True
        return False
    
    def formatar_texto(self, texto: str):
        """
        Formata um texto para letras maiúsculas e remove espaços em branco no início e no final.

        Args:
            texto (str): O texto a ser formatado.

        Returns:
            str: O texto formatado.
        """
        return texto.upper().strip()

    def formatar_sexo(self, texto: str):
        """
        Formata o texto representando gênero para 'MASCULINO', 'FEMININO' ou None se for inválido.

        Args:
            texto (str): O texto que representa o gênero.

        Returns:
            str or None: O texto formatado ('MASCULINO' ou 'FEMININO') ou None se for inválido.
        """
        if self.valida_texto(texto):
            return None
        
        texto_formatado = self.formatar_texto(texto)
        
        if texto_formatado == 'M' or texto_formatado == 'MASCULINA':
            return 'MASCULINO'
        elif texto_formatado == 'F' or texto_formatado == 'FEMININA':
            return 'FEMININO'
        return texto_formatado
    
    def formatar_data_nascimento(self, texto):
        """
        Formata uma data de nascimento no formato 'AAAA-MM-DD' a partir de uma string no formato 'DD/MM/AAAA'.

        Args:
            texto (str): A data de nascimento no formato 'DD/MM/AAAA'.

        Returns:
            datetime or None: O objeto datetime resultante ou None se for inválido.
        """
        if self.valida_texto(texto):
            return None
        
        texto_formatado = self.formatar_texto(texto)
        
        texto_formatado = texto_formatado.split('/')
        
        if int(texto_formatado[1]) > 12:
            data = f'{texto_formatado[2]}-{texto_formatado[0]}-{texto_formatado[1]}'
        else:
            data = f'{texto_formatado[2]}-{texto_formatado[1]}-{texto_formatado[0]}'

        return datetime.strptime(data, '%Y-%m-%d')
    
    def formatar_numero_identificacao(self, texto):
        """
        Remove caracteres especiais de um número de identificação.

        Args:
            texto (str): O número de identificação a ser formatado.

        Returns:
            str or None: O número de identificação formatado ou None se for inválido.
        """
        if self.valida_texto(texto):
            return None
        
        texto_formatado = self.formatar_texto(texto)
        
        numero_final = texto_formatado.strip().replace('.', '').replace('-', '').replace(' ', '').replace('_', '')
        
        return numero_final
    
    def formatar_numero_contato(self, texto):
        """
        Formata um número de contato, removendo caracteres especiais e o '0' inicial, se presente.

        Args:
            texto (str): O número de contato a ser formatado.

        Returns:
            str or None: O número de contato formatado ou None se for inválido.
        """
        if self.valida_texto(texto):
            return None
        
        texto_formatado = self.formatar_texto(texto) 
        
        celular_formatado = texto_formatado.strip().replace('-', '').replace('(', '').replace(')', '').replace(' ', '').replace('.', '')
            
        if celular_formatado.startswith('0'):
            celular_formatado = celular_formatado[1:]
            
        return celular_formatado
