from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder_string = '''
ScreenManager:
    Main:
<Main>:
    MDTextField:
        id: input
        hint_text: 'Enter some text'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.61, 'center_x':0.5}
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