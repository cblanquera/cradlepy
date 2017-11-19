class RouterTrait:
    'Designed for the HttpHandler we are parting this out to lessen the confusion'

    def all(self, path, callback)
        'Adds routing middleware for all methods'
        pass

    def delete(self, path, callback)
        'Adds routing middleware for delete method'
        pass

    def get(self, path, callback)
        'Adds routing middleware for get method'
        pass

    def get_router(self)
        'Returns a router object'
        pass

    def post(self, path, callback)
        'Adds routing middleware for post method'
        pass

    def put(self, path, callback)
        'Adds routing middleware for put method'
        pass

    def route(self, method, path, callback)
        'Adds routing middleware'
        pass

    def set_router(self, router)
        'Sets the router to use'
        pass

    def trigger_route(self, method, path, *args)
        'Manually trigger a route'
        pass

class Router:
    'Handles method-path matching and routing'

    def __init__(self, handler = None)
        'Allow to pass a custom EventHandler'
        pass

    def process(self, request, *args):
        'Process routes'
        pass

    def route(self, method, pattern, callback):
        'Adds routing middleware'
        pass
