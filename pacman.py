from public import Public
from rectangle import Rectangle


class Pacman:

    def __init__(self, public: Public):

        # Initial parameters
        self.screen = public.screen
        self.settings = public.settings
        self.image = self.settings.pacman_image
        self.rect = self.image.get_rect()
        self.rectangle_sample = Rectangle(public)
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.rect.y = self.rect.x + self.rectangle_sample.rect.height
        # Moving settings
        self.forward = False
        self.backward = False
        self.rightward = False
        self.leftward = False

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def pacman_movement(self):

        if self.forward:
            self.rect.y -= self.settings.pacman_speed
        if self.backward:
            self.rect.y += self.settings.pacman_speed
        if self.rightward:
            self.rect.x += self.settings.pacman_speed
        if self.leftward:
            self.rect.x -= self.settings.pacman_speed
