import pygame as pg
from pytmx.util_pygame import load_pygame
from Const import *
from Event import Event
from GameUI import GameUI
class Map(object):
    """

    This class will contain every map object: tiles, mobs and player. Also,
    there are camera, event and UI.

    """

    def __init__(self, world_num):
       

        self.oEvent = Event()
        self.oGameUI = GameUI()
      

    def loadWorld_11(self):
        pass


    

    def update(self, core):

        
        pass
        
    
    def render_map(self, core):
        """

        Rendering only tiles. It's used in main menu.

        """
        pass

    def render(self, core):
        """

        Renders every object.

        """
        pass

     
























