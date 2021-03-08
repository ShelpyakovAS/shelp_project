import sqlite3
from models import Teacher, Student, Course, SubCourse, Category

sdb_connection = sqlite3.connect('shelp_base.db')


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
    @staticmethod
    def take_tablename_variables_values(obj):
        table_name = obj.__class__.__name__.lower() + 's'
        obj_list_variables = list(obj.__dict__.keys())
        obj_list_values = list(obj.__dict__.values())
        obj_variables = ""
        obj_values = ""
        for variable in obj_list_variables:
            if variable == obj_list_variables[-1]:
                obj_variables += f'{variable}'
            else:
                obj_variables += f'{variable}, '
        for values in obj_list_values:
            if type(values) == str:
                values = f"'{values}'"
            if values == obj_list_values[-1]:
                obj_values += f'{values}'
            else:
                obj_values += f'{values}, '
        return table_name, obj_variables, obj_values

    def __init__(self, sdb_connection):
        self.sdb_connection = sdb_connection
        self.cursor = sdb_connection.cursor()
        self.table_dict = {
            'students': Student,
            'teachers': Teacher
        }

    def __call__(self):
        users = {}
        for table in self.table_dict.keys():
            statement = f'SELECT * from {table}'
            self.cursor.execute(statement)
            result = []
            for item in self.cursor.fetchall():
                item_id = item[0]
                item.remove(item[0])
                object = self.table_dict[table](*item)
                object.id = item_id
                result.append(object)
            users.update({table: result})
        return users

    def insert(self, obj):
        table_name, obj_variables, obj_values = UsersMapper.take_tablename_variables_values(obj)
        statement = f"INSERT INTO {table_name} ({obj_variables}) VALUES ({obj_values})\n"
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

    def __call__(self):
        categories = []
        statement = f'SELECT * from categories'
        self.cursor.execute(statement)
        for item in self.cursor.fetchall():
            item_id = item[0]
            item.remove(item[0])
            object = Category(*item)
            object.id = item_id
            categories.append(object)
        return categories

    def insert(self, obj):
        table_name, obj_variables, obj_values = UsersMapper.take_tablename_variables_values(obj)
        statement = f"INSERT INTO {table_name} ({obj_variables}) VALUES ({obj_values})\n"
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


class CourseMapper:
    pass