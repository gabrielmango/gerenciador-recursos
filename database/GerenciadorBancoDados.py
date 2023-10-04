from Conexao import session
from Modals import Cliente

from sqlalchemy.exc import SQLAlchemyError


class GerenciadorBancoDados:
    def __init__(self, Session, engine):
        """Inicializa a classe GerenciadorBancoDados."""
        self._session = Session
        self._engine = engine
        self.sessao = self._session(self._engine)
  
    def _fecha_sessao(self):
        """Fecha a sessão de forma segura."""
        try:
            self.sessao.close()
        except SQLAlchemyError as e:
            self.sessao.rollback()
            raise e 

    def inserir_dados(self, tabela, dados):
        """Insere dados no banco de dados."""
        with self.sessao as sessao:
            try:
                instancia_tabela = tabela(**dados)
                sessao.add(instancia_tabela)
                sessao.commit()
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e
