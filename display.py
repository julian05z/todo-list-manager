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


def filter_completion(task_list):
    while True:
        wanted = input("Filter by completion (Open/Finished): ").strip().lower()
        if wanted == "open":
            status = False
            break
        elif wanted == "finished":
            status = True
            break
        else:
            print("Wrong input please try again.")

    for task in task_list:
        if task["is_complete"] == status:
            print(task)


def filter_priority(task_list):
    while True:
        wanted = input("Filter by priority (High/Medium/Low): ").strip().lower()
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

    for task in task_list:
        if task["priority"] == priority:
            print(task)


def filter_category(task_list):
    categories = set()

    for task in task_list:  
        categories.add((task["category"]).lower())

    while True:
        print("Available Categories:", ", ".join(categories))
        wanted = input("Filter by category: ").lower().strip()
        
        if wanted in categories:
            for task in task_list:
                if task["category"].lower() == wanted:
                    print(task)
            break
        else:
            print("Wrong input please try again.")




