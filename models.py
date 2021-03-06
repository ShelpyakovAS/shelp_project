class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)


class Teacher(User):
    pass


class Student(User):
    pass


class Category:
    add_id = 0

    def __init__(self, name):
        self.category_id = Category.add_id
        Category.add_id += 1
        self.name = name


class Course:

    def __init__(self, name, category, sub_course):
        self.name = name
        self.category = category
        self.sub_courses = sub_course
        self.students = []
        self.teachers = []

    def add_del_user(self, user, user_type, change_type):
        if change_type == 'del':
            if user in self.students or user in self.teachers:
                if user_type == 'student':
                    self.students.remove(user)
                else:
                    self.teachers.remove(user)
        if change_type == 'add':
            if user_type == 'student':
                self.students.append(user)
            else:
                self.teachers.append(user)

    def change_self(self, course_name, category, change_sub_courses_type, sub_course, courses):
        if course_name != '':
            self.name = course_name
        self_course = self
        for course in courses:
            course.change_sub_courses(self_course, change_sub_courses_type, sub_course)
        if category == None:
            return
        self.category = category

    def change_sub_courses(self, self_course, change_sub_courses_type, sub_course):
        change_type = {
            'no-change': self.no_change,
            'add-child': self.add_child,
            'add-parent': self.add_parent,
            'del-child': self.del_child,
            'del-parent': self.del_parent
        }
        change_type[change_sub_courses_type](self_course, sub_course)

    def no_change(self, self_course, sub_course):
        pass

    def add_child(self, self_course, sub_course):
        print(f'СМОТРИМ СЮДА {self.sub_courses} {self_course.sub_courses} {sub_course.sub_courses}')
        if self == self_course:
            self.sub_courses.children.append(sub_course)
        elif self == sub_course:
            self.sub_courses.parents.append(self_course)

    def add_parent(self, self_course, sub_course):
        if self == self_course:
            self.sub_courses.parents.append(sub_course)
        elif self == sub_course:
            self.sub_courses.children.append(self_course)

    def del_child(self, self_course, sub_course):
        if self == self_course:
            self.sub_courses.children.remove(sub_course)
        elif self == sub_course:
            self.sub_courses.parents.remove(self_course)

    def del_parent(self, self_course, sub_course):
        if self == self_course:
            self.sub_courses.parents.remove(sub_course)
        elif self == sub_course:
            self.sub_courses.children.remove(self_course)


class SubCourse:
    def __init__(self):
        self.parents = []
        self.children = []

    @staticmethod
    def parent(course, courses):
        pass

    @staticmethod
    def child(course, courses):
        pass

    @staticmethod
    def del_parent(course, courses):
        pass

    @staticmethod
    def del_child(course, courses):
        pass


class ShelpSite:

    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.courses_category = []
        self.user_types = {
            'teacher': [self.teachers, Teacher],
            'student': [self.students, Student],
        }

    def create_user(self, name, surname, age, user_type):
        self.user_types[user_type][0].append(self.user_types[user_type][1](name, surname, age))

    def create_category(self, name):
        for category in self.courses_category:
            if self.courses_category:
                if name == category.name:
                    print("Данное имя категории уже существует!")
                    return
        self.courses_category.append(Category(name))
        print(f'Категория - {name}, успешно создана!')

    @staticmethod
    def create_sub_courses(course, sub_type):
        sub_courses = SubCourse()
        if sub_type == 'parent':
            sub_courses.parents.append(course)
        else:
            sub_courses.children.append(course)
        return sub_courses

    @staticmethod
    def create_empty_sub_courses():
        sub_courses = SubCourse()
        return sub_courses

    def create_course(self, name, category_name, sub_courses):
        for course in self.courses:
            if name == course.name:
                print("Данное имя курса уже занято!")
                return
        if sub_courses.children != [] or sub_courses.parents != []:
            for sub_course in sub_courses.children:
                for course in self.courses:
                    if sub_course.name == course.name:
                        course.sub_courses.parents.append(sub_course)
            for sub_course in sub_courses.parents:
                for course in self.courses:
                    if sub_course.name == course.name:
                        course.sub_courses.children.append(course)
        if self.courses_category:
            for category in self.courses_category:
                if category.name == category_name:
                    self.courses.append(Course(name, category, sub_courses))
                    return
        print("Такой категории курса не существут!")

    def take_category(self, category_name):
        if self.courses_category:
            for category in self.courses_category:
                if category.name == category_name:
                    return category

    def take_course(self, course_name):
        if self.courses:
            for course in self.courses:
                if course.name == course_name:
                    return course

    def take_user(self, name, surname):
        for user in self.students:
            if user.name == name and user.surname == surname:
                return user, 'student'
        for user in self.teachers:
            if user.name == name and user.surname == surname:
                return user, 'teacher'

