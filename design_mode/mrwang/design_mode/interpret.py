# -*- coding=utf-8 -*-
"""
解释器模式：
意图：给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器用来表示语言中的句子。
适用性：
当有一个语言需要解释执行，并且你可将该语言中的句子表示为一个抽象语法树时，可使用解释器模式。当存在以下情况是该模式效果最好：
该文法简单对于复杂的文法，问答的类层次变得庞大而无法管理。此时语法分析程序生成这样的工具是最好的选择。他们无需构建抽象语法树即可集是表达式，这样可以节省空间而却可以节省时间。
效率不是一个关键问题，高效的解释器通常不是通过解释器语法解析树实现的，而是首先将他们转换成另一种形式。例如，正则表达式，通常被转换称状态机。但是即使种种情况下，转换机仍然可以用解释器实现，该模式仍是有用的。
"""

class Context:
    def __init__(self):
        self.imput = None
        self.output = None
        pass
    pass

class AbractExpression:
    def Interpret(self, context):
        pass
    pass

class Expression(AbractExpression):
    def Interpret(self, context):
        print("terminal interpret")

class NonterminalExpression(AbractExpression):
    def Interpret(self, context):
        print("Nonterminal interpret")

if __name__ == "__main__":
    context = []
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)