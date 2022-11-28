import pygame
import PygameUtils as pu


pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()
clock_is_avalible_checkbox = pu.checkbox((255, 0, 0), 740, 10, 10, 10, text="tick available", size=20)
screen = pygame.display.set_mode([1000, 1000])
SCALE = 10 ** 6
G = 6.67430 * 10 ** -11

earth_weight = 5.972 * 10 ** 24
earth_diameter = 12_742_000

moon_weight = 7.3476 * 10 ** 22
moon_diameter = 3_474_800
