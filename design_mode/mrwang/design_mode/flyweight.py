# -*- coding:utf-8 -*-

import weakref

class Card(object):
    """The object pool. Has builtin reference counting"""
    _CardPool = weakref.WeakValueDictionary()

    """Flyweight implementation. If the object exists in the 
    pool just return it (instead of creating a new one)"""
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit, None)
        print("create new obj")
        if not obj:
            print("running!!!!!!!!!!!!!!!!!!!!!!!")
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)

if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    print("creat c1")
    c1 = Card('9', 'h')
    print("creat c2")
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2)
    print(id(c1), id(c2))
