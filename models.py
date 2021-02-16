class Category:
    add_id = 0

    def __init__(self, name):
        self.category_id = Category.add_id
        Category.add_id += 1
        self.name = name


class Course:
    def __init__(self, name, category):
        self.name = name
        self.category = category


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

    def create_course(self, name, category_name):
        for course in self.courses:
            if name == course.name:
                print("Данное имя курса уже занято!")
                return
        if self.courses_category:
            print("Я ТУТ")
            for category in self.courses_category:
                print("Я ТУТ")
                print(category.name)
                print(type(category.name))
                print(category_name)
                print(type(category_name))
                print(category.name == category_name)
                if category.name == category_name:
                    print("Я ТУТ")
                    self.courses.append(Course(name, category))
                    return
        print("Такой категории курса не существут!")

    def take_category(self, category_name):
        if self.courses_category:
            for category in self.courses_category:
                if category.name == category_name:
                    return category



