from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///banco_dados.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(100))
    data_nascimento = Column(Date)
    sexo = Column(String(10))
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class Endereco(Base):
    __tablename__ = 'enderecos'

    id_endereco = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    cep = Column(String(10))
    rua = Column(String(100))
    numero = Column(Integer)
    bairro = Column(String(100))
    cidade = Column(String(100))
    estado = Column(String(100))
    data_criacao = Column(Date)
    data_alteracao = Column(Date)

class Contato(Base):
    __tablename__ = 'contatos'

    id_contato = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    email = Column(String(100))
    telefone = Column(String(100))
    celular = Column(String(100))
    whatsapp = Boolean
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class InformacoesPagamento(Base):
    __tablename__ = 'info_pagamento'  

    id_info_pagamento = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente')) 
    bandeira = Column(String(100))
    numero_cartao = Column(String(100))
    data_validade = Column(Date)
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class Documentos(Base):
    __tablename__ = 'documentos'

    id_documento = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    numero = Column(String(100))
    tipo = Column(String(100))
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class Pedido(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    id_info_pagamento = Column(Integer, ForeignKey('info_pagamento.id_info_pagamento'))
    codigo = Column(Integer)
    data_pedido = Column(Date)
    total_pedido = Column(Integer)
    observacao = Column(String(255))
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class EntregaPedido(Base):
    __tablename__ = 'entrega_pedidos'

    id_entrega_pedidos = Column(Integer, primary_key=True, autoincrement=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido'))
    id_contato = Column(Integer, ForeignKey('contatos.id_contato'))
    frete = Column(Integer)
    previsao_entrega = Column(Date)
    responsavel_recebimento =  Column(String(100))
    observacao = Column(String(255))
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class Produtos(Base):
    __tablename__ = 'produtos'

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    categoria = Column(String(100))
    tamanho = Column(String(10))
    preco_unitario = Column(Integer)
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class Estoque(Base):
    __tablename__ = 'estoque'

    id_estoque = Column(Integer, primary_key=True, autoincrement=True)
    id_produto = Column(Integer, ForeignKey('produtos.id_produto'))
    quantidade = Column(Integer)
    data_criacao = Column(Date)
    data_alteracao = Column(Date)


class ProdutoPedido(Base):
    __tablename__ = 'produto_pedido'

    id_produto_pedido = Column(Integer, primary_key=True, autoincrement=True)
    id_produto = Column(Integer, ForeignKey('produtos.id_produto'))
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido'))
    quantidade = Column(Integer)
    subtotal = Column(Integer)
    data_criacao = Column(Date)
    data_alteracao = Column(Date)