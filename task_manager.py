import json

# Task class to represent each task with ID, title, and completion status
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id          # Unique ID for each task
        self.title = title         # Title or description of the task
        self.completed = completed # Boolean indicating if the task is completed

# Function to add a new task
def add_task(tasks, title):
    task_id = len(tasks) + 1     # Generate a new ID based on the number of tasks
    new_task = Task(task_id, title) # Create a new Task object
    tasks.append(new_task)        # Add the new task to the list

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:                 # Check if there are any tasks in the list
        print("No tasks available.")
        return
    for task in tasks:            # Loop through each task in the list
        status = "Completed" if task.completed else "Pending" # Determine task status
        print(f"ID: {task.id}, Title: {task.title}, Status: {status}")

# Function to delete a task by its ID
def delete_task(tasks, task_id):
    for task in tasks:            # Search for the task with the given ID
        if task.id == task_id:
            tasks.remove(task)    # Remove the task from the list if found
            print(f"Task ID {task_id} deleted.")
            return
    print(f"Task ID {task_id} not found.") # Print a message if task ID is not found

# Function to mark a task as complete by its ID
def complete_task(tasks, task_id):
    for task in tasks:            # Search for the task with the given ID
        if task.id == task_id:
            task.completed = True # Mark the task as completed
            print(f"Task ID {task_id} marked as completed.")
            return
    print(f"Task ID {task_id} not found.") # Print a message if task ID is not found

# Function to save tasks to a JSON file
def save_tasks(tasks, filename='tasks.json'):
    # Convert each task object to a dictionary and save as a JSON file
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

# Function to load tasks from a JSON file
def load_tasks(filename='tasks.json'):
    tasks = []
    try:
        # Open the JSON file and load the tasks data
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            # Reconstruct each task from the loaded data
            for data in tasks_data:
                task = Task(data['id'], data['title'], data['completed'])
                tasks.append(task)
    except FileNotFoundError:
        # If the file does not exist, start with an empty task list
        print("No saved tasks found. Starting with an empty task list.")
    return tasks

# Main function to run the CLI application
def main():
    tasks = load_tasks()          # Load existing tasks from the file at startup
    while True:                   # Infinite loop to keep the CLI running
        # Display the menu options
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        # Handle user input and call the corresponding functions
        if choice == '1':
            title = input("Enter task title: ")
            add_task(tasks, title)
            print("Task added successfully.")
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(tasks, task_id)
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")
        elif choice == '5':
            save_tasks(tasks)     # Save tasks before exiting the application
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option, please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
