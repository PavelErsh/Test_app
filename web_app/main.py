from web_app.my_app import app
from web_app.routers import messages

app.include_router(messages.router)
