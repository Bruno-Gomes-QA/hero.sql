import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlacodegen.codegen import CodeGenerator
from .models import Base, User, Progress


class Database:
    def __init__(self, url, database_name):

        self.url = url
        self.database_name = database_name

        self.engine = sa.create_engine(f'{self.url}/{self.database_name}')
        self.SessionFactory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.SessionFactory)

        self.metadata = sa.MetaData(bind=self.engine)
        self.metadata.reflect(bind=self.engine)
        self.inspects = sa.inspect(self.engine)

    def create_tables(self, Base):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

    def execute_query(self, query):
        session = self.get_session()
        try:
            result = session.execute(query)
            session.commit()
            return result
        except sa.exc.SQLAlchemyError as e:
            session.rollback()
            error_message = str(e.__dict__['orig'])
            raise Exception(error_message)
        finally:
            session.close()
