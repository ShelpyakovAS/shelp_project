from views import Error404


class Application:

    def __init__(self, urls_routes, fronts):
        self.urls_routes = urls_routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        print('work')
        path = environ['PATH_INFO']
        if path[len(path)-1] != "/":
            if path[len(path)-1] == "\\":
                path = path[:-1]
                path = path + "/"
            else:
                path = path + "/"
        if path in self.urls_routes:
            view = self.urls_routes[path]
        else:
            view = Error404()
        request = {}
        # front controller
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body