import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    debug = True
    URL = os.getenv("URL")
    INTERVAL = os.getenv("INTERVAL")
    MONGO_URL = os.getenv("MONGO_URL")
    MONGO_PORT = os.getenv("MONGO_PORT")
    HTML_TAG = os.getenv("HTML_TAG")
    HTML_CLASS = os.getenv("HTML_CLASS")


settings = Settings()
