from pydantic import BaseModel,Field

class MemoSchema(BaseModel):
    memo_id:int=Field()
    content:str=Field(max_length=100)

    class config:
        orm_mode=True

class MemoCreateSchema(BaseModel):
    content:str=Field(max_length=100)

    class config:
        orm_mode=True