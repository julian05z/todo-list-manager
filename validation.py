# Define function for task number checking - check if task number is valid &  check if number is 0 to exit option

def get_task_index(task_list):
    while True:
        task_number = input('Enter a task number (Enter 0 to cancel): ')
        try:
            number = int(task_number) # Input always stores as a string, this converts it to an integer
        except ValueError: # if a user enters something that can't be converted to an integer, this catches it
            print("That's not a number.")
            continue
        if number == 0: # Cancel choice
            return None # Used later for main.py to know if option should be exited
        elif number >= 1 and number <= len(task_list):
            return number - 1 # Return index - number minus 1 because 0 is actually the first task, but shows up as 1
        else:
            print(f"That task number doesn't exist. Enter a number between 1 and {len(task_list)} or 0 to cancel.")


# Define functions for checking valid description user input

def ask_description():
    # Ask once, then repeat while the input is empty (spaces are removed by strip)
    description = input("Write a description for your task: ").strip()
    while len(description) == 0:
        print("The description is empty.")
        description = input("Please write a valid description for your task: ").strip()
    # Hand the valid description back to the caller
    return description


# Define functions for checking valid deadline user input

def ask_deadline():
    # Number of days in each month (February at 28, leap year is handled below)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ask until the user enters a valid date
    while True:
        
        deadline = input("When is the task due? (DD.MM.YYYY): ").strip()

        # Cut the text into its three parts (the end number of a slice is not included)
        day = deadline[0:2]
        month = deadline[3:5]
        year = deadline[6:10]
        
        # All checks must be true. The length check comes first, so short text
        # can't crash deadline[2], and isdigit() comes before int()
        if (
            len(deadline) == 10
            and deadline[2] == "."
            and deadline[5] == "."
            and day.isdigit()
            and month.isdigit()
            and year.isdigit()
            and 1 <= int(day) <= 31
            and 1 <= int(month) <= 12
            and (
                int(day) <= days_in_month[int(month) - 1] # day must exist in that month
                or (int(month) == 2 and int(day) == 29 and int(year) % 4 == 0) # 29.02. only in leap years
            )
            ):
            return deadline
        else:
            print("That's not a valid date. Use the format (DD.MM.YYYY).")

   
# Define functions for checking valid priority user input

def ask_priority():    
    # Ask until the user enters a valid priority
    while True:
        wanted = input("Write the priority for this task (High/Medium/Low): ").strip().lower()
        # Assign correct value based on user input
        if wanted == "high":
            priority = "High"
            return priority
        elif wanted == "medium":
            priority = "Medium"
            return priority
        elif wanted == "low":
            priority = "Low"
            return priority
        else:
            print("Please write a valid priority for your task. (High/Medium/Low)")


# Define functions for checking valid category user input

def ask_category():
    # Same pattern as ask_description: repeat while the input is empty
    category = input("What is the category of this task?: ").strip()
    while len(category) == 0:
        print("The category is empty.")
        category = input("Please write a valid category for your task: ").strip()
    return category