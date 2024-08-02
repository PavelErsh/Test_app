from fastapi import APIRouter, Depends
from web_app.schemas import Message, MessageCreate
from web_app.crud import get_messages, create_message
from web_app.dependencies import get_db, get_redis
from motor.motor_asyncio import AsyncIOMotorDatabase
import redis

router = APIRouter()

@router.get("/api/v1/messages/", response_model=list[Message])
async def read_messages(db: AsyncIOMotorDatabase = Depends(get_db), redis: redis.Redis = Depends(get_redis)):
    cached_messages = redis.get('messages')
    if cached_messages:
        return cached_messages
    messages = await get_messages(db)
    redis.set('messages', messages)
    return messages

@router.post("/api/v1/message/", response_model=Message)
async def create_new_message(message: MessageCreate, db: AsyncIOMotorDatabase = Depends(get_db), redis: redis.Redis = Depends(get_redis)):
    new_message = await create_message(db, message)
    redis.delete('messages')
    return new_message
