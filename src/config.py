import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    debug = True
    URL = os.getenv("URL")
    INTERVAL = os.getenv("INTERVAL")
    MONGO_URL = os.getenv("MONGO_URL")
    MONGO_PORT = os.getenv("MONGO_PORT")


settings = Settings()
