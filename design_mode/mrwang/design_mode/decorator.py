# -*- coding:utf-8 -*-
class foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")

class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("decoratee f1")
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)

u = foo()
v = foo_decorator(u)
v.f1()
v.f2()

