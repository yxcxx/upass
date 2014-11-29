__author__ = 'yxc'

from sqlalchemy import Column, String, Integer

from db.db import Base


class StudentInfo(Base):
    __tablename__ = "StudentInfo"

#    def __init__(self, number, password, ):
#        """student number analyse
#        eg:11205090604
#        [0,1] year
#        [2,4] college
#        [5,6]major
#        [7,8]
#        [9]class
#        [10,11]number
#        """
#        self.number = number
#        self.password = password
#        year = self.number[0, 1]
#        college = self.number[3, 4]
#        major = self.number[5, 6]

    number = Column(Integer, primary_key=True)
    password = Column(String(20), nullable=False)
