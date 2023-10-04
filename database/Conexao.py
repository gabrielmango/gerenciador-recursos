from Modals import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///banco_dados.db')
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':

    Base.metadata.create_all(engine)