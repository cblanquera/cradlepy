import json
from ..components.data import Registry

class ContentTrait:
    'Designed for the Response Object Adds methods to process raw content'

    def get_content(self):
        'Returns the content body'
        self.get('body')

    def has_content(self):
        'Returns true if content is set'
        body = self.get_content()
        return body != None and len(body)

    def set_content(self, content):
        'Sets the content'

        if isinstance(content, (list, dict, tuple)):
            content = json.dumps(content, indent = 4)

        if isinstance(content, bool):
            if content:
                content = '1'
            else:
                content = '0'

        if content is None:
            content = ''

        self.set('body', content)
        return self

class RestTrait:
    'Designed for the Response Object Adds methods to process REST type responses'

    def add_validation(self, *args):
        'Adds a JSON validation message or sets all the validations'

        if len(args) < 2:
            return self

        return self.set('json', 'validation', *args)

    def get_results(self, *args):
        'Returns JSON results if still in array mode'

        if not len(args):
            return self.get_dot('json.results')

        return self.get('json', 'results', *args)

    def get_message(self):
        'Returns the message'

        return self.get_dot('json.message')

    def get_message_type(self):
        'Determines the message type based on error'

        error = self.get('json', 'error')

        if error is True:
            return 'error'

        if error is False:
            return 'success'

        return 'info'

    def get_validation(self, name = None, *args):
        'Returns JSON validations if still in array mode'

        if name is None:
            return self.get_dot('json.validation')

        return self.get('json', 'validation', name, *args)

    def has_json(self, *args):
        'Returns true if theres any JSON'

        if not len(args):
            return self.exists('json')

        return self.exists('json', *args)

    def has_message(self):
        'Returns true if theres a message'

        return self.has_json('message')

    def has_results(self, *args):
        'Returns true if theres any results given name'
        return self.has_json('results', *args)

    def has_validation(self, *args):
        'Returns true if theres any validations given name'
        return self.has_json('validation', *args)

    def is_error(self):
        'Returns true if theres an error'

        return self.get('json', 'error')

    def is_success(self):
        'Returns true if theres no error'

        return not self.get('json', 'error')

    def remove_results(self, *args):
        'Removes results given name or all of the results'

        if not len(args):
            return self

        return self.remove('json', 'results', *args)

    def remove_validation(self, *args):
        'Removes a validation given name or all the validations'

        if not len(args):
            return self

        return self.remove('json', 'validation', *args)

    def set_error(self, status, message = None):
        'Sets a JSON error message'

        self.set_dot('json.error', status)

        if isinstance(message, str):
            self.set_dot('json.message', message)

        return self

    def set_results(self, data, *args):
        'Sets a JSON result'

        if isinstance(data, (list, tuple, dict)):
            return self.set_dot('json.results', data)

        return self.set('json', 'results', data, *args)

class ResponseInterface:
    'Response Object Interface'

    def add_validation(self, field, message):
        'Adds a JSON validation message or sets all the validations'
        pass

    def get_content(self):
        'Returns the content body'
        pass

    def get_results(self, *args):
        'Returns JSON results if still in array mode'
        pass

    def get_message(self):
        'Returns the message'
        pass

    def get_message_type(self):
        'Determines the message type based on error'
        pass

    def get_validation(self, name = None, *args):
        'Returns JSON validations if still in array mode'
        pass

    def has_content(self):
        'Returns true if content is set'
        pass

    def has_json(self, *args):
        'Returns true if theres any JSON'
        pass

    def has_message(self):
        'Returns true if theres a message'
        pass

    def has_results(self, *args):
        'Returns true if theres any results given name'
        pass

    def has_validation(self, *args):
        'Returns true if theres any validations given name'
        pass

    def is_error(self):
        'Returns true if theres an error'
        pass

    def is_success(self):
        'Returns true if theres no error'
        pass

    def remove_results(self, name):
        'Removes results given name or all of the results'
        pass

    def remove_validation(self, name):
        'Removes a validation given name or all the validations'
        pass

    def set_content(self, content):
        'Sets the content'
        pass

    def set_error(self, status, message = None):
        'Sets a JSON error message'
        pass

    def set_results(self, data, *args):
        'Sets a JSON result'
        pass

class ResponseTrait:
    'Designed for Handlers we are parting this out to lessen the confusion'

    _response = None

    def get_response(self):
        'Returns a response object'

        if self._response is None:
            self.set_response(Response(), True)

        return self._response;

    def set_response(self, response):
        'Sets the response object to use'

        # make sure this is an ResponseInterface
        if not isinstance(handler, ResponseInterface):
            return self

        self._response = response

        return self

class Response(Registry, ContentTrait, RestTrait, ResponseInterface):
    'Response Object'

    def load(self):
        'Loads default data'
        pass
