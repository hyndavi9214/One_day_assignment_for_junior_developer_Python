# Task Manager CLI Application

## Project Description
The Task Manager CLI Application is a simple, user-friendly command-line interface (CLI) program that enables users to manage their tasks efficiently. It supports functionalities such as adding new tasks, viewing all tasks, deleting tasks, and marking tasks as complete. The application ensures data persistence by saving tasks to a JSON file (`tasks.json`) and loading them when the application starts.

## Features
- **Add Task**: Add a new task to the task list with a unique ID and title.
- **View Tasks**: Display all tasks along with their IDs, titles, and completion status (Pending or Completed).
- **Delete Task**: Remove a task from the list by entering its ID.
- **Complete Task**: Mark a task as completed by entering its ID.
- **Save/Load Tasks**: Save tasks to a JSON file (`tasks.json`) and load them automatically when the application starts.

## Prerequisites
- Python 3.6 or later must be installed on your machine.

## Setup Instructions
1. Clone the repository or download the project files to your local machine.
2. Navigate to the project directory (`task_manager`) using the terminal or command prompt.

## How to Run the Application
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `task_manager.py` file.
3. Run the application using the following command:
   ```bash
   python task_manager.py

==> The application will display a menu with the following options:
Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Complete Task
5. Exit
Choose an option:

==> Enter the number corresponding to the action you want to perform, and follow the prompts.

## Example Menu Usage
=> Add Task: Enter a task title. A new task is added with a "Pending" status.
=> View Tasks: Displays all tasks with their IDs, titles, and statuses.
=> Delete Task: Enter a task ID to delete the task if the ID is valid.
=> Complete Task: Enter a task ID to mark it as complete if the ID is valid.
=> Exit: Saves tasks to tasks.json and exits the application.

## Code Overview
## Task Class
# Attributes:
    => id: Unique identifier for each task.
    => title: Task description.
    => completed: Boolean indicating if the task is completed (True or False).

## Functions
=> add_task(tasks, title): Adds a new task to the list.
=> view_tasks(tasks): Displays tasks with their ID, title, and status.
=> delete_task(tasks, task_id): Deletes a task based on its ID.
=> complete_task(tasks, task_id): Marks a task as completed.
=> save_tasks(tasks, filename='tasks.json'): Saves tasks to a JSON file.
=> load_tasks(filename='tasks.json'): Loads tasks from a JSON file.

## CLI Loop
=> Displays the menu and waits for user input to perform actions like adding, viewing, deleting, and completing tasks.
=> Saves tasks before exiting the application.

## File Handling
=> Save Tasks: The save_tasks() function converts tasks to a JSON-compatible format and writes them to tasks.json.
=> Load Tasks: The load_tasks() function reads data from tasks.json and reconstructs the task list. If the file is not found, it initializes an empty list.

## Troubleshooting
=> Task ID Issues: Ensure the task ID is numeric; otherwise, an error message will be displayed.
=> File Not Found: If tasks.json is missing, an empty task list will be initialized, and the file will be created upon saving.