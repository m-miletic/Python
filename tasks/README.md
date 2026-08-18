# Task Tracker CLI

A simple **command-line task management application** built with Python.

The application allows users to create, update, delete, and manage tasks directly from the terminal. Tasks are stored persistently in a JSON file.

---

##  Features

-  Add new tasks
-  Update existing tasks
-  Delete tasks
-  Mark tasks as `TODO`
-  Mark tasks as `IN-PROGRESS`
-  Mark tasks as `DONE`
-  List all tasks
-  Filter tasks by status
-  Automatically generate task IDs
-  Persist tasks using JSON
-  Unit tests using Python's `unittest` framework

---

##  Technologies

- **Python**
- **argparse** — command-line argument parsing
- **JSON** — persistent task storage
- **pathlib** — file and path handling
- **datetime** — task timestamps
- **Enum** — task status management
- **unittest** — automated unit testing

---

##  Requirements

- Python **3.10+**
- No external Python packages are required.

---

##  Project Structure

```text
task-tracker/
│
├── task_tracker.py
├── tasks.json
│
└── tests/
    └── test_task_tracker.py
```

---

#  Usage

Run the application from the project directory.

##  Add a Task

Creates a new task and automatically assigns it an ID.

```bash
python task_tracker.py add "Learn Python"
```

Example output:

```text
Task added successfully (ID: 1)
```

---

##  Update a Task

Updates the description of an existing task.

```bash
python task_tracker.py update 1 "Learn unittest"
```

---

##  Delete a Task

Deletes a task using its ID.

```bash
python task_tracker.py delete 1
```

Example output:

```text
Task removed!
```

---

##  Mark Task as In-Progress

```bash
python task_tracker.py mark-in-progress 1
```

---

##  Mark Task as Done

```bash
python task_tracker.py mark-done 1
```

---

##  Mark Task as TODO

```bash
python task_tracker.py mark-todo 1
```

---

##  List Tasks

### List all tasks

```bash
python task_tracker.py list
```

### List TODO tasks

```bash
python task_tracker.py list todo
```

### List in-progress tasks

```bash
python task_tracker.py list in-progress
```

### List completed tasks

```bash
python task_tracker.py list done
```

---

#  Task Statuses

| Status | Description |
|--------|-------------|
| `TODO` | Task has not been started |
| `IN-PROGRESS` | Task is currently being worked on |
| `DONE` | Task has been completed |

---

#  Data Storage

Tasks are stored in a `tasks.json` file.

Each task contains:

- `id`
- `description`
- `status`
- `created_at`
- `updated_at`

Example:

```json
[
    {
        "id": 1,
        "description": "Learn Python",
        "status": "TODO",
        "created_at": "2026-08-18 10:00:00",
        "updated_at": "2026-08-18 10:00:00"
    }
]
```

Task IDs are automatically generated when new tasks are added.

---

#  Testing

This project uses Python's built-in `unittest` framework for automated testing.

Tests are located in:

```text
tests/
└── test_task_tracker.py
```

## Run All Tests

From the project root directory:

```bash
python -m unittest discover
```

You can also run the specific test module:

```bash
python -m unittest tests.test_task_tracker
```

The tests use **temporary directories and files** so that the real `tasks.json` file is not modified during testing.

---

#  What I Learned

This project was built to practice Python programming and software development fundamentals.

Through this project I practiced:

- Object-oriented programming
- Classes and `Enum`
- Functions and modules
- File handling
- JSON serialization and deserialization
- Command-line interfaces with `argparse`
- Error handling
- Unit testing
- Temporary test environments
- Writing reusable code
- Separating application logic from testing

---

#  Future Improvements

Possible improvements for future versions include:

- Better error handling
- More comprehensive test coverage
- Refactoring the application into multiple modules
- Improved CLI output
- Input validation
- More advanced testing with `pytest`

---
