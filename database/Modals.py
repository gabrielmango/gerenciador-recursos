from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///banco_dados.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True)
    nome_completo = Column(String(100))
    data_nascimento = Column(Date)
    sexo = Column(String(10))
    data_criacao = Column(Date)
    data_alteracao = Column(Date)
