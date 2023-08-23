from sqlalchemy import create_engine, event, DDL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql://root:admin@localhost/my_app', pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from Data.Domain import ChapterLesson
    Base.metadata.create_all(bind=engine)