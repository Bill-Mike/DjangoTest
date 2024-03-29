# -*- coding:utf-8 -*-
"""
意图：
允许一个对象再起运行时改变他的行为。对象看起来似乎修改了他的类
适用性：
一个对象的行为取决于他的状态，并且必须在运行时刻根据状态改变他的行为
一个操作中含有庞大的多分支条件语句，且这些分支依赖于该对象的状态。这个状态通常用于一个或多个枚举常量表示。通常有多个操作包含着以相同条件结构。state模式将每一个条件分支防御一个独立的类中。这事得你可以根据对象自身的请去昂讲对象的状态作为一个对象，这一对象可以不依赖于其他对象而独立变化。
"""


class State(object):
    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Scanning... Station is", self.stations[self.pos], self.name)


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio(object):
    """A radio.     It has a scan button, and an AM/FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

# Test out radio out
if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    print("*" * 10)
    print(actions)
    print("*" * 10)
    actions = actions * 2
    print(actions)
    print("*" * 10)

    for actions in actions:
        actions()