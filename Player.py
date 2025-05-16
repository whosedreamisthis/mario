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
        
        self.x_vel = 0
        
        self.y_vel = 0
        
        self.direction = True
        self.on_ground = False
        self.fast_moving = False
        self.sprite_tick = 0
        self.pos_x = x_pos
        self.pos_y = y_pos
        self.image = pg.image.load("images/Mario/mario.png").convert_alpha()
        self.sprites = []
        self.rect = pg.Rect(x_pos,y_pos,32,32)
        self.load_sprites()

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
            self.sprites.append(pg.transform.flip(self.sprites[i], 180,0))
        
    def update(self,core):
        self.player_physics (core)
        self.update_image(core)
    
    def player_physics(self,core):
        if core.keyR:
            self.x_vel += SPEED_INCREASE_RATE
            self.direction = True
        if core.keyL:
            self.x_vel -= SPEED_INCREASE_RATE
            self.direction = False
            
        if not core.keyU:
            self.already_jumped = False
        elif core.keyU:
            if self.on_ground and not self.already_jumped:
                self.y_vel -= JUMP_POWER
                self.already_jumped = True
                self.next_jump_time = pg.time.get_ticks() + 750
        
        if not(core.keyR or core.keyL):
            if self.x_vel > 0:
                self.x_vel -= SPEED_DECREASE_RATE
            
            elif self.x_vel < 0:
                self.x_vel += SPEED_DECREASE_RATE
        
        else:
            if self.x_vel > 0:
                if self.fast_moving:
                    if self.x_vel > MAX_FASTMOVE_SPEED:
                        self.x_vel = MAX_FASTMOVE_SPEED
                    else:
                        if self.x_vel > MAX_MOVE_SPEED:
                            self.x_vel = MAX_MOVE_SPEED
            if self.x_vel < 0:
                if self.fast_moving:
                    if (-self.x_vel) > MAX_FASTMOVE_SPEED:
                        self.x_vel = -MAX_FASTMOVE_SPEED
                    else:
                        if (-self.x_vel) > MAX_MOVE_SPEED:
                            self.x_vel = -MAX_MOVE_SPEED
            
            blocks = core.get_map().get_blocks_for_collision(self.rect.x//32,self.rect.y//32)
            
            self.pos_x += self.x_vel
            self.rect.x = self.pos_x
            
            self.update_x_pos(blocks)
            
            self.rect.y = self.pos_y + self.y_vel
            self.update_y_pos(blocks,core)
            
            
                
        
    def set_image (self,image_id):
        if self.direction == True:
            self.image = self.sprites[image_id % 8]
        else:
            self.image = self.sprites[(image_id % 8) + 8]
            
    def update_image(self,core):
        self.sprite_tick += 1.0
        
        if core.keyShift:
            self.sprite_tick += 1
            
        if self.power_level in (0,1,2):
            if self.x_vel == 0:
                self.set_image(0)
                self.sprite_tick = 0
            
            elif (
                ((self.x_vel > 0) and core.keyR and not core.keyL) or
                ((self.x_vel < 0) and core.keyL and not core.keyR) or
                ((self.x_vel > 0) and not core.keyL and not core.keyR) or
                ((self.x_vel < 0) and not (core.keyL and core.keyR))):
                if (self.sprite_tick > 30):
                    self.sprite_tick = 0
                
                if self.sprite_tick <= 10:
                    self.set_image(1)

                elif 11 <=self.sprite_tick <= 20:
                    self.set_image(2) 
                elif 21 <=self.sprite_tick <= 30:
                    self.set_image(3) 
                elif self.sprite_tick == 31:
                    self.sprite_tick = 0
                    self.set_image(1)              
            elif ((self.x_vel > 0 and core.keyL and not core.keyR) or
                (self.x_vel < 0 and core.keyR and not core.keyL) or
                (self.x_vel > 0 and not (core.keyR and  core.keyL)) or
                (self.x_vel < 0 and not (core.keyR and  core.keyL))):
                self.set_image(8)
                self.sprite_tick = 0
            if not self.on_ground:
                self.sprite_tick = 0
                self.set_image(4)
    
    def render(self,core):
        if self.visible:
            core.screen.blit(self.image,core.get_map().get_Camera().apply(self))
    
    def update_x_pos(self, blocks):
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                block.debugLight = True
                if pg.Rect.colliderect(self.rect, block.rect):
                    if self.x_vel > 0:
                        self.rect.right = block.rect.left
                        self.pos_x = self.rect.left
                        self.x_vel = 0 #idle stop moving
                    elif self.x_vel < 0:
                        self.rect.left = block.rect.right
                        self.pos_x = self.rect.left
                        self.x_vel = 0

    def update_y_pos(self, blocks, core):
        self.on_ground = False
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pg.Rect.colliderect(self.rect, block.rect):

                    if self.y_vel > 0:
                        self.on_ground = True
                        self.rect.bottom = block.rect.top
                        self.y_vel = 0

                    elif self.y_vel < 0:
                        self.rect.top = block.rect.bottom
                        self.y_vel = -self.y_vel / 3