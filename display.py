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
            print(f"{task_number}. {task['description']} | Deadline: {task['deadline']} | Status: {status}") # print all existing tasks in agreed upon format


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
    for task in task_list:
        if task["is_complete"] == status:
            print(task)


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
    for task in task_list:
        if task["priority"] == priority:
            print(task)


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