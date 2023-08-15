import pygame
import sys
from settings import Settings
from pacman import Pacman
from public import Public
from rectangle import Rectangle


class Game:

    def __init__(self):

        # Initial parameters
        pygame.init()
        self.settings = Settings()
        self.public = Public(self.settings)

        # Display sets
        self.screen = self.public.screen
        self.rect = self.screen.get_rect()
        self.settings.width = self.screen.get_width()
        self.settings.height = self.screen.get_height()
        pygame.display.set_caption("Pacman")

        # Pacman sets
        self.pacman = Pacman(self.public)

        # Rec sets
        self.rectangles = pygame.sprite.Group()
        self._generate_map()

    def run_game(self):

        while True:
            self._check_events()
            self._first_update_components()
            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():

            # Display events
            if event.type == pygame.QUIT:
                sys.exit()

            # Keydown events
            if event.type == pygame.KEYDOWN:
                self._keydown_events(event)

            # keyup events
            if event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):

        # Display events
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_q:
            sys.exit()

        # Pacman movement
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.pacman.image = self.settings.pacman_image
            self.pacman.forward = True
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.pacman.image = self.settings.pacman_image
            self.pacman.backward = True
            self.pacman.image = pygame.transform.rotate(self.pacman.image, 180)
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.pacman.image = self.settings.pacman_image
            self.pacman.rightward = True
            self.pacman.image = pygame.transform.rotate(self.pacman.image, -90)
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.pacman.image = self.settings.pacman_image
            self.pacman.leftward = True
            self.pacman.image = pygame.transform.rotate(self.pacman.image, 90)

    def _keyup_events(self, event):

        # Pacman movement
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.pacman.forward = False
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.pacman.backward = False
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.pacman.rightward = False
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.pacman.leftward = False

    def _first_update_components(self):
        self.pacman.pacman_movement()

    def _update_screen(self):
        self.screen.fill(self.settings.back_color)
        self.pacman.blit()
        self._draw_rectangles()
        pygame.display.flip()

    def _generate_map(self):
        rectangle_sample = Rectangle(self.public)
        width = rectangle_sample.rect.width
        height = rectangle_sample.rect.height
        number_of_alien_by_x = self.rect.width // width
        number_of_alien_by_y = self.rect.height // width - 2

        for i in range(number_of_alien_by_x):

            my_rectangle = Rectangle(self.public)
            my_rectangle.rect.x = i * width
            my_rectangle.rect.y = 0
            self.rectangles.add(my_rectangle)

        for i in range(number_of_alien_by_x):
            my_rectangle = Rectangle(self.public)
            my_rectangle.rect.x = i * width
            my_rectangle.rect.bottom = self.rect.bottom
            self.rectangles.add(my_rectangle)

        for i in range(number_of_alien_by_y):
            my_rectangle = Rectangle(self.public)
            my_rectangle.image = pygame.transform.rotate(my_rectangle.image, 90)
            my_rectangle.rect.x = 0
            my_rectangle.rect.y = 3 + height + i * width
            self.rectangles.add(my_rectangle)

        for i in range(number_of_alien_by_y):
            my_rectangle = Rectangle(self.public)
            my_rectangle.image = pygame.transform.rotate(my_rectangle.image, 90)
            my_rectangle.rect.right = self.rect.right + 4
            my_rectangle.rect.y = 3 + height + i * width
            self.rectangles.add(my_rectangle)

    def _draw_rectangles(self):

        for rectangle in self.rectangles:
            rectangle.blit()

    def _check_allow_movement(self):
        


if __name__ == "__main__":
    main = Game()
    main.run_game()
