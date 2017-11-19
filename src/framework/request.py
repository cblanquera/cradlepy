class CliTrait:
    'Designed for the Request Object; Adds CLI methods'

    def get_args(self):
        'Returns CLI args if any'

        return self.get('args')

    def set_args(self, argsv):
        'Sets CLI args'

        return self.set('args', argsv)

class ContentTrait:
    'Designed for the Request Object; Adds methods to store raw input'

    def get_content(self):
        'Returns final input stream'

        return self.get('body')

    def has_content(self):
        'Returns true if has content'

        return not self.is_empty('body')

    def set_content(self, content):
        'Sets content'

        return self.set('body', content)

class CookieTrait:
    'Designed for the Request Object; Adds methods to store $_COOKIE data'

    def get_cookies(self, *args):
        'Returns $_COOKIE given name or all $_COOKIE'

        return self.get('cookie', *args)

    def remove_cookies(self, *args):
        'Removes $_COOKIE given name or all $_COOKIE'

        return self.remove('cookie', *args)

    def has_cookies(self, *args):
        'Returns true if has $_COOKIE given name or if $_COOKIE is set'

        return self.exists('cookie', *args)

    def set_cookies(self, data, *args):
        'Sets $_COOKIE'

        if isinstance(data, (list, dict, tuple)):
            return self.set('cookie', data)

        if len(args) == 0:
            return self

        return self.set('cookie', data, *args)

class FileTrait:
    'Designed for the Request Object; Adds methods to store $_FILES data'

    def get_files(self, *args):
        'Returns $_FILES given name or all $_FILES'

        return self.get('files', *args)

    def remove_files(self, *args):
        'Removes $_FILES given name or all $_FILES'

        return self.remove('files', *args)

    def has_files(self, *args):
        'Returns true if has $_FILES given name or if $_FILES is set'

        return self.exists('files', *args)

    def set_files(self, data, *args):
        'Sets $_FILES'

        if isinstance(data, (list, dict, tuple)):
            return self.set('files', data)

        if len(args) == 0:
            return self

        return self.set('files', data, *args)

class GetTrait:
    'Designed for the Request Object; Adds methods to store $_GET data'

    def get_get(self, *args):
        'Returns $_GET given name or all $_GET'
        pass

    def remove_get(self, *args):
        'Removes $_GET given name or all $_GET'
        pass

    def has_get(self, *args):
        'Returns true if has $_GET given name or if $_GET is set'
        pass

    def set_get(self, data, *args):
        'Sets $_GET'
        pass

class PostTrait:
    'Designed for the Request Object; Adds methods to store $_POST data'

    def get_post(self, *args):
        'Returns $_POST given name or all $_POST'
        pass

    def remove_post(self, *args):
        'Removes $_POST given name or all $_POST'
        pass

    def has_post(self, *args):
        'Returns true if has $_POST given name or if $_POST is set'
        pass

    def set_post(self, data, *args):
        'Sets $_POST'
        pass

class RouteTrait:
    'Designed for the Request Object; Adds methods to store passed Router data'

    def get_route(self, name = None, *args):
        'Returns route data given name or all route data'
        pass

    def get_parameters(self, name = None):
        'Returns route data given name or all route data'
        pass

    def get_variables(self, index = None):
        'Returns route data given name or all route data'
        pass

    def set_route(self, route):
        'Sets a request route'
        pass

class ServerTrait:
    'Designed for the Request Object; Adds methods to store $_SERVER data'

    def get_method(self):
        'Returns method if set'
        pass

    def get_path(self, name = None):
        'Returns path data given name or all path data'
        pass

    def get_query(self):
        'Returns string query if set'
        pass

    def get_server(self, name = None):
        'Returns SERVER data given name or all SERVER data'
        pass

    def has_server(self, name = None):
        'Returns SERVER data given name or all SERVER data'
        pass

    def is_method(self, method):
        'Returns true if method is the one given'
        pass

    def set_method(self, method):
        'Sets request method'
        pass

    def set_path(self, path):
        'Sets path given in string or array form'
        pass

    def set_query(self, query):
        'Sets query string'
        pass

    def set_server(self, server):
        'Sets SERVER'
        pass

class SessionTrait:
    'Designed for the Request Object; Adds methods to store $_SESSION data'

    def get_session(self, *args):
        'Returns $_SESSION given name or all $_SESSION'
        pass

    def remove_session(self, *args):
        'Removes $_SESSION given name or all $_SESSION'
        pass

    def has_session(self, *args):
        'Returns true if has $_SESSION given name or if $_SESSION is set'
        pass

    def set_session(self, data, *args):
        'Sets $_SESSION'
        pass

class StageTrait:
    'Designed for the Request Object; Adds methods to store $_REQUEST data'

    def get_stage(self, *args):
        'Returns $_REQUEST given name or all $_REQUEST'
        pass

    def has_stage(self, *args):
        'Returns true if has $_REQUEST given name or if $_REQUEST is set'
        pass

    def remove_stage(self, *args):
        'Removes $_REQUEST given name or all $_REQUEST'
        pass

    def set_soft_stage(self, data):
        'Clusters request data together softly'
        pass

    def set_stage(self, data, *args):
        'Sets $_POST'
        pass

class RequestTrait:
    'Designed for the HttpHandler we are parting this out to lessen the confusion'

    def get_request(self):
        'Returns a request object'
        pass

    def set_request(self, request):
        'Sets the request object to use'
        pass

class Request:
    'Http Request Object'

    def load(self):
        'Loads default data given by PHP'
        pass
