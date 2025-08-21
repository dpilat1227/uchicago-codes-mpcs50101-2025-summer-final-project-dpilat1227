#!/usr/bin/env python3

import argparse
import pickle
import os
from datetime import datetime, date

# save tasks to home directory so it works from anywhere
DATA_FILE = os.path.join(os.path.expanduser('~'), '.todo.pickle')


class Task:
    """Simple Task object"""

    def __init__(self, uid, name, priority=1, due=None):
        self.id = uid
        self.name = name
        self.priority = priority
        self.created = datetime.now()
        self.completed = None
        self.due = due  # can be None

    def mark_done(self):
        self.completed = datetime.now()

    def age_days(self):
        return (date.today() - self.created.date()).days


class Tasks:
    """Holds a list of Task objects"""

    def __init__(self):
        # try to load saved tasks if file exists
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "rb") as f:
                    self.tasks = pickle.load(f)
            else:
                self.tasks = []
        except:
            # if file is corrupted, start fresh
            self.tasks = []

    def save(self):
        with open(DATA_FILE, "wb") as f:
            pickle.dump(self.tasks, f)

    def next_id(self):
        if not self.tasks:
            return 1
        return max(t.id for t in self.tasks) + 1

    def add(self, name, priority=1, due=None):
        # check if name is actually a string
        if not isinstance(name, str):
            print('There was an error in creating your task. Run "todo -h" for instructions.')
            return
        
        t = Task(self.next_id(), name, priority, due)
        self.tasks.append(t)
        self.save()
        print(f"Created task {t.id}")

    def delete(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                self.tasks.remove(t)
                self.save()
                print(f"Deleted task {task_id}")
                return
        print("Task not found")

    def done(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                t.mark_done()
                self.save()
                print(f"Completed task {task_id}")
                return
        print("Task not found")

    def list_tasks(self, show_all=False, query_terms=None):
        # sort by due date, then priority
        def sort_key(t):
            return (
                t.due if t.due else date.max,
                -t.priority,
            )

        tasks_to_show = []
        for t in self.tasks:
            if not show_all and t.completed:
                continue
            if query_terms:
                if not any(word.lower() in t.name.lower() for word in query_terms):
                    continue
            tasks_to_show.append(t)

        tasks_to_show.sort(key=sort_key)

        # don't print anything if no tasks
        if not tasks_to_show:
            return

        # print header
        if show_all:
            print("ID   Age  Due Date   Priority   Task                Created                       Completed")
            print("--   ---  --------   --------   ----                ---------------------------   -------------------------")
        else:
            print("ID   Age  Due Date   Priority   Task")
            print("--   ---  --------   --------   ----")

        # print rows
        for t in tasks_to_show:
            due_str = t.due.strftime("%m/%d/%Y") if t.due else "-"
            age_str = str(t.age_days()) + "d"
            if show_all:
                created_str = t.created.strftime("%a %b %d %H:%M:%S CST %Y")
                completed_str = t.completed.strftime("%a %b %d %H:%M:%S CST %Y") if t.completed else "-"
                print(f"{t.id:<4} {age_str:<4} {due_str:<10} {t.priority:<10} {t.name:<19} {created_str:<29} {completed_str}")
            else:
                print(f"{t.id:<4} {age_str:<4} {due_str:<10} {t.priority:<10} {t.name}")


def parse_due(due_str):
    # basic date parsing
    try:
        return datetime.strptime(due_str, "%m/%d/%Y").date()
    except:
        try:
            return datetime.strptime(due_str, "%m/%d/%y").date()
        except:
            return None


def main():
    parser = argparse.ArgumentParser(description="Ccommand line task manager")
    parser.add_argument("--add", type=str, help="add a new task")
    parser.add_argument("--due", type=str, help="due date in MM/DD/YYYY")
    parser.add_argument("--priority", type=int, choices=[1, 2, 3], default=1)
    parser.add_argument("--list", action="store_true", help="list tasks")
    parser.add_argument("--report", action="store_true", help="list all tasks")
    parser.add_argument("--query", nargs="+", help="search tasks by keyword(s)")
    parser.add_argument("--done", type=int, help="mark task done by id")
    parser.add_argument("--delete", type=int, help="delete task by id")

    args = parser.parse_args()
    task_list = Tasks()

    if args.add:
        due = parse_due(args.due) if args.due else None
        task_list.add(args.add, args.priority, due)

    elif args.list:
        task_list.list_tasks(show_all=False)

    elif args.report:
        task_list.list_tasks(show_all=True)

    elif args.query:
        task_list.list_tasks(show_all=False, query_terms=args.query)

    elif args.done:
        task_list.done(args.done)

    elif args.delete:
        task_list.delete(args.delete)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()