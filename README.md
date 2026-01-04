# Class_Manager


## Detailed Description
This project is a modern, user-friendly Student Management System built with PySide6 and Qt Designer, designed to simplify student management for teachers and facilitate data visualization. It provides a clean, interactive interface with smooth animations and real-time updates, allowing users to easily manage students, classes, grades, attendance, and statistics. The system ensures data security with encryption while offering dynamic visualizations and intuitive navigation across all screens.

- Modern UI built with PySide6 
- Animated transitions between the login and create account screens
- Login screen with username and password fields, including input validation
- Create account screen with username and password fields, including password strength checking
- Smooth UI animations for widgets sliding in and out
- Automatic navigation to the main application window after successful login
- Student information stored separatly for each user
- All stored student data is protected using encryption based on a Key Derivation Function (KDF)
- Dynamic, interconnected tables that automatically update classes, subjects, students, and grades in real time
- **Students Information page**- View, manage and edit students details
- **Adding Classes**-View, creat and edit new Classes
- **Grades Page**-Add, delete subjects and students grades
- **Attendance Page**-Mark, edit, and track student attendance with clear status indicators and real-time updates
- **Statistics Page** – A page for visualizing student data such as grades, attendance and gender distribution using matplotlib for graphs (with animations on hover) and highlighting top-performing students (real-time updates)
- **Data storage** – Uses SQLite for student data and pickles for user information (passwords are never stored in raw form).

---

### Upcoming Features

- Change Student's Class – Allows updating a student’s class assignment in the database.
- Configurable maximum marks: teachers can set the maximum score.


  
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
pip install matplotlib
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
- **data.pkl** - Binary storage file (Pickle) used to persist application data (students, classes, marks, attendance records).
- **users.pkl** - Binary storage file (Pickle) containing user authentication data, including unique per-user salts and salted password hashes.

## Screenshots 

<img width="1974" height="1131" alt="image" src="https://github.com/user-attachments/assets/59d6bd7c-fd31-49b6-a881-f91c83d0fa5b" />
<img width="1975" height="1178" alt="image" src="https://github.com/user-attachments/assets/d4ca972e-ed91-4694-9509-2d01136fe3a8" />
<img width="1980" height="1171" alt="Screenshot 2025-12-28 225644" src="https://github.com/user-attachments/assets/1bd6f18c-98bd-47f3-83fe-26a2e6bab5da" />
<img width="1973" height="1169" alt="image" src="https://github.com/user-attachments/assets/57d541f3-81f0-45e1-a5b6-d65fdd39a9ea" />



