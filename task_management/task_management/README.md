# My Django Project

This is a Django web application that allows users to manage tasks and their profiles. It includes features like user authentication, task creation, task updates, and profile management.

## Features

- User registration, login, and logout
- Create, update, and delete tasks
- User profile management (update profile, delete account)
- Web Style by Bootstrap4 and some custom css styles
- Django admin interface for managing users and tasks

## Technologies Used

- **Django 5.1.1** - Web framework
- **Python** - Backend programming language
- **Mysql** - database management
- **Custom CSS, Bootstrap** - For unique styling
- **HTML5** - For templates
- **JavaScript** - For client-side interactions

## Installation

### Prerequisites

- Python 
- Django 5.1.1
- A virtual environment tool (`venv`)
- djangorestframework
- mysqlclient

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Zerro2003/the_tasker.git


### Purposes:

Each **setup instruction** is telling what to do and why it's necessary. 

- Cloning: Copies the project code to your machine.
- Virtual environment: Isolates dependencies.
- Installing dependencies: Makes sure your project has the libraries it needs to function.
- Migrations: Sets up your database tables based on models.
- Superuser: Gives you access to Django’s powerful admin interface for managing users.
- Running the server: Allows you to run the project locally and test it.

---

## Usage

### Task Management

1. **Create a Task:**
   - Go to the "Create Task" page to add new tasks to your list.
   
2. **View and Update Tasks:**
   - Navigate to the "View Tasks" page to see all tasks and edit them as needed.

3. **Delete a Task:**
   - On the task view page, use the delete option to remove a task.

### User Profile

1. **View Profile:**
   - Go to the "Profile" page to view your account details.

2. **Update Profile:**
   - Click the "Update Profile" button to change your username or email.

3. **Delete Account:**
   - Use the "Delete Account" button to remove your account from the system.

## API Endpoints (Optional Section if you're using APIs)

This section outlines the API endpoints for interacting with the system programmatically.

- `/api/register/` for registering
- `/api/tasks/create/` for creating new task
- `/api/login/` for logging in the created account
- `/api/homepage/` to land to the home page
- `/api/task/` this is for viewing the created task and track/manage


### challenges and the solutions taken to overcome the erros

---

## Challenges Faced During Development

### 1. User Authentication and Authorization
- **Issue:** Any Unauthorized users could access profile updates and it took long to configure.
- **Solution:** I used Django’s `LoginRequiredMixin` to restrict access.
- **Outcome:** Secured sensitive views, ensuring only authenticated users could access them.

### 2. Customizing Form Error Messages
- **Issue:** Default form error messages were too generic (not very tailored for this application).
- **Solution:** Overrode `error_messages` in forms for clearer feedback.
- **Outcome:** Improved user experience with customized error messages.

### 3. Database Migrations
- **Issue:** Difficulty applying migrations smoothly after model changes.
- **Solution:** Used `makemigrations` and `migrate` commands to sync database.
- **Outcome:** Solved migration issues and learned to carefully plan model updates.

### 4. User Account Deletion
- **Issue:** Ensuring safe and confirmed account deletion.
- **Solution:** Added a confirmation step and used Django’s `delete()` method securely.
- **Outcome:** Prevented accidental deletions and ensured data integrity.

### 5. Development Environment Setup
- **Issue:** Incompatible dependencies and database connection errors.
- **Solution:** Pinned package versions and configured environment settings.
- **Outcome:** Achieved a consistent and stable development environment.

### 6. Filtering and sorting task
- **Issue** Implementing a flexible task filtering system was complex due to the need to filter tasks based on various user inputs (e.g., status,    priority, etc.).
- **Solution** We used Django’s filter() method to chain multiple filters, applying them based on user-provided conditions.
- **Outcome** The filter() method provided a scalable solution, making the filtering system more flexible and easier to maintain.
---


