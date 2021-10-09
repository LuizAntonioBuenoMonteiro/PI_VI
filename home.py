from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''

'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class AppBoasCompras(MDApp):
    def build(self):
        return Builder.load_file('HomeNavigationDrawer.kv')


AppBoasCompras().run()