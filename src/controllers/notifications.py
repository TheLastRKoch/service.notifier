from flask import Blueprint, render_template

from services.notification import NotificationService


class NotificationsController:
    bp = Blueprint('notifications', __name__)

    def __init__(self, cache):
        self.notification_service = NotificationService()
        self.cache = cache

    @bp.route('/notifications')
    def index(self):
        return render_template('notifications.jinja2')
