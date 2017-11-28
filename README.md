# Cradle the Meta Framework

Cradle is a micro framework built on traits. Cradle is a different approach to developing applications in Python. It is not bound to any specific ORM or template engine, you are free to use any you like.


## Running Test

```
pip install coverage
```

```
coverage run -m unittest discover -v && coverage report
```

## Contributing

 1. Go to this directory
 2. `pip3 install -e .`
 3. Create or go to a sandbox folder (in a different directory)
 4. Create a python file and include the following and run it:

```
from cradlepy import Model
print(Model().setFoo('bar'))
```

### Notes:
 - Please use `export PYTHONDONTWRITEBYTECODE=1` during development
