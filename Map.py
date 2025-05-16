import pygame as pg
from pytmx.util_pygame import load_pygame

from GameUI import GameUI

from Event import Event

from Const import *
from Platform import Platform

from Camera import Camera
from Player import Player


from BGObject import BGObject
class Map(object):
    """

    This class will contain every map object: tiles, mobs and player. Also,
    there are camera, event and UI.

    """

    def __init__(self, world_num):
        self.obj = []
        self.obj_bg = []
        
        self.tubes = []

        self.debris = []
        self.mobs = []
        self.projectiles = []
        self.text_objects = []
        self.map = 0
        self.flag = None

        self.mapSize = (0, 0)
        self.sky = 0

        self.textures = {}
        self.worldNum = world_num
        self.loadWorld_11()

        self.is_mob_spawned = [False, False]
        self.score_for_killing_mob = 100
        self.score_time = 0

        self.in_event = False
        self.tick = 0
        self.time = 400

        self.oEvent = Event()
        self.oGameUI = GameUI()
        self.oCamera = Camera(self.mapSize[0] * 32, 14)

        self.oPlayer = Player(128,351)


    def loadWorld_11(self):
        tmx_data = load_pygame("worlds/tmx/W11.tmx")
        self.mapSize = (tmx_data.width, tmx_data.height)

        self.sky = pg.Surface((WINDOW_W, WINDOW_H))
        self.sky.fill((pg.Color('#5c94fc')))

        # 2D List
        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]

        

        layer_num = 0
        for layer in tmx_data.visible_layers:
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):

                    # Getting pygame surface
                    image = tmx_data.get_tile_image(x, y, layer_num)

                    # It's none if there are no tile in that place
                    if image is not None:
                        tileID = tmx_data.get_tile_gid(x, y, layer_num)

                        if layer.name == 'Foreground':

                            # 22 ID is a question block, so in taht case we shoud load all it's images
                            if tileID == 22:
                                image = (
                                    image,                                      # 1
                                    tmx_data.get_tile_image(0, 15, layer_num),   # 2
                                    tmx_data.get_tile_image(1, 15, layer_num),   # 3
                                    tmx_data.get_tile_image(2, 15, layer_num)    # activated
                                )

                            self.map[x][y] = Platform(x * tmx_data.tileheight, y * tmx_data.tilewidth, image, tileID)
                            self.obj.append(self.map[x][y])

                        if layer.name == 'Background':
                            self.map[x][y] = BGObject(x * tmx_data.tileheight, y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
            layer_num += 1

      



    def get_Camera(self):
        return self.oCamera

    def get_player(self):
        return self.oPlayer
 

#code to get position where player is currently standing on the gound
    
   
   
    def update_player(self,core):
        self.get_player().update(core)

    def update(self, core):

        
        if not core.get_map().in_event:
             self.update_player(core)
        else:
            self.get_event().update(core)
            
        if not self.in_event:
            self.get_Camera().update(core.get_map().get_player().rect)
            

   
      
        
    
    def render_map(self, core):
        """

        Rendering only tiles. It's used in main menu.

        """
        core.screen.blit(self.sky, (0, 0))

        for obj_group in (self.obj_bg, self.obj):
            for obj in obj_group:
                obj.render(core)


    def get_blocks_for_collision(self,x,y):
        """
        
        """
        return (
            self.map[x][y-1],
            self.map[x][y+1],
            self.map[x][y],
            self.map[x-1][y],
            self.map[x-1][y+1],
            self.map[x-1][y-1],
            self.map[x+1][y],
            self.map[x+2][y],
            self.map[x+1][y+1],
            self.map[x+1][y-1],
        )
    def render(self, core):
        """

        Renders every object.

        """
        core.screen.blit(self.sky, (0, 0))

        for obj in self.obj_bg:
            obj.render(core) #clouds and so on


        

        for obj in self.obj:
            obj.render(core) #bricks

      
        self.get_player().render(core)
     

























# import pygame as pg
# from pytmx.util_pygame import load_pygame
# from Const import *
# from Event import Event
# from GameUI import GameUI
# from BGObject import BGObject
# from Camera import Camera
# from Platform import Platform

# class Map(object):
#     """

#     This class will contain every map object: tiles, mobs and player. Also,
#     there are camera, event and UI.

#     """

#     def __init__(self, world_num):
       

#         self.o_event = Event()
#         self.o_gameUI = GameUI()
        
#         self.map_size = (0,0)
#         self.sky = 0
#         self.obj = []
#         self.obj_bg = []
#         self.loadWorld_11()
        

      
#         self.o_camera = Camera(self.map_size[0] * 500, 14)

#     def loadWorld_11(self):
#         tmx_data = load_pygame("worlds/tmx/W11.tmx")
#         self.map_size = (tmx_data.width,tmx_data.height)
#         self.sky = pg.Surface((WINDOW_W,WINDOW_W))
#         self.sky.fill(pg.Color("#5c94fc"))
        
#         self.map = [[0]*tmx_data.height for i in range(tmx_data.width)]

#         layer_num = 0
        
#         for layer in tmx_data.visible_layers:
#             for y in range(tmx_data.height):
#                 for x in range(tmx_data.width):
#                     image = tmx_data.get_tile_image(x,y,layer_num)
                    
#                     if image is not None:
#                         tile_ID = tmx_data.get_tile_gid(x,y, layer_num)
                        
#                         if layer.name == "Background":
#                             self.map[x][y] = BGObject(x*tmx_data.tileheight,y * tmx_data.tilewidth, image)
#                             self.obj_bg.append(self.map[x][y])
#                         elif layer.name == "Foreground":
#                             if tile_ID == 21:
#                                 image = (image,
#                                     tmx_data.get_tile_image(0,15,layer_num),
#                                     tmx_data.get_tile_image(1,15,layer_num),
#                                     tmx_data.get_tile_image(2,15,layer_num)
#                                     )
#                             self.map[x][y] = Platform(x*tmx_data.tileheight, y*tmx_data.width,image, tile_ID)
#                             self.obj.append(self.map[x][y])
#                         # print(f"{x} {y} {self.map[x][y]}")
#             layer_num += 1

#     def get_camera(self):
#         return self.o_camera
    

#     def update(self, core):

        
#         pass
        
    
#     def render_map(self, core):
#         """

#         Rendering only tiles. It's used in main menu.

#         """
#         core.screen.blit(self.sky,(0,0))

#     def render(self, core):
#         """

#         Renders every object.

#         """
#         core.screen.blit(self.sky,(0,0))
        
#         for obj in self.obj_bg:
#             obj.render(core)
            
#         for obj in self.obj:
#             obj.render(core)
            

     
























