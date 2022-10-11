import pygame
import os
from src.buttons import *

easy_images = []
normal_images = []
hard_images = []

for x in range(10):
    add_str = str(x + 1)
    easy_images.append(pygame.image.load(os.path.join('img/buttons/main_menu/animation', 'easy' + add_str + '.png')))

for x in range(10):
    add_str = str(x + 1)
    normal_images.append(pygame.image.load(os.path.join('img/buttons/main_menu/animation', 'normal' + add_str + '.png')))

for x in range(10):
    add_str = str(x + 1)
    hard_images.append(pygame.image.load(os.path.join('img/buttons/main_menu/animation', 'hard' + add_str + '.png')))

class MainMenu:
    def __init__(self):
        self.image = pygame.image.load('img/others/main_menu_bg.png')
        self.active = True
        self.animation_start = False
        self.easy_anim_images = easy_images
        self.easy_counter = 0
        self.animation_finish = False
        self.normal_anim_images = normal_images
        self.normal_counter = 0
        self.hard_anim_images = hard_images
        self.hard_counter = 0



    def draw(self, dest, mouse_pos):
        dest.blit(self.image, (0, 0))
        new_game.draw(dest, mouse_pos)
        tutorial.draw(dest, mouse_pos)
        credit.draw(dest, mouse_pos)
        self.animation(dest)
        if self.animation_finish == True:
            easy.draw(dest, mouse_pos)
            normal.draw(dest, mouse_pos)
            hard.draw(dest, mouse_pos)
        pygame.display.update()

    def animation(self, dest):
        if self.animation_start == True:
            if credit.pos_y < 806:
                tutorial.pos_y += 10
                credit.pos_y += 10
            if tutorial.pos_y >= 450 and self.easy_counter < 10:
                dest.blit(self.easy_anim_images[self.easy_counter], (new_game.pos_x - 10, new_game.pos_y + new_game.image.get_height() - 5))
                self.easy_counter += 1
            else:
                if self.easy_counter == 10:
                    dest.blit(self.easy_anim_images[9], (new_game.pos_x - 10, new_game.pos_y + new_game.image.get_height() - 5))

            if tutorial.pos_y >= 549 and self.normal_counter < 10:
                dest.blit(self.normal_anim_images[self.normal_counter],
                            (easy.pos_x, easy.pos_y + easy.image.get_height() - 5))
                self.normal_counter += 1
            else:
                if self.normal_counter == 10:
                    dest.blit(self.normal_anim_images[self.normal_counter - 1],
                            (easy.pos_x, easy.pos_y + easy.image.get_height() - 5))

            if tutorial.pos_y >= 632 and self.hard_counter < 10:
                dest.blit(self.hard_anim_images[self.hard_counter],
                            (normal.pos_x, normal.pos_y + normal.image.get_height() - 5))
                self.hard_counter += 1

            if self.easy_counter == 10 and self.normal_counter == 10 and self.hard_counter == 10:
                self.animation_finish = True
                self.animation_start = False
                self.easy_counter = 0
                self.normal_counter = 0
                self.hard_counter = 0





main_menu = MainMenu()
