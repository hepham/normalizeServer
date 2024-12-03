from flask import Blueprint, request, jsonify
from services.assignment_service import (
    get_all_assignments,
    add_task_to_user,
    remove_task_from_user,
    get_user_task_from_db
)

assignment_bp = Blueprint('assignment_bp', __name__)

@assignment_bp.route('/', methods=['GET'])
def get_assignments():
    """
    API to retrieve all task assignments.
    """
    return get_all_assignments()

@assignment_bp.route('/', methods=['POST'])
def assign_task():
    """
    API to assign a task to a specific user.
    Request Body:
    {
        "user_id": 1,
        "task_id": 2,
        "start_index": 0,
        "end_index": 10,
        "date": "2024-12-03",
        "status": "not_done"
    }
    """
    data = request.get_json()
    return add_task_to_user(data)

@assignment_bp.route('/', methods=['DELETE'])
def delete_assignment():
    """
    API to delete a task assignment for a specific user.
    Query Parameters:
    - user_id (int): ID of the user.
    - task_id (int): ID of the task.
    """
    user_id = request.args.get('user_id', type=int)
    task_id = request.args.get('task_id', type=int)
    if user_id==None or not task_id==None:
        return jsonify({"error": "Both user_id and task_id are required"}), 400
    return remove_task_from_user(user_id, task_id)
@assignment_bp.route("/getUserTask",methods=['POST'])
def get_user_task():
    data=request.get_json()
    print(data)
    return get_user_task_from_db(data)