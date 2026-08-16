import json
from datetime import datetime


class TodoList:
    def __init__(self, filename='todolist.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task = {
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        return self.tasks
    
    
tdl = TodoList()
tdl.add_task("Buy groceries")
tdl.add_task("Read a book")
tdl.complete_task(0)
for idx, task in enumerate(tdl.list_tasks()):
    status = "Done" if task['completed'] else "Pending"
    print(f"{idx}. {task['description']} - {status} (Created at: {task['created_at']})")