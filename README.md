# todo_shell_app

## 1. How to install

#### Method-1
  1. Clone or Download the repository
  2. Copy ```todo.py``` file to your home directory
  3. Add the script to  ```.bash_aliases``` file
  ```
    todo()
    {
        python3 ~/todo.py "$@"
    }
  ```
#### Method-2
  1. Open terminal and run 
  ```
  GET https://raw.githubusercontent.com/Anooppandikashala/todo_shell_app/main/todo.py > ~/todo.py
  ```
  2. Add the script to  ```.bash_aliases``` file
  ```
    todo()
    {
        python3 ~/todo.py "$@"
    }
  ```

## 2. Usage: todo <command> [arguments]
### Commands:
  1. ```add <task-name> [label-1] ...[label-n]``` Add a new task with labels
  2. ```ls```  Show the list of tasks
  3. ```rm <task-number>``` Delete the existing task
  4. ```add-labels <task-number> <label-1> ...[label-n]``` add additional info to existing task
