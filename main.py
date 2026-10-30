##IMPORT YOUR FUNCTIONS HERE##
from storage import load_tasks, save_tasks
from tasks import add_task, edit_task, complete_task, remove_task
from display import view_tasks, filter_completion, filter_priority, filter_category
from validation import get_task_index

tasks = load_tasks()
view_tasks(tasks)

while True:
    
    print("""
1. Add task
2. View tasks
3. Edit task
4. Mark as completed
5. Remove task
6. Filter tasks
7. Search tasks
8. Show progress
0. Exit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        
        description = input("Write a description for your task: ")
        
        deadline = input("When is the task due? (DD.MM.YYYY): ")
       
        priority = input("Write the priority for this task (High, Medium, Low): ")
       
        category = input("What is the category of this task?: ")
       
        notes = input("Add any extra notes to this task (optional): ")
        
        add_task(tasks, description, deadline, priority, category, notes)
        
        save_tasks(tasks)

        print(f"Task added: {description} (due {deadline})")
   
    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        edit_task(tasks)
        save_tasks(tasks)
        
    elif choice == "4":
        if len(tasks) != 0:
            view_tasks(tasks)
            chosen_task = get_task_index(tasks)
            complete_task(tasks, chosen_task)
            save_tasks(tasks)
            print("Task completed: " + tasks[chosen_task]["description"])
        else:
            print("There aren't any tasks yet.")
    
    elif choice == "5":
        if len(tasks) != 0:
            view_tasks(tasks)
            chosen_task = get_task_index(tasks)
            removed_task = remove_task(tasks, chosen_task)
            save_tasks(tasks)
            print("Task removed: " + removed_task["description"])
        else:
            print("There aren't any tasks yet.")     

   
    elif choice in ["6", "7", "8"]:
        print("Coming soon.")
    
    elif choice == "0":
        print("Goodbye!")
        break
   
    else:
        print("That wasn't a valid choice. Please enter a number between 0 and 8")
