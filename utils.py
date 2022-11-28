from cmath import rect, phase
from dataclasses import dataclass
import pygame
from pygame import locals

from constants import G


@dataclass
class SolarObject:
    name: str
    speed: complex
    _position: complex
    weight: int
    diameter: int
    color: tuple
    scale: int
    font: pygame.font.Font
    font_color: tuple
    speed_position: tuple

    @property
    def position(self):
        return int(self._position.imag), int(self._position.real)

    def distance(self, other_position):
        return self._position - other_position

    def change_position(self):
        self._position += self.speed

    def change_speed(self, other):
        dif_pos = other.distance(self._position)
        force = G * other.weight / ((abs(dif_pos) * self.scale) ** 2)
        self.speed += rect(force, phase(dif_pos))

    def draw(self, surface):
        speed_surface = self.font.render(f'{self.name} {abs(self.speed):.2f} km/s', False, self.font_color)
        scaled_diameter = int(self.diameter / self.scale)
        pygame.draw.circle(surface, self.color, self.position, scaled_diameter)
        surface.blit(speed_surface, self.speed_position)
        if scaled_diameter < 3:
            line_pos_1 = self._position + (-10 + 10j)
            line_pos_2 = line_pos_1 + (0 + 60j)
            points = (self.position, (int(line_pos_1.imag), int(line_pos_1.real)), (int(line_pos_2.imag), int(line_pos_2.real)))
            pygame.draw.lines(surface, (100, 100, 100), False, points)
            object_surface = self.font.render(self.name, False, self.font_color)
            name_position = line_pos_1 + (-self.font.get_linesize() + 0j)
            surface.blit(object_surface, (int(name_position.imag), int(name_position.real)))


class Rocket(SolarObject):
    def control(self, key_stat):
        for key, state in key_stat.items():
            if not state:
                continue
            if key == locals.K_w:
                self.speed -= complex(0.01, 0)
            elif key == locals.K_s:
                self.speed += complex(0.01, 0)
            elif key == locals.K_d:
                self.speed += complex(0, 0.01)
            elif key == locals.K_a:
                self.speed -= complex(0, 0.01)
