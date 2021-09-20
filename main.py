from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.behaviors import FocusBehavior


KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'MyApp'
            left_action_items: [['menu', lambda x: x]]
            right_action_items: [['dots-vertical', lambda x: x]]
        TelaLogin:

<TelaCadastro>:
    id: cadastro
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color
        MDLabel:
            text: 'Faça o seu cadastro'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 0.9
        MDIconButton:
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1, 1, 1, 1
            on_release: root.fechar()
    MDFloatLayout:
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: 'Nome:'
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Email:'
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Cidade:'
        ButtonFocus:
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            text: 'Registrar'
            focus_color: app.theme_cls.accent_color
            unfocus_color: app.theme_cls.primary_color     
                    

<SenhaCard>:
    id: card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color
        MDLabel:
            text: 'Mudar senha'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 0.9
        MDIconButton:
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1, 1, 1, 1
            on_release: root.fechar()
    MDFloatLayout:
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: 'Código enviado por email'
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Nova senha:'
            helper_text_mode: "on_focus"
            password: True
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Confirmar nova senha:'
            helper_text_mode: "on_focus"
            password: True
        ButtonFocus:
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            text: 'Recadastrar'
            focus_color: app.theme_cls.accent_color
            unfocus_color: app.theme_cls.primary_color

<TelaLogin>:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        icon: 'account'
        user_font_size: '75sp'
    MDTextFieldRound:
        icon_left: 'email'
        size_hint_x: .8
        hint_text: 'E-mail:'
        pos_hint: {'center_x': .5, 'center_y': .6}
    MDTextFieldRound:
        id: text_field
        icon_left: 'key-variant'
        size_hint_x: .8
        hint_text: 'Senha:'
        pos_hint: {'center_x': .5, 'center_y': .5}
        password: True
    MDIconButton:
        icon: "eye-off"
        ripple_scale: .5
        pos_hint: {'center_x': .85, 'center_y': .5}
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True
    ButtonFocus:
        size_hint_x: .9
        pos_hint: {'center_x': .5, 'center_y': .4}
        text: 'Login'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        size_hint_x: .9
        pos_hint: {'center_x': .5, 'center_y': .29}
        text: 'Cadastrar'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
        on_release: root.registrar()
    MDLabel:
        pos_hint: {'center_y': .15}
        halign: 'center'
        text: 'Esqueceu sua senha?'
    MDTextButton:
        pos_hint: {'center_x': .5, 'center_y': .1}
        text: 'Clique Aqui'
        on_release: root.abrir_card()
'''


class ButtonFocus(MDRaisedButton, FocusBehavior):
    ...


class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class TelaCadastro(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

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

        return Builder.load_string(KV)


MyApp().run()