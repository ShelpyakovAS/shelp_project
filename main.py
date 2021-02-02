from shelp_framework.wsgi_app import Application
from urls import urls_routes


def secret_controller(request):
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urls_routes, front_controllers)