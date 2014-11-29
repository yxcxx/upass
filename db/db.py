__author__ = 'yxc'

from sqlalchemy import String, Binary, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

Base = declarative_base()
