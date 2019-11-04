import os

from dotenv import load_dotenv


load_dotenv()  # for local development, if there is a .env file, load the key/values as env vars


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
