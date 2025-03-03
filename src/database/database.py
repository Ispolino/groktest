from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.config import settings
from src.logs import getLogger

pymongo_logger = getLogger("pymongo")
pymongo_logger.setLevel("WARNING")

try:
    client = MongoClient(settings.MONGO_URL, int(settings.MONGO_PORT))
    db = client["test"]
    db_price = db["price"]

except ConnectionFailure as e:
    pymongo_logger.error("Ошибка подключения к MongoDB")
