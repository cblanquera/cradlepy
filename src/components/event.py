import re
from inspect import signature

class EventObserver:
    'Event observer object'

    _id = None

    _callback = None

    def __init__(self, callback):
        'We need a callback'
        self.set_callback(callback)

    def get_callback(self):
        'Returns the set callback'
        return self._callback

    def set_callback(self, callback):
        'You can add a different callback if you want'

        self._callback = callback
        self._id = id(callback)
        return self

    def assert_equals(self, callback):
        return self._id == id(callback)

class EventInterface: #ignore coverage
    '''
    Allows the ability to listen to events made known by another
    piece of functionality. Events are items that transpire based
    on an action. With events you can add extra functionality
    right after the event has triggered.
    '''

    def off(self, event = None, callback = None):
        'Stops listening to an event'
        pass

    def on(self, event, callback = None, priority = 0):
        '''
        Attaches an instance to be notified
        when an event has been triggered
        '''
        pass

    def trigger(self, event, *args):
        'Notify all observers of that a specific event has happened'
        pass

class EventHandler(EventInterface):
    '''
    Allows the ability to listen to events made known by another
    piece of functionality. Events are items that transpire based
    on an action. With events you can add extra functionality
    right after the event has triggered.
    '''

    _meta = True

    def __init__(self):
        self._observers = {}
        self._regex = []

    def get_meta(self):
        'Returns the current matched handler'
        return EventHandler._meta

    def match(self, event):
        'Returns possible event matches'
        matches = {}

        #do the obvious match
        if event in self._observers.keys():
            matches[event] = {
                'event': event,
                'pattern': event,
                'variables': []
            }

        #deal with regexp
        for pattern in self._regex:
            regexp = re.compile(pattern[1:-1])

            # if it matches
            match = re.findall(regexp, event)

            if len(match):
                # [':something'] or [('*', ':something')]
                variables = []
                for variable in match:
                    if isinstance(variable, str):
                        variables.append(variable)
                    elif isinstance(variable, (list, tuple)):
                        for partial in variable:
                            if isinstance(partial, str):
                                variables.append(variable)

                matches[pattern] = {
                    'event': event,
                    'pattern': pattern,
                    'variables': variables
                }

        return matches.values()

    def off(self, event = None, callback = None):
        'Stops listening to an event'

        # if there is no event and not callable
        if not isinstance(event, str) and not callable(callback):
            # it means that they want to remove everything
            self._observers = {}
            return self

        # if event is a string
        if isinstance(event, str):
            # if there are callbacks listening to
            # this and no callback was specified
            if event in self._observers.keys() and not callable(callback):
                # it means that they want to remove
                # all callbacks listening to this event
                del self._observers[event]
                return self

            # if there are callbacks listening
            # to this and we have a callback
            if event in self._observers.keys() and callable(callback):
                return self._remove_observers_by_event(event, callback)
        # if no event, but there is a callback
        elif callable(callback):
            return self._remove_observers_by_callback(callback);

        return self

    def on(self, event, callback = None, priority = 0):
        '''
        Attaches an instance to be notified
        when an event has been triggered
        '''

        # decorator
        # as in @events.on('foobar')
        if not callable(callback):
            # if as in @events.on('foobar', 3)
            if isinstance(callback, (int, float)):
                priority = callback

            def wrapper(callback):
                self.on(event, callback, priority)

            return wrapper

        # deal with multiple events
        if isinstance(event, list):
            for item in event:
                self.on(item, callback, priority)
            return self

        # set up the observer
        observer = EventObserver(callback)

        # is there a regexp ?
        if event[0:1] == '#' and event[-1:] == '#':
            self._regex.append(event);
        # is there a sprintf ?
        # because sscanf will match Render Home Page
        # and Render Home Body with Render %s Page
        elif re.search(r'%[sducoxXbgGeEfF]', event):
            event = re.sub(r'%[sducoxXbgGeEfF]', '(.+)', event)
            self._regex.append('#' + event + '#');

        if not event in self._observers.keys():
            self._observers[event] = {}

        if not priority in self._observers[event].keys():
            self._observers[event][priority] = []

        self._observers[event][priority].append(observer)

        return self

    def trigger(self, event, *args):
        'Notify all observers of that a specific event has happened'

        matches = self.match(event)

        def krsort(d):
            return [d[k] for k in sorted(d.keys(), reverse=True)]

        for match in matches:
            # add on to match
            match['args'] = args
            event = match['pattern']

            # if no direct observers
            if not event in self._observers.keys():
                continue

            # sort it out
            rsorted = krsort(self._observers[event])
            observers = []

            for items in rsorted:
                observers += items[:]

            # for each observer
            for observer in observers:
                # get the callback
                callback = observer.get_callback()
                # add on to match
                match['callback'] = callback
                # set the current
                EventHandler._meta = match

                # if this is the same event, call the method, if the method returns false
                siggy = signature(callback)
                if '*' in str(siggy):
                    if callback(*args) == False:
                        EventHandler._meta = False
                        return self
                else:
                    max = len(siggy.parameters)
                    new_args = args[:max]

                    if callback(*new_args) == False:
                        EventHandler._meta = False
                        return self

        EventHandler._meta = True
        return self

    def _remove_observers_by_callback(self, callback):
        # find the callback
        for event in self._observers.keys():
            self._remove_observers_by_event(event, callback)

        return self

    def _remove_observers_by_event(self, event, callback):
        # if event isn't set
        if not event in self._observers:
            # do nothing
            return self

        # 'foobar' => array(
        for observers in self._observers[event].values():
            # 0 => array(
            for i, observer in enumerate(observers):
                # 0 => callback
                if observer.assert_equals(callback):
                    del observers[i]

        return self

class EventTrait:
    'Trait used to attach events functionality to classes'

    _global_event_handler = None

    _event_handler = None

    def get_event_handler(self):
        'Returns an EventHandler object if none was set, it will auto create one'

        if EventTrait._global_event_handler == None:
            self.set_event_handler(EventHandler(), True)

        if self._event_handler == None:
            self._event_handler = EventTrait._global_event_handler

        return self._event_handler;

    def on(self, event, callback = None, priority = 0):
        '''
        Attaches an instance to be notified
        when an event has been triggered
        '''

        handler = self.get_event_handler()

        # decorator
        # as in @events.on('foobar')
        if not callable(callback):
            # if as in @events.on('foobar', 3)
            if isinstance(callback, (int, float)):
                priority = callback

            def wrapper(callback):
                handler.on(event, callback, priority)

            return wrapper

        handler.on(event, callback, priority)

        return self;

    def set_event_handler(self, handler, is_static = False):
        'Allow for a custom dispatcher to be used'

        # make sure this is an EventHandler
        if not isinstance(handler, EventHandler):
            return self

        if is_static:
            EventTrait._global_event_handler = handler

        self._event_handler = handler

        return self

    def trigger(self, event, *args):
        'Notify all observers of that a specific event has happened'

        self.get_event_handler().trigger(event, *args)
