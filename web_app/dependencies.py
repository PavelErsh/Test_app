from web_app.my_app import mongodb, redis_client


async def get_db():
    return mongodb


async def get_redis():
    return redis_client
