from .request import Request
from .response import Response

class HttpRequestCookieTrait:
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

class HttpRequestGetTrait:
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

class HttpRequestPostTrait:
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

class HttpRequestServerTrait:
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

class HttpRequestSessionTrait:
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

class HttpRequest(
    Request,
    HttpRequestCookieTrait,
    HttpRequestGetTrait,
    HttpRequestPostTrait,
    HttpRequestServerTrait,
    HttpRequestSessionTrait
):
    'Http Request Object'

    def load(self):
        'Loads default data given by PHP'
        pass

class HttpResponseHeaderTrait:
    'Designed for the Response Object; Adds methods to process headers'

    def add_header(self, name, value = None):
        'Adds a header parameter'
        pass

    def get_headers(self, name = None):
        'Returns either the header value given the name or the all headers'
        pass

    def remove_header(self, name):
        'Removes a header parameter'
        pass

class HttpResponsePageTrait:
    'Designed for the Response Object; Adds methods to process REST type responses'

    def add_meta(self, name, content):
        'Adds a page meta item'
        pass

    def get_flash(self):
        'Returns flash data'
        pass

    def get_meta(self, *args):
        'Returns meta given path or all meta data'
        pass

    def get_page(self, *args):
        'Returns page data given path or all page data'
        pass

    def has_page(self, *args):
        'Returns true if theres any page data'
        pass

    def remove_page(self, *args):
        'Removes arbitrary page data'
        pass

    def set_flash(self, message, type = 'info'):
        'Sets a Page flash'
        pass

    def set_page(self, *args):
        'Sets arbitrary page data'
        pass

    def set_title(self, title):
        'Sets a Page title'
        pass

class HttpResponseStatusTrait:
    'Designed for the Response Object; Adds methods to process status codes'

    def get_status(self):
        'Returns the status code'
        pass

    def set_status(self, code, status):
        'Sets a status code'
        pass

class HttpResponse(
    Response,
    HttpResponseHeaderTrait,
    HttpResponsePageTrait,
    HttpResponseStatusTrait
):
    'Http Response Object'

    def load(self):
        'Loads default data'
        pass

class HttpRouterTrait:
    'Designed for the HttpHandler we are parting this out to lessen the confusion'

    def all(self, path, callback):
        'Adds routing middleware for all methods'
        pass

    def delete(self, path, callback):
        'Adds routing middleware for delete method'
        pass

    def get(self, path, callback):
        'Adds routing middleware for get method'
        pass

    def get_router(self):
        'Returns a router object'
        pass

    def post(self, path, callback):
        'Adds routing middleware for post method'
        pass

    def put(self, path, callback):
        'Adds routing middleware for put method'
        pass

    def route(self, method, path, callback):
        'Adds routing middleware'
        pass

    def set_router(self, router):
        'Sets the router to use'
        pass

    def trigger_route(self, method, path, *args):
        'Manually trigger a route'
        pass

class HttpRouterInterface:
    'Handles method-path matching and routing'

    def __init__(self, handler = None):
        'Allow to pass a custom EventHandler'
        pass

    def process(self, request, *args):
        'Process routes'
        pass

    def route(self, method, pattern, callback):
        'Adds routing middleware'
        pass

class HttpRouter(HttpRouterInterface):
    'Handles method-path matching and routing'

    def __init__(self, handler = None):
        'Allow to pass a custom EventHandler'
        pass

    def process(self, request, *args):
        'Process routes'
        pass

    def route(self, method, pattern, callback):
        'Adds routing middleware'
        pass

class HttpDispatcher:
    pass

class HttpHandler:
    pass

class HttpDispatcherTrait:
    pass

class HttpTrait:
    pass
