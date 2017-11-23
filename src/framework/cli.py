from .request import Request
from .response import Response

class CliTrait:
    'Designed for the Request Object; Adds CLI methods'

    def get_args(self):
        'Returns CLI args if any'

        return self.get('args')

    def set_args(self, argsv):
        'Sets CLI args'

        return self.set('args', argsv)

class CliRequest(Request, CliTrait):
    'CLI Request Object'

    def load(self):
        'Loads default data given by PHP'
        pass

class CliResponse(Response):
    'CLI Response Object'

    def load(self):
        'Loads default data'
        pass
