from enviroment import (FLASK_HOST, FLASK_PORT, FLASK_DEBUG, FLASK_SECRET_KEY,
                        CACHE_DEFAULT_TIMEOUT, CACHE_TYPE, CACHE_DIR,
                        CACHE_THRESHOLD)

from controllers.notifications import init_notifications_blueprint
from api.notifications import init_api_notifications_blueprint

from flask_caching import Cache
from flask import Flask

app = Flask(__name__)

app.config['CACHE_DEFAULT_TIMEOUT'] = CACHE_DEFAULT_TIMEOUT

# Cache config
cache = Cache(
    config={
        'CACHE_TYPE': CACHE_TYPE,
        'CACHE_DIR': CACHE_DIR,
        'CACHE_THRESHOLD': CACHE_THRESHOLD
    })
cache.init_app(app)

if not cache.get('notification_list'):
    cache.set('notification_list', [], timeout=0)

# register blueprints
app.register_blueprint(init_notifications_blueprint())
app.register_blueprint(init_api_notifications_blueprint(cache))

# Security
app.secret_key = FLASK_SECRET_KEY

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
