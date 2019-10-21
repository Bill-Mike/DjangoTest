# -*- coding:utf-8 -*-
"""
命令模式：
意图：
将一个请求封装为一个对象，从而使你可以用不同的请求对客户进行参数化，队请求排队或记录请求日志，以及支持可撤销的操作。
适用性：
抽象出待执行的动作以参数化某对象，你可是用使用构成语言中的回调（call back）函数表达式这种参数化机制。所谓回调函数是指函数先在某处注册，而它将在稍后某个需要的时候被调用.Command模式是回调机制的一个面向对象的替代品。
在不同的时刻指定、排列和执行的请求、一个Command对象可以有一个与初始请求无关的生存期。如果一个请求的接受者可用一种与地址空间无关的表达式，那么就可将负责该请求的命令对象传递给另一个不同的进程并在那里实现该请求。
支持可取消操作。Command的Excute操作可以在事项操作前将该状态存储起来，在取消操作室这个状态用来取消该操作的影响。
Command接口必须添加一个Unexecute和Execute调用的效果。执行的命令被存储在一个历史列表中。可以通过向后和向前遍历之一列表分别低阿勇UNexecute和Execute来是想重数不限的取消和重做。
支持修改日志，这样当系统崩溃是，这些修改可以被重做一遍。在Command接口添加装载操作盒存储操作，可以用来爆出变动的一个一致的修改日志。从崩溃中恢复的过程包扣从磁盘中重新读取记录下来的命令并用Execute操作重新执行他们。
用构建在原语操作上的高层操作构造一个系统。这样一种狗仔在支持事物的信息系统中很常见。一个事物封装了对数据的一组变动。Command木事提供了对食物进行操作的方法。Command有一个公共的接口，使得你可以用同一种方式调用所有的事物。同时使用该模式也易于添加新事物扩展系统。
"""

import os

class MoveFileCommand(object):
    def __init__(self,src,dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self()

    def __call__(self):
        print("renaming{} to {}".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print("renaming{} to {}".format(self.src, self.dest))
        os.rename(self.src, self.dest)

if __name__ == "__main__":
    commad_stack = []
    # command are just pushed into command stack
    commad_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    commad_stack.append(MoveFileCommand('bar.txt', 'foo.txt'))

    #they can be execute later on
    for cmd in commad_stack:
        cmd.execute()

    # and can also be undone at will
    for cmd in reversed(commad_stack):
        cmd.undo()