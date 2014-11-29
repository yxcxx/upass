__author__ = 'yxc'

from sqlalchemy import String, Binary, Integer
from sqlalchemy import create_engine

from setting import engine

engine = create_engine(target=engine)


