from database import DataBase
from config import Config

config = Config()
db = DataBase(config.get_mongodb_link(), config.get_db_name(), config.get_collection())

account = db.log_in()


