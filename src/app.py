from enviroment import (FLASK_HOST, FLASK_PORT, FLASK_DEBUG, FLASK_SECRET_KEY,
                        FLASK_DEFAULT_SESSION_LIFETIME)

from controllers.notifications import notifications_bp
from api.notifications import notifications_api_bp

from flask import Flask

app = Flask(__name__)

# register blueprints
app.register_blueprint(notifications_bp)
app.register_blueprint(notifications_api_bp)

# Settings
# app.permanent_session_lifetime = FLASK_DEFAULT_SESSION_LIFETIME

# Security
app.secret_key = FLASK_SECRET_KEY

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
