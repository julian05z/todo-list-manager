import json

TASKS_FILE = "tasks.json" # Value doesn't change, used for saving and loading tasks from file

# Function to save tasks into JSON file. "With open" only works with strings, so using JSON

def save_tasks(task_list):
    with open(TASKS_FILE, "w") as file: # open TASKS_FILE, where tasks.json is stored. "w" stands for "write" (deletes old content then writes - everything up to date) since the task is being saved.
        json.dump(task_list, file, indent=4) #convert list into JSON, write into TASKS_FILE

# Function to read tasks from created JSON file and convert it back into a list of dictionaries

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file: # read TASKS_FILE
            loaded_tasks = json.load(file) # opposite of json.dump - read JSON text from created file and turn it back into python list of dictionaries
        return loaded_tasks # return tasks as list of dictionaries
    except FileNotFoundError: # if tasks.json is missing - create an empty file and an empty list
        save_tasks([])
        return []