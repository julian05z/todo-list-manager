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

# Define function for editing a existing task

def edit_task(task_list, index, field, new_value):
    task_list[index][field] = new_value

# Define function for setting task status to complete

def complete_task(task_list, index):
    task_list[index]['is_complete'] = True

# Define function for removing tasks from the list - return removed_task for message in main.py

def remove_task(task_list, index):
    removed_task = task_list.pop(index)
    return removed_task

