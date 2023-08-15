from public import Public
from pygame.sprite import Sprite


class Rectangle(Sprite):

    def __init__(self, public: Public):
        # Initial parameters
        super().__init__()
        self.screen = public.screen
        self.settings = public.settings
        self.image = self.settings.rectangle_image
        self.rect = self.image.get_rect()
        self.width = self.rect.height
        self.rect.midtop = self.screen.get_rect().midtop

    def blit(self):
        self.screen.blit(self.image, self.rect)
