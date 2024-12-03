from flask import Flask
from db import db
from flask_sqlalchemy import SQLAlchemy
from models import User, Task, Assignment, Proofread
# App setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize database
db.init_app(app)
# Import models to ensure they're registered with SQLAlchemy
with app.app_context():

    db.create_all()  # Create tables if not exists

# Import controllers
# from controllers.user_controller import user_bp
# from controllers.task_controller import task_bp


# Register Blueprints
# app.register_blueprint(user_bp, url_prefix='/users')
# app.register_blueprint(task_bp, url_prefix='/tasks')


if __name__ == '__main__':
    from controllers.assignment_controller import assignment_bp
    from controllers.progress_controller import progress_bp
    app.register_blueprint(assignment_bp, url_prefix='/assignments')
    app.register_blueprint(progress_bp, url_prefix='/progressProofRead')
    app.run(debug=True)
