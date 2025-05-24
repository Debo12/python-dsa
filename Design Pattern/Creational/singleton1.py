# Basic Singleton Pattern
# Same object, same value
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

s1 = Singleton()
print("s1 object ====> ", s1)
s1.data = 5

s2 = Singleton()
print("s2 object ====> ", s2)
print("s1 object ====> ", s2.data)
s2.data = 10

print("s1 object ====> ", s1.data)