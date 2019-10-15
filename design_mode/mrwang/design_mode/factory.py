# -*- coding:utf-8 -*-
class ChinaGetter:
    """A simple localizer la gettext"""
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglisthGetter:
    """simple echoes the msg ids"""

    def get(self,msgid):
        return str(msgid)

def get_localizer(languege="English"):
    """the factory method"""
    langueges = dict(English=EnglisthGetter, China=ChinaGetter)
    return langueges[languege]()

# create our localizers
e,g = get_localizer("English"),get_localizer("China")
#localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))

