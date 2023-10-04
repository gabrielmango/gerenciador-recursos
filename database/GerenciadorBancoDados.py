from database.Conexao import session
from database.Modals import Cliente, Endereco

from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

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

    def inserir_cliente(self, dados):
        with self.sessao as sessao:
            try:
                instancia_tabela = Cliente(**dados)
                sessao.add(instancia_tabela)
                sessao.commit()
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e
    

    def inserir_endereco(self, dados):
        with self.sessao as sessao:
            try:
                instancia_tabela = Endereco(**dados)
                sessao.add(instancia_tabela)
                sessao.commit()
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e

    def consulta_id_cliente(self, nome):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Cliente.id_cliente).filter(Cliente.nome_completo == nome)
                return consulta.first()
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    


