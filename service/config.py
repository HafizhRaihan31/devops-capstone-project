"""
Global Configuration for Application
"""
import os

# Get configuration from environment
DATABASE_URI = os.getenv("DATABASE_URI")

# Use SQLite if no DATABASE_URI provided
if not DATABASE_URI:
    DATABASE_URI = "sqlite:///dev.db"

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "s3cr3t-key-shhhh")
