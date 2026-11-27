from datetime import datetime, timedelta # used for comparing deadlines with today's date

# Task format - 1. 'Description' | Deadline: 'date' | Status: 'state'

# Define function for viewing tasks 

def view_tasks(task_list):
    if len(task_list) == 0: # check if task list is empty
        print("There aren't any tasks yet.")
        return
    else:
        for task_number, task in enumerate(task_list, start=1): # enumerate goes through the list and gives the task with its position - instead of a manual counter variable
            if task["is_complete"]: # convert bool into string
                status = "Finished"
            else:
                status = "Open"
            print(f"{task_number}. {task['description']} | Deadline: {task['deadline']} | Category: {task['category']} | Notes: {task['notes']} | Status: {status}") # print all existing tasks in agreed upon format


# Define functions for filtering by completion status

def filter_completion(task_list):
    # Ask until the user enters a valid completion status
    while True:
        wanted = input("Filter by completion (Open/Finished): ").strip().lower()

        # Assign correct value based on user input
        if wanted == "open":
            # open tasks have is_complete = False
            status = False
            break
        elif wanted == "finished":
            status = True
            break
        else:
            print("Wrong input please try again.")

    # Print only the tasks with the chosen status
    found = False
    for task in task_list:
        if task["is_complete"] == status:
            print(task)
            found = True

    if not found:
        print("No task available with this status.")


# Define functions for filtering by priority

def filter_priority(task_list):
    # Ask until the user enters a valid priority
    while True:
        wanted = input("Filter by priority (High/Medium/Low): ").strip().lower()
        
        # Assign correct value based on user input
        if wanted == "high":
            priority = "High"
            break
        elif wanted == "medium":
            priority = "Medium" 
            break
        elif wanted == "low":
            priority = "Low" 
            break
        else:
            print("Wrong input please try again.")

    # Print only the tasks with the chosen priority
    found = False
    for task in task_list:
        if task["priority"] == priority:
            print(task)
            found = True

    if not found:
        print("No task available with this priority.")


# Define functions for filtering by category

def filter_category(task_list):
    # Collect every existing category once
    categories = set()

    # Save all categories inside the set
    for task in task_list:  
        categories.add((task["category"]).lower())

    # Ask until the user enters a category that exists
    while True:
        print("Available Categories:", ", ".join(categories))
        wanted = input("Filter by category: ").lower().strip()
        
        if wanted in categories:
            # Compare User input to task list and print the according tasks
            for task in task_list:
                if task["category"].lower() == wanted:
                    print(task)
            break
        else:
            print("That's not a valid category, please try again.")


# Define function for the filter menu

def filter_menu(task_list):
    # Ask until the user picks a valid filter
    while True:
        print("""
1. Filter by status
2. Filter by priority
3. Filter by category
        """)
        selected_filter = input("By what would you like to filter? (1/2/3): ")

        if selected_filter == "1":
            filter_completion(task_list)
            break
        elif selected_filter == "2":
            filter_priority(task_list)
            break
        elif selected_filter == "3":
            filter_category(task_list)
            break
        else:
            print("Wrong input please try again.")


# Define function for searching tasks by keyword

def search_tasks(task_list):
    if len(task_list) == 0: # nothing to search in
        print("There aren't any tasks yet.")
        return

    # Ask until the user enters a keyword that isn't empty
    keyword = input("Search for a keyword: ").strip()
    while len(keyword) == 0:
        print("The keyword is empty.")
        keyword = input("Please enter a keyword to search for: ").strip()

    # Compare in lowercase so "programming" also finds "Programming"
    found = False
    for task_number, task in enumerate(task_list, start=1): # keep the original number so it matches "View tasks"
        if keyword.lower() in task["description"].lower():
            if task["is_complete"]:
                status = "Finished"
            else:
                status = "Open"
            print(f"{task_number}. {task['description']} | Deadline: {task['deadline']} | Category: {task['category']} | Notes: {task['notes']} | Status: {status}")
            found = True

    if not found:
        print(f"No matching tasks found for '{keyword}'.")


# Define function for warning about overdue tasks and tasks that are due soon

def show_deadline_warnings(task_list):
    today = datetime.today().date() # only the date, without the time
    soon = today + timedelta(days=3) # timedelta adds 3 days to today's date

    for task in task_list:
        if task["is_complete"]: # finished tasks don't need a warning
            continue

        # strptime turns the text "DD.MM.YYYY" into a real date we can compare
        try:
            deadline = datetime.strptime(task["deadline"], "%d.%m.%Y").date()
        except ValueError: # dates like 31.02.2026 can't be converted, so skip them
            continue

        if deadline < today:
            print(f"Overdue: {task['description']} (was due {task['deadline']})")
        elif deadline <= soon:
            print(f"Due soon: {task['description']} (due {task['deadline']})")


# Define function for showing how many tasks are completed

def show_progress(task_list):
    if len(task_list) == 0: # avoid dividing by zero when there are no tasks
        print("There aren't any tasks yet.")
        return

    # Count the completed tasks
    done = 0
    for task in task_list:
        if task["is_complete"]:
            done = done + 1

    total = len(task_list)
    percent = done / total * 100
    print(f"{done} of {total} tasks completed ({percent:.0f}%)") # :.0f rounds to a whole number