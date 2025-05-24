# Monostate pattern
# Diff object, same value
"""
    1. _shared1 is a class level attribute
    2. when a new object of Borg is created, first it will search for _shared1 attribute 
    in object, if it's not present all the assigned variables are stored in class level 
    attribute of same name
"""
class Borg(object):
    _shared1 = {}
    def __init__(self):
        print("calling Borg: ", self._shared1)
        self.__dict__ = self._shared1

class Singleton(Borg):
    def __init__(self, args):
        super().__init__()
        self.val = args

s1 = Singleton("Hardik")
print("s1 object ====> ", s1)
print("s1 object value ====>", s1.val)

s2 = Singleton("Deb")
print("s2 object ====> ", s2)
print("s2 object value ====>", s2.val)
print("s1 object value ====>", s1.val)

print(s1._shared1)
print(s2._shared1)