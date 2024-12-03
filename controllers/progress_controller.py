from flask import Blueprint, request, jsonify
from services.progress_service import (get_list_sentence_task)

progress_bp = Blueprint("progress_bp", __name__)
# progress_service = ProgressService()
@progress_bp.route("/getTaskSentences", methods=["POST"])
def get_task_sentences():
    data = request.get_json()
    return get_list_sentence_task(data)
    
# @progress_bp.route("/submit", methods=["POST"])
# def submit_progress():
#     data = request.json
#     response = progress_service.submit_progress(data)
#     return jsonify(response), response.get("status", 200)
