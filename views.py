from shelp_framework.templates import render
from logging_app import Logger, debug


logger = Logger('views')


@debug
class Index:

    def __call__(self, request):
        secret = request.get('secret_key', None)
        return '200 OK', render('index.html', secret=secret)


class Courses:

    def __call__(self, request):
        secret = request["site"].courses
        return '200 OK', render('curses.html', secret=secret)


class About:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                title = data['title']
                text = data['text']
                email = data['email']
                logger.log(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
            secret = request.get('secret_key', None)
            return '200 OK', render('about.html', secret=secret)
        else:
            secret = request.get('secret_key', None)
            return '200 OK', render('about.html', secret=secret)


class Other:

    def __call__(self, request):
        secret = request.get('secret_key', None)
        return '200 OK', render('other.html', secret=secret)


class ControlPanel:

    def __call__(self, request):
        secret = request.get('secret_key', None)
        return '200 OK', render('base-control-panel.html', secret=secret)


class CreateCategory:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                name = data['category-name']
                request["site"].create_category(name)
                logger.log(request["site"].courses_category)
        return '200 OK', render('create-category.html', secret=request['path'])


class CreateCurse:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                name = data['curse-name']
                category = data['category']
                creation_type = data['creation-type']
                if creation_type == 'new':
                    request["site"].create_course(name, category)
                else:
                    sub_courses = request["site"].create_sub_courses(data['sub-curse'], data['creation-type'])
                    print(f"ASDASDASDASDASD ____ {data['sub-curse'], data['creation-type']}  ")
                    request["site"].create_course(name, category, sub_courses)
        secret = request.get('secret_key', None)
        logger.log(f'{request["site"].courses} - ЭТО КУРСЫ')
        return '200 OK', render('create-curse.html', secret=request['path'])


class Error404:

    def __call__(self, request):
        print(request)
        """Это для Эксперемнта"""
        return '404 Error', [b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    '
                             b'<meta charset="UTF-8">\n    '
                             b'<title>\xd0\x9e \xd0\xbd\xd0\xb0\xd1\x81</title>\n</head>\n<body>\n    '
                             b'<h1>Error 404</h1>\n</body>\n</html>']
