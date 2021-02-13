from shelp_framework.templates import render


class Index:

    def __call__(self, request):
        secret = request.get('secret_key', None)
        print(request)
        return '200 OK', render('index.html', secret=secret)


class About:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            if data:
                title = data['title']
                text = data['text']
                email = data['email']
                print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
            secret = request.get('secret_key', None)
            return '200 OK', render('about.html', secret=secret)
        else:
            secret = request.get('secret_key', None)
            return '200 OK', render('about.html', secret=secret)


class Other:

    def __call__(self, request):
        secret = request.get('secret_key', None)
        print(request)
        return '200 OK', render('other.html', secret=secret)


class Error404:

    def __call__(self, request):
        print(request)
        """Это для Эксперемнта"""
        return '404 Error', [b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    '
                             b'<meta charset="UTF-8">\n    '
                             b'<title>\xd0\x9e \xd0\xbd\xd0\xb0\xd1\x81</title>\n</head>\n<body>\n    '
                             b'<h1>Error 404</h1>\n</body>\n</html>']
