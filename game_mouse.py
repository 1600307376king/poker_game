import pygame
from pygame.sprite import Sprite


class GameMouse(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1, 1))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
    
    def set_pos(self, rect):
        self.rect.center = rect
    # def update(self):
    #     self.rect.center = pygame.mouse.get_pos()
        