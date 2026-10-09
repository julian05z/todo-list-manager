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

#### 🛡️ User Story 1 – Data Validation

**As a** student,
**I want** the ToDo List Manager to validate the data I enter when creating a task,
**so that** I can avoid saving tasks with incorrect or incomplete data.

**✔️ Acceptance Criteria 1**
- *Given* a student is creating or editing a task and enters a task description and a deadline,
- *When* the student enters an empty description or an invalid date format,
- *Then* the system rejects the input and prompts the student to enter valid data.

**✔️ Acceptance Criteria 2**
- *Given* a student is creating or editing a task,
- *When* the student enters a valid description and a valid deadline,
- *Then* the system accepts the task and saves it.

---

#### 🚦 User Story 2 – Priority

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

#### 🔎 User Story 3 – Filter

**As a** student,
**I want** to filter my existing tasks by criteria such as priority or completion status,
**so that** I can quickly find the tasks that are important to me.

**✔️ Acceptance Criteria 1**
- *Given* the task list contains two completed tasks and three incomplete tasks,
- *When* the student filters the list by "Incomplete",
- *Then* only the three incomplete tasks are displayed.

**✔️ Acceptance Criteria 2**
- *Given* the task list contains tasks with "High", "Medium", and "Low" priority,
- *When* the student filters the list by "High",
- *Then* only the tasks with "High" priority are displayed.

---

#### ➕ User Story 4 – 

**As a** ,
**I want** ,
**so that** .

**✔️ Acceptance Criteria 1**
- *Given* ,
- *When* ,
- *Then* .

**✔️ Acceptance Criteria 2**
- *Given* ,
- *When* ,
- *Then* .

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

| Name       | Contribution |
|------------|--------------|
|            |              |
|            |              |
|            |              |

## 🤝 Contributing

- Use this repository as a starting point by importing it into your own GitHub account.
- Work only within your own copy — do not push to the original template.
- Commit regularly to track your progress.

## 📜 License

This project is provided for **educational use only** as part of the Programming Foundations module.
[MIT License](LICENSE)
