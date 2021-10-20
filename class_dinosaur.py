import pygame

from class_tree import Tree

class Dinosaur:

    def __init__(self, x_pos, y_pos, pic):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.pic = pygame.image.load(pic) 
        self.y_vel = 0

    def check_on_ground(self):
        if self.y_pos == 230:
            return True
        else:
            return False
    
    def jump(self):
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.y_pos > 210:
            self.y_vel -= 1

        # add gravity
        self.y_vel += 0.2
        if self.y_vel > 10:
            self.y_vel = 10

        if self.y_pos > 230:
            self.y_vel = 0
            self.y_pos = 230
        
        dy += self.y_vel

        self.y_pos += dy


        