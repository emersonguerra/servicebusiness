import os

class Config:
    # Secret Key usada para sessão, login etc.
    SECRET_KEY = os.environ.get("SECRET_KEY", "OhblesqBom13$")

    # Usa o banco do Render (PostgreSQL) se estiver definido, senão usa SQLite local
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///finance.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
