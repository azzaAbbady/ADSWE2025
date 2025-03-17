# HR Management System

A simple Human Resources (HR) management system built with Django. This app allows you to manage departments and employees, including adding, editing, and viewing their details.

---

## Features

1. **Department Management**:
   - Add new departments.
   - Edit existing departments.
   - View a list of all departments.

2. **Employee Management**:
   - Add new employees.
   - Edit existing employees.
   - View a list of all employees.

3. **User-Friendly Interface**:
   - Responsive design using **Bootstrap**.
   - Clean and intuitive forms for adding/editing data.
   - Interactive tables for displaying departments and employees.

4. **Admin Panel**:
   - Use Django's built-in admin interface to manage departments and employees.
   - Accessible at `/admin/`.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)
- Django 4.x

---

## How to Run the Project

Follow these steps to set up and run the HR Management System on your local machine.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/hr-management-system.git
cd hr-management-system
```
### Step 2: Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```
### Step 3: Apply Migrations
Run the following commands to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```
### Step 4: Create a Superuser
Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```
Follow the prompts to set up your username, email, and password.

### Step 5: Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
### Step 6: Access the Application
-   Open your browser and go to http://127.0.0.1:8000/.
-   Use the navigation bar to access:
        Departments: http://127.0.0.1:8000/hr/departments/
        Employees: http://127.0.0.1:8000/hr/employees/

-   Access the admin panel at http://127.0.0.1:8000/admin/ and log in with your superuser credentials.
