from database.Conexao import session
from database.GerenciadorBancoDados import GerenciadorBancoDados
from database.Modals import Cliente

import json
from datetime import datetime
from unicodedata import normalize


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


    def cadastrar_cliente(self):
        if not self.cliente_cadastrado():
            dados = self._arquivo[0]['cliente']
            self.database.inserir_cliente({
                'nome_completo': self.padronizacao.formatar_texto(dados['nome_completo']),
                'data_nascimento': self.padronizacao.formatar_data_nascimento(dados['data_nascimento']),
                'sexo': self.padronizacao.formatar_sexo(dados['sexo']),
                'data_criacao': datetime.now(),
                'data_alteracao': None
            })


    def cadastrar_endereco(self):
        id_cliente = self.database.consulta_id(self._arquivo[0]['cliente']['nome_completo'].upper())
        dados = self._arquivo[0]['cliente']
        self.database.inserir_endereco({

        })



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