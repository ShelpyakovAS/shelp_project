class Category:
    add_id = 0

    def __init__(self, name):
        self.category_id = Category.add_id
        Category.add_id += 1
        self.name = name


class Course:
    def __init__(self, name, category, sub_courses):
        self.name = name
        self.category = category
        self.sub_courses = sub_courses


class SubCourses:
    def __init__(self):
        self.parents = []
        self.children = []


class ShelpSite:
    def __init__(self):
        self.courses = []
        self.courses_category = []

    def create_category(self, name):
        for category in self.courses_category:
            if self.courses_category:
                if name == category.name:
                    print("Данное имя категории уже существует!")
                    return
        self.courses_category.append(Category(name))
        print(f'Категория - {name}, успешно создана!')

    @staticmethod
    def create_sub_courses(course_name, sub_type):
        sub_courses = SubCourses()
        if sub_type == 'parents':
            sub_courses.parents.append(course_name)
        else:
            sub_courses.children.append(course_name)
        return sub_courses

    def create_course(self, name, category_name, sub_courses=SubCourses()):
        for course in self.courses:
            if name == course.name:
                print("Данное имя курса уже занято!")
                return
        if sub_courses.children != [] or sub_courses.parents != []:
                for course_name in sub_courses.children:
                    for course in self.courses:
                        if course_name == course.name:
                            course.sub_courses.children.append(course_name)
                for course_name in sub_courses.parents:
                    for course in self.courses:
                        if course_name == course.name:
                            course.sub_courses.parents.append(course_name)
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



