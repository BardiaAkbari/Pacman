import pygame
import sys
from settings import Settings
from pacman import Pacman
from public import Public


class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.public = Public(self.settings)
        # Display sets
        self.screen = self.public.screen
        self.settings.width = self.screen.get_width()
        self.settings.height = self.screen.get_height()
        pygame.display.set_caption("Pacman")

        # Pacman sets
        self.pacman = Pacman(self.public)

    def run_game(self):

        while True:
            self._check_events()
            self._first_update_components()
            self._update_screen()
            self.second_update_components()

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
            self.pacman.forward = True
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.pacman.backward = True
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.pacman.rightward = True
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.pacman.leftward = True

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
        pygame.display.flip()




if __name__ == "__main__":
    main = Game()
    main.run_game()
