import pygame

class Score:
    def __init__(self, font, size):
        self.font = pygame.font.SysFont(font, size)
        self.point = 0

    def inc_score(self):
        self.point += 1