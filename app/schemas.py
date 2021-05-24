from pydantic import BaseModel, PositiveInt, constr
from typing import Optional

class Text(BaseModel):

    TextID: PositiveInt
    Text: Optional[constr(max_length=160)]
    Counter: PositiveInt

    class Config:
        orm_mode = True