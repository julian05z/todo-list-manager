from display import view_tasks
from validation import get_task_index

# EXAMPLE OF TASK FORMAT
#
# tasks = [
#     {"description": "Send Application", "notes": "Heading 3", "deadline": "19.05.2026", "priority": "High", "category": "Math", "is_complete": False},
#     {"description": "Send Application", "notes": "", "deadline": "19.05.2026", "priority": "High", "category": "Math", "is_complete": False},
# ]

# Define function for adding tasks to list of tasks

def add_task(task_list, description, deadline, priority, category, notes):
    new_task = {
        "description": description,
        "notes": notes,
        "deadline": deadline,
        "priority": priority,
        "category": category,
        "is_complete": False,
    }
    task_list.append(new_task)

# Define function for editing an existing task

def edit_task(task_list):
    if len(task_list) == 0:
        print("There are no tasks to edit")
        return
    # View tasks 
    view_tasks(task_list)
    
    # Choose a task
    index = get_task_index(task_list)
    
    # Choose a field
    print("1. Description")
    print("2. Deadline")
    print("3. Priority")
    print("4. Category")
    print("5. Notes")
    
    while True:
        field_choice = input("Which field do you want to edit?")
    
        if field_choice == "1":
            field = "description"
            break
        elif field_choice == "2":
            field = "deadline"
            break
        elif field_choice == "3":
            field = "priority"
            break
        elif field_choice == "4":
            field = "category"
            break
        elif field_choice == "5":
            field = "notes"
            break
        else:
            print("Please choose a valid field.")

    # Edit your field
    new_value = input("Enter the new value: ")
    task_list[index][field] = new_value
    print(f"{field} was changed to {new_value}.")

# Define function for setting task status to complete

def complete_task(task_list, index):
    task_list[index]['is_complete'] = True

# Define function for removing tasks from the list - return removed_task for message in main.py

def remove_task(task_list, index):
    removed_task = task_list.pop(index)
    return removed_task

