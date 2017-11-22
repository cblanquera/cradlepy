import unittest

from src.components.data import *

class DataStub(MagicTrait, DotTrait):
    pass

class TestMagicTrait(unittest.TestCase):
    def setUp(self):
        self.instance = DataStub()

    def tearDown(self):
        del self.instance

    def test__init__(self):
        '@covers: __init__'
        instance = DataStub()
        self.instance.foobar = 1
        instance.foobar = 2
        self.assertEqual(self.instance.foobar, 1)
        self.assertEqual(instance.foobar, 2)

    def test_attr(self):
        '@covers: __delattr__, __getattr__, __setattr__'
        self.instance.foo = 'bar';
        self.assertEqual(self.instance.foo, 'bar')
        del self.instance.foo
        self.assertEqual(self.instance.foo, None)

    def test_item(self):
        '@covers: __delitem__, __getitem__, __setitem__'
        self.instance['foo'] = 'bar';
        self.assertEqual(self.instance['foo'], 'bar')
        del self.instance['foo']
        self.assertEqual(self.instance['foo'], None)
        del self.instance['foo']
        self.assertEqual(self.instance['foo'], None)

    def test_call(self):
        '@covers: __getattr__, __delitem__, __getitem__, __setitem__'
        self.instance.set_foo_bar('MooZoo')

        self.assertEqual(self.instance.get_foo_bar(), 'MooZoo')
        self.assertEqual(self.instance['foo_bar'], 'MooZoo')
        self.assertEqual(self.instance.foo_bar, 'MooZoo')

        self.instance.set_foo_bar()
        self.assertEqual(self.instance.get_foo_bar(), None)
        self.assertEqual(self.instance['foo_bar'], None)
        self.assertEqual(self.instance.foo_bar, None)

        self.instance.set_foo_bar('MooZoo2', '__')
        self.assertEqual(self.instance.get_foo_bar('__'), 'MooZoo2')
        self.assertEqual(self.instance['foo__bar'], 'MooZoo2')
        self.assertEqual(self.instance.foo__bar, 'MooZoo2')

        self.instance.set_foo_bar(None, '__')
        self.assertEqual(self.instance.get_foo_bar('__'), None)
        self.assertEqual(self.instance['foo__bar'], None)
        self.assertEqual(self.instance.foo__bar, None)

    def test_iteration(self):
        '@covers: __iter__'
        self.instance['foo'] = 'bar';
        for key, value in self.instance:
            self.assertEqual(key, 'foo')
            self.assertEqual(value, 'bar')
            break

    def test__len__(self):
        '@covers: __len__'
        self.assertEqual(len(self.instance), 0)
        self.instance.x = 4
        self.assertEqual(len(self.instance), 1)

    def test__str__(self):
        '@covers: __str__'
        self.instance.x = 4
        self.assertEqual(str(self.instance), '{\n    "x": 4\n}')

class TestDotTrait(unittest.TestCase):
    def setUp(self):
        self.instance = DataStub()

    def tearDown(self):
        del self.instance

    def test_get_dot(self):
        '@covers: set_dot, get_dot'
        test1 = self.instance.get_dot('foo.bar')
        self.assertEqual(test1, None)
        test2 = self.instance.set_dot('foo.bar', 4).get_dot('foo.bar')
        self.assertEqual(test2, 4)

        self.assertEqual(self.instance.get_foo()['bar'], 4)
        self.assertEqual(self.instance['foo']['bar'], 4)
        self.assertEqual(self.instance.foo['bar'], 4)

        test3 = self.instance.set_dot({}, 4).get_dot({})
        self.assertEqual(test3, None)

        test4 = self.instance.set_dot('', 4).get_dot('')
        self.assertEqual(test3, None)

        self.assertEqual(self.instance.get_dot('foo.bar.zoo'), None)
        self.assertEqual(self.instance.get_dot('foo.zoo'), None)

        self.instance.set_dot('foo.bar.zoo', 5)
        self.assertEqual(self.instance.get_dot('foo.bar.zoo'), 5)

    def test_is_dot(self):
        '@covers: set_dot, is_dot'
        test2 = self.instance.set_dot('foo.bar', 4)
        self.assertEqual(self.instance.is_dot('foo.bar'), True)
        self.assertEqual(self.instance.is_dot('foo'), True)
        self.assertEqual(self.instance.is_dot('bar'), False)
        self.assertEqual(self.instance.is_dot({}), False)
        self.assertEqual(self.instance.is_dot(''), False)
        self.assertEqual(self.instance.is_dot('foo.bar.zoo'), False)
        self.assertEqual(self.instance.is_dot('foo.zoo'), False)

    def test_remove_dot(self):
        '@covers: set_dot, get_dot, remove_dot, is_dot'
        test2 = self.instance.set_dot('foo.bar', 4).get_dot('foo.bar')
        self.assertEqual(test2, 4)

        self.instance.remove_dot('foo.bar')
        self.assertEqual(self.instance.is_dot('foo.bar'), False)
        self.assertEqual(self.instance.is_dot('foo'), True)

        self.instance.remove_dot({})
        self.assertEqual(self.instance.is_dot({}), False)

        self.instance.remove_dot('')
        self.assertEqual(self.instance.is_dot(''), False)

        self.instance.remove_dot('foo.bar.zoo')
        self.assertEqual(self.instance.is_dot('foo.bar.zoo'), False)

        self.instance.remove_dot('foo.zoo')
        self.assertEqual(self.instance.is_dot('foo.zoo'), False)

    def test_set_dot(self):
        '@covers: set_dot'
        pass

class TestRegistry(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__init__(self):
        pass

    def test_exists(self):
        pass

    def test_get(self):
        pass

    def test_is_empty(self):
        pass

    def test_remove(self):
        pass

    def test_set(self):
        pass

class TestModel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__init__(self):
        pass

    def test_get(self):
        pass

    def test_set(self):
        pass

class TestCollection(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__delattr__(self):
        pass

    def test__delitem__(self):
        pass

    def test__getattr__(self):
        pass

    def test__getitem__(self):
        pass

    def test__init__(self):
        pass

    def test__iter__(self):
        pass

    def test__len__(self):
        pass

    def test__setattr__(self):
        pass

    def test__setitem__(self):
        pass

    def test__str__(self):
        pass

    def test_add(self):
        pass

    def test_cut(self):
        pass

    def test_each(self):
        pass

    def test_get(self):
        pass

    def test_set(self):
        pass
