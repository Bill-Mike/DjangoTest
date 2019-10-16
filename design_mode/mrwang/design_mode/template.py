# -*- codingLutf-8 -*-
"""
意图：
定义一个操作中的算法骨架，而将一些步骤延迟到子类中。templateMethod使得子类可以不改变一个算法结构即可重新定义算法的某些特定步骤
适用性：
一次性展现一个算法的不变部分，并将可变部分留给子类来实现
各个子类中公共的行为应该被提出来并集中到一个公共父类中以避免代码重复。这是Opdyke和Johnson所描述的重分解以一般化的一个很好的例子、首先识别代码中的不同之处，并将以不同的处分奋力为一个新的操作。最后，用一个调用这些新的操作的模板方法来替换这些不同的代码。
"""

ingredients = "Spam eggs apple"
line = "_" * 10

# Skeleton
def iter_elements(getter, action):
    """template skeleton that iteration items"""
    for element in getter():
        action(element)
        print(line)

def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""
    for element in getter():
        action(element)
        print(line)

#Getter
def get_list():
    return ingredients.split()

def get_lists():
    return [list(x) for x in ingredients.split()]

#Action
def print_item(item):
    print(item)

def reverse_item(item):
    print(item[::-1])

# Make templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""
    def template():
        skeleton(getter, action)
    return template

# Create our template functions
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]
# Excute them
for template in templates:
    template()