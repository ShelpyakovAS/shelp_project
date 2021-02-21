from shelp_framework.wsgi_app import Application, LogApplication, FakeApplication
from urls import urls_routes





def secret_controller(request):
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = LogApplication(urls_routes, front_controllers)

fake_app = FakeApplication(urls_routes, front_controllers)

