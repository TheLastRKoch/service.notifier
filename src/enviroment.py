from datetime import datetime, timedelta, timezone
from os import environ as env

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask defaults
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8080
FLASK_DEBUG = True
FLASK_DEFAULT_SESSION_LIFETIME = datetime.now(
    timezone.utc) + timedelta(days=30)

# Security
FLASK_SECRET_KEY = env.get("FLASK_SECRET_KEY")
