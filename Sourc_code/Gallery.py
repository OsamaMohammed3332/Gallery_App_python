from glob import glob
from random import randint
from os.path import join
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.logger import Logger




class Pictures(Scatter):
    source = StringProperty(None)


class Demo(App):
    def build(self):
        root = self.root
        for fn in glob(join('p', '*')):
            try:
                pic = Pictures(source=fn, rotation=randint(0, 5))
                root.add_widget(pic)

            except Exception:
                Logger.exception('Unable to load <%s>' % fn)


if __name__ == '__main__':
    Demo().run()
