from views import Error404
from models import ShelpSite


class Application:
    shelp_site = ShelpSite()

    def data_string_parse(self, data):
        query_request = {}
        if data:
            query_list = data.split('&')
            for query in query_list:
                q, v = query.split('=')
                query_request[q] = v
        return query_request

    def parse_wsgi_input_data(self, data: bytes):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.data_string_parse(data_str)
        return result

    def get_wsgi_input_data(self, environ):
        content_length_data = environ.get('CONTENT_LENGTH')
        print(content_length_data)
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        print(data)
        return data

    def __init__(self, urls_routes, fronts):
        self.urls_routes = urls_routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        # берем текущий url
        path = environ['PATH_INFO']
        # проверяем на /
        if path[len(path) - 1] != "/":
            if path[len(path) - 1] == "\\":
                path = path[:-1]
                path = path + "/"
            else:
                path = path + "/"
        # Получаем данные для запроса
        response_method = environ['REQUEST_METHOD']
        query_request = self.data_string_parse(environ['QUERY_STRING'])
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        print('ЭТО ТЕ ДАННЫЕ', data)

        if path in self.urls_routes:
            view = self.urls_routes[path]
            request = {}
            # добавляем параметры запросов
            request['method'] = response_method
            request['data'] = data
            request['request_params'] = query_request
            request['path'] = path
            request['site'] = Application.shelp_site
            # front controller
            for front in self.fronts:
                front(request)
            code, body = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            print(body)
            return body
        else:
            view = Error404()


class LogApplication(Application):
    def __init__(self, urlpatterns, front_controllers):
        self.application = Application(urlpatterns, front_controllers)
        super().__init__(urlpatterns, front_controllers)

    def __call__(self, environ, start_response):
        print('log -- app -- start')
        return self.application(environ, start_response)


class FakeApplication(Application):

    def __init__(self, urlpatterns, front_controllers):
        self.application = Application(urlpatterns, front_controllers)
        super().__init__(urlpatterns, front_controllers)

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'<h1>Hello from Fake</h1>']