Task Tracker CLI

A simple command-line task tracker built with Python. It allows users to create, update, delete, and manage tasks directly from the terminal. Tasks are stored persistently in a JSON file.

Features
Add new tasks
Update existing tasks
Delete tasks
Mark tasks as TODO
Mark tasks as in-progress
Mark tasks as done
List all tasks
Filter tasks by status
Automatically generate task IDs
Store tasks persistently in a JSON file
Unit tests using Python's built-in unittest framework
Requirements
Python 3.10 or newer
No external Python packages are required

Usage

Run the application from the project directory.

Add a task

Creates a new task.

python task_tracker.py add "Learn Python"

Example output:

Task added successfully (ID: 1)
Update a task

Updates the description of an existing task.

python task_tracker.py update 1 "Learn unittest"
Delete a task

Deletes a task using its ID.

python task_tracker.py delete 1

Example output:

Task removed!
Mark a task as in-progress
python task_tracker.py mark-in-progress 1
Mark a task as done
python task_tracker.py mark-done 1
Mark a task as TODO
python task_tracker.py mark-todo 1
List all tasks
python task_tracker.py list
List TODO tasks
python task_tracker.py list todo
List in-progress tasks
python task_tracker.py list in-progress
List completed tasks
python task_tracker.py list done
Task Statuses

Tasks can have one of three statuses:

Status	Description
TODO	Task has not been started
IN-PROGRESS	Task is currently being worked on
DONE	Task has been completed
Data Storage

Tasks are stored in a tasks.json file.

Each task contains an ID, description, status, creation timestamp, and last updated timestamp.

Example:

[
    {
        "id": 1,
        "description": "Learn Python",
        "status": "TODO",
        "created_at": "2026-08-18 10:00:00",
        "updated_at": "2026-08-18 10:00:00"
    }
]

Task IDs are automatically generated when new tasks are added.

Testing

The project uses Python's built-in unittest framework.

Tests are located in:

tests/test_task_tracker.py

Run all tests from the project directory:

python -m unittest discover

Or run the specific test module:

python -m unittest tests.test_task_tracker

The tests use temporary directories and files so that the real tasks.json file is not modified during testing.

Technologies
Python
argparse — command-line argument parsing
json — persistent task storage
pathlib — file and path handling
datetime — task timestamps
enum — task status management
unittest — automated unit testing
What I Learned

This project was built to practice Python programming and software development fundamentals, including:

Object-oriented programming
Classes and enums
Functions
File handling
JSON serialization and deserialization
Command-line interfaces with argparse
Error handling
Unit testing
Temporary test environments
Writing reusable and maintainable code
