PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS students;
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
name VARCHAR (32),
surname VARCHAR (32),
age INTEGER NOT NULL
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
name VARCHAR (32),
surname VARCHAR (32),
age INTEGER NOT NULL
);

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
name VARCHAR (32)
);

DROP TABLE IF EXISTS courses;
CREATE TABLE courses (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
name VARCHAR (32),
category_id INTEGER NOT NULL,
FOREIGN KEY (category_id) references categories(id)
);

DROP TABLE IF EXISTS curses_teachers;
CREATE TABLE curses_teachers (
course_id INTEGER NOT NULL,
teacher_id INTEGER NOT NULL,
FOREIGN KEY (course_id) references courses(id),
FOREIGN KEY (teacher_id) references teachers(id)
);

DROP TABLE IF EXISTS curses_students;
CREATE TABLE curses_students (
course_id INTEGER NOT NULL,
students_id INTEGER NOT NULL,
FOREIGN KEY (course_id) references courses(id),
FOREIGN KEY (students_id) references students(id)
);

DROP TABLE IF EXISTS subcourses;
CREATE TABLE subcourses (
parent_id INTEGER NOT NULL,
child_id INTEGER NOT NULL,
FOREIGN KEY (parent_id) references courses(id),
FOREIGN KEY (child_id) references courses(id)
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
