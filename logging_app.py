import time


class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, text):
        with open(f'logging/{self.file_name}.txt', 'a') as f:
            f.write(f'LOG ---> {text} ---> {time.asctime()}\n')

    def debug(self, text):
        with open(f'logging/{self.file_name}.txt', 'a') as f:
            f.write(f'DEBUG ---> {text} ---> {time.asctime()}\n')


def debug(view):
    print(f'DEBUG ---> {view.__name__} ---> {time.asctime()}')
    view()
    return view