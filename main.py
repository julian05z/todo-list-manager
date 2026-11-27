# Import functions from the files
from storage import load_tasks, save_tasks
from tasks import add_task, edit_task, complete_task, remove_task
from display import view_tasks, filter_menu, search_tasks, show_deadline_warnings, show_progress
from validation import ask_description, ask_deadline, ask_priority, ask_category, get_task_index

import os #for clearing menu

# Define function for clearing the screen with the matching command for the operating system
def clear_screen():
    if os.name == "nt": # Windows
        os.system("cls")
    else: # macOS and Linux
        os.system("clear")


# Program start: load the saved tasks from tasks.json and show them
tasks = load_tasks()
view_tasks(tasks)
show_deadline_warnings(tasks) # warn about overdue tasks and tasks due soon at startup


# Main menu: repeats until the user chooses 0 to exit
while True:
    
    print("""
===== ToDo List Manager =====
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

    clear_screen()

    # Menu option 1: add a task
    if choice == "1":
        
        description = ask_description()
        
        deadline = ask_deadline()
       
        priority = ask_priority()
       
        category = ask_category()
       
        notes = input("Add any extra notes to this task (optional): ")
        
        add_task(tasks, description, deadline, priority, category, notes)
        
        save_tasks(tasks) # save after every change so no tasks are lost when the program is closed

        print(f"Task added: {description} (due {deadline})")

    # Menu option 2: view tasks
    elif choice == "2":
        view_tasks(tasks)

    # Menu option 3: edit a task
    elif choice == "3":
        edit_task(tasks)
        save_tasks(tasks)

    # Menu option 4: mark a task as completed   
    elif choice == "4":
        if len(tasks) != 0:
            view_tasks(tasks)
            chosen_task = get_task_index(tasks)
            if chosen_task is None: # get_task_index returns None when the user enters 0 to cancel
                print("Cancelled.")
            else:
                complete_task(tasks, chosen_task)
                save_tasks(tasks)
                print("Task completed: " + tasks[chosen_task]["description"])
        else:
            print("There aren't any tasks yet.")

    # Menu option 5: remove a task
    elif choice == "5":
        if len(tasks) != 0:
            view_tasks(tasks)
            chosen_task = get_task_index(tasks)
            if chosen_task is None:
                print("Cancelled.")
            else:
                removed_task = remove_task(tasks, chosen_task)
                save_tasks(tasks)
                print("Task removed: " + removed_task["description"])
        else:
            print("There aren't any tasks yet.")     
    
    # Menu option 6: filter tasks
    elif choice == "6":
        if len(tasks) != 0:
            filter_menu(tasks)
        else:
            print("There aren't any tasks yet.")

    # Menu option 7: search tasks by keyword
    elif choice == "7":
        search_tasks(tasks)

    # Menu option 8: show progress
    elif choice == "8":
        show_progress(tasks)

    # Menu option 0: exit the program
    elif choice == "0":
        print("Goodbye!")
        break # leave the menu loop, which ends the program

    # Any other input is not a valid option
    else:
        print("That wasn't a valid choice. Please enter a number between 0 and 8")