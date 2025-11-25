from flask import Blueprint, jsonify, request

from services.notification import NotificationService


class NotificationsAPI:

    bp = Blueprint('api', __name__, url_prefix='/api/v1')

    def __init__(self, cache):
        self.notification_service = NotificationService()
        self.cache = cache

    @bp.route('/notification', methods=['POST'])
    def add_notification(self):
        request_data = request.get_json()
        notification_list = self.cache.get("notification_list")
        self.notification_service.add(notification_list=notification_list,
                                      title=request_data.get("title"),
                                      source=request_data.get("source"),
                                      type=request_data.get("type"),
                                      status=request_data.get("status"),
                                      body=request_data.get("body"))
        self.cache.set('notification_list', notification_list, timeout=0)
        return jsonify({"msg": "Notification added successfully"}), 201

    @bp.route('/notification/<id>', methods=['GET'])
    def get_notification_by_id(self, id):
        notification_list = self.cache.get("notification_list")
        notification_body = self.notification_service.get_by_id(
            notification_list=notification_list, id=id)
        return jsonify(notification_body), 200

    @bp.route('/notification', methods=['GET'])
    def get_notification_list(self):
        notification_list = self.cache.get("notification_list")
        return jsonify(notification_list), 200

    @bp.route('/notification/<id>', methods=['DELETE'])
    def delete_notification(self, id):
        notification_list = self.cache.get("notification_list")
        self.notification_service.remove_by_id(
            notification_list=notification_list, id=id)
        self.cache.set('notification_list', notification_list, timeout=0)
        return jsonify(
            {"msg": "The notification has been removed successfully"}), 200
