from time import sleep
from itertools import cycle


class traffic_lights:

    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 3))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)


traffic_light = traffic_lights()
traffic_light.running()
