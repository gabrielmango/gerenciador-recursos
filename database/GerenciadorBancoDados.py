from database.Conexao import session
from database.Modals import Cliente, Endereco, Produtos, Estoque, InformacoesPagamento, Pedido, Endereco, Contato

from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError
from time import sleep
from datetime import datetime

class GerenciadorBancoDados:
    def __init__(self):
        """Inicializa a classe GerenciadorBancoDados."""
        self.sessao = session
  

    def _fecha_sessao(self):
        """Fecha a sessão de forma segura."""
        try:
            self.sessao.close()
        except SQLAlchemyError as e:
            self.sessao.rollback()
            raise e 


    def inserir_dados(self, tabela, dados):
        with self.sessao as sessao:
            try:
                instancia_tabela = tabela(**dados)
                sessao.add(instancia_tabela)
                sessao.commit()
                sleep(0.5)
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consulta_id_cliente(self, nome):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Cliente.id_cliente).filter(Cliente.nome_completo == nome.upper())
                dado = consulta.first()
                return dado[0]
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e
    

    def consulta_id_infopagamento(self, numero):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(InformacoesPagamento.id_info_pagamento).filter(InformacoesPagamento.numero_cartao == numero)
                dado = consulta.first()
                return dado[0]
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consulta_id_pedido(self, codigo):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Pedido.id_pedido).filter(Pedido.codigo == codigo)
                dado = consulta.first()
                return dado[0]
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consulta_id_endereco(self, id_cliente):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Endereco.id_cliente).filter(Endereco.id_cliente == id_cliente)
                dado = consulta.first()
                return dado[0]
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consulta_id_contato(self, id_cliente):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Contato.id_cliente).filter(Contato.id_cliente == id_cliente)
                dado = consulta.first()
                return dado[0]
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consulta_id_produto(self, nome):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Produtos.id_produto).filter(Produtos.nome == nome)
                dado = consulta.first()
                return dado[0]
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consulta_estoque(self, id_produto):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Estoque.quantidade).filter(Estoque.id_produto == id_produto)
                dado = consulta.first()
                return dado[0]
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e
            

    def atualiza_estoque(self, tabela, id_produto, valores):
        with self.sessao as sessao:
            try:
                atualizacao = update(tabela).where(tabela.id_produto == id_produto).values(**valores)
                session.execute(atualizacao)
                session.commit()
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    
    def cadastra_estoque(self):
        self.inserir_dados(Produtos, {
            'nome': 'Camisetas de algodão'.upper(),
            'categoria': 'Roupas'.upper(),
            'tamanho': 'G',
            'cor': 'preto'.upper(),
            'preco_unitario': 19.90,
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })

        self.inserir_dados(Estoque, {
            'id_produto': 1,
            'quantidade': 20,
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })

        self.inserir_dados(Produtos, {
            'nome': 'Jeans skinny'.upper(),
            'categoria': 'Roupas'.upper(),
            'tamanho': '42',
            'cor': 'jeans'.upper(),
            'preco_unitario': 49.90,
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })

        self.inserir_dados(Estoque, {
            'id_produto': 2,
            'quantidade': 20,
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })

        self.inserir_dados(Produtos, {
            'nome': 'Perfume Chanel No. 5'.upper(),
            'categoria': 'Produtos de Beleza'.upper(),
            'tamanho': None,
            'cor': None,
            'preco_unitario': 299.90,
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })

        self.inserir_dados(Estoque, {
            'id_produto': 3,
            'quantidade': 10,
            'data_criacao': datetime.now(),
            'data_alteracao': None
        })
        
