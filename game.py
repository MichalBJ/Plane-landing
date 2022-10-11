from src.main_menu import *
from src.buttons import *
from src.other_elements import *
from src.landing_road import *
import pygame


pygame.init()
plane_font = pygame.font.SysFont('arial', 13)
score_font = pygame.font.SysFont('arial', 21)
setter_font = pygame.font.SysFont('arial_black', 17)


class Game:
    def __init__(self):
        self.width = 1280
        self.height = 960
        self.new_game = False
        self.tik_value = 30
        self.win = pygame.display.set_mode((self.width, self.height))
        self.game_bg = pygame.image.load('img/others/bg.png')
        self.baner = pygame.image.load('img/others/baner.png')
        self.control_panel = pygame.image.load('img/others/ovladanie.png')
        self.game_over_bg = pygame.image.load('img/others/game_over_bg.png')
        self.game_buttons = [button_turn_left,
                             button_turn_right,
                             button_plus_altitude,
                             button_minus_altitude,
                             button_set_plus_altitude,
                             button_set_minus_altitude,
                             button_plus_speed,
                             button_minus_speed,
                             button_set_plus_speed,
                             button_set_minus_speed
                             ]
        self.mouse_pos = ()
        self.game_over = False



    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            mouse_click = False
            clock.tick(self.tik_value)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click = pygame.mouse.get_pressed(num_buttons=3)[0]
                self.mouse_pos = pygame.mouse.get_pos()

            if main_menu.active:
                main_menu.draw(self.win, self.mouse_pos)
                new_game.start_animation(self.mouse_pos, mouse_click, main_menu)
                if main_menu.animation_finish:
                    easy.easy_start_settings(self.mouse_pos, mouse_click, planes, game, main_menu, tutorial, credit)
                    normal.normal_start_settings(self.mouse_pos, mouse_click, planes, game, main_menu, tutorial, credit)
                    hard.hard_start_settings(self.mouse_pos, mouse_click, planes, game, main_menu, tutorial, credit)


            if self.new_game:
                game_elements.tik()
                self.draw(self.mouse_pos)

                # set plane if new game
                planes.start_new_game()


                # move planes
                planes.move(self.width, self.height)

                # activating and deactivating the altitude change
                button_plus_altitude.plus_altitude(self.mouse_pos, mouse_click, button_minus_altitude, planes)
                button_minus_altitude.minus_altitude(self.mouse_pos, mouse_click, button_plus_altitude, planes)
                planes.change_altitude(game_elements, self.tik_value)

                # activating and deactivating the speed change
                button_plus_speed.plus_speed(self.mouse_pos, mouse_click, button_minus_speed, planes)
                button_minus_speed.minus_speed(self.mouse_pos, mouse_click, button_plus_speed, planes)
                planes.change_speed(game_elements, self.tik_value)

                # set setter altitude and speed value
                button_set_minus_altitude.setting_alt_minus_value(self.mouse_pos, mouse_click, planes)
                button_set_plus_altitude.setting_alt_plus_value(self.mouse_pos, mouse_click, planes)
                button_set_minus_speed.setting_speed_minus_value(self.mouse_pos, mouse_click, planes)
                button_set_plus_speed.setting_speed_plus_value(self.mouse_pos, mouse_click, planes)


                # selected plane
                planes.select_plane(self.mouse_pos, mouse_click, button_plus_altitude, button_minus_altitude, button_plus_speed, button_minus_speed)

                # turn planes right or left
                button_turn_left.activate_turn_left(self.mouse_pos, mouse_click)
                button_turn_right.activate_turn_right(self.mouse_pos, mouse_click)
                planes.change_direction(button_turn_right, button_turn_left)

                planes.fuel_consume(game_elements, self.tik_value)
                planes.new_plane(game_elements)

                planes.landing_or_crash(landing_road,
                                        game_elements,
                                        button_plus_altitude,
                                        button_minus_altitude,
                                        button_plus_speed,
                                        button_minus_speed,
                                        )

                planes.up_difficulty()
                game_elements.crash_sound()

                self.end_game(game_elements)
            if self.game_over:
                b_main_menu.to_main_menu(self.mouse_pos, mouse_click, planes, main_menu, game, game_elements)

        pygame.quit()

    def draw(self, mouse_pos):
        self.win.blit(self.game_bg, (0, 0))

        landing_road.draw(self.win)

        planes.draw(self.win, plane_font, game_elements)

        self.win.blit(self.baner, (0, 0))
        self.win.blit(self.control_panel, (0, 780))

        for button in self.game_buttons:
            button.draw(self.win, mouse_pos)

        game_elements.draw(score_font, self.win, planes, self.tik_value, setter_font)
        game_elements.animation(self.win)
        if self.game_over:
            self.win.blit(self.game_over_bg, (0, 0))
            b_main_menu.draw(self.win, self.mouse_pos)
            game_elements.final_score(self.win, score_font)

        pygame.display.update()

    def end_game(self, game):
        if game.lives == 0:
            self.game_over = True

if __name__ == '__main__':

    game = Game()
    game.run()
