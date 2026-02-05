import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-later")

    SQLALCHEMY_DATABASE_URI = "sqlite:///secure_access.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 🔐 JWT Configuration
    JWT_SECRET_KEY = os.environ.get(
        "JWT_SECRET_KEY",
        "jwt-secret-change-later"
    )
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60  # 1 hour
