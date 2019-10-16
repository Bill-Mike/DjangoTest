#! /usr/bin/python
# -*-coding:utf-8 -*-
"""
Proxy
在需要用比较通用和复杂对象指针代替简单的指针的时候，使用Proxy模式。
1）远程代理（Remote Proxy）为一个对象在不同的地址空间提供局部代表。NEXTSTEP（Add94）使用NXProxy类事项这一目的。Coplien[Cop92]称这种代理为“大使”（Ambassador）》
2）虚代理（Virtual Proxy）根据需求创建开销很大的对象。
3）代理保护（Protection Proxy）控制对原始对象的访问。保护代理使用对象应该有不同的访问权限的时候。
4）智能指引（Smart Reference）取代了简单的指针，他在访问对象执行一些附加操作。它的典型用途包括：对指向实际对象的使用指针，这样当该对象没有引用时，可以自动释放他。
"""
import time
class SalesManager:
    def work(self):
        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")

class Proxy:
    def __init__(self):
        self.busy = "No"
        self.sales = None

    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == "No":
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")

if __name__ == "__main__":
    p = Proxy()
    p.work()
    p.busy = "Yes"
    p.work()