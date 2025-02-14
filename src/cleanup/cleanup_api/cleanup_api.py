
from flask import Blueprint, request, jsonify
from cleanup.cleaup_services.cleanup_services import CleanUpService
from db_session import get_db
from src.file.services.service import FileManagement

cleanup_api=Blueprint('cleanup_api',__name__)

@cleanup_api.route("/file/cleanup",methods=['POST'])
def perform_cleanup():
    try:
        request_data = request.get_json()
        cleanup_actions = request_data.get("cleanup_actions")

        if not cleanup_actions or not isinstance(cleanup_actions, list):
            return jsonify({"error": "No cleanup actions specified or invalid format"}), 400

        result = CleanUpService.perform_cleanup(cleanup_actions)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500