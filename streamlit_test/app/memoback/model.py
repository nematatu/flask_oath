#DBモデル定義
from sqlalchemy import Column,Integer,String
from .database import Base

class Memo(Base):
    __tablename__='memos'
    
    memo_id=Column(Integer,primary_key=True,autoincrement=True)
    #primary_keyで数字を一意に取得する的な
    #autoincrementで増加させる
    #indexはなんかあると検索とかに便利らしい
    content=Column(String(255))