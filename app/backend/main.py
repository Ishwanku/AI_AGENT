from quart import Quart
from api.chat import chat_bp
from core.logger import setup_logger
from config import Config

app = Quart(__name__)
app.config.from_object(Config)
app.register_blueprint(chat_bp, url_prefix="/api")
logger = setup_logger()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=Config.HOST, port=Config.PORT, reload=True)