# Singleton pattern guarantees that there will be a single instance of a certain class in the program.
class Singleton(type):
    _instances = {}

# The __call__ method is called when the instance is accessed as a function.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # super(type, obj) -> bound super object; requires isinstance(obj, type)
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(a)
    print(b)
    print(a is b)
