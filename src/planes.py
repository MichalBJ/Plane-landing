import pygame
import random


images = [pygame.image.load('img/others/plane_tr.png'),
          pygame.image.load('img/others/plane_td.png'),
          pygame.image.load('img/others/plane_tl.png'),
          pygame.image.load('img/others/plane_tu.png'),
          ]

class Planes:
    def __init__(self, pos_x, pos_y, direction, altitude, speed, fuel):
        self.planes = []
        self.selected_plane = False
        self.new_game = True
        self.sc = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        self.image = images
        self.actual_image = self.image[self.direction]
        self.plane_mask = pygame.mask.from_surface(self.actual_image)
        self.altitude = altitude
        self.speed = speed
        self.fuel = fuel
        self.plus_altitude = False
        self.minus_altitude = False
        self.setter_altitude = 100
        self.plus_speed = False
        self.minus_speed = False
        self.setter_speed = 50
        self.score = 0
        self.next_plane = 2700
        self.crash = False
        self.crash_time = 0
        self.crash_x = 0
        self.crash_y = 0
        self.start_count_plane = 0
        self.fuel_setting_min = 0
        self.fuel_setting_max = 0
        self.time_to_new_plane = 0
        self.next_level = 5


    def draw(self, dest, font, element):
        for plane in self.planes:
            if plane.selected_plane == True:
                pygame.draw.rect(dest, 'black', (plane.pos_x - 2, plane.pos_y - 2,
                                                 plane.actual_image.get_width() + 2,
                                                 plane.actual_image.get_height() + 2),
                                                 width=1
                                                )
            if plane.plus_altitude == True or plane.minus_altitude == True:
                color_alt = 'red'
            else:
                color_alt = 'black'
            if plane.plus_speed == True or plane.minus_speed == True:
                color_speed = 'red'
            else:
                color_speed = 'black'
            info_altitude = font.render(f'ALTITUDE: {plane.altitude} m', True, color_alt)
            info_speed = font.render(f'SPEED: {plane.speed} km/h', True, color_speed)
            info_fuel = font.render(f'FUEL: {plane.fuel} L', True, 'black')
            dest.blit(plane.actual_image, (plane.pos_x, plane.pos_y))
            dest.blit(info_altitude, (plane.pos_x, plane.pos_y - 48))
            dest.blit(info_speed, (plane.pos_x, plane.pos_y - 33))
            dest.blit(info_fuel, (plane.pos_x, plane.pos_y - 18))




    def start_new_game(self):
        if self.new_game == True:
            for plane in range(self.start_count_plane):
                self.pos_x = random.randrange(50, 1100)
                self.pos_y = random.randrange(150, 600)
                self.direction = random.randrange(0, 4)
                self.altitude = random.randrange(7000, 10000, 200)
                self.speed = random.randrange(600, 900, 50)
                self.fuel = random.randrange(self.fuel_setting_min, self.fuel_setting_max)
                self.planes.append(Planes(self.pos_x, self.pos_y, self.direction, self.altitude, self.speed, self.fuel))
            self.new_game = False

    def select_plane(self, mouse_pos, mouse_click, plus_alt_but, minus_alt_but, plus_speed_but, minus_speed_but):
        if mouse_pos[0] in range(0, 1280) and mouse_pos[1] in range(100, 780) and mouse_click:
            for plane in self.planes:
                if mouse_pos[0] in range(int(plane.pos_x), int(plane.pos_x) + plane.actual_image.get_width()) and mouse_pos[1] in range(int(plane.pos_y),
                                            int(plane.pos_y) + plane.actual_image.get_height()):
                    plane.selected_plane = True
                    if plane.plus_altitude == True:
                        plus_alt_but.active = True
                    elif plane.minus_altitude == True:
                        minus_alt_but.active = True

                    if plane.plus_speed == True:
                        plus_speed_but.active = True
                    elif plane.minus_speed == True:
                        minus_speed_but.active = True
                else:
                    plane.selected_plane = False



    def move(self, width, height):
        for plane in self.planes:
            if plane.direction == 0:
                plane.pos_x += (1 + plane.speed / 1000)
                if plane.pos_x > width:
                    plane.pos_x = 0 - plane.actual_image.get_width() + 5
            elif plane.direction == 1:
                plane.pos_y += (1 + plane.speed / 1000)
                if plane.pos_y > height - 180:
                    plane.pos_y = 0 - plane.actual_image.get_height() + 100
            elif plane.direction == 2:
                plane.pos_x -= (1 + plane.speed / 1000)
                if plane.pos_x < 0:
                    plane.pos_x = width - plane.actual_image.get_width() + 5
            elif plane.direction == 3:
                plane.pos_y -= (1 + plane.speed / 1000)
                if plane.pos_y < 100 - plane.actual_image.get_height() + 3:
                    plane.pos_y = 780 - plane.actual_image.get_height() + 5

    def change_direction(self, r_button, l_button):
        for plane in self.planes:
            if plane.selected_plane == True:
                if r_button.to_right == True:
                    plane.direction += 1
                    if plane.direction == 4:
                        plane.direction = 0
                    r_button.to_right = False
                if l_button.to_left == True:
                    plane.direction -= 1
                    if plane.direction == -1:
                        plane.direction = 3
                    l_button.to_left = False
                plane.actual_image = self.image[plane.direction]

    def fuel_consume(self, time, tik):
        for plane in self.planes:
            plane.fuel -= 1

    def change_altitude(self, time, tik):
        if time.time % tik == 0:
            for plane in self.planes:
                if plane.plus_altitude == True:
                    plane.altitude += plane.setter_altitude
                elif plane.minus_altitude == True:
                    plane.altitude -= plane.setter_altitude
                    if plane.altitude < 0:
                        plane.altitude = 0
                        continue

    def change_speed(self, time, tik):
        if time.time % tik == 0:
            for plane in self.planes:
                if plane.plus_speed == True:
                    plane.speed += plane.setter_speed
                elif plane.minus_speed == True:
                    plane.speed -= plane.setter_speed
                    if plane.speed < 0:
                        plane.speed = 0
                        continue

    def new_plane(self,  game):
        if game.time / self.next_plane == 1:
            self.pos_x = random.randrange(50, 1100)
            self.pos_y = random.randrange(150, 600)
            self.direction = random.randrange(0, 4)
            self.altitude = random.randrange(7000, 10000, 200)
            self.speed = random.randrange(600, 900, 50)
            self.fuel = random.randrange(self.fuel_setting_min, self.fuel_setting_max)
            self.planes.append(Planes(self.pos_x, self.pos_y, self.direction, self.altitude, self.speed, self.fuel))
            self.next_plane = game.time + self.time_to_new_plane

        if len(self.planes) == 0 and game.lives > 0:
            self.pos_x = random.randrange(50, 1100)
            self.pos_y = random.randrange(150, 600)
            self.direction = random.randrange(0, 4)
            self.altitude = random.randrange(7000, 10000, 200)
            self.speed = random.randrange(600, 900, 50)
            self.fuel = random.randrange(self.fuel_setting_min, self.fuel_setting_max)
            self.planes.append(Planes(self.pos_x, self.pos_y, self.direction, self.altitude, self.speed, self.fuel))
            self.next_plane = game.time + self.time_to_new_plane

        if len(self.planes) == 1 and game.lives > 0:
            self.pos_x = random.randrange(50, 1100)
            self.pos_y = random.randrange(150, 600)
            self.direction = random.randrange(0, 4)
            self.altitude = random.randrange(7000, 10000, 200)
            self.speed = random.randrange(600, 900, 50)
            self.fuel = random.randrange(self.fuel_setting_min, self.fuel_setting_max)
            self.planes.append(Planes(self.pos_x, self.pos_y, self.direction, self.altitude, self.speed, self.fuel))

    def landing_or_crash(self, road, game, button1, button2, button3, button4):
        for plane in self.planes:
            if int(plane.pos_x) in range(road.pos_x - int(plane.actual_image.get_width() / 2), road.pos_x + road.img.get_width() - int(plane.actual_image.get_width() / 2)) and int(plane.pos_y) in range(road.pos_y - int(plane.actual_image.get_height() / 2), road.pos_y + int(plane.actual_image.get_height() / 2)):
                if plane.direction == 0 or plane.direction == 2:
                    if plane.altitude <= 0 and plane.speed <= 0 and plane.fuel > 0:
                        game.score += 1
                        self.planes.remove(plane)
                        button1.active = False
                        button2.active = False
                        button3.active = False
                        button4.active = False
                    elif plane.altitude > 0 and plane.speed == 0:
                        plane.crash_results(self, game, plane, button1, button2, button3, button4)
                        self.planes.remove(plane)
            else:
                if plane.fuel == 0 or plane.altitude <= 0 or plane.speed <= 0:
                    plane.crash_results(game, plane, button1, button2, button3, button4)
                    self.planes.remove(plane)

    def crash_results(self, game, plane, button1, button2, button3, button4):
        #zistit prečo ked vlozim tuto funkciu do vyššej funkcie a ma sa vykonať preskoči to jeden cely cyklus
        game.lives -= 1
        game.animation_start = True
        game.sound_start = True
        game.ani_x = plane.pos_x - (plane.actual_image.get_width() / 2) - 10
        game.ani_y = plane.pos_y - (plane.actual_image.get_height() / 2) - 10
        button1.active = False
        button2.active = False
        button3.active = False
        button4.active = False

    def up_difficulty(self):
        if self.score > 0:
            if self.next_level / self.score == 1:
                self.time_to_new_plane -= 300
                self.next_level += 5




planes = Planes(0, 0, 0, 0, 0, 0)


#offset = (int(plane.pos_x) - road.pos_x , int(plane.pos_y) - road.pos_y - 30)
#collision = road.road_mask.overlap(plane.plane_mask, offset)
#if collision and plane.altitude <= 0 and plane.speed <= 0 and plane.fuel > 0:
                #if plane.direction == 0 or plane.direction == 2:
                    #score.score += 1
                    #self.planes.remove(plane)























