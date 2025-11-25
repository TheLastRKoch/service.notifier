from enviroment import (FLASK_HOST, FLASK_PORT, FLASK_DEBUG, FLASK_SECRET_KEY,
                        FLASK_DEFAULT_SESSION_LIFETIME)

from controllers.notifications import NotificationsController
from api.notifications import NotificationsAPI

from flask_caching import Cache
from flask import Flask

app = Flask(__name__)

# Cache config
cache = Cache(
    config={
        'CACHE_TYPE': 'FileSystemCache',
        'CACHE_DIR': 'flask_cache',
        'CACHE_THRESHOLD': 0
    })
cache.init_app(app)

if not cache.get('notification_list'):
    cache.set('notification_list', [], timeout=0)

# Define controllers/apis
notifications_controller = NotificationsController(cache=cache)
notifications_api = NotificationsAPI(cache=cache)

# register blueprints
app.register_blueprint(notifications_controller.bp)
app.register_blueprint(notifications_api.bp)

# Security
app.secret_key = FLASK_SECRET_KEY

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
