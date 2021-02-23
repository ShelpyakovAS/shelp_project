from shelp_framework.templates import render
from logging_app import Logger, debug


logger = Logger('views')


@debug
class Index:

    def __call__(self, request):
        return '200 OK', render('index.html', secret=request)


class Courses:

    def __call__(self, request):
        return '200 OK', render('curses.html', secret=request)


class About:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                title = data['title']
                text = data['text']
                email = data['email']
                logger.log(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('about.html', secret=request)


class Other:

    def __call__(self, request):
        return '200 OK', render('other.html', secret=request)


class ControlPanel:

    def __call__(self, request):
        return '200 OK', render('base-control-panel.html', secret=request)


class CreateCategory:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                name = data['category-name']
                request["site"].create_category(name)
                logger.log(request["site"].courses_category)
        return '200 OK', render('create-category.html', secret=request)


class CreateCurse:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                name = data['course-name']
                category = data['category']
                creation_type = data['creation-type']
                if creation_type == 'new':
                    sub_courses = request['site'].create_empty_sub_courses()
                    request["site"].create_course(name, category, sub_courses)
                else:
                    sub_courses = request["site"].create_sub_courses(request['site'].take_course(data['sub-course']),
                                                                     data['creation-type'])
                    request["site"].create_course(name, category, sub_courses)
        logger.log(f'{request["site"].courses} - ЭТО КУРСЫ')
        return '200 OK', render('create-curse.html', secret=request)


class CreateUser:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                user_name = data['user-name']
                user_surname = data['user-surname']
                user_age = data['user-age']
                creation_type = data['creation-type']
            request["site"].create_user(user_name, user_surname, user_age, creation_type)
        return '200 OK', render('create-user.html', secret=request)


class ChangeCourse:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                course_name = data['course-name']
                new_course_name = data['new-course-name']
                category = request['site'].take_category(data['category'])
                change_sub_course = data['change-sub-course']
                sub_course = request['site'].take_course(data['sub-course'])
                request['site'].take_course(course_name).change_self(new_course_name, category, change_sub_course,
                                                                    sub_course, request['site'].courses)

        return '200 OK', render('change-course.html', secret=request)


class EnrollCourse:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                user_name = data['user-name']
                print(user_name)
                user_name = user_name.split('+')
                print(user_name)
                change_type = data['change-type']
                course_name = data['course-name']
                user, user_type = request['site'].take_user(user_name[1], user_name[2])
                request['site'].take_course(course_name).add_del_user(user, user_type, change_type)

        return '200 OK', render('enroll-course.html', secret=request)


class Error404:

    def __call__(self, request):
        print(request)
        """Это для Эксперемнта"""
        return '404 Error', [b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    '
                             b'<meta charset="UTF-8">\n    '
                             b'<title>\xd0\x9e \xd0\xbd\xd0\xb0\xd1\x81</title>\n</head>\n<body>\n    '
                             b'<h1>Error 404</h1>\n</body>\n</html>']
