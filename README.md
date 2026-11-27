# ✅ ToDo List Manager

## 💡 Problem & Goal

**❗ Problem**

Students have many things to do, such as school assignments and daily tasks, which makes it difficult to keep track of everything and remember different deadlines. This can make it difficult to decide which task to do first and find specific tasks.

**🎯 Goal**

The goal is to help students organize their daily tasks and school assignments more easily. The ToDo List Manager allows students to create tasks, set priorities, and filter tasks so they can find important tasks faster and better organize their work.

## 📝 Analysis

### 👤 User Roles

| Role | Description |
|------|-------------|
| 🎓 **Student** | Creates and manages tasks and wants to keep track of deadlines and priorities. |

### 📖 User Stories

---

#### ➕ User Story 1 – Add and View Tasks

**As a** student,
**I want** to add new tasks to my to-do list and view all of them in the console,
**so that** I can keep track of everything I need to do in one place.

**✔️ Acceptance Criteria 1**
- *Given* the student has opened the To-Do List Manager and selected the option “Add task”,
- *When* the student enters a task description and a deadline and confirms,
- *Then* the system adds the task to the list, displays the new task, and shows a confirmation message.

**✔️ Acceptance Criteria 2**
- *Given* the task list contains at least one task,
- *When* the student selects the option “View tasks”,
- *Then* all tasks are displayed in the console with their description, deadline, and status.

**✔️ Acceptance Criteria 3**
- *Given* the task list is empty,
- *When* the student selects the option “View tasks”,
- *Then* the system displays a message that there are no tasks yet instead of an empty list.

---

#### ☑️ User Story 2 – Complete and Remove Tasks

**As a** student,
**I want** to mark tasks as completed and remove tasks I no longer need,
**so that** my list only shows what is still relevant and I can see my progress.

**✔️ Acceptance Criteria 1**
- *Given* the task list contains an incomplete task called “Submit assignment”,
- *When* the student selects the option “Mark as completed” and chooses this task,
- *Then* the task is saved with the status “Completed”.

**✔️ Acceptance Criteria 2**
- *Given* the task list contains a task the student no longer needs,
- *When* the student selects the option “Remove task” and chooses this task,
- *Then* the task is deleted from the list and no longer appears when the list is displayed.

**✔️ Acceptance Criteria 3**
- *Given* the task list contains three tasks,
- *When* the student tries to complete, remove, or edit a task using a number that does not exist,
- *Then* the system rejects the input, shows an error message, and prompts the student to choose a valid task.

---

#### 💾 User Story 3 – Save and Load Tasks

**As a** student,
**I want** my tasks to be saved to a file and loaded automatically when I start the program,
**so that** I do not lose my tasks when I close the application.

**✔️ Acceptance Criteria 1**
- *Given* a student has added, changed, or removed a task,
- *When* the change is confirmed,
- *Then* the system writes the updated task list to the file.

**✔️ Acceptance Criteria 2**
- *Given* a task file with saved tasks exists,
- *When* the student starts the To-Do List Manager,
- *Then* the system reads the file and displays all previously saved tasks.

**✔️ Acceptance Criteria 3**
- *Given* no task file exists yet when the student starts the program for the first time,
- *When* the program starts,
- *Then* the system creates a new empty task file and starts with an empty task list without crashing.

---

#### ✏️ User Story 4 – Edit a Task

**As a** student,
**I want** to edit my existing tasks,
**so that** I can update their description, deadline, priority, or category when something changes.

**✔️ Acceptance Criteria 1**
- *Given* a task already exists in the task list,
- *When* the student selects the option “Edit task”, chooses this task, changes the description, deadline, priority, or category, and saves the changes,
- *Then* the task is updated with the new information and a confirmation message is shown.

---

#### 🛡️ User Story 5 – Data Validation

**As a** student,
**I want** the ToDo List Manager to validate the data I enter when creating or editing a task,
**so that** I can avoid saving tasks with incorrect or incomplete data.

**✔️ Acceptance Criteria 1**
- *Given* a student is creating or editing a task and enters a task description and a deadline,
- *When* the student enters an empty description or an invalid date format,
- *Then* the system rejects the input and prompts the student to enter valid data.

**✔️ Acceptance Criteria 2**
- *Given* a student is creating or editing a task,
- *When* the student enters a valid description and a valid deadline,
- *Then* the system accepts the task and saves it.

**✔️ Acceptance Criteria 3**
- *Given* a student is selecting a priority for a task,
- *When* the student enters a value other than "High", "Medium" or "Low",
- *Then* the system rejects the input, shows an error message, and asks for a valid priority.

**✔️ Acceptance Criteria 4**
- *Given* the student is in the main menu,
- *When* the student enters an option that does not exist (for example a letter or a number outside the menu),
- *Then* the system shows an error message and displays the menu again without crashing.

---

#### 🚦 User Story 6 – Priority

**As a** student,
**I want** to assign a priority to my tasks,
**so that** I can easily identify which tasks I should focus on first.

**✔️ Acceptance Criteria 1**
- *Given* a student is creating a task called "Study for programming exam",
- *When* the student selects "High" as the priority,
- *Then* the task is saved with the priority "High".

**✔️ Acceptance Criteria 2**
- *Given* three tasks have the priorities "Low", "High", and "Medium",
- *When* the student views the task list,
- *Then* the tasks are displayed in the order "High", "Medium", "Low".

---

#### 🏷️ User Story 7 – Category / Subject Assignment

**As a** student,
**I want** to assign a subject or category to each task,
**so that** I can organize my tasks by course.

**✔️ Acceptance Criteria 1**
- *Given* a student is creating or editing a task,
- *When* the student assigns the category “Mathematics” and saves the task,
- *Then* the task is saved with the category “Mathematics”.

**✔️ Acceptance Criteria 2**
- *Given* a task has a category assigned,
- *When* the student views the task list,
- *Then* the category is displayed with the corresponding task.

---

#### 🗒️ User Story 8 – Notes

**As a** student,
**I want** to add and change notes on my tasks,
**so that** I can store extra information related to the task.

**✔️ Acceptance Criteria 1**
- *Given* a task called “Programming homework” already exists,
- *When* the student adds the note “Review loops” and saves it,
- *Then* the note “Review loops” is saved and displayed with the task.

**✔️ Acceptance Criteria 2**
- *Given* a task already contains a note,
- *When* the student changes the note and saves it,
- *Then* the updated note is displayed with the task.

---

#### 🔎 User Story 9 – Filter

**As a** student,
**I want** to filter my existing tasks by criteria such as priority, category, or completion status,
**so that** I can quickly find the tasks that are important to me.

**✔️ Acceptance Criteria 1**
- *Given* the task list contains two completed tasks and three incomplete tasks,
- *When* the student selects the filter “Incomplete”,
- *Then* only the three incomplete tasks are displayed.

**✔️ Acceptance Criteria 2**
- *Given* the task list contains tasks with "High", "Medium", and "Low" priority,
- *When* the student filters the list by "High",
- *Then* only the tasks with "High" priority are displayed.

**✔️ Acceptance Criteria 3**
- *Given* the task list contains tasks assigned to different categories,
- *When* the student filters the list by the category "Mathematics",
- *Then* only the tasks in the category "Mathematics" are displayed.

---

#### 🔍 User Story 10 – Search by Keyword

**As a** student,
**I want** to search my tasks by entering a keyword,
**so that** I can quickly find a specific task without scrolling through the whole list.

**✔️ Acceptance Criteria 1**
- *Given* the task list contains the tasks "Study for programming exam", "Buy groceries" and "Programming homework",
- *When* the student searches for the keyword "programming",
- *Then* only the two tasks containing "programming" are displayed, regardless of upper or lower case.

**✔️ Acceptance Criteria 2**
- *Given* the task list contains no task matching the keyword,
- *When* the student searches for "biology",
- *Then* the system displays a message that no matching tasks were found.

---

#### ⏰ User Story 11 – Overdue and Upcoming Deadlines

**As a** student,
**I want** to be warned about overdue tasks and tasks due within the next three days when I start the program,
**so that** I don't miss any deadlines.

**✔️ Acceptance Criteria 1**
- *Given* the task list contains an incomplete task whose deadline has already passed,
- *When* the student starts the To-Do List Manager,
- *Then* the system displays a warning listing this task as "Overdue".

**✔️ Acceptance Criteria 2**
- *Given* the task list contains an incomplete task with a deadline within the next 3 days,
- *When* the student starts the To-Do List Manager,
- *Then* the system displays this task as "Due soon".

**✔️ Acceptance Criteria 3**
- *Given* a task with a past deadline is already marked as completed,
- *When* the student starts the To-Do List Manager,
- *Then* the task is not shown as overdue.

---

#### 📊 User Story 12 – Progress Overview

**As a** student,
**I want** to see a summary of my completed and open tasks,
**so that** I can track my progress and stay motivated.

**✔️ Acceptance Criteria 1**
- *Given* the task list contains 2 completed and 3 incomplete tasks,
- *When* the student selects the option "Show progress",
- *Then* the system displays "2 of 5 tasks completed (40%)".

**✔️ Acceptance Criteria 2**
- *Given* the task list is empty,
- *When* the student selects the option "Show progress",
- *Then* the system displays a message that there are no tasks yet instead of an error.

## 🕹️ Main Functionality

The ToDo List Manager is a console application that helps students organise their tasks.

When the program starts, it loads all saved tasks from `tasks.json`, shows the task list and warns about tasks that are overdue or due within the next 3 days.

After that, a menu is shown where the user can:

1. **Add a task** with a description, deadline, priority, category and optional notes
2. **View all tasks** with their details and status
3. **Edit a task**, for example to change its deadline or notes
4. **Mark a task as completed**
5. **Remove a task** that is no longer needed
6. **Filter tasks** by status, priority or category
7. **Search tasks** by a keyword
8. **Show progress**, meaning how many tasks are already completed

<!-- -->

0. **Exit** the program

All user input is checked, so empty descriptions, wrong date formats or invalid task numbers are rejected. Every change is saved to `tasks.json` right away, so no tasks are lost when the program is closed.

### ⚙️ Control Flow Logic
Our control flow logic for the ToDo List Manager is as follows:

<img src="docs/control%20flow%20logic.png" alt="Control Flow Logic" width="500">

## ✅ Project Requirements

The app meets the three required criteria:

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

### 1. 💻 Interactive App (Console Input)
The user controls the app through a console menu and can add, view, edit, complete, remove, filter and search tasks, as well as see their progress.

### 2. 🛡️ Data Validation
All input is checked in `validation.py` and `main.py`:
- Descriptions can't be empty
- Deadlines must use the format DD.MM.YYYY
- Priority must be High, Medium or Low
- Task numbers must exist (0 cancels)
- Invalid menu choices show an error and the menu appears again

### 3. 📁 File Processing
Tasks are stored in `tasks.json` (`storage.py`):
- **📥 Read:** at startup, tasks are loaded from the file (an empty file is created if none exists)
- **📤 Write:** every change is saved to the file right away

Example of one saved task in `tasks.json`:
```json
[
  {
    "description": "Programming homework",
    "notes": "Review loops",
    "deadline": "05.12.2026",
    "priority": "High",
    "category": "Programming",
    "is_complete": false
  }
]
```

## ⚙️ Implementation

### 🐍 Technology
- Python 3.x
- Environment: Visual Studio Code (local)
- No external libraries

### 📂 Project Structure

```text
ToDoListManager/
├── main.py                    # main program logic (console application)
├── tasks.py                   # creating and editing tasks (add_task, edit_task, complete_task, remove_task)
├── validation.py              # input validation (get_task_index, ask_description, ask_deadline, ask_priority, ask_category)
├── storage.py                 # saving and loading tasks (save_tasks, load_tasks)
├── display.py                 # displaying tasks and the progress overview (view_tasks, filter_completion, filter_priority, filter_category, search_tasks, show_deadline_warnings, show_progress)
├── tasks.json                 # task data, created automatically on first start (listed in .gitignore)
├── docs/                      # documentation, not needed to run the program
│   └── control flow logic.png # control flow diagram used in this README
└── README.md                  # project description and documentation
```

### ▶️ How to Run
1. Clone the repository to your device:
```bash
git clone https://github.com/julian05z/todo-list-manager.git
```
2. Open the Terminal and go into the project folder:
```bash
cd todo-list-manager
```
3. Start the program:
```bash
python3 main.py
```
On Windows, use `python main.py` or `py main.py` instead.

### 📚 Libraries Used
- `json`: Used in `storage.py` to save the task list to `tasks.json` and load it again when the program starts.
- `datetime`: Used in `display.py` (`datetime` and `timedelta`) to compare deadlines with today's date and find tasks that are overdue or due within the next 3 days.
- `os`: Used in `main.py` to clear the console screen (`cls` on Windows, `clear` on macOS/Linux) so the menu stays easy to read.

These libraries are part of the Python standard library, so no external installation is required. They were chosen because they are simple and cover everything the app needs: saving data, working with dates and keeping the console clean.

## 👥 Team & Contributions

### BIT PTD-26

| Name       | Contribution |
|------------|--------------|
| Mateja Dimitrijevic | User Stories 1, 2, 3: Add and View Tasks, Complete and Remove Tasks, Save and Load Tasks |
| Milos Dumitrovic | User Stories 4, 7, 8: Edit a task, Category / Subject Assignment, Notes |
| Fabio Rubin | User Stories 5, 6, 9: Data Validation, Priority, Filter |
| Julian Zurkinden | User Stories 10, 11, 12: Search by Keyword, Overdue and Upcoming Deadlines, Progress Overview |