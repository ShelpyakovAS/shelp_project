import sqlite3

sdb_connection = sqlite3.connect('shelp_base.db')

class CreatyBase:

    def __init__(self):
        self.sdb_connection = sdb_connection
        self.cursor = sdb_connection.cursor()

    def __call__(self):
        statement = f'PRAGMA foreign_keys = on'
        self.cursor.execute(statement)

        statement = f'DROP TABLE IF EXISTS students'
        self.cursor.execute(statement)
        statement = f'CREATE TABLE students (' \
                    f'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, ' \
                    f'name VARCHAR (32), ' \
                    f'surname VARCHAR (32), ' \
                    f'age INTEGER NOT NULL)'
        self.cursor.execute(statement)

        statement = f'DROP TABLE IF EXISTS teachers'
        self.cursor.execute(statement)
        statement = f'CREATE TABLE teachers (' \
                    f'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, ' \
                    f'name VARCHAR (32), ' \
                    f'surname VARCHAR (32), ' \
                    f'age INTEGER NOT NULL)'
        self.cursor.execute(statement)

        statement = f'DROP TABLE IF EXISTS categories'
        self.cursor.execute(statement)
        statement = f'CREATE TABLE categories (' \
                    f'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, ' \
                    f'name VARCHAR (32))'
        self.cursor.execute(statement)

        statement = f'DROP TABLE IF EXISTS courses'
        self.cursor.execute(statement)
        statement = f'CREATE TABLE courses (' \
                    f'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, ' \
                    f'name VARCHAR (32), ' \
                    f'category_id INTEGER PRIMARY KEY, ' \
                    f'FOREIGN KEY (category_id) references categories(id))'
        self.cursor.execute(statement)

        statement = f'DROP TABLE IF EXISTS curses_teachers'
        self.cursor.execute(statement)

        statement = f'CREATE TABLE curses_teachers (' \
                    f'course_id INTEGER PRIMARY KEY, ' \
                    f'teacher_id INTEGER PRIMARY KEY' \
                    f'FOREIGN KEY (course_id) references courses(id)' \
                    f'FOREIGN KEY (teacher_id) references teachers(id))'
        self.cursor.execute(statement)

        statement = f'DROP TABLE IF EXISTS curses_students'
        self.cursor.execute(statement)

        statement = f'CREATE TABLE curses_teachers (' \
                    f'course_id INTEGER PRIMARY KEY, ' \
                    f'students_id INTEGER PRIMARY KEY' \
                    f'FOREIGN KEY (course_id) references courses(id)' \
                    f'FOREIGN KEY (students_id) references students(id))'
        self.cursor.execute(statement)

        statement = f'DROP TABLE IF EXISTS subcourses'
        self.cursor.execute(statement)

        statement = f'CREATE TABLE subcourses (' \
                    f'parent_id INTEGER PRIMARY KEY, ' \
                    f'child_id INTEGER PRIMARY KEY' \
                    f'FOREIGN KEY (parent_id) references courses(id)' \
                    f'FOREIGN KEY (child_id) references courses(id))'
        self.cursor.execute(statement)

CreatyBase()

