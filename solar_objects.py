from constants import moon_weight, moon_diameter, my_font, earth_weight, earth_diameter
from utils import SolarObject


moon = SolarObject("moon", 1 + 0j, 500 + 110j, moon_weight, moon_diameter, (0, 0, 255), my_font, (0, 0, 0), (850, 0))
earth = SolarObject("earth", 0 + 0j, 500 + 500j, earth_weight, earth_diameter, (0, 255, 0), my_font, (0, 0, 0), (850, 20))
