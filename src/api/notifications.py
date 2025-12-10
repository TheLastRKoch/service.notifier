from flask import Blueprint, jsonify, request

from services.notification import NotificationService
from models.notification import Notification


def init_api_notifications_blueprint(cache, socket):
    """
    Create and configure a Flask Blueprint exposing notification HTTP endpoints and Socket.IO events.
    
    The returned Blueprint registers routes to add, retrieve (single and list), and delete notifications under the '/api/v1' prefix, and it registers Socket.IO handlers for client connect/disconnect and emits events when notifications are added or removed.
    
    Parameters:
        cache (object): Cache instance used to persist and retrieve the in-memory `notification_list`.
        socket (object): Socket.IO instance used to register connect/disconnect handlers and emit notification events.
    
    Returns:
        bp (flask.Blueprint): Configured Blueprint with notification routes and associated Socket.IO event wiring.
    """
    bp = Blueprint('api', __name__, url_prefix='/api/v1')
    notification_service = NotificationService()

    @socket.event
    def connect():
        """
        Handle a SocketIO client connection event.
        
        Prints "Client connected" to standard output when a client connects.
        """
        print("Client connected")

    @socket.event
    def disconnect():
        """
        Handle a client disconnection event.
        
        Prints "Client disconnected" to standard output when a client disconnects.
        """
        print("Client disconnected")

    @bp.route('/notification', methods=['POST'])
    def add_notification():
        """
        Add a new notification from the incoming request payload and broadcast it to connected clients.
        
        Reads the request JSON to construct a Notification, appends it to the cached notification list, updates the cache, and emits a 'notification_added' SocketIO event with the notification as a dictionary.
        
        Returns:
            A JSON response containing {"msg": "Notification added successfully"} and HTTP status 201.
        """
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
        """
        Remove a notification by its identifier, persist the updated notification list to cache, and notify connected clients.
        
        Parameters:
            id (str|int): Identifier of the notification to remove.
        
        Returns:
            response (dict), status (int): JSON message confirming removal and HTTP status 200.
        """
        notification_list = cache.get("notification_list")
        notification_service.remove_by_id(notification_list=notification_list,
                                          id=id)
        cache.set('notification_list', notification_list, timeout=0)
        socket.emit('notification_removed', id)
        return jsonify(
            {"msg": "The notification has been removed successfully"}), 200

    return bp