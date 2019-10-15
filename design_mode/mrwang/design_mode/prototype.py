# -#- conding:utf-8 -#-
import copy
class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registerd object and inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

def main():
    class A:
        def __str__(self):
            return "I am A"

    a = A()
    property = Prototype()
    property.register_object('a', a)
    b = property.clone("a", a=1, b = 2, c = 3)
    print(a)
    print(b.a, b.b, b.c)

if __name__ == "__main__":
    main()