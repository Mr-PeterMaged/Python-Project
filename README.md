# Task Manager Project

#### Video Demo: <URL HERE>

#### Description:
This Task Manager project allows users to add, view, and mark tasks as completed using a simple command-line interface. The tasks are stored in a JSON file, providing persistence between program runs. The program provides the following functionalities:

1. **Add a Task**: Users can input a task description along with an optional deadline. The task is then saved to a JSON file.
2. **View Tasks**: Users can see all tasks in a numbered list. Each task is displayed with its description, deadline (if provided), and status (completed or not).
3. **Complete a Task**: Users can mark a task as completed by selecting the task number. The status of the task is updated, and the task will be shown with a checkmark symbol.
4. **Exit**: The user can save all changes to the JSON file and exit the program.

### File Descriptions:
- **`task_manager.py`**: This is the main script for the task manager. It contains all the logic for managing tasks, including adding, viewing, and completing tasks. The tasks are loaded from and saved to a JSON file named `tasks.json`.
- **`tasks.json`**: This is a JSON file where tasks are stored. Each task includes a description, an optional deadline, and a completion status. The tasks are saved as a list of dictionaries in JSON format.

### Functionality Walkthrough:
- **Loading Tasks**: Upon starting the program, the tasks are loaded from the `tasks.json` file, ensuring that any previously added tasks persist.
- **Adding a Task**: The program prompts the user for a description and an optional deadline for a new task. This task is appended to the list of tasks.
- **Viewing Tasks**: Users can view all current tasks, along with their deadlines and completion statuses. The tasks are displayed in a clean, numbered list.
- **Completing a Task**: The user is prompted to select a task by number to mark it as completed. A checkmark will indicate that the task has been completed.
- **Exiting the Program**: When the user exits, the current list of tasks is saved back to `tasks.json`, ensuring all changes are stored for future sessions.

### Design Decisions:
- **Data Persistence**: Using JSON allows for easy data storage and retrieval, and it is simple to manage with Python's built-in `json` library.
- **User Interface**: A text-based interface is used to ensure simplicity and usability. The design is minimalistic, focusing on functionality rather than visual complexity.
- **Error Handling**: Basic error handling is implemented, such as checking if the user enters a valid task number when completing a task, or if a task file is missing.

### Future Improvements:
- **Task Priorities**: Allow users to set priorities for tasks, such as "High," "Medium," or "Low."
- **Due Dates**: Include functionality to sort tasks by their due dates and alert users about upcoming deadlines.
- **Graphical User Interface (GUI)**: In future versions, this project could benefit from a graphical interface to make it more interactive and visually appealing.

### Conclusion:
This project is a practical and efficient way to manage tasks, offering the core functionalities needed for a task manager while being simple and user-friendly. It is a great starting point for further enhancements and a useful tool for organizing tasks.

