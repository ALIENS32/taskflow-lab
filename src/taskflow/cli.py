"""Command line interface for taskflow."""
import sys
import json
import os
from pathlib import Path

DATA_FILE = Path.home() / ".taskflow_tasks.json"

def load_tasks():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding="utf-8")

def add_task(title):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "completed": False})
    save_tasks(tasks)
    print(f"Added task #{task_id}: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("ID | Status | Title")
    print("-" * 30)
    for t in tasks:
        status = "[x]" if t["completed"] else "[ ]"
        print(f"{t['id']:2d} |  {status}  | {t['title']}")

def done_task(task_id):
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"Marked task #{task_id} as completed.")
    else:
        print(f"Task #{task_id} not found.", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: taskflow [add <title> | list | done <id>]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3:
            print("Error: missing task title.", file=sys.stderr)
            sys.exit(1)
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Error: missing task ID.", file=sys.stderr)
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: invalid task ID.", file=sys.stderr)
            sys.exit(1)
        done_task(task_id)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
