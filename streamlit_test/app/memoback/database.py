#DBの設定
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DB_URL='mysql://root@db:3306/demo?charset=utf8'

engine=create_engine(DB_URL,echo=True)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
