from pydantic import BaseModel


class MessageCreate(BaseModel):
    user: str
    text: str


class Message(BaseModel):
    id: str
    user: str
    text: str
