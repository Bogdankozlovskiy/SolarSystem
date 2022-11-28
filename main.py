import pygame
from pygame import locals
import PygameUtils as pu

from constants import my_font, screen, earth_weight, moon_weight, earth_diameter, moon_diameter, clock
from utils import SolarObject, Rocket

pygame.init()

moon = SolarObject("moon", 1 + 0j, 500 + 110j, moon_weight, moon_diameter, (0, 0, 255), my_font, (0, 0, 0), (850, 0))
earth = SolarObject("earth", 0 + 0j, 500 + 500j, earth_weight, earth_diameter, (0, 255, 0), my_font, (0, 0, 0), (850, 20))
rocket = Rocket("rocket", 0 + 0j, 10 + 10j, 1000, 5, (255, 0, 0), my_font, (0, 0, 0), (850, 40))
key_stat = {locals.K_a: False, locals.K_s: False, locals.K_d: False, locals.K_w: False}
checkb = pu.checkbox((255, 0, 0), 740, 10, 10, 10, text="tick available", size=20)

running = True
while running:
    if checkb.check:
        dt = clock.tick(30) / 1000  # sec
    else:
        dt = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == locals.KEYDOWN:
            if event.key == locals.K_ESCAPE:
                running = False
            if event.key == locals.K_w:
                key_stat[locals.K_w] = True
            if event.key == locals.K_s:
                key_stat[locals.K_s] = True
            if event.key == locals.K_d:
                key_stat[locals.K_d] = True
            if event.key == locals.K_a:
                key_stat[locals.K_a] = True
        elif event.type == locals.KEYUP:
            if event.key == locals.K_w:
                key_stat[locals.K_w] = False
            if event.key == locals.K_s:
                key_stat[locals.K_s] = False
            if event.key == locals.K_d:
                key_stat[locals.K_d] = False
            if event.key == locals.K_a:
                key_stat[locals.K_a] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if checkb.isOver(pos):
                checkb.convert()

    rocket.control(key_stat)
    moon.change_speed(earth, dt)
    rocket.change_speed(earth, dt)
    rocket.change_speed(moon, dt)
    moon.change_position(dt)
    rocket.change_position(dt)

    screen.fill((255, 255, 255))
    checkb.draw(screen)

    moon.draw(screen)
    earth.draw(screen)
    rocket.draw(screen)
    pygame.display.flip()

pygame.quit()
