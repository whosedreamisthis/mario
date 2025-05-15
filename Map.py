import pygame as pg
from pytmx.util_pygame import load_pygame
from Const import *
from Event import Event
from GameUI import GameUI
from BGObject import BGObject
from Camera import Camera
class Map(object):
    """

    This class will contain every map object: tiles, mobs and player. Also,
    there are camera, event and UI.

    """

    def __init__(self, world_num):
       

        self.o_event = Event()
        self.o_gameUI = GameUI()
        
        self.map_size = (0,0)
        self.sky = 0
        self.obj = []
        self.obj_bg = []
        self.loadWorld_11()
        

      
        self.o_camera = Camera(self.map_size[0] * 500, 14)

    def loadWorld_11(self):
        tmx_data = load_pygame("worlds/tmx/W11.tmx")
        self.map_size = (tmx_data.width,tmx_data.height)
        self.sky = pg.Surface((WINDOW_W,WINDOW_W))
        self.sky.fill(pg.Color("#5c94fc"))
        
        self.map = [[0]*tmx_data.height for i in range(tmx_data.width)]

        layer_num = 0
        
        for layer in tmx_data.visible_layers:
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):
                    image = tmx_data.get_tile_image(x,y,layer_num)
                    
                    if image is not None:
                        tile_ID = tmx_data.get_tile_gid(x,y, layer_num)
                        
                        if layer.name == "Background":
                            self.map[x][y] = BGObject(x*tmx_data.tileheight,y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
                        # print(f"{x} {y} {self.map[x][y]}")
            layer_num += 1

    def get_camera(self):
        return self.o_camera
    

    def update(self, core):

        
        pass
        
    
    def render_map(self, core):
        """

        Rendering only tiles. It's used in main menu.

        """
        core.screen.blit(self.sky,(0,0))

    def render(self, core):
        """

        Renders every object.

        """
        core.screen.blit(self.sky,(0,0))
        
        for obj in self.obj_bg:
            obj.render(core)
            

     
























