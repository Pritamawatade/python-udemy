import os

FILE_NAME = "todo.txt"
def read_task():
    tasks = []
    if(os.path.exists(FILE_NAME)):
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            for line in file:
                text, status = line.strip().split('||', 1)
                tasks.append({'text': text, 'done': status == 'done'})

    return tasks    

def save_tasks(tasks):
        with open(FILE_NAME, "w", encoding='utf-8') as f:
            for task in tasks:
                status = "done" if task["done"] else "not_done"
                f.write(f"{task['text']} || {status}\n")

def display_tasks(tasks):
    
    if not tasks:
        print("no task found")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['text']}")
        print()
    # with open(FILE_NAME, "r", encoding="utf-8") as f:
        
    #     print("Your tasks")
    #     for line in f:
    #         print(line)
            
        

def task_manager():
    tasks = read_task()
    while True:
        print("-------------Task list manger====")
        print('1. View tasks')
        print('2. Add task')
        print('3. Mark task as done')
        print('4. Delete task')     
        
        choice = input("Enter your choice (1-5)")
        
        match choice:
            case '1':
                display_tasks(tasks)
            case '2':
                task_text = input("Enter task description: ")
                tasks.append({'text': task_text, 'done': False})
                save_tasks(tasks)
                print("Task added successfully.")
            case '3':
                display_tasks(tasks)
                task_num = int(input("Enter task number to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['done'] = True
                    save_tasks(tasks)
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")
            case '4':
                display_tasks(tasks)
                    
            case _:
                print("Invalid choice. Please try again.")
                
                

task_manager()                
                
   