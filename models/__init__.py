from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()  # Inisialisasi SQLAlchemy
Base = declarative_base()