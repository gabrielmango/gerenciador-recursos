from database.GerenciadorBancoDados import GerenciadorBancoDados
from database.Modals import Base, engine

from time import sleep

Base.metadata.create_all(engine)
sleep(1)

dba = GerenciadorBancoDados()
dba.cadastra_estoque()