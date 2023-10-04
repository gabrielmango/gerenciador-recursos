# Importa a classe "Base" do módulo "Modals" no pacote "database"
from database.Modals import Base

# Importa as bibliotecas necessárias do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cria uma instância de mecanismo de banco de dados SQLite e especifica o arquivo "banco_dados.db"
engine = create_engine('sqlite:///banco_dados.db')

# Cria uma classe de sessão usando o mecanismo de banco de dados criado anteriormente
Session = sessionmaker(bind=engine)

# Cria uma instância de sessão, que será usada para interagir com o banco de dados
session = Session()

# Verifica se este arquivo está sendo executado diretamente (não importado como um módulo)
if __name__ == '__main__':
    # Cria todas as tabelas definidas no modelo (classe "Base") no banco de dados especificado (engine)
    Base.metadata.create_all(engine)
