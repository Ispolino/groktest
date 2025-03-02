from pymongo import MongoClient
from config import settings
from src.logs import getLogger

pymongo_logger = getLogger("pymongo")
pymongo_logger.setLevel("WARNING")

client = MongoClient(settings.MONGO_URL, int(settings.MONGO_PORT))
db = client["test"]

db_price = db["price"]
