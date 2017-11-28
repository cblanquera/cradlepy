import unittest

from cradlepy.components.data import *

class DataStub(MagicTrait, DotTrait):
    pass

class ModelStub(Model):
    def test_call(self):
        return 'called'

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
        self.instance.set_dot('foo.bar', 4)
        self.assertEqual(self.instance.is_dot('foo.bar'), True)
        self.assertEqual(self.instance.is_dot('foo'), True)
        self.assertEqual(self.instance.is_dot('bar'), False)
        self.assertEqual(self.instance.is_dot({}), False)
        self.assertEqual(self.instance.is_dot(''), False)
        self.assertEqual(self.instance.is_dot('foo.bar.zoo'), False)
        self.assertEqual(self.instance.is_dot('foo.zoo'), False)

    def test_remove_dot(self):
        '@covers: set_dot, get_dot, remove_dot, is_dot'
        test = self.instance.set_dot('foo.bar', 4).get_dot('foo.bar')
        self.assertEqual(test, 4)

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
        self.instance = Registry({'foo': {'bar': 'zoo'}})

    def tearDown(self):
        del self.instance

    def test_exists(self):
        '@covers exists'
        self.assertEqual(self.instance.exists('foo'), True)
        self.assertEqual(self.instance.exists('foo', 'bar'), True)
        self.assertEqual(self.instance.exists('foo', 'bar', 'zoo'), False)
        self.assertEqual(self.instance.exists('foo', 'zoo'), False)
        self.assertEqual(self.instance.exists(), True)

    def test_get(self):
        '@covers get, set'
        test1 = self.instance.get('foo', 'bar', 'zoo')
        self.assertEqual(test1, None)
        test2 = self.instance.set('foo', 'bar', 4).get('foo', 'bar')
        self.assertEqual(test2, 4)

        self.assertEqual(self.instance.get_foo()['bar'], 4)
        self.assertEqual(self.instance['foo']['bar'], 4)
        self.assertEqual(self.instance.foo['bar'], 4)

        self.assertEqual(self.instance.get('foo', 'bar', 'zoo'), None)
        self.assertEqual(self.instance.get('foo', 'zoo'), None)

        self.instance.set('foo', 'bar', 'zoo', 5)
        self.assertEqual(self.instance.get('foo', 'bar', 'zoo'), 5)
        self.assertEqual(self.instance.get()['foo']['bar']['zoo'], 5)

        self.instance.set() #coverage
        self.instance.set('foo') #coverage

        self.instance.set({'hello': {'hello': 'kitty'}})
        self.assertEqual(self.instance.get('foo', 'bar', 'zoo'), 5)
        self.assertEqual(self.instance.get('hello', 'hello'), 'kitty')

    def test_empty(self):
        '@covers empty'
        test = self.instance.empty('foo', 'bar')
        self.assertEqual(test, False)

        test = self.instance.set('foo', 'bar', 4).empty('foo', 'bar')
        self.assertEqual(test, True)

        test = self.instance.set('foo', 'bar', 4.5).empty('foo', 'bar')
        self.assertEqual(test, True)

        test = self.instance.set('foo', 'bar', 0).empty('foo', 'bar')
        self.assertEqual(test, True)

        test = self.instance.set('foo', 'bar', '').empty('foo', 'bar')
        self.assertEqual(test, True)

        test = self.instance.set('foo', 'bar', {}).empty('foo', 'bar')
        self.assertEqual(test, True)

        test = self.instance.set('foo', 'bar', ()).empty('foo', 'bar')
        self.assertEqual(test, True)

        test = self.instance.set('foo', 'bar', []).empty('foo', 'bar')
        self.assertEqual(test, True)

        self.assertEqual(self.instance.empty(), False)

        test = self.instance.empty('foo', 'zoo', 'bar')
        self.assertEqual(test, True)

    def test_remove(self):
        '@covers remove'
        self.instance.remove('foo', 'bar')
        self.assertEqual(self.instance.is_dot('foo.bar'), False)
        self.assertEqual(self.instance.is_dot('foo'), True)

        self.instance.remove() #coverage

class TestModel(unittest.TestCase):
    def setUp(self):
        self.instance = Model({'foo': 'bar', 'bar': 'zoo'})

    def tearDown(self):
        del self.instance

    def test_get(self):
        '@covers get'
        self.assertEqual(self.instance.get()['foo'], 'bar')
        self.assertEqual(self.instance.get()['bar'], 'zoo')

    def test_set(self):
        '@covers set'
        self.instance.set({'foo': 'zoo', 'bar': 'foo'})
        self.assertEqual(self.instance.foo, 'zoo')
        self.assertEqual(self.instance.bar, 'foo')

        self.instance.set('foo') #coverage

class TestCollection(unittest.TestCase):
    def setUp(self):
        self.instance = Collection([Model({'foo': 'bar', 'bar': 'zoo'})])

    def tearDown(self):
        del self.instance

    def test_attr(self):
        '@covers __delattr__, __getattr__, add'
        self.instance.add({'foo': 'zoo', 'bar': 'foo'})
        self.instance.add({'zoo': 'zoo', 'foo': 'foo'})

        self.assertEqual(self.instance.foo[0], 'bar')
        self.assertEqual(self.instance.foo[1], 'zoo')
        self.assertEqual(self.instance.foo[2], 'foo')

        self.assertEqual(self.instance[0].foo, 'bar')
        self.assertEqual(self.instance[1].foo, 'zoo')
        self.assertEqual(self.instance[2].foo, 'foo')

        del self.instance.foo

        self.assertEqual(self.instance.foo[0], None)
        self.assertEqual(self.instance.foo[1], None)
        self.assertEqual(self.instance.foo[2], None)

        test = self.instance.set_foo_bar('zoo').get_foo_bar()

        self.assertEqual(test[0], 'zoo')
        self.assertEqual(test[1], 'zoo')
        self.assertEqual(test[2], 'zoo')

        list = []
        list.append(ModelStub({'foo': 'bar', 'bar': 'zoo'}))
        list.append(Model({'foo': 'zoo', 'bar': 'foo'}))
        list.append(ModelStub({'zoo': 'zoo', 'foo': 'foo'}))
        self.instance = Collection(list)

        test = self.instance.test_call()

        self.assertEqual(test[0], 'called')
        self.assertEqual(test[1], False)
        self.assertEqual(test[2], 'called')

    def test__item__(self):
        '@covers __delitem__, __getitem__, __setitem__'
        self.instance.add({'foo': 'zoo', 'bar': 'foo'})
        self.instance.add({'zoo': 'zoo', 'foo': 'foo'})

        self.assertEqual(self.instance['foo'][0], 'bar')
        self.assertEqual(self.instance['foo'][1], 'zoo')
        self.assertEqual(self.instance['foo'][2], 'foo')

        self.assertEqual(self.instance[0]['foo'], 'bar')
        self.assertEqual(self.instance[1]['foo'], 'zoo')
        self.assertEqual(self.instance[2]['foo'], 'foo')
        self.assertEqual(self.instance[25], None)

        self.instance['foo'] = 'zap'
        self.assertEqual(self.instance[0]['foo'], 'zap')
        self.assertEqual(self.instance[1]['foo'], 'zap')
        self.assertEqual(self.instance[2]['foo'], 'zap')

        del self.instance['foo']

        self.assertEqual(self.instance['foo'][0], None)
        self.assertEqual(self.instance['foo'][1], None)
        self.assertEqual(self.instance['foo'][2], None)

        del self.instance[0]

        self.assertEqual(self.instance[0]['bar'], 'foo')

        del self.instance[25] #coverage

    def test__iter__(self):
        for model in self.instance:
            self.assertEqual(model.get()['foo'], 'bar')
            self.assertEqual(model.get()['bar'], 'zoo')
            break

    def test__len__(self):
        self.assertEqual(len(self.instance), 1)

    def test__str__(self):
        '@covers str'
        expected = '[\n    {\n        "foo": "bar",\n        "bar": "zoo"\n    }\n]'
        self.assertEqual(str(self.instance), expected)
        pass

    def test_add(self):
        '@covers add'
        self.instance.add({'foo': 'zoo', 'bar': 'foo'})
        self.instance.add({'zoo': 'zoo', 'foo': 'foo'})

        self.instance.add('foo')
        self.assertEqual(self.instance[0].foo, 'bar')
        self.assertEqual(self.instance[0].bar, 'zoo')
        self.assertEqual(self.instance[1].foo, 'zoo')
        self.assertEqual(self.instance[1].bar, 'foo')

    def test_cut(self):
        '@covers add, cut'
        self.instance.add({'foo': 'zoo', 'bar': 'foo'})
        self.instance.add({'zoo': 'zoo', 'foo': 'foo'})

        self.instance.cut(1)
        self.assertEqual(self.instance[1].foo, 'foo')

        self.instance.cut('first')
        self.assertEqual(self.instance[0].foo, 'foo')

        self.instance.cut('last')
        self.assertEqual(len(self.instance), 0)

        self.instance.cut(0) #coverage

    def test_each(self):
        '@covers add, each'

        self.instance.add({'foo': 'zoo', 'bar': 'foo'})
        self.instance.add({'zoo': 'zoo', 'foo': 'foo'})

        @self.instance.each
        def hello(self, index, model):
            model.set_foo('bar')

        self.assertEqual(self.instance[0]['foo'], 'bar')
        self.assertEqual(self.instance[1]['foo'], 'bar')
        self.assertEqual(self.instance[2]['foo'], 'bar')

        self.instance.each('foo') #coverage

    def test_get(self):
        '@covers get'
        test = self.instance.get()
        self.assertEqual(self.instance[0].foo, 'bar')
        self.assertEqual(self.instance[0].bar, 'zoo')

    def test_set(self):
        '@covers set'
        self.instance.set('foo') #coverage
