from web_app.app import app
from web_app.routers import messages

app.include_router(messages.router)
