from flask import Flask
from controllers.notifications import notifications_bp

app = Flask(__name__)

# register blueprints
app.register_blueprint(notifications_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
