from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.behaviors import FocusBehavior
from kivy.core.window import Window

#dimensionar tela para tamanho de uma tela de celular
Window.size = (280, 500)

#imports para o banco de dados firebase
import requests
import json


class ButtonFocus(MDRaisedButton, FocusBehavior):
    ...


class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class TelaCadastro(MDCard):
    firebasedb_url = "https://boascompras-1cbe9-default-rtdb.firebaseio.com/.json"

    def fechar(self):
        self.parent.remove_widget(self)

    def cadastrarUsuario(self, nome, email, cidade):
        data = {"Nome": nome, "Email": email, "Cidade": cidade}
        res = requests.post(url=self.firebasedb_url, json=data)
        print(res) #manda os dados para o firebase
        #self.change_screen("tela_login")

class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())
    def registrar(self):
            self.add_widget(TelaCadastro())

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.primary_hue = '700'

        # self.theme_cls.theme_style = 'Dark'
        
MyApp().run()
