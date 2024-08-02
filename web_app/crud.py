from web_app.models import Message
from motor.motor_asyncio import AsyncIOMotorDatabase

async def get_messages(db: AsyncIOMotorDatabase):
    messages = await db["messages"].find().to_list(1000)
    return messages

async def create_message(db: AsyncIOMotorDatabase, message: Message):
    await db["messages"].insert_one(message.dict())
    return message
