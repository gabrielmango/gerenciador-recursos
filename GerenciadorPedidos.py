from database.Conexao import session
from database.GerenciadorBancoDados import GerenciadorBancoDados
from database.Modals import Cliente, Endereco, Contato, InformacoesPagamento, Documentos

import json
from datetime import datetime
from unicodedata import normalize
from time import sleep


class GerenciadorPedidos:
    def __init__(self, caminho_arquivo):
        self._caminho_arquivo = caminho_arquivo
        self._arquivo = self.abrir_arquivo(self._caminho_arquivo)
        self.database = GerenciadorBancoDados()
        self.padronizacao = PadronizaDados()

    def abrir_arquivo(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError as e:
            raise e
    
    def cliente_cadastrado(self):
        return self._arquivo[0]['cliente']['cliente_cadastrado']

    def _lista_dados_cliente(self):
        return {
            'cliente': self._arquivo[0]['cliente'],
            'endereco': self._arquivo[0]['cliente']['endereco'],
            'documentos': self._arquivo[0]['cliente']['documentos'],
            'contato': self._arquivo[0]['cliente']['contato'],
            'info_pagamento': self._arquivo[0]['cliente']['info_pagamento'],
        }



    def cadastrar_cliente(self):
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
            print('cliente foi.')
            sleep(1)

            _id = self.database.consulta_id_cliente(dados_cliente['nome_completo'])
            id_cliente = _id[0]

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
                print('endereco foi.')

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
            print('contato foi.')

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
                print('info_pagamento foi.')

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
                    print('documentos foi.')
                elif chave == 'rg':
                    self.database.inserir_dados(Documentos, {
                        'id_cliente': id_cliente,
                        'numero': self.padronizacao.formatar_numero_identificacao(valor),
                        'tipo': 'IDENTIDADE',
                        'data_criacao': datetime.now(),
                        'data_alteracao': None
                    })
                    print('documentos foi.')

    def cadastrar_pedido(self):
        self.database.consulta_id_cliente(self._arquivo[0]['cliente']['nome_completo'])




class PadronizaDados:
    def valida_texto(self, texto):
        texto = texto
        if texto == 'nan' or texto == '' or texto == ' ':
            return True
        return False
    
    def formatar_texto(self, texto: str):
        return texto.upper().strip()

    def formatar_sexo(self, texto: str):
        if self.valida_texto(texto):
            return None
        
        texto_formatado = self.formatar_texto(texto)
        
        if texto_formatado == 'M' or texto_formatado == 'MASCULINA':
            return 'MASCULINO'
        elif texto_formatado == 'F' or texto_formatado == 'FEMININA':
            return 'FEMININO'
        return texto_formatado
    
    def formatar_data_nascimento(self, texto):
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
        if self.valida_texto(texto):
            return None
        
        texto_formatado = self.formatar_texto(texto)
        
        numero_final = texto_formatado.strip().replace('.', '').replace('-', '').replace(' ', '').replace('_', '')
        
        return numero_final
    
    def formatar_numero_contato(self, texto):
        if self.valida_texto(texto):
            return None
        
        texto_formatado = self.formatar_texto(texto) 
        
        celular_formatado = texto_formatado.strip().replace('-', '').replace('(', '').replace(')', '').replace(' ', '').replace('.', '')
            
        if celular_formatado.startswith('0'):
            celular_formatado = celular_formatado[1:]
            
        return celular_formatado