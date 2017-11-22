import re
import uuid
import json

class MagicTrait:
    'An inventory of magical data references'

    def __delattr__(self, name):
        'Processes delete properties'
        self.__delitem__(name)

    def __delitem__(self, key):
        'Deletes the item accessed like an array'
        # if it exists
        if key in self.__dict__.keys():
            #remove it
            del self.__dict__[key]

    def __getattr__(self, name):
        'Processes get and set type methods processes get property'
        def function(*args):
            #if the method starts with get
            if name[:3] == 'get':
                #get_user_name('-')
                separator = '_'
                if len(args) and isinstance(args[0], str):
                    separator = args[0]

                #determine the key name
                key = name.replace('_', separator)
                #lowercase and get rid of prefix
                key = key[(3 + len(separator)):]

                #get attribute or None
                return self.__getitem__(key)
            # the method has to start with set
            #set_user_name('-')
            separator = '_'
            if len(args) > 1 and isinstance(args[1], str):
                separator = args[1]

            #determine the key name
            key = name.replace('_', separator)
            #get rid of prefix
            key = key[(3 + len(separator)):]

            #if there are no arguments and its a key
            if not len(args) and key in self.__dict__.keys():
                #remove it
                self.__delitem__(key)
            else:
                #otherwise set it
                self.__setitem__(key, args[0])

            #either way return this
            return self
        # if its a function
        if name[:3] == 'get' or name[:3] == 'set':
            return function

        #Lastly return the attribute or None
        return self.__getitem__(name)

    def __getitem__(self, key):
        'Returns the value accessed like an array'
        # if key is of invalid type or value, the list values will raise the error
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return None

    def __iter__(self):
        'Iterates throught the data'
        return iter(self.__dict__.items())

    def __len__(self):
        'Returns the length'
        return len(self.__dict__)

    def __setattr__(self, name, value):
        'Processes set properties'
        self.__setitem__(name, value)

    def __setitem__(self, key, value):
        'Sets the item accessed like an array'
        self.__dict__[key] = value

    def __str__(self):
        'Object to string'
        return json.dumps(self.__dict__, indent = 4)

class DotTrait:
    '''
    The _dotTrait allows multidimensional data to be
    accessed like `foo.bar.zoo` as well as be manipulated
    in the same fashion.
    '''

    def get_dot(self, notation = '', separator = '.'):
        'Gets a value given the path in the registry.'

        # notation should be a string
        if not isinstance(notation, str):
            return None

        keys = notation.split(separator)

        # notation should something
        if notation == '' or not len(keys):
            return self.__dict__

        # get the last key, this will be treated separately
        last = keys.pop();

        pointer = self.__dict__

        # Now parse
        for key in keys:
            if not isinstance(pointer, dict) or not key in pointer:
                return None

            pointer = pointer[key];

        # last round
        if not isinstance(pointer, dict) or not last in pointer:
            return None

        return pointer[last]

    def is_dot(self, notation = '', separator = '.'):
        'Checks to see if a key is set'

        # notation should be a string
        if not isinstance(notation, str):
            return False

        keys = notation.split(separator)

        # notation should something
        if notation == '' or not len(keys):
            return False

        # get the last key, this will be treated separately
        last = keys.pop();

        pointer = self.__dict__

        # Now parse
        for key in keys:
            if not isinstance(pointer, dict) or not key in pointer:
                return False

            pointer = pointer[key];

        # last round
        if not isinstance(pointer, dict) or not last in pointer:
            return False

        return True

    def remove_dot(self, notation = '', separator = '.'):
        'Removes name space given notation'

        # notation should be a string
        if not isinstance(notation, str):
            return self

        keys = notation.split(separator)

        # notation should something
        if notation == '' or not len(keys):
            return self

        # get the last key, this will be treated separately
        last = keys.pop();

        pointer = self.__dict__

        # Now parse
        for key in keys:
            if not isinstance(pointer, dict) or not key in pointer:
                return self

            pointer = pointer[key];

        # last round
        if not isinstance(pointer, dict) or not last in pointer:
            return self

        del pointer[last]

        return self

    def set_dot(self, notation, value, separator = '.'):
        'Creates the name space given the space and sets the value to that name space'
        if not isinstance(notation, str):
            return self

        keys = notation.split(separator)

        if notation == '' or not len(keys):
            return self

        last = keys.pop();

        pointer = self.__dict__

        # Now parse
        for key in keys:
            if not key in pointer or not isinstance(pointer[key], dict):
                pointer[key] = {}

            pointer = pointer[key];

        pointer[last] = value

        return self

class RegistryInterface: #ignore coverage
    '''
    Registry are designed to easily manipulate data in
    preparation to integrate with any multi dimensional
    data store.
    '''

    def exists(self, *args):
        'Returns true if the path keys exist in the dataset'
        pass

    def get(self, *args):
        'Returns the exact data given the path keys'
        pass

    def empty(self, *args):
        'Returns true if the path keys does not exist in the dataset or if it has an empy value'
        pass

    def remove(self, *args):
        'Removes the data found in the path keys'
        pass

    def set(self, *args):
        'Sets the given data to given the path keys'
        pass

class Registry(MagicTrait, DotTrait, RegistryInterface):
    '''
    Registry are designed to easily manipulate data in
    preparation to integrate with any multi dimensional
    data store.
    '''

    def __init__(self, data = None):
        'Sets up the data'
        self.set(data)

    def exists(self, *args):
        'Returns true if the path keys exist in the dataset'

        if not len(args):
            return not self.empty(*args)

        separator = '--' + str(uuid.uuid4().hex) + '--'

        return self.is_dot(separator.join(map(str, args)), separator);

    def get(self, *args):
        'Returns the exact data given the path keys'

        if not len(args):
            return self.__dict__;

        separator = '--' + str(uuid.uuid4().hex) + '--'

        return self.get_dot(separator.join(map(str, args)), separator)

    def empty(self, *args):
        'Returns true if the path keys does not exist in the dataset or if it has an empy value'

        if args == None or not len(args):
            return len(self.__dict__) == 0

        separator = '--' + str(uuid.uuid4().hex) + '--'

        value = self.get_dot(separator.join(map(str, args)), separator)

        if value == None:
            return True

        if isinstance(value, (list, tuple, str)):
            return len(value) == 0

        return True

    def remove(self, *args):
        'Removes the data found in the path keys'

        if not len(args):
            return self

        separator = '--' + str(uuid.uuid4().hex) + '--'
        return self.remove_dot(separator.join(map(str, args)), separator)

    def set(self, *args):
        'Sets the given data to given the path keys'

        if not len(args):
            return self

        if len(args) == 1:
            if isinstance(args[0], dict):
                for key, value in args[0].items():
                    self.__setitem__(key, value)
            return self

        separator = '--' + str(uuid.uuid4().hex) + '--'
        args = list(args)
        value = args.pop()
        return self.set_dot(separator.join(map(str, args)), value, separator)

class ModelInterface: #ignore coverage
    '''
    Models are designed to easily manipulate data in
    preparation to integrate with any one dimensional
    data store. This is the main model object.
    '''

    def get(self):
        'Returns the entire data'
        pass

    def set(self, data):
        'Sets the entire data'
        pass

class Model(MagicTrait, DotTrait, ModelInterface):
    '''
    Models are designed to easily manipulate data in
    preparation to integrate with any one dimensional
    data store. This is the main model object.
    '''

    def __init__(self, data = None):
        'Sets up the data'
        self.set(data)

    def get(self):
        'Returns the entire data'
        return self.__dict__

    def set(self, data):
        'Sets the entire data'
        if isinstance(data, dict):
            for key, value in data.items():
                self.__setitem__(key, value)
        return self

class CollectionInterface: #ignore coverage
    '''
    Collections are a managable list of models. Model
    methods called by the collection are simply passed
    to each model in the collection. Collections perform
    the same functionality as a model, except on a more
    massive level. This is the main collection object.
    '''

    def add(self, model = {}):
        'Adds a row to the collection'
        pass

    def cut(self, index = 'last'):
        'Removes a row and reindexes the collection'
        pass

    def each(self, callback):
        'Loops through returned result sets'
        pass

    def get(self):
        'Returns the entire data'
        pass

    def set(self, collection):
        pass

class Collection(CollectionInterface):
    '''
    Collections are a managable list of models. Model
    methods called by the collection are simply passed
    to each model in the collection. Collections perform
    the same functionality as a model, except on a more
    massive level. This is the main collection object.
    '''

    FIRST = 'first'

    LAST = 'last'

    def __delattr__(self, name):
        'Processes delete properties'
        self.__delitem__(name)

    def __delitem__(self, key):
        'Deletes the item accessed like an array'

        #if its an integer
        if isinstance(key, int):
            if key < len(self._list):
                del self._list[key]
            return

        # it is not an integer
        # go through each model and delete
        for model in self._list:
            del model[key]

    def __getattr__(self, name):
        'Processes get and set type methods processes get property'
        def function(*args):
            #if the method starts with get
            if name[:3] == 'get':
                results = [];
                for model in self._list:
                    results.append(model.__getattr__(name)(*args))

                return results
            #if the method starts with set
            if name[:3] == 'set':
                for model in self._list:
                    model.__getattr__(name)(*args)

                #either way return this
                return self

            # call real function
            results = [];
            for model in self._list:
                callback = getattr(model, name, None)
                if callable(callback):
                    results.append(callback(*args))
                    continue

                results.append(False)

            return results

        # getter or setter ?
        if name[:3] == 'get' or name[:3] == 'set':
            return function

        # real function ?
        for model in self._list:

            if hasattr(model, name) and callable(getattr(model, name)):
                return function

        return self.__getitem__(name)

    def __getitem__(self, key):
        'Returns the value accessed like an array'

        #if it's an integer
        if isinstance(key, int):
            #they probably mean the list row
            if key < len(self._list):
                return self._list[key]
            return None
        # if key is of invalid type or value, the list values will raise the error
        results = [];
        for model in self._list:
            results.append(model[key]);

        return results

    def __init__(self, collection = None):
        'Sets up the data'
        self._list = []
        self.set(collection)

    def __iter__(self):
        'Iterates throught the data'
        return iter(self._list)

    def __len__(self):
        'Returns the length'
        return len(self._list)

    def __setitem__(self, key, value):
        'Sets the item accessed like an array'
        for model in self._list:
            model[key] = value

    def __str__(self):
        'Object to string'
        results = []
        for model in self._list:
            results.append(model.get())
        return json.dumps(results, indent = 4)

    def add(self, model = {}):
        'Adds a row to the collection'

        if isinstance(model, dict):
            model = Model(model)

        if isinstance(model, ModelInterface):
            self._list.append(model)

        return self

    def cut(self, index = 'last'):
        'Removes a row and reindexes the collection'

        if index == self.FIRST:
            index = 0
        elif index == self.LAST:
            index = len(self._list) - 1

        if index < len(self._list):
            del self._list[index]

        return self

    def each(self, callback):
        'Loops through returned result sets'

        if not callable(callback):
            return self
        #print self._list
        for i, value in enumerate(self._list):
            callback(self, i, value)

        return self

    def get(self):
        'Returns the entire data'

        results = []
        for model in self._list:
            results.append(model.get())
        return results

    def set(self, collection):
        'Sets the entire data'

        if isinstance(collection, list):
            for model in collection:
                self.add(model)

        return self
