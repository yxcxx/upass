__author__ = 'yxc'

import os
from sqlalchemy import session, sessionmaker

URL1 = "http://219.231.0.187/default_ysdx.aspx"
URL2 = "http://jw2.ahjzu.edu.cn/default_ysdx.aspx "

SQL = {"mysql": 0, "redis": 0, "PostgreSql": 0}

setting = {
    "debug": True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

engine = "mysql//root:yxc@localhost:3096/uPass"
