# -*- coding:utf-8 -*-
"""
迭代器
意图：提供一共方法顺序访问一个聚合对象中各个元素，而又不需要暴露该对象的内部元素
适用性：访问一个聚合对象的内容而无需暴露它的内部表示。
支持对聚合对象的多种遍历
为遍历不动听你的聚合结构提供一个统一的接口（既：支持多迭代）
"""

def count_to(count):
    """ count by word numbers, up to a maximun of five"""
    numbers = ["one", "two", "three", "four", "five"]
    # enumeerate() returns a tuple containing a count (from start withch defaults to 0) and the values obtained form iterating over sequence
    for pos, number in zip(range(count), numbers):
        yield number

# test the generator
count_to_two = lambda : count_to(2)
count_to_five = lambda: count_to(5)

print("Counting to two")
for number in count_to_two():
    print(number)

print("         ")
print("Count to five...")
for number in count_to_five():
    print(number)
print("              ")