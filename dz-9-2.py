class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt(self):
        asphalt = self._length * self._width * 25 * 5 / 1000
        return asphalt


dimension_road = Road(35, 7500)
print(dimension_road.calc_asphalt(), '(Т.)')
