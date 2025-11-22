from flask import Flask

from controllers.notifications import notifications_bp

from enviroment import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

app = Flask(__name__)

# register blueprints
app.register_blueprint(notifications_bp)

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
