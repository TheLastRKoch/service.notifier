from flask import Blueprint, jsonify, request, session

from services.notification import NotificationService

# Initialize Blueprint for API routes
notifications_api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Init services
notification_service = NotificationService()


@notifications_api_bp.route('/notification', methods=['POST'])
def add_notification():
    request_data = request.get_json()
    notification_list = session.get("notification_list")
    notification_service.add(notification_list=notification_list,
                             title=request_data.get("title"),
                             source=request_data.get("source"),
                             type=request_data.get("type"),
                             status=request_data.get("status"),
                             body=request_data.get("body"))
    session["notification_list"] = notification_list
    return jsonify({"msg": "Notification added successfully"}), 201


@notifications_api_bp.route('/notification/<id>', methods=['GET'])
def get_notification_by_id(id):
    notification_list = session.get("notification_list")
    notification_body = notification_service.get_by_id(
        notification_list=notification_list, id=id)
    return jsonify(notification_body), 200


@notifications_api_bp.route('/notification', methods=['GET'])
def get_notification_list():
    # Init the notification_list if is undefined
    if not session.get("notification_list"):
        session["notification_list"] = []

    notification_list = session.get("notification_list")
    return jsonify(notification_list), 200


@notifications_api_bp.route('/notification/<id>', methods=['DELETE'])
def delete_notification(id):
    notification_list = session.get("notification_list")
    notification_service.remove_by_id(notification_list=notification_list,
                                      id=id)
    session["notification_list"] = notification_list
    return jsonify({"msg": "The notification has been removed successfully"
                    }), 200
