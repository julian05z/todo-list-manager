# Define function for task number checking - check if task number is valid

def get_task_index(task_list):
    while True:
        task_number = input('Enter a task number: ')
        try:
            number = int(task_number) # Input always stores as a string, this converts it to an integer
        except ValueError: # if a user enters something that can't be converted to an integer, this catches it
            print("That's not a number.")
            continue
        if number >= 1 and number <= len(task_list):
            return number - 1 # Return index - number minus 1 because 0 is actually the first task, but shows up as 1
        else:
            print(f"That task number doesn't exist. Enter a number between 1 and {len(task_list)}")
