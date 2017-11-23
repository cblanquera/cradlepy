import unittest

from src.components.event import *

class EventStub(EventTrait):
    pass

class EventHandlerStub(EventHandler):
    pass

class TestEventObserver(unittest.TestCase):
    def setUp(self):
        def callback(self):
            return self

        self.instance = EventObserver(callback)

    def tearDown(self):
        del self.instance

    def test_callback(self):
        '@covers set_callback, get_callback'
        def callback(self):
            return self

        self.instance.set_callback(callback)

        callback = self.instance.get_callback()
        self.assertEqual(callback.__name__, 'callback')

    def test_assert_equals(self):
        '@covers get_callback, assert_equals'

        callback = self.instance.get_callback()
        self.assertTrue(self.instance.assert_equals(callback))

class TestEventHandler(unittest.TestCase):
    def setUp(self):
        self.instance = EventHandler()

    def tearDown(self):
        del self.instance

    def test_events(self):
        '@covers on, trigger, match, get_meta, off'
        self.trigger1 = False
        self.trigger2 = False
        self.trigger3 = False
        self.trigger4 = False
        self.trigger5 = False

        def callback1(*args):
            self.trigger1 = True
            self.assertEqual(args[0], 'foo')
            self.assertEqual(args[1], 'bar')
            self.assertEqual(args[2], 'zoo')
            self.assertEqual(args[3], 'bam')

            self.assertTrue(self.trigger1)
            self.assertFalse(self.trigger2)
            self.assertFalse(self.trigger3)
            self.assertFalse(self.trigger4)
            self.assertFalse(self.trigger5)

            self.assertEqual(self.instance.get_meta()['pattern'], 'foobar')

        def callback2(foo, bar):
            self.trigger2 = True
            self.assertEqual(foo, 'foo')
            self.assertEqual(bar, 'bar')

            self.assertTrue(self.trigger1)
            self.assertTrue(self.trigger2)
            self.assertFalse(self.trigger3)
            self.assertFalse(self.trigger4)
            self.assertFalse(self.trigger5)

            self.assertEqual(self.instance.get_meta()['pattern'], 'foobar')

        def callback3(foo, bar, zoo):
            self.trigger3 = True
            self.assertEqual(foo, 'foo')
            self.assertEqual(bar, 'bar')
            self.assertEqual(zoo, 'zoo')

            self.assertTrue(self.trigger1)
            self.assertTrue(self.trigger2)
            self.assertTrue(self.trigger3)
            self.assertFalse(self.trigger4)
            self.assertFalse(self.trigger5)

            self.assertEqual(self.instance.get_meta()['pattern'], 'foobar')

        self.instance.on('foobar', callback2)
        self.instance.on('foobar', callback1, 2)
        self.instance.on(['foobar', 'foobar2'], callback3)

        @self.instance.on('#foo#')
        def callback4(foo, bar):
            self.trigger4 = True
            self.assertEqual(foo, 'foo')
            self.assertEqual(bar, 'bar')

            self.assertTrue(self.trigger1)
            self.assertTrue(self.trigger2)
            self.assertTrue(self.trigger3)
            self.assertTrue(self.trigger4)
            self.assertFalse(self.trigger5)

            self.assertEqual(self.instance.get_meta()['pattern'], '#foo#')

        @self.instance.on('foo%s', 0)
        def callback5(*args):
            self.trigger5 = True

            self.assertEqual(args[0], 'foo')
            self.assertEqual(args[1], 'bar')
            self.assertEqual(args[2], 'zoo')
            self.assertEqual(args[3], 'bam')

            self.assertTrue(self.trigger1)
            self.assertTrue(self.trigger2)
            self.assertTrue(self.trigger3)
            self.assertTrue(self.trigger4)
            self.assertTrue(self.trigger5)

            self.assertEqual(self.instance.get_meta()['pattern'], 'foo%s')
            self.assertEqual(self.instance.get_meta()['variables'][0], 'bar')

            return False

        self.instance.trigger('foobar', 'foo', 'bar', 'zoo', 'bam')

        self.trigger1 = False
        self.trigger2 = False
        self.trigger3 = False
        self.trigger4 = False
        self.trigger5 = False
        self.instance.trigger('foobar', 'foo', 'bar', 'zoo', 'bam')

        self.instance.off('foobar', callback1) #coverage
        self.instance.off(None, callback2) #coverage
        self.instance.off('foobar', callback3) #coverage

class TestEventTrait(unittest.TestCase):
    def setUp(self):
        self.instance = EventStub()

    def tearDown(self):
        del self.instance

    def test_get_event_handler(self):
        '@covers get_event_handler'
        handler = self.instance.get_event_handler()

        self.assertTrue(isinstance(handler, EventInterface))
        self.assertTrue(isinstance(handler, EventHandler))

    def test_events(self):
        '@covers on, trigger, off'
        self.trigger1 = False
        self.trigger2 = False
        self.trigger3 = False
        self.trigger4 = False
        self.trigger5 = False

        def callback1(*args):
            self.trigger1 = True
            self.assertEqual(args[0], 'foo')
            self.assertEqual(args[1], 'bar')
            self.assertEqual(args[2], 'zoo')
            self.assertEqual(args[3], 'bam')

            self.assertTrue(self.trigger5)
            self.assertTrue(self.trigger1)
            self.assertFalse(self.trigger4)
            self.assertFalse(self.trigger2)
            self.assertFalse(self.trigger3)

        def callback2(foo, bar, zoo):
            self.trigger2 = True
            self.assertEqual(foo, 'foo')
            self.assertEqual(bar, 'bar')
            self.assertEqual(zoo, 'zoo')

            self.assertTrue(self.trigger5)
            self.assertTrue(self.trigger1)
            self.assertTrue(self.trigger4)
            self.assertTrue(self.trigger2)
            self.assertFalse(self.trigger3)

        def callback3(foo, bar):
            self.trigger3 = True
            self.assertEqual(foo, 'foo')
            self.assertEqual(bar, 'bar')

        self.instance.on('#foo#', callback2)
        self.instance.on('foobar', callback1)
        self.instance.on('foobar2', callback3)

        @self.instance.on('foobar')
        def callback4(foo, bar):
            self.trigger4 = True
            self.assertEqual(foo, 'foo')
            self.assertEqual(bar, 'bar')

            self.assertTrue(self.trigger5)
            self.assertTrue(self.trigger1)
            self.assertTrue(self.trigger4)
            self.assertFalse(self.trigger2)
            self.assertFalse(self.trigger3)

        @self.instance.on('foobar', 2)
        def callback5(foo, bar):
            self.trigger5 = True
            self.assertEqual(foo, 'foo')
            self.assertEqual(bar, 'bar')

            self.assertTrue(self.trigger5)
            self.assertFalse(self.trigger1)
            self.assertFalse(self.trigger4)
            self.assertFalse(self.trigger2)
            self.assertFalse(self.trigger3)

        self.instance.trigger('foobar', 'foo', 'bar', 'zoo', 'bam')

    def test_set_event_handler(self):
        self.instance.set_event_handler(EventHandlerStub())
        handler = self.instance.get_event_handler()

        self.assertTrue(isinstance(handler, EventHandler))
        self.assertTrue(isinstance(handler, EventHandlerStub))

        self.instance.set_event_handler('foo') #coverage
