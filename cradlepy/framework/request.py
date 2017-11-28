from ..components.data import Registry

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

class FileTrait:
    'Designed for the Request Object; Adds methods to store FILES data'

    def get_files(self, *args):
        'Returns FILES given name or all FILES'
        return self.get('files', *args)

    def remove_files(self, *args):
        'Removes FILES given name or all FILES'
        return self.remove('files', *args)

    def has_files(self, *args):
        'Returns true if has FILES given name or if FILES is set'
        return self.exists('files', *args)

    def set_files(self, data, *args):
        'Sets FILES'

        if isinstance(data, (list, dict, tuple)):
            return self.set('files', data)

        if len(args) == 0:
            return self

        return self.set('files', data, *args)

class RouteTrait:
    'Designed for the Request Object; Adds methods to store passed Router data'

    def get_route(self, name = None, *args):
        'Returns route data given name or all route data'
        if name is None:
            return self.get('route')

        return self.get('route', name, *args)

    def get_parameters(self, name = None):
        'Returns route data given name or all route data'
        if name is None:
            return self.get('parameters')

        return self.get('parameters', name, *args)

    def get_variables(self, index = None):
        'Returns route data given name or all route data'
        if name is None:
            return self.get('variables')

        return self.get('variables', name, *args)

    def set_route(self, route):
        'Sets a request route'
        return self.set('route', route);

class StageTrait:
    'Designed for the Request Object; Adds methods to store REQUEST data'

    def get_stage(self, *args):
        'Returns REQUEST given name or all REQUEST'
        return self.get('stage', *args);

    def has_stage(self, *args):
        'Returns true if has REQUEST given name or if REQUEST is set'
        return self.exists('stage', *args);

    def remove_stage(self, *args):
        'Removes REQUEST given name or all REQUEST'
        return self.remove('stage', *args);

    def set_soft_stage(self, data):
        'Clusters request data together softly'

        #only non scalar
        if isinstance(data, (list, tuple)):
            data = enumerate(data)
        elif isinstance(data, dict):
            data = data.items()
        else:
            return self

        #one dimenstions soft setter
        for key, value in data:
            if self.exists('stage', key):
                continue

            self.set('stage', key, value)

        return self

    def set_stage(self, data, *args):
        'Sets POST'

        #non scalar
        if isinstance(data, (list, tuple, dict)):
            if isinstance(data, (list, tuple)):
                data = enumerate(data)
            elif isinstance(data, dict):
                data = data.items()

            #one dimenstions soft setter
            for key, value in data:
                self.set('stage', key, value)

            return self

        if len(args) == 0:
            return self

        return self.set('stage', data, *args);

class RequestTrait:
    'Designed for Handlers we are parting this out to lessen the confusion'

    _request = None

    def get_request(self):
        'Returns a request object'

        if self._request is None:
            self.set_request(Request(), True)

        return self._request;

    def set_request(self, request):
        'Sets the request object to use'

        # make sure this is an RequestInterface
        if not isinstance(handler, RequestInterface):
            return self

        self._request = request

        return self

class RequestInterface:
    'Request Object Interface'

    def get_content(self):
        'Returns final input stream'
        pass

    def get_files(self, *args):
        'Returns FILES given name or all FILES'
        pass

    def get_route(self, name = None, *args):
        'Returns route data given name or all route data'
        pass

    def get_parameters(self, name = None):
        'Returns route data given name or all route data'
        pass

    def get_stage(self, *args):
        'Returns REQUEST given name or all REQUEST'
        pass

    def get_variables(self, index = None):
        'Returns route data given name or all route data'
        pass

    def has_content(self):
        'Returns true if has content'
        pass

    def has_files(self, *args):
        'Returns true if has FILES given name or if FILES is set'
        pass

    def has_stage(self, *args):
        'Returns true if has REQUEST given name or if REQUEST is set'
        pass

    def remove_files(self, *args):
        'Removes FILES given name or all FILES'
        pass

    def remove_stage(self, *args):
        'Removes REQUEST given name or all REQUEST'
        pass

    def set_content(self, content):
        'Sets content'
        pass

    def set_files(self, data, *args):
        'Sets FILES'
        pass

    def set_route(self, route):
        'Sets a request route'
        pass

    def set_soft_stage(self, data):
        'Clusters request data together softly'
        pass

    def set_stage(self, data, *args):
        'Sets POST'
        pass

class Request(Registry, ContentTrait, FileTrait, RouteTrait, StageTrait, RequestInterface):
    pass
