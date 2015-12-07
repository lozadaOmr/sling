__version__ = '0.1.0'


class HelloResource(object):

    def on_get(self, req, res):
        res.body = "Hello! I'm ExampleModule."


class HelloNameResource(object):

    def on_get(self, req, res, name):
        res.body = 'Hello, %s' % name


def install_module(app):
    app.api.add_route('/hello', HelloResource())
    app.api.add_route('/hello/{name}', HelloNameResource())
    import command
