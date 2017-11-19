class ContentTrait:
    'Designed for the Response Object; Adds methods to process raw content'

    def get_content(self):
        'Returns the content body'
        pass

    def has_content(self):
        'Returns true if content is set'
        pass

    def set_content(self, content):
        'Sets the content'
        pass

class HeaderTrait:
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

class PageTrait:
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
        'Returns true if there's any page data'
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

class RestTrait:
    'Designed for the Response Object; Adds methods to process REST type responses'

    def add_validation(self, field, message):
        'Adds a JSON validation message or sets all the validations'
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

    def has_json(self, *args):
        'Returns true if there's any JSON'
        pass

    def has_message(self):
        'Returns true if there's a message'
        pass

    def has_results(self, *args):
        'Returns true if there's any results given name'
        pass

    def has_validation(self, *args):
        'Returns true if there's any validations given name'
        pass

    def is_error(self):
        'Returns true if there's an error'
        pass

    def is_success(self):
        'Returns true if there's no error'
        pass

    def remove_results(self, name):
        'Removes results given name or all of the results'
        pass

    def remove_validation(self, name):
        'Removes a validation given name or all the validations'
        pass

    def set_error(self, status, message = None):
        'Sets a JSON error message'
        pass

    def set_results(self, data, *args):
        'Sets a JSON result'
        pass

class StatusTrait:
    'Designed for the Response Object; Adds methods to process status codes'

    def get_status(self):
        'Returns the status code'
        pass

    def set_status(self, code, status):
        'Sets a status code'
        pass

class ResponseTrait:
    'Designed for the HttpHandler we are parting this out to lessen the confusion'

    def get_response(self):
        'Returns a response object'
        pass

    def set_response(self, response):
        'Sets the response object to use'
        pass

class Response:
    'Http Response Object'

    def load(self):
        'Loads default data'
        pass
