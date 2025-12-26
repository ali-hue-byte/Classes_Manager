# Class_Manager


## Detailed Description
This project is a work in progress.

Features included in this prototype:

- Modern UI built with PySide6 (Qt Designer)
- Animated transitions between the login and create account screens
- Login screen with username and password fields, including input validation
- Create account screen with username and password fields, including password strength checking
- Smooth UI animations for widgets sliding in and out
- Automatic navigation to the main application window after successful login
- Secure password storage using a salted hash
- Student information stored separatly for each user
- All stored student data is protected using encryption based on a Key Derivation Function (KDF)
  
---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ali-hue-byte/Class_Manager.git
cd Class_Manager
```
2. Install the required dependencies:

```bash
pip install PySide6
pip install cryptography
```
3. Run the main application:

```bash
python Student_Management.py
```

--- 

## Files

- **Student_Management.py** – The main Python file used to run the application.
- **App.py** – The Python file generated from Qt Designer that contains all the UI widgets and layouts.
- **Functions.py** - Python file containing helper functions for user authentication, password hashing, validation, and user data management used throughout the app.

## Screenshots 

<img width="1974" height="1131" alt="image" src="https://github.com/user-attachments/assets/59d6bd7c-fd31-49b6-a881-f91c83d0fa5b" />


