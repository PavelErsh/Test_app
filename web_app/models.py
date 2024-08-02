from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    id: Optional[str]
    user: str
    text: str
