import pygame
from pygame import locals

from constants import my_font, screen, clock, clock_is_avalible_checkbox
from solar_objects import moon, earth
from utils import Rocket

pygame.init()

rocket = Rocket("rocket", 0 + 0j, 10 + 10j, 1000, 5, (255, 0, 0), my_font, (0, 0, 0), (850, 40))
key_stat = {locals.K_a: False, locals.K_s: False, locals.K_d: False, locals.K_w: False}

running = True
while running:
    if clock_is_avalible_checkbox.check:
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
            if clock_is_avalible_checkbox.isOver(pos):
                clock_is_avalible_checkbox.convert()

    rocket.control(key_stat)
    moon.change_speed(earth, dt)
    rocket.change_speed(earth, dt)
    rocket.change_speed(moon, dt)
    moon.change_position(dt)
    rocket.change_position(dt)

    screen.fill((255, 255, 255))
    clock_is_avalible_checkbox.draw(screen)

    moon.draw(screen)
    earth.draw(screen)
    rocket.draw(screen)
    pygame.display.flip()

pygame.quit()
