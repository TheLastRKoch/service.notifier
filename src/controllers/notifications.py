from flask import Blueprint, render_template, session

notifications_bp = Blueprint('notifications', __name__)


@notifications_bp.route('/notifications')
def index():

    # Init the notification_list if is undefined
    if not session.get("notification_list"):
        session["notification_list"] = []

    return render_template('notifications.jinja2')
