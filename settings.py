import pygame.image


class Settings:
    """Class for storing all settings of game"""

    def __init__(self):
        # Game screen
        self.width = 800
        self.height = 600
        self.back_color = (255, 255, 255)

        # Image URLs
        self.main_path = "D:\\Final Projects\\OwnProjects\\Pacman\\Images\\"
        self.pacman_image_path = self.main_path + "Pacman.bmp"

        # Pacman
        self.pacman_speed = 1
        self.pacman_image = pygame.image.load(self.pacman_image_path)
