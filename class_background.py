import pygame

class Background:

    def __init__(self, x_pos, y_pos, pic):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pic = pygame.image.load(pic)

    def Movement(self):
        self.x_pos -= 5    
