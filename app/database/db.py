import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

load_dotenv()

DB_URL = os.getenv('DATABASE_URL')