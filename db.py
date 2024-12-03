import sqlite3
import os
from contextlib import contextmanager

# Define the database file name
DATABASE_FILE = "database.db"

@contextmanager
def get_db_connection():
    """
    Context manager to get a database connection.
    Automatically closes the connection after use.
    """
    connection = None
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        connection.row_factory = sqlite3.Row  # Enable dict-like access for rows
        yield connection
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            connection.close()

def initialize_database():
    """
    Create tables if they don't exist.
    Checks if the database file exists before initialization.
    """
    # Check if the database file exists
    if not os.path.exists(DATABASE_FILE):
        print(f"{DATABASE_FILE} not found, initializing database.")
        
        create_user_table = '''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE
        )
        '''
        
        create_task_table = '''
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        '''
        
        create_assignment_table = '''
        CREATE TABLE IF NOT EXISTS assignment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            task_id INTEGER NOT NULL,
            start_index INTEGER,
            end_index INTEGER,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (id),
            FOREIGN KEY (task_id) REFERENCES task (id)
        )
        '''
        
        create_proofread_table = '''
        CREATE TABLE IF NOT EXISTS proofread (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input TEXT NOT NULL,
            expect TEXT,
            expect_raw TEXT,
            modifier_date TEXT,
            duration_review INTEGER,
            ip_review TEXT
        )
        '''
        
        # Execute all table creation queries
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(create_user_table)
            cursor.execute(create_task_table)
            cursor.execute(create_assignment_table)
            cursor.execute(create_proofread_table)
            conn.commit()
            print("Database initialized successfully.")
    else:
        print(f"{DATABASE_FILE} already exists. Skipping initialization.")
# db.py
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def init_db(app):
    """
    Initialize the database with the Flask app.
    This should be called in the main app setup file (e.g., app.py).
    """
    db.init_app(app)

    # Create all tables if they don't exist
    with app.app_context():
        db.create_all()
        print("Database initialized and tables created.")
