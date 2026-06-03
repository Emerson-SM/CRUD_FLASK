from flask import Flask
from app.routes.user_routes import user_bp
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app.database.db import db
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(user_bp)

    return app