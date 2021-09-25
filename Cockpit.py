from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.behaviors import FocusBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

#dimensionar tela para tamanho de uma tela de celular
Window.size = (280, 500)


class ButtonFocus(MDRaisedButton, FocusBehavior):
  ...

class TelaManager(ScreenManager):
    pass

class MenuCockpit_Frutas(Screen):
    pass
class MenuCockpit_principal(Screen):
    pass
class MenuCockpit_Bebidas(Screen):
    pass
class MenuCockpit_Massas(Screen):
    pass
class MenuCockpit_Derivados(Screen):
    pass

class Main(MDApp):
    def build(self):
        return TelaManager()
Main().run()

