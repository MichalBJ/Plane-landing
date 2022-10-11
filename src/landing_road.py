import pygame

class LandingRoad:
    def __init__(self):
        self.img = pygame.image.load('img/others/landing_place.png')
        self.road_mask = pygame.mask.from_surface(self.img)
        self.pos_x = 640 - int(self.img.get_width() / 2)
        self.pos_y = 480 - int(self.img.get_height() / 2)

    def draw(self, dest):
        dest.blit(self.img, (self.pos_x, self.pos_y))


landing_road = LandingRoad()