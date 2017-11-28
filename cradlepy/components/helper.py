from inspect import signature

class ConditionalTrait:
    'Adds a generic `when()` method used during chainable calls'

    def when(self, conditional, callback = None):
        'Invokes Callback if conditional callback is true'

        # if the callback is not callable
        if not callable(callback):
            # if the conditional is callable
            # as in: @object.when
            if callable(conditional):
                def wrapper(callback):
                    callback(self, conditional(self))

                conditional.callback = wrapper

                #return the condition to have global access to it
                return conditional

            # otherwise the conditional is not callable
            # as in: @object.when(True)
            def wrapper(callback):
                callback(self, conditional)

            return wrapper

        # otherwise the callback is callable
        # if the conditional is callable
        if callable(conditional):
            #flatten out the conditional
            conditional = conditional(self)

        #go ahead and call the callback
        callback(self, conditional)

        return self

class LoopTrait:
    'Adds a generic `loop()` method used during chainable calls'

    def loop(self, callback = None):
        # if callback is callable
        # as in: @object.loop
        if callable(callback):
            index = 0
            #please return false :)
            while(callback(self, index) != False):
                index += 1
