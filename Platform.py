import pygame as pg

class Platform(object):
    def __init__(self, x, y, image,type_ID):
        self.type_ID = type_ID
        self.image = image
        
        self.rect = pg.Rect(x,y,32,32)
        
        self.type = "Platform"
        
        self.shaking = False
        self.shaking_up = True
        self.shake_offset = 0
        
        if self.type_ID == 3:
            self.current_image = 0
            self.image_tick = 0
            self.is_activated = False
            self.bonus = "coin"
            
    def update(self):
       if self.type_ID == 3:
            self.imageTick += 1
            if self.image_tick == 50:
               self.current_image = 1
            elif self.image_tick == 60:
               self.current_image = 2
            elif self.image_tick == 70:
                self.current_image = 1
            elif self.image_tick == 80:
                self.current_image = 0
                self.image_tick = 0
               
        
    def shake(self):
        if self.shaking_up:
            self.shake_offset -= 2
            self.rect.y -= 2
        
        else:
            self.shake_offset += 2
            self.rect.y += 2
        
        if self.shake_offset == -20:
            self.shaking_up = False

        if self.shake_offset == 0:
            self.shaking = False
            self.shaking_up = True
    
    def render(self,core):
        if self.type_ID == 3:
            if not self.is_activated:
                self.update()
            elif self.shaking:
                self.shake()
            core.screen.blit(self.image,core.get_map().get_Camera().apply(self))
        
        elif self.type_ID == 2 and self.shaking:
            self.shake()
            
        else:
            core.screen.blit(self.image,core.get_map().get_Camera().apply(self))

            
        
        
        