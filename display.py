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