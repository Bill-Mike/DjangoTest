# -*- coding:utf-8 -*-
"""
策略模式：
意图：
定义一系类的算法，把他们一个个封装起来，并且使他们可相互替换。本模式使得算法可以独立于使用他的客户端而变化。
适用性：
许多相关的类仅仅是行为而异。策略模式提供一种用多个行为中的一个行为来配置以各类的方法。
需要使用一个算法的不同辩题，例如，你可能会定义一些放映不同的空间、时间权衡的算法。当这些变体实现为一个算法的类层次时，可以使用
算法利用客户端而不应该知道的数据。可使用策略模式以避免暴露疯赞的、于算法相关的数据结构。
一个类定义了多重昂行为，并且这些行为在这个类的操作中以多个条件语句的形式出现。将相关的条件分支移动到他们各自的strategy类中以代替这些条件语句。
"""

import types

class StrategyExample:
    def __init__(self,func=None):
        self.name = "Strategy Example 0"
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)

def execute_replacement1(self):
    print(self.name + " from execute 1")

def execute_replacement2(self):
    print(self.name + " from execute 2")

if __name__ == '__main__':
    stra0 = StrategyExample()

    stra1 = StrategyExample(execute_replacement1)
    stra1.name = "Strategy Example 1"

    stra2 = StrategyExample(execute_replacement2)
    stra2.name = "Strategy Example 2"

    stra0.execute()
    stra1.execute()
    stra2.execute()