import sys
import os

TODO_FILE = os.path.expanduser("~") + "/todo.txt"

todo_list = []

def is_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def show_help():
    print("Usage: todo <command> [arguments]")
    print("Commands:")
    print("  add <task-name> [label-1] ...[label-n] Add a new task with labels")
    print("  ls  Show the list of tasks")
    print("  rm <task-number>  Delete the existing task")
    print("  add-labels <task-number> <label-1> ...[label-n] add additional info to existing task")

def add_task(args):
    if len(args) < 1:
        print("Error: Task name cannot be empty.")
        return
    task_name = " ".join(args)
    # print("Task name : ",task_name)
    if not task_name:
        print("Error: Task name cannot be empty.")
        return

    with open(TODO_FILE, "a") as file:
        file.write(task_name + "\n")
    
    print(f"Task added: {task_name}")
    list_tasks()

def writeToFile():
    with open(TODO_FILE, "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def remove_task(args):
    task_number = args[0]
    if is_integer(task_number) and int(task_number) > 0 and int(task_number) <= len(todo_list):
        task_index = int(task_number)-1
        print("Deleting ", todo_list[task_index])
        todo_list.remove(todo_list[task_index])
        writeToFile()

def add_labels(args):
    if len(args) < 2:
        print("Give Valid task number and labels")
        print("todo add-labels <task-number> <label-1> ...[label-n]")
        return
    task_number = args[0]
    labels = args[1:]
    if is_integer(task_number) and int(task_number) > 0 and int(task_number) <= len(todo_list):
        task_index = int(task_number)-1
        print("Updating ", todo_list[task_index])
        current_task_and_labels = str(todo_list[task_index]).split(" ")
        # print(current_task_and_labels)
        for label in labels:
            current_task_and_labels.append(label)
        # print(current_task_and_labels)
        todo_list[task_index] = " ".join(current_task_and_labels)
        writeToFile()
    else:
        print("Give Valid task number")
        print("todo add-labels <task-number> <label-1> ...[label-n]")
    
    list_tasks()
        

def list_tasks():
    load_tasks()
    if len(todo_list) > 0:
        print("TODO List:")
    else:
        print("No tasks found.")
        return
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task.strip()}")               

def load_tasks():
    todo_list.clear()
    try:
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            if tasks:
                for i, task in enumerate(tasks, start=1):
                    # print(f"{i}. {task.strip()}")
                    todo_list.append(task.strip())
            else:
                print("No tasks found.")
    except FileNotFoundError:
        # print("TODO file not found. Create a task first.")
        pass

def init():
    todo_list.clear()
    try:
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            if tasks:
                for i, task in enumerate(tasks, start=1):
                    # print(f"{i}. {task.strip()}")
                    todo_list.append(task.strip())
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("TODO file not found. Create a task first.")
        
def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]
    init()

    if command == "add":
        add_task(args)
    elif command == "ls":
        list_tasks()
    elif command == "rm":
        remove_task(args)
    elif command == "add-label":
        add_labels(args)
    else:
        show_help()

if __name__ == "__main__":
    main()
