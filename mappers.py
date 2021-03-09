import sqlite3
import models

sdb_connection = sqlite3.connect('shelp_base.sqlite')


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class UsersMapper:

    def __init__(self, sdb_connection):
        self.sdb_connection = sdb_connection
        self.cursor = sdb_connection.cursor()
        self.table_dict = {
            'students': models.Student,
            'teachers': models.Teacher
        }

    def take_users(self):
        users = {}
        for table in self.table_dict.keys():
            statement = f'SELECT * from {table}'
            try:
                self.cursor.execute(statement)
            except:
                return
            result = []
            print(type(self.cursor.fetchall()))
            if self.cursor.fetchall():
                for item in self.cursor.fetchall():
                    item_id = item[0]
                    item.remove(item[0])
                    object = self.table_dict[table](*item)
                    object.id = item_id
                    result.append(object)
                users.update({table: result})
            else:
                users = {
                    'students': [],
                    'teachers': []
                }
        return users

    def insert(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        statement = f"INSERT INTO {table_name} (name, surname, age) VALUES ({obj.__dict__['name']}, " \
                    f"{obj.__dict__['surname']}, {obj.__dict__['age']})"
        self.cursor.execute(statement, (obj.name,))
        try:
            self.sdb_connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        obj_id = obj.id
        obj_dict = obj.__dict__
        obj_dict.pop('id', None)
        for variable in list(obj_dict.keys()):
            statement = ''
            if type(obj_dict[variable]) == str:
                obj_dict[variable] = f"'{obj_dict[variable]}'"
            statement = statement + f"UPDATE {table_name} SET {variable}={obj_dict[variable]} WHERE id={obj_id}\n"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbUpdateException(e.args)

    def delete(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        obj_id = obj.i
        statement = f"DELETE FROM {table_name} WHERE id={obj_id}"
        self.cursor.execute(statement)
        try:
            self.sdb_connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class CategoriesMapper:
    def __init__(self, sdb_connection):
        self.sdb_connection = sdb_connection
        self.cursor = sdb_connection.cursor()

    def take_categories(self):
        categories = []
        statement = f'SELECT * from categories'
        self.cursor.execute(statement)
        for item in self.cursor.fetchall():
            item_id = item[0]
            item.remove(item[0])
            object = models.Category(*item)
            object.id = item_id
            categories.append(object)
        return categories

    def insert(self, obj):
        statement = f"INSERT INTO categories (name) VALUES ({obj.__dict__['name']})"
        self.cursor.execute(statement, (obj.name,))
        try:
            self.sdb_connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        obj_id = obj.id
        obj_dict = obj.__dict__
        obj_dict.pop('id', None)
        for variable in list(obj_dict.keys()):
            statement = ''
            if type(obj_dict[variable]) == str:
                obj_dict[variable] = f"'{obj_dict[variable]}'"
            statement = statement + f"UPDATE {table_name} SET {variable}={obj_dict[variable]} WHERE id={obj_id}\n"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbUpdateException(e.args)

    def delete(self, obj):
        table_name = obj.__class__.__name__.lower() + 's'
        obj_id = obj.i
        statement = f"DELETE FROM {table_name} WHERE id={obj_id}"
        self.cursor.execute(statement)
        try:
            self.sdb_connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class CoursesMapper:

    def __init__(self, sdb_connection):
        self.sdb_connection = sdb_connection
        self.cursor = sdb_connection.cursor()

    def take_courses(self):
        courses = []
        statement = f'SELECT * from courses'
        self.cursor.execute(statement)
        for item in self.cursor.fetchall():
            item_id = item[0]
            item.remove(item[0])

            statement = f'SELECT child_id from subcourses where parent_id={item_id}'
            self.cursor.execute(statement)
            sub_course_children = []
            for item in self.cursor.fetchall():
                sub_course_children.append(item)

            statement = f'SELECT parent_id from subcourses where child_id={item_id}'
            self.cursor.execute(statement)
            sub_course_parents = []
            for item in self.cursor.fetchall():
                sub_course_parents.append(item)

            sub_course = models.SubCourse()
            sub_course.children_id = sub_course_children
            sub_course.parents_id = sub_course_parents
            object = models.Course(*item, sub_course)
            object.id = item_id
            courses.append(object)
        return courses

    def insert(self, obj):
        category_id = obj.category.id
        obj_id = obj.id
        statement = f"INSERT INTO courses (name, category_id) VALUES ({obj.__dict__['name']}, {category_id})"
        self.cursor.execute(statement, (obj.name,))
        try:
            self.sdb_connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

        for parent_id in obj.parents_id:
            statement = f"INSERT INTO subcourses (parent_id, child_id) VALUES ({parent_id}, {obj_id})"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)
        for child_id in obj.children_id:
            statement = f"INSERT INTO subcourses (parent_id, child_id) VALUES ({obj_id}, {child_id})"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)

    def update(self, obj):
        obj_id = obj.id
        obj_dict = obj.__dict__
        statement = f"UPDATE courses SET name={obj_dict['name']} WHERE id={obj_id}\n" \
                    f"UPDATE courses SET category_id={obj_dict['category']} WHERE id={obj_id}\n"
        self.cursor.execute(statement)
        try:
            self.sdb_connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

        for parent_id in obj.parents_id:
            statement = f"INSERT INTO subcourses (parent_id, child_id) VALUES ({parent_id}, {obj_id})"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)
        for child_id in obj.children_id:
            statement = f"INSERT INTO subcourses (parent_id, child_id) VALUES ({obj_id}, {child_id})"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)

    def delete(self, obj):
        for parent_id in obj.parents_id:
            statement = f"DELETE FROM subcourses child_id where parent_id={parent_id})"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)
        for child_id in obj.children_id:
            statement = f"DELETE FROM subcourses parent_id where child_id={child_id})"
            self.cursor.execute(statement)
            try:
                self.sdb_connection.commit()
            except Exception as e:
                raise DbCommitException(e.args)

        obj_id = obj.i
        statement = f"DELETE FROM curses WHERE id={obj_id}"
        self.cursor.execute(statement)
        try:
            self.sdb_connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class MapperRegistry:
    mappers = {
        'student': UsersMapper,
        'techer': UsersMapper,
        'category': CategoriesMapper,
        'course': CoursesMapper
    }

    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, models.Student):
            return UsersMapper(sdb_connection)
        if isinstance(obj, models.Teacher):
            return UsersMapper(sdb_connection)
        if isinstance(obj, models.Category):
            return CategoriesMapper(sdb_connection)
        if isinstance(obj, models.Course):
            return CoursesMapper(sdb_connection)

    @staticmethod
    def get_current_mapper(name):
        return MapperRegistry.mappers[name](sdb_connection)


a = UsersMapper(sdb_connection)

s = models.Student('вася', 'пупкин', 52)
a.insert(s)

