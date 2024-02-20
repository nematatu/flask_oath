from fastapi import FastAPI,Depends
from typing import List
from sqlalchemy.orm import Session

from . import model,schema,crud
from .database import Sessionlocal,engine

model.Base.metadata.create_all(bind=engine)
#定義したテーブルを作成する

app=FastAPI()

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
#各セッションを作ってるらしい

@app.get('/memos',response_model=List[schema.MemoSchema])
def read_memo(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    memos=crud.get_memos(db,skip=skip,limit=limit)
    #returnのためにわざわざ関数噛ませてるってことか？
    return memos

@app.post('/memos',response_model=schema.MemoSchema)
def create_memo(memo:schema.MemoCreateSchema,db:Session=Depends(get_db)):
    return crud.create_memo(db=db,memo=memo)
