import unittest

from src.components.helper import *

class HelperStub(ConditionalTrait, LoopTrait):
    ordered = [4, 5, 6, 7]

class TestConditionalTrait(unittest.TestCase):
    def setUp(self):
        self.instance = HelperStub()

    def tearDown(self):
        del self.instance

    def test_when(self):
        self.trigger1 = False
        self.trigger2 = False
        self.trigger3 = False
        self.trigger4 = False

        @self.instance.when
        def test(instance):
            self.trigger1 = True
            return False

        @test.callback
        def callback1(instance, results):
            self.trigger2 = True
            self.assertFalse(results)

        @self.instance.when(True)
        def callback2(instance, results):
            self.trigger3 = True
            self.assertTrue(results)

        def callback3(instance, results):
            self.trigger4 = True
            self.assertFalse(results)

        self.instance.when(test, callback3)

        self.assertTrue(self.trigger1)
        self.assertTrue(self.trigger2)
        self.assertTrue(self.trigger3)
        self.assertTrue(self.trigger4)

class TestLoopTrait(unittest.TestCase):
    def setUp(self):
        self.instance = HelperStub()

    def tearDown(self):
        del self.instance

    def test_loop(self):
        self.trigger1 = False
        @self.instance.loop
        def iterate(instance, i):
            self.trigger1 = True
            if i < 4:
                self.assertTrue(instance.ordered[i], HelperStub.ordered[i])
                return True
            return False
        self.assertTrue(self.trigger1)
