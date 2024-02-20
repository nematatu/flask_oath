from sqlalchemy.orm import Session
from . import model,schema

def get_memos(db:Session,skip:int=0,limit:int=0):
    return db.query(model.Memo).offset(skip).limit(limit).all()
    #受け取ったdbから、memoモデルに対応するクエリを作成
    #skip分最初からスキップ、limit分だけ取得

def create_memo(db:Session,memo:schema.MemoCreateSchema):
    db_memo=model.Memo(content=memo.content)
    #引数をDBモデルにするよ
    db.add(db_memo)
    db.commit()
    db.refresh(db_memo)
    return db_memo
