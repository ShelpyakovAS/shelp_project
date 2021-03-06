import sqlite3
from models import Teacher, Student, Course, SubCourse, Category

sdb_connection = sqlite3.connect('shelp_base.db')

test_stubent = Student('вася', 'пупкин', 33)
test_teacher = Teacher('не вася', ' не пупкин', 34)
test_сategory = Category('имя категории')
test_subcourse = SubCourse()
test_course = Course('имя курса', test_сategory, test_subcourse)


class CreatyBase:

    def __init__(self):
        self.sdb_connection = sdb_connection
        self.cursor = sdb_connection.cursor()
        self.table_dict = {
            'students': Student,
            'teachers': Teacher,
            'categorys': Category,
            'courses': Course,
            'subcourses': SubCourse
        }

    def __call__(self):
        statement = f'DROP TABLE IF EXISTS students'
        self.cursor.execute(statement)
        statement = f'CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, name VARCHAR (32))' \
                    f'age NUMBER'
        self.cursor.execute(statement)