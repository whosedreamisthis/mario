import pygame as pg
from Const import *

class Player:
    def __init__(self, x_pos,y_pos):
        self.num_lives = 3
        self.score = 0
        self.coins = 0
        
        self.visible = True
        self.power_level = 0
        self.unkillable=False
        self.unkillable_time=  0
        
        self.inLevelUpAnimation = False
        self.inLevelUpAnimationTime = 0
        
        self.inLevelDownAnimation = False
        self.inLevelDownAnimationTime = 0
        
        self.x_vel = 0.0
        
        self.y_vel = 0.0
        
        self.direction = True
        self.on_ground = False
        self.fast_moving = False
        
        self.pos_x = x_pos
        self.pos_y = y_pos
        self.image = pg.image.load("images/Mario/mario.png").convert_alpha()
        self.sprites = []
        self.rect = pg.Rect(x_pos,y_pos,32,32)

    def load_sprites(self):
        self.sprites = [
            pg.image.load("images/Mario/mario.png").convert_alpha(),
            pg.image.load("images/Mario/mario_move0.png").convert_alpha(),
            pg.image.load("images/Mario/mario_move1.png").convert_alpha(),
            pg.image.load("images/Mario/mario_move2.png").convert_alpha(),
            pg.image.load("images/Mario/mario_jump.png").convert_alpha(),
            pg.image.load("images/Mario/mario_end.png").convert_alpha(),
            pg.image.load("images/Mario/mario_end1.png").convert_alpha(),
            pg.image.load("images/Mario/mario_st.png").convert_alpha()
            

            
        ]
        
        for i in range(len(self.sprites)):
            self.sprites.append(pg.transform.flip(self.sprites[i]), 180,0)
        
    def update(self,core):
        self.player_physics (core)
        self.update_image(core)
    
    def set_image (self,image_id):
        if self.direction == True:
            self.image = self.sprites[image_id % 8]
        else:
            self.image = self.sprites[(image_id % 8) + 8]
            
    def update_image(self,core):
        pass
    
    def render(self,core):
        if self.visible:
            core.screen.blit(self.image,core.get_map().get_Camera().apply(self))
    def move_left():
        pass
    def move_right():
        pass