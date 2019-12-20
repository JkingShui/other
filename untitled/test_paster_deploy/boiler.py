# boiler.py
class Boiler(object):
    def __init__(self, app, in_arg):
        self.app = app
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Boiler'
        return self.app(environ, start_response)


def filter_app_factory(app, global_config, in_arg):
    return Boiler(app, in_arg)
