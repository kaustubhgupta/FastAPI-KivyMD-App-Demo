from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name: 'main'
    MDLabel:
        text: 'Analytics Vidhya'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H4'
    MDLabel:
        text: 'Blogathon'
        halign: 'center'
        pos_hint: {'center_y':0.7}
        text_color: (1, 0.2, 0.3, 1)
        font_style: 'H5'
        theme_text_color: 'Custom'
'''

class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))

class App(MDApp):   
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        return self.help_string

App().run()