from datetime import datetime, timedelta, timezone
from os import environ as env

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# werkzeug
ALLOW_UNSAFE_WERKZEUG = True

# Flask defaults
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8080
FLASK_DEBUG = True

# Cache
CACHE_DEFAULT_TIMEOUT = 2592000  # 1 Month
CACHE_TYPE = 'FileSystemCache'
CACHE_DIR = 'flask_cache'
CACHE_THRESHOLD = 0

# Security
FLASK_SECRET_KEY = env.get("FLASK_SECRET_KEY")
