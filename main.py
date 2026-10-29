##IMPORT YOUR FUNCTIONS HERE##
from storage import load_tasks, save_tasks
from tasks import add_task, edit_task, complete_task, remove_task
from display import view_tasks
from validation import get_task_index

tasks = load_tasks()

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
        print("Coming soon.")
    elif choice == "2":
        print("Coming soon.")
    elif choice == "4":
        print("Coming soon.")
    elif choice == "5":
        print("Coming soon.")
    elif choice in ["3", "6", "7", "8"]:
        print("Coming soon.")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("That wasn't a valid choice. Please enter a number between 0 and 8")
