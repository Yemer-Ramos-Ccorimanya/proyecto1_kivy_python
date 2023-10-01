
import kivy
import sqlite3
import os
from kivy.config import Config
Config.set("graphics","width","340")
Config.set("graphics", "height","640")
from kivy.app import App
from kivy.graphics import Ellipse, Line
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen

def connect_to_database(path):
    try:
        con = sqlite3.connect(path)

        cursor = con.cursor()
        create_table_productos(cursor)
        con.commit()
        con.close()
    except Exception as e:
        print(e)

def create_table_productos(cursor):
    cursor.execute(
        """
        CREATE TABLE Productos(
        ID          INT PRIMARY KEY      NOT NULL,
        Nombre      TEXT                NOT NULL,
        Marca       TEXT                NOT NULL,
        Costo      FLOAT               NOT NULL,
        Almacen     INT                 NOT NULL
        )
        """
    )

# este es el wid primcipal aca se deb agragar un boton o un afuncion de algo para que aparesca en la pantalla principal
class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super(MainWid,self).__init__()
        self.APP_PATH = os.getcwd() 
        self.DB_PATH = self.APP_PATH+"/my_database.db"
        self.StartWid = StartWid(self)
        self.DataBaseWid =  DataBaseWid(self)

        wid = Screen(name='start')
        wid.add_widget(self.StartWid)
        self.add_widget(wid)

        #aca tambien lo agregamos para poderlo invocar mas tarde
        wid = Screen(name='database')
        wid.add_widget(self.DataBaseWid)
        self.add_widget(wid)

        self.goto_start()
    
    
    # estas funciones haran que se entre a una interfas diferente del interfas principal
    def goto_start(self):

        self.current = 'start'

    def goto_database(self):

        self.current = 'database'


class StartWid(BoxLayout):
    def __init__(self, mainwid,**kwargs):
        super(StartWid,self).__init__()
        self.mainwid = mainwid 

    def create_database(self):
        connect_to_database(self.mainwid.DB_PATH)

        # en esta linea invocamaos el cambio de pantallas
        self.mainwid.goto_database()  

#es el boton que contine la base de datos y que sera para agregar mas datos
# hera de Boxlayaut por eso tien como parametro este nombre       
class DataBaseWid(BoxLayout):
    
    def __init__(self, mainwid, **kwargs):
        super(DataBaseWid, self).__init__()
        self.mainwid = mainwid


class MainApp(App):
    title =' INventario SIMPLE'
    def build(self):
        return MainWid()
    
if __name__ == '__main__':
    MainApp().run()