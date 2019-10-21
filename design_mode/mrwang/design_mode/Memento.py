# -*- coding:utf-8 -*-
"""
备忘录:
意图：在不被破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样以后就可将该对象恢复到原来保存的状态。
适应性：
必须保存一个对象在某一个时刻的（部分）状态。这样以后需要的时候他才能恢复到先前状态。
如果一个用捷库来让其他对象直接得到这些状态，将会暴露对象的实现细节并破坏对象的封装性。
"""

import copy
def Memento(obj, deep=False):
    state = (copy.copy, copy.deepcopy)[bool(deep)](obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore

class Transaction:
    """
    Adds transactional semantics to methods. Methods decorated with @transational will rollback to entry state upon exceptions.
    """
    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        pass