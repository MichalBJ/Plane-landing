import pygame.image

pygame.mixer.init()


class Buttons:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.type = None
        self.active = False
        self.image_active = None
        self.image = None
        self.tran_img_active = None
        self.tran_img = None
        self.tran_pos_x = self.pos_x
        self.tran_pos_y = self.pos_y


    def draw(self, dest, mouse_pos):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y, self.pos_y + self.image.get_height()):
            if self.type == 'B':
                if self.active == True:
                    self.tran_img_active = pygame.transform.scale(self.image_active, (int(self.image_active.get_width() * 1.05), int(self.image_active.get_height() * 1.05)))
                    x, y = self.pos_x, self.pos_y
                    x -= (int(self.image_active.get_width() * 1.05) - self.image_active.get_width()) / 2
                    y -= (int(self.image_active.get_height() * 1.05) - self.image_active.get_height()) / 2
                    dest.blit(self.tran_img_active, (x, y))
                else:
                    self.tran_img = pygame.transform.scale(self.image, (
                    int(self.image.get_width() * 1.05), int(self.image.get_height() * 1.05)))
                    x, y = self.pos_x, self.pos_y
                    x -= (int(self.image.get_width() * 1.05) - self.image.get_width()) / 2
                    y -= (int(self.image.get_height() * 1.05) - self.image.get_height()) / 2
                    dest.blit(self.tran_img, (x, y))

            else:
                self.tran_img = pygame.transform.scale(self.image, (
                    int(self.image.get_width() * 1.05), int(self.image.get_height() * 1.05)))
                x, y = self.pos_x, self.pos_y
                x -= (int(self.image.get_width() * 1.05) - self.image.get_width()) / 2
                y -= (int(self.image.get_height() * 1.05) - self.image.get_height()) / 2
                dest.blit(self.tran_img, (x, y))
        else:
            if self.type == 'B':
                if self.active == True:
                    dest.blit(self.image_active, (self.pos_x, self.pos_y) )
                else:
                    dest.blit(self.image, (self.pos_x, self.pos_y))
            else:
                dest.blit(self.image, (self.pos_x, self.pos_y))


class Button_turn_left(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 323
        self.pos_y = 795
        self.type = 'A'
        self.image = pygame.image.load('img/buttons/to_left.png')
        self.to_left = False

    def activate_turn_left(self, mouse_pos, mouse_click):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y,
                                        self.pos_y + self.image.get_height()) and mouse_click:
            self.to_left = True

class Button_turn_right(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 441
        self.pos_y = 795
        self.type = 'A'
        self.image = pygame.image.load('img/buttons/to_right.png')
        self.to_right = False

    def activate_turn_right(self, mouse_pos, mouse_click):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y,
                                        self.pos_y + self.image.get_height()) and mouse_click:
            self.to_right = True

class Button_minus_altitude(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 654
        self.pos_y = 861
        self.type = 'B'
        self.image_active = pygame.image.load('img/buttons/minus_active.png')
        self.image = pygame.image.load('img/buttons/minus.png')

    def minus_altitude(self, mouse_pos, click, other, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(
                self.pos_y, self.pos_y + self.image.get_height()) and click:
            if self.active == False and other.active == False:
                self.active = True
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.minus_altitude = True
            else:
                self.active = False
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.minus_altitude = False

        elif mouse_pos[0] in range(0, 1200) and mouse_pos[1] in range(0, 760) and click:
            self.active = False

class Button_plus_altitude(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 575
        self.pos_y = 861
        self.type = 'B'
        self.image_active = pygame.image.load('img/buttons/plus_active.png')
        self.image = pygame.image.load('img/buttons/plus.png')

    def plus_altitude(self, mouse_pos, click, other, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(
                self.pos_y, self.pos_y + self.image.get_height()) and click:
            if self.active == False and other.active == False:
                self.active = True
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.plus_altitude = True
            else:
                self.active = False
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.plus_altitude = False

        elif mouse_pos[0] in range(0, 1200) and mouse_pos[1] in range(0, 760) and click:
            self.active = False

class Button_set_minus_altitude(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 582
        self.pos_y = 829
        self.type = 'A'
        self.image = pygame.image.load('img/buttons/arrow_left.png')

    def setting_alt_minus_value(self, mouse_pos, mouse_click, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y, self.pos_y + self.image.get_height()) and mouse_click:
            for plane in planes.planes:
                if plane.selected_plane == True:
                    if plane.setter_altitude > 10:
                        plane.setter_altitude -= 10
                        break

class Button_set_plus_altitude(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 706
        self.pos_y = 829
        self.type = 'A'
        self.image = pygame.image.load('img/buttons/arrow_right.png')

    def setting_alt_plus_value(self, mouse_pos, mouse_click, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(
                self.pos_y, self.pos_y + self.image.get_height()) and mouse_click:
            for plane in planes.planes:
                if plane.selected_plane == True:
                    if plane.setter_altitude < 200:
                        plane.setter_altitude += 10
                        break

class Button_plus_speed(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 749
        self.pos_y = 861
        self.type = 'B'
        self.image_active = pygame.image.load('img/buttons/plus_active.png')
        self.image = pygame.image.load('img/buttons/plus.png')

    def plus_speed(self, mouse_pos, click, other, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(
                self.pos_y, self.pos_y + self.image.get_height()) and click:
            if self.active == False and other.active == False:
                self.active = True
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.plus_speed = True
            else:
                self.active = False
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.plus_speed = False

        elif mouse_pos[0] in range(0, 1200) and mouse_pos[1] in range(0, 760) and click:
            self.active = False

class Button_minus_speed(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 828
        self.pos_y = 861
        self.type = 'B'
        self.image_active = pygame.image.load('img/buttons/minus_active.png')
        self.image = pygame.image.load('img/buttons/minus.png')

    def minus_speed(self, mouse_pos, click, other, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(
                self.pos_y, self.pos_y + self.image.get_height()) and click:
            if self.active == False and other.active == False:
                self.active = True
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.minus_speed = True
            else:
                self.active = False
                for plane in planes.planes:
                    if plane.selected_plane == True:
                        plane.minus_speed = False

        elif mouse_pos[0] in range(0, 1200) and mouse_pos[1] in range(0, 760) and click:
            self.active = False

class Button_set_minus_speed(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 757
        self.pos_y = 829
        self.type = 'A'
        self.image = pygame.image.load('img/buttons/arrow_left.png')

    def setting_speed_minus_value(self, mouse_pos, mouse_click, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(
                self.pos_y, self.pos_y + self.image.get_height()) and mouse_click:
            for plane in planes.planes:
                if plane.selected_plane == True:
                    if plane.setter_speed > 10:
                        plane.setter_speed -= 10
                        break

class Button_set_plus_speed(Buttons):
    def __init__(self):
        super().__init__()
        self.pos_x = 881
        self.pos_y = 829
        self.type = 'A'
        self.image = pygame.image.load('img/buttons/arrow_right.png')

    def setting_speed_plus_value(self, mouse_pos, mouse_click, planes):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(
                self.pos_y,
                self.pos_y + self.image.get_height()) and mouse_click:
            for plane in planes.planes:
                if plane.selected_plane == True:
                    if plane.setter_speed < 50:
                        plane.setter_speed += 10
                        break


class MainMenuButton:
    def __init__(self, x, y, image, image_a):
        self.pos_x = x
        self.start_pos_y = y
        self.pos_y = self.start_pos_y
        self.image = pygame.image.load(image)
        self.image_a = pygame.image.load(image_a)
        self.play_sound = True

    def draw(self, dest, mouse_pos):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y, self.pos_y + self.image.get_height()):
            dest.blit(self.image_a, (self.pos_x, self.pos_y))
            if self.play_sound == True:
                sound = pygame.mixer.Sound('sound/stop.mp3')
                pygame.mixer.Sound.set_volume(sound, 0.5)
                pygame.mixer.Sound.play(sound)
                self.play_sound = False
        else:
            dest.blit(self.image, (self.pos_x, self.pos_y))
            self.play_sound = True

    def start_animation(self, mouse_pos, click, open):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y,
                            self.pos_y + self.image.get_height()) and click:
            open.animation_start = True
            sound = pygame.mixer.Sound('sound/klik.mp3')
            pygame.mixer.Sound.set_volume(sound, 0.5)
            pygame.mixer.Sound.play(sound)

    def easy_start_settings(self, mouse_pos, click, planes, open, close, tut, cred):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y,
                                                 self.pos_y + self.image.get_height()) and click:
            planes.planes = []
            planes.start_count_plane = 3
            planes.fuel_setting_min = 7200
            planes.fuel_setting_max = 9000
            planes.time_to_new_plane = 3000
            planes.next_plane = 3000
            planes.new_game = True
            open.new_game = True
            close.animation_start = False
            close.animation_finish = False
            close.active = False
            tut.pos_y = tut.start_pos_y
            cred.pos_y = cred.start_pos_y


    def normal_start_settings(self, mouse_pos, click, planes, open, close, tut, cred):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y,
                                                 self.pos_y + self.image.get_height()) and click:
            planes.planes = []
            planes.start_count_plane = 4
            planes.fuel_setting_min = 6300
            planes.fuel_setting_max = 8100
            planes.time_to_new_plane = 2400
            planes.next_plane = 2400
            planes.new_game = True
            open.new_game = True
            close.animation_start = False
            close.animation_finish = False
            close.active = False
            tut.pos_y = tut.start_pos_y
            cred.pos_y = cred.start_pos_y

    def hard_start_settings(self, mouse_pos, click, planes, open, close, tut, cred):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y,
                                                 self.pos_y + self.image.get_height()) and click:
            planes.planes = []
            planes.start_count_plane = 5
            planes.fuel_setting_min = 5500
            planes.fuel_setting_max = 7200
            planes.time_to_new_plane = 2000
            planes.new_game = True
            planes.next_plane = 2000
            open.new_game = True
            close.animation_start = False
            close.animation_finish = False
            close.active = False
            tut.pos_y = tut.start_pos_y
            cred.pos_y = cred.start_pos_y

    def to_main_menu(self, mouse_pos, click, planes, open, close, game):
        if mouse_pos[0] in range(self.pos_x, self.pos_x + self.image.get_width()) and mouse_pos[1] in range(self.pos_y,
                                                                                                            self.pos_y + self.image.get_height()) and click:

            open.active = True
            close.game_over = False
            close.new_game = False
            game.time = 1
            game.lives = 3
            game.score = 0
            planes.planes = []



button_turn_left = Button_turn_left()
button_turn_right = Button_turn_right()
button_plus_altitude = Button_plus_altitude()
button_minus_altitude = Button_minus_altitude()
button_set_plus_altitude = Button_set_plus_altitude()
button_set_minus_altitude = Button_set_minus_altitude()
button_plus_speed = Button_plus_speed()
button_minus_speed = Button_minus_speed()
button_set_plus_speed = Button_set_plus_speed()
button_set_minus_speed = Button_set_minus_speed()

# main menu buttons
new_game = MainMenuButton(478, 263, 'img/buttons/main_menu/new_game.png', 'img/buttons/main_menu/new_game_a.png')
tutorial = MainMenuButton(478, new_game.pos_y + new_game.image.get_height() - 5 , 'img/buttons/main_menu/tutorial.png', 'img/buttons/main_menu/tutorial_a.png' )
credit = MainMenuButton(478, tutorial.pos_y + tutorial.image.get_height() - 5, 'img/buttons/main_menu/credit.png', 'img/buttons/main_menu/credit_a.png')
easy = MainMenuButton(468, new_game.pos_y + new_game.image.get_height() - 5, 'img/buttons/main_menu/easy.png', 'img/buttons/main_menu/easy_a.png' )
normal = MainMenuButton(easy.pos_x, easy.pos_y + easy.image.get_height() - 5, 'img/buttons/main_menu/normal.png', 'img/buttons/main_menu/normal_a.png' )
hard = MainMenuButton(normal.pos_x, normal.pos_y + normal.image.get_height() - 5, 'img/buttons/main_menu/hard.png', 'img/buttons/main_menu/hard_a.png' )
b_main_menu = MainMenuButton(451, 538, 'img/buttons/main_menu/main_menu.png', 'img/buttons/main_menu/main_menu_a.png')

