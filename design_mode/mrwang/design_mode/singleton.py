# -#- coding:utf-8 -#-
class Singleton(object):
    ''''' A python style singleton '''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam()
    print(id(s1), s1)
    s2 = SingleSpam()
    print(id(s2), s2)
    print(id(s1), s1)