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
    # View tasks 
    number = 1
    for task in task_list:
        print(f"{number}. {task['description']}")
        number = number + 1
    
    # Choose a task
    task_choice = int(input("Which task do you want to edit?"))
    index = task_choice - 1
    
    # Choose a field
    print("1. Description")
    print("2. Deadline")
    print("3. Priority")
    print("4. Category")
    print("5. Notes")
    
    field_choice = input("Which field do you want to edit?")
    
    if field_choice == "1":
        field = "description"
    elif field_choice == "2":
        field = "deadline"
    elif field_choice == "3":
        field = "priority"
    elif field_choice == "4":
        field = "category"
    elif field_choice == "5":
        field = "notes"
    else:
        print("Please choose a valid field.")
        return

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


if __name__ == "__main__":
    tasks = [
        {
            "description": "Study Python",
            "notes": "",
            "deadline": "05.11.2026",
            "priority": "High",
            "category": "Programming",
            "is_complete": False
        },
        {
            "description": "Finish statistics",
            "notes": "Chapter 3",
            "deadline": "08.11.2026",
            "priority": "Medium",
            "category": "Statistics",
            "is_complete": False
        }
    ]

    print("Before:")
    print(tasks)

    edit_task(tasks)
