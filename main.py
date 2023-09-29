
import kivy

from kivy.config import Config
Config.set("graphics","width","340")
Config.set("graphics", "height","640")
from kivy.app import App
from kivy.graphics import Ellipse, Line
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen

class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super(MainWid,self).__init__()
        self.StartWid = StartWid()
        wid = Screen(name='start')
        wid.add_widget(self.StartWid)
        self.add_widget(wid)

class StartWid(BoxLayout):
    pass

class MainApp(App):
    title =' INventario SIMPLE'
    def build(self):
        return MainWid()
    
if __name__ == '__main__':
    MainApp().run()