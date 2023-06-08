from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.lang import Builder
#builder string
helper_string ='''
ScreenManager: 
     Hello:
<Hello>:
     name:'hello'
     MDLabel:
          text:"HELLO WORLD"
    
      


'''
class Hello(Screen):
      pass
sm=ScreenManager()
sm.add_widget(Hello(name='hello'))
class DemoApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(helper_string)
        return self.strng
DemoApp().run()