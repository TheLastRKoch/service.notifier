from flask import Blueprint, jsonify, request

from services.notification import NotificationService
from models.notification import Notification


def init_api_notifications_blueprint(cache, socket):
    bp = Blueprint('api', __name__, url_prefix='/api/v1')
    notification_service = NotificationService()

    @socket.event
    def connect():
        print("Client connected")

    @socket.event
    def disconnect():
        print("Client disconnected")

    @bp.route('/notification', methods=['POST'])
    def add_notification():
        request_data = request.get_json()
        notification_list = cache.get("notification_list")
        new_notification = Notification(title=request_data.get("title"),
                                        source=request_data.get("source"),
                                        type=request_data.get("type"),
                                        status=request_data.get("status"),
                                        body=request_data.get("body"))
        notification_service.add(notification_list, new_notification)
        cache.set('notification_list', notification_list, timeout=0)
        socket.emit('notification_added', new_notification.to_dict())
        return jsonify({"msg": "Notification added successfully"}), 201

    @bp.route('/notification/<id>', methods=['GET'])
    def get_notification_by_id(id):
        notification_list = cache.get("notification_list")
        notification_body = notification_service.get_by_id(
            notification_list=notification_list, id=id)
        return jsonify(notification_body), 200

    @bp.route('/notification', methods=['GET'])
    def get_notification_list():
        notification_list = cache.get("notification_list")
        return jsonify(notification_list), 200

    @bp.route('/notification/<id>', methods=['DELETE'])
    def delete_notification(id):
        notification_list = cache.get("notification_list")
        notification_service.remove_by_id(notification_list=notification_list,
                                          id=id)
        cache.set('notification_list', notification_list, timeout=0)
        socket.emit('notification_removed', id)
        return jsonify(
            {"msg": "The notification has been removed successfully"}), 200

    return bp
