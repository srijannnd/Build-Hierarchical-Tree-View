from pymongo import MongoClient
from config.settings.base import get_secret

password = get_secret("DB_PASSWORD")
username = get_secret("DB_USER")
db_name = get_secret("DB_NAME")
db_host_mongo = get_secret("DB_HOST")

mongo_uri = "mongodb+srv://{username}:{password}@{host}/{db_name}".format(
    username=username, password=password, host=db_host_mongo, db_name=db_name)

client = MongoClient(mongo_uri)
database = client[db_name]
