from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import redis

app = FastAPI()
mongodb_client = AsyncIOMotorClient("mongodb://mongo:27017")
mongodb = mongodb_client["message_db"]
redis_client = redis.Redis(host="redis", port=6379, db=0)


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://mongo:27017")
    app.mongodb = app.mongodb_client["message_db"]
    app.redis = redis.Redis(host="redis", port=6379, db=0)


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
