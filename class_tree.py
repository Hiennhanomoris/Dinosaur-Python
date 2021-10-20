import pygame

class Tree:

    def __init__(self, x_pos, y_pos, pic):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pic = pygame.image.load(pic)
        self.x_vel = 2
        self.point = 0

    def inc_point(self):
        self.point += 1
    
    def move(self):
        self.x_pos -= self.x_vel  
        if self.x_pos < 0:
            self.x_pos = 550
            self.inc_point()

        self.x_vel += 0.001
        


    