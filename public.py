import pygame


class Public:

    def __init__(self, settings):
        self.settings = settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
