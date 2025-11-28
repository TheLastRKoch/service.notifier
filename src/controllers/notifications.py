from flask import Blueprint, render_template


def init_notifications_blueprint():
    bp = Blueprint('notifications', __name__)

    @bp.route('/notifications')
    def index():
        return render_template('notifications.jinja2')

    return bp
