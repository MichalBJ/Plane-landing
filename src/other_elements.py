import os
from src.planes import *
import pygame


pygame.mixer.init(44100)

ani_img = []

for i in range(7):
    add_str = str(i + 1)
    ani_img.append(pygame.image.load(os.path.join('img/animation', 'a' + add_str + '.png')))

class GameElements:
    def __init__(self):
        self.time = 1
        self.score = 0
        self.score_x = 1063
        self.score_y = 37
        self.lives = 3
        self.live_x = 625
        self.live_y = 35
        self.animation_start = False
        self.sound_start = False
        self.animatiom_img = ani_img
        self.animation_count = 0
        self.ani_x = 0
        self.ani_y = 0


    def tik(self):
        self.time += 1

    def draw(self, font, dest, planes, tik, font_setting):
        info_score = font.render(f'{self.score}', True, 'white')
        dest.blit(info_score, (self.score_x, self.score_y))
        for x in range(self.lives):
            dest.blit(pygame.transform.scale(planes.image[0], (int(planes.image[0].get_width() * 0.4), int(planes.image[0].get_height() * 0.4))), (self.live_x, self.live_y))
            self.live_x += pygame.transform.scale(planes.image[0], (int(planes.image[0].get_width() * 0.4), int(planes.image[0].get_height() * 0.4))).get_width() + 3
        self.live_x = 625
        self.banner_info(planes, tik, font, dest, font_setting)

    def animation(self, dest):
        if self.animation_start == True:
            dest.blit(self.animatiom_img[self.animation_count], (self.ani_x, self.ani_y))
            if self.time % 2 == 0:
                self.animation_count += 1
                if self.animation_count > len(self.animatiom_img) - 1:
                    self.animation_count = 0
                    self.animation_start = False

    def crash_sound(self):
        if self.sound_start == True:
            sound = pygame.mixer.Sound('sound/ex.ogg')
            pygame.mixer.Sound.set_volume(sound, 0.5)
            pygame.mixer.Sound.play(sound)
            self.sound_start = False

    def banner_info(self, planes, tik, font, dest, font_setting):
        time_to_next_plane = int((planes.next_plane - self.time) / tik)
        if time_to_next_plane % 60 < 10:
            s = '0' + str(time_to_next_plane % 60)
        else:
            s = time_to_next_plane % 60
        info_time = font.render(f'0{time_to_next_plane // 60}:{s}', True, 'white')
        dest.blit(info_time, (234, 37))

        for plane in planes.planes:
            if plane.selected_plane == True:
                info_setter_speed = font_setting.render(f'{plane.setter_speed} km/h', True, (116, 228, 245))
                info_setter_altitude = font_setting.render(f'{plane.setter_altitude} m', True, (116, 228, 245))
                dest.blit(info_setter_altitude, (631, 835))
                dest.blit(info_setter_speed, (798, 835))

    def final_score(self, dest, font):
        final_score = font.render(f'{self.score}', True, (52, 154, 251))
        dest.blit(final_score, (628, 440))


game_elements = GameElements()