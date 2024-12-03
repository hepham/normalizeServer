from app import db
from models import Assignment,User
from flask import jsonify

def get_all_assignments():
    """
    Retrieve all task assignments.
    """
    assignments = Assignment.query.all()
    assignment_list = [
        {
            "id": a.id,
            "user_id": a.user_id,
            "task_id": a.task_id,
            "start_index": a.start_index,
            "end_index": a.end_index,
            "date": a.date,
            "status": a.status,
        }
        for a in assignments
    ]
    return jsonify(assignment_list), 200

def add_task_to_user(data):
    """
    Add a task for a specific user.

    Args:
        data (dict): Contains `user_id`, `task_id`, `start_index`, `end_index`, `date`, and `status`.

    Returns:
        Response: Success or failure response.
    """
    user_id = data.get('user_id')
    task_id = data.get('task_id')
    start_index = data.get('start_index')
    end_index = data.get('end_index')
    date = data.get('date')
    status = data.get('status')

    if user_id==None or task_id==None or date ==None or status==None:
        print(f"userId:{user_id}{not user_id}")
        print(f"task_id:{task_id}{ not task_id}")
        print(f"date:{date}{not date}")
        print(f"status:{status}{not status}")
        return jsonify({"error": "Missing required fields"}), 400

    # Check if the task is already assigned
    existing_assignment = Assignment.query.filter_by(user_id=user_id, task_id=task_id).first()
    if existing_assignment:
        return jsonify({"error": "Task already assigned to this user"}), 400

    # Create new assignment
    new_assignment = Assignment(
        user_id=user_id,
        task_id=task_id,
        start_index=start_index,
        end_index=end_index,
        date=date,
        status=status,
    )
    try:
        db.session.add(new_assignment)
        db.session.commit()
        return jsonify({"message": "Task successfully assigned", "id": new_assignment.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def remove_task_from_user(user_id, task_id):
    """
    Remove a task assignment for a specific user.

    Args:
        user_id (int): ID of the user.
        task_id (int): ID of the task.

    Returns:
        Response: Success or failure response.
    """
    assignment = Assignment.query.filter_by(user_id=user_id, task_id=task_id).first()
    if not assignment:
        return jsonify({"error": "Assignment not found"}), 404

    try:
        db.session.delete(assignment)
        db.session.commit()
        return jsonify({"message": "Assignment successfully removed"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
def get_user_task_from_db(data):
    username=data.get("username")
    user=User.query.filter_by(username=username).first()
    print(user.id)
    assignments = Assignment.query.filter_by(user_id=user.id)
    assignment_list=[
        {
            "id": a.id,
            "user_id": a.user_id,
            "task_id": a.task_id,
            "start_index": a.start_index,
            "end_index": a.end_index,
            "date": a.date,
            "status": a.status,
        }
        for a in assignments if a.status!="done"
    ]
    return jsonify(assignment_list), 200
    