class ParseReverseProxyPrefix:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        prefix = environ.get('HTTP_X_FORWARDED_PREFIX')

        if prefix:
            script = environ.get('SCRIPT_NAME', '/')
            environ['SCRIPT_NAME'] = '/{}/{}'.format(
                prefix.strip('/'),
                script.lstrip('/'),
            )

            if environ.get('SCRIPT_URL'):
                environ['SCRIPT_URL'] = ''

        return self.app(environ, start_response)
