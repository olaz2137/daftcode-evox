from pydantic import BaseModel, PositiveInt, constr

class Text(BaseModel):

    TextID: PositiveInt
    Text: constr(max_length=160)
    Counter: PositiveInt

    class Config:
        orm_mode = True
