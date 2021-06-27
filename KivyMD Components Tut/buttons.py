from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder_string = '''
ScreenManager:
    Main:
<Main>:
    MDRaisedButton:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        text: 'Predict'
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