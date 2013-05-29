import util
from random import randint
from viz import drawable

SIZE = 20
TL = (20, 20)
TR = (760, 20)
BR = (760, 560)
BL = (20, 560)

class Unit(drawable):
    
    def __init__(self, utype, owner):
        self.id = util.id_generator()
        self.condition = 'Normal'
        self.owner = owner
        self.utype = utype
        
        if self.owner == 1 :
            self.x = TL[0]
            self.y = TL[1]            
        elif self.owner == 2 :
            self.x = TR[0]
            self.y = TR[1]            
        elif self.owner == 3 :
            self.x = BR[0]
            self.y = BR[1]            
        elif self.owner == 4 :
            self.x = BL[0]
            self.y = BL[1]            
                
        if self.utype == 'A' :
            pass
        elif self.utype == 'B' :
            self.y -= SIZE
        elif self.utype == 'C' :
            self.x += SIZE
        elif self.utype == 'D' :
            self.y += SIZE
        elif self.utype == 'E' :
            self.x -= SIZE
            
    def up(self):
        if self.x % 20 == 0 and self.y > 0: 
            self.y -= 1

    def down(self):
        if self.x % 20 == 0 and self.y < 580:
            self.y += 1
    
    def left(self):
        if self.y % 20 == 0 and self.x > 0:
            self.x -= 1
    
    def right(self):
        if self.y % 20 == 0 and self.x < 780:
            self.x += 1
               
    def draw(self, pygame, screen):
        pygame.draw.rect(screen, (255, 255, 0), [self.x, self.y, SIZE, SIZE], 2) 

    
    def to_json(self):
        return '{ "id" : "' + self.id + ', "x" : "' + self.x + '", "y" : "' + self.y + '", "condition" : "' + self.condition + '" }'
    
    def vision_to_json(self):
        return '{}'