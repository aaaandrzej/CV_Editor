from sqlalchemy import event, create_engine
from sqlalchemy.orm import sessionmaker


def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')


def get_session(echo=False):
    engine = create_engine('sqlite:///CV_Editor.sqlite', echo=echo)
    DBSession = sessionmaker(bind=engine)

    event.listen(engine, 'connect', _fk_pragma_on_connect)

    return DBSession()
