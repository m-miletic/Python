import argparse
import json
from pathlib import Path
from datetime import datetime
from enum import Enum

class Task:
    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

class Status(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN-PROGRESS"
    DONE = "DONE"

FILE = Path("tasks.json")

## helper fucntions for opening and saving to files (DRY)

def load_tasks():
    if not FILE.exists():
        return []

    with FILE.open("r") as file:
        return json.load(file)

def save_tasks(tasks):
    with FILE.open("w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()

    all_ids = [task["id"] for task in tasks]
    new_id = max(all_ids, default=0) + 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_task = Task(
        new_id,
        description,
        Status.TODO.value,
        now,
        now
    )

    tasks.append(new_task.__dict__)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")


def list_tasks(status):
    tasks = load_tasks()

    for task in tasks:
        if status is None or task["status"].lower() == status:
            print(task)

def update_task(id, updated_description):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == id:
            t["description"] = updated_description
            t["updated_at"] =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with FILE.open("w") as file:
                json.dump(tasks, file, indent=4)
            print("Task updated!")
            return

    print(f"Task with ID:{id} not found.")

def delete_task(id):
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        if t["id"] == id:
            tasks.pop(i)
            with FILE.open("w") as file:
                json.dump(tasks, file, indent=4)
            print("Task removed!")
            return
        
    print(f"Task with ID:{id} not found.")

def mark_task_status(id, status):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == id:
            t["status"] = status
            with FILE.open("w") as file:
                json.dump(tasks, file, indent=4)
            return
        
    print(f"Task with ID:{id} not found.")

## Implementing argparse with subparsers
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", description="subcommands listed out:", help="All possible actions")

add_parser = subparsers.add_parser("add", help="add new task")
add_parser.add_argument("description")

update_parser = subparsers.add_parser("update", help="update a task")
update_parser.add_argument("id", type=int)
update_parser.add_argument("description")

delete_parser = subparsers.add_parser("delete", help="delete a task")
delete_parser.add_argument("id", type=int)

mark_progress_parser = subparsers.add_parser("mark-in-progress")
mark_progress_parser.add_argument("id", type=int)

mark_done_parser = subparsers.add_parser("mark-done")
mark_done_parser.add_argument("id", type=int)

marko_todo_parser = subparsers.add_parser("mark-todo")
marko_todo_parser.add_argument("id", type=int)

list_parser = subparsers.add_parser("list", help="list all tasks")
list_parser.add_argument(
    "status",
    nargs="?",
    choices=["todo", "in-progress", "done"])

args = parser.parse_args()

match args.command:
    case "add":
        add_task(args.description)
    case "list":
        list_tasks(args.status)
    case "update":
        update_task(args.id, args.description)
    case "delete":
        delete_task(args.id)
    case "mark-in-progress":
        mark_task_status(args.id, Status.IN_PROGRESS.value)
    case "mark-done":
        mark_task_status(args.id, Status.DONE.value)
    case "mark-todo":
        mark_task_status(args.id, Status.TODO.value)