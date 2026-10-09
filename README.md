# ✅ ToDo List Manager

## 📝 Analysis

**❗ Problem**

Students have many things to do, such as school assignments and daily tasks, which makes it difficult to keep track of everything and remember different deadlines. This can make it difficult to decide which task to do first and find specific tasks.

**🎯 Goal**

The goal is to help students organize their daily tasks and school assignments more easily. The ToDo List Manager allows students to create tasks, set priorities, and filter tasks so they can find important tasks faster and better organize their work.

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

---

**🧩 Use cases:**
- 

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. 💻 Interactive App (Console Input)

The application interacts with the user via the console. Users can:
- 

---

### 2. 🛡️ Data Validation

The application validates all user input to ensure data integrity and a smooth user experience:

- 

---

### 3. 📁 File Processing

The application reads and writes data using files:

- **📥 Input file:** 
- **📤 Output file:** 

## ⚙️ Implementation

### 🐍 Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
ToDoListManager/
├── main.py             # main program logic (console application)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### ▶️ How to Run
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
```bash
	python3 main.py
```

### 📚 Libraries Used

- 

## 👥 Team & Contributions

# BIT PTD-26

| Name       | Contribution |
|------------|--------------|
| Milos Dumitrovic     |              |
| Julian Zurkinden    |              |
| Fabio Rubin     |              |
| Mateja Dimitrijevic     |              |
