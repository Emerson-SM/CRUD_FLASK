# Full-Stack User Management System (CRUD)

A web application for managing user records through a RESTful API built with Flask and SQLAlchemy. The project follows a modular architecture using Flask Blueprints and provides a responsive frontend for performing Create, Read, Update, and Delete (CRUD) operations.

## Overview

This application allows users to be created, viewed, updated, and deleted through a browser-based interface. The frontend communicates asynchronously with the backend using the Fetch API, providing a smooth user experience without full page reloads.

## Features

* Full CRUD operations for user management
* RESTful API built with Flask
* Modular architecture using Flask Blueprints
* Database management with Flask-SQLAlchemy
* Password hashing and verification using Werkzeug
* Environment variable configuration with Python-Dotenv
* Responsive user interface built with Bootstrap 5
* Asynchronous communication using the Fetch API

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript (ES6+)
* Bootstrap 5 / Bootswatch

### Backend

* Python 3
* Flask
* Flask-SQLAlchemy
* PyMySQL
* Python-Dotenv
* Werkzeug

### Database

* MySQL

---

## Project Structure

```text
app/
├── database/
│   ├── db.py
│   └── models/
├── routes/
├── static/
│   ├── css/
│   └── js/
├── templates/
└── __init__.py

run.py
requirements.txt
README.md
.env
```

---

## Installation

### Prerequisites

* Python 3.x
* MySQL Server
* Git (optional)

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

macOS/Linux:

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

Windows (Command Prompt):

```bash
venv\Scripts\activate
```

Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root directory:

```env
DATABASE_URL=mysql+pymysql://YOUR_MYSQL_USER:YOUR_MYSQL_PASSWORD@localhost:3306/YOUR_DATABASE_NAME
```

---

## Running the Application

Make sure your MySQL server is running and that the database specified in your `.env` file already exists.

Start the application:

```bash
python run.py
```

When the application starts, Flask-SQLAlchemy will create the required tables if they do not already exist.

Open your browser and navigate to:

```text
http://127.0.0.1:5000/
```

---

## Security Features

* Passwords are never stored in plain text.
* Password hashing is handled using Werkzeug.
* Database credentials are stored in environment variables through `.env`.
* Transaction rollbacks are used to maintain database integrity when errors occur.

---

## Future Improvements

* User authentication and authorization
* User roles and permissions
* Automated testing
* Docker containerization
* Application deployment
* Pagination and search functionality

---

## License

This project is available for educational and portfolio purposes.
