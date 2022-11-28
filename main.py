import pygame
from cmath import phase, rect
from pygame import locals

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1000, 1000])
scale = 10 ** 6

moon_speed = 1 + 0j
moon_position = 500 + 110j
moon_weight = 10000
moon_diameter = 3474800

earth_position = 500 + 500j
earth_weight = 5.972 * 10 ** 24
earth_diameter = 12_742_000

G = 6.67430 * 10 ** -11
key_stat = {locals.K_a: False, locals.K_s: False, locals.K_d: False, locals.K_w: False}

running = True
while running:
    # dt = clock.tick(30) / 1000  # sec
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
    for key, state in key_stat.items():
        if not state:
            continue
        if key == locals.K_w:
            moon_speed -= complex(0.01, 0)
        elif key == locals.K_s:
            moon_speed += complex(0.01, 0)
        elif key == locals.K_d:
            moon_speed += complex(0, 0.01)
        elif key == locals.K_a:
            moon_speed -= complex(0, 0.01)

    dif_pos = earth_position - moon_position
    earth_force = G * earth_weight / ((abs(dif_pos) * scale) ** 2)
    moon_speed += rect(earth_force, phase(dif_pos))  # * dt
    moon_position += moon_speed  # * dt

    speed_surface = my_font.render(f'{abs(moon_speed):.2f} km/s', False, (0, 0, 0))
    distance_surface = my_font.render(f'{(abs(dif_pos) * scale - earth_diameter / 2) / 1000:.2f} km', False, (0, 0, 0))

    screen.fill((255, 255, 255))
    screen.blit(speed_surface, (850, 0))
    screen.blit(distance_surface, (850, 20))

    pygame.draw.circle(
        screen,
        (0, 0, 255),
        (int(moon_position.imag), int(moon_position.real)),
        int(moon_diameter / scale)
    )
    pygame.draw.circle(
        screen,
        (0, 255, 0),
        (int(earth_position.imag), int(earth_position.real)),
        int(earth_diameter / scale)
    )
    pygame.display.flip()

pygame.quit()
