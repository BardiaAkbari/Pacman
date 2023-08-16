import pygame
import random

class Public:

    def __init__(self, settings):
        self.settings = settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.matrix = [[0] * 48] * 27
        self._generate_map()

    def _generate_map(self):

        my_list = []
        c = [1] * 48
        for i in range(25):
            col = []
            for j in range(46):
                col.append(1)
            my_list.append(col)
        my_list[0][0] = 0
        force_choice_pick = [1, 2, 3, 4]
        for i in range(25):
            for j in range(46):
                up = False
                down = False
                right = False
                left = False
                force_to_make_it_emtpy = False
                number_of_choices = 0

                if i > 0:
                    up = bool(my_list[i - 1][j])
                    number_of_choices += int(up)

                if i < 24:
                    down = bool(my_list[i + 1][j])
                    number_of_choices += int(down)
                if j > 0:
                    left = bool(my_list[i][j - 1])
                    number_of_choices += int(left)
                if j < 45:
                    right = bool(my_list[i][j + 1])
                    number_of_choices += int(right)

                if number_of_choices == 4:
                    force_to_make_it_emtpy = True

                if force_to_make_it_emtpy:
                    x = random.choice(force_choice_pick)
                    if x == 1:
                        my_list[i - 1][j] = 0
                    if x == 2:
                        my_list[i + 1][j] = 0
                    if x == 3:
                        my_list[i][j - 1] = 0
                    if x == 4:
                        my_list[i][j + 1] = 0

                    number_of_choices -= 1

                if number_of_choices > 0:
                    t = random.randrange(0, number_of_choices)

                while t != 0:
                    x = random.choice(force_choice_pick)

                    if x == 1 and up:
                        my_list[i - 1][j] = 0
                        t -= 1
                        continue
                    elif x == 2 and down:
                        my_list[i + 1][j] = 0
                        t -= 1
                        continue
                    elif x == 3 and left:
                        my_list[i][j - 1] = 0
                        t -= 1
                        continue
                    elif x == 4 and right:
                        my_list[i][j + 1] = 0
                        t -= 1
                        continue
        for i in range(25):
            my_list[i].insert(0, 1)
            my_list[i].insert(47, 1)

        my_list.insert(0, c)
        my_list.insert(26, c)

        self.matrix = my_list
        for i in range(27):
            print(my_list[i])