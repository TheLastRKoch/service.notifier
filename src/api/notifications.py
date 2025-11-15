from flask import Blueprint, jsonify, request, abort

# Initialize Blueprint for API routes
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')


# API Routes
@api_bp.route('/notification', methods=['GET'])
def get_notification_list():
    pass


@api_bp.route('/notification', methods=['GET'])
def get_notification_by_id():
    pass


@api_bp.route('/notification', methods=['GET'])
def get_notification_by_id():
    pass
