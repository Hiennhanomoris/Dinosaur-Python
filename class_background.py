import pygame

class Background:

    def __init__(self, x_pos, y_pos, pic):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pic = pygame.image.load(pic)
        self.x_vel = 2

    def move(self):
        self.x_pos -= self.x_vel   
        if self.x_pos < -600:
            self.x_pos = 0
        self.x_vel += 0.001

