import random

import pygame

from constants import BOUND_HEIGHT, BOUND_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_SIZE
from square import ObjectType, Square


class Fruit(Square):
    def __init__(self) -> None:
        self.__x_close_bound = (SCREEN_WIDTH - BOUND_WIDTH) // 2 + WALL_SIZE
        self.__x_far_bound = (SCREEN_WIDTH - BOUND_WIDTH) // 2 + BOUND_WIDTH - WALL_SIZE
        self.__y_close_bound = (SCREEN_HEIGHT - BOUND_HEIGHT) // 2 + WALL_SIZE
        self.__y_far_bound = (
            (SCREEN_HEIGHT - BOUND_HEIGHT) // 2 + BOUND_HEIGHT - WALL_SIZE
        )
        x, y = random.randrange(
            self.__x_close_bound, self.__x_far_bound, WALL_SIZE
        ), random.randrange(self.__y_close_bound, self.__y_far_bound, WALL_SIZE)
        super().__init__(x, y, WALL_SIZE, pygame.Color("green"), ObjectType.FRUIT)

    def respawn(self):
        x, y = random.randrange(
            self.__x_close_bound, self.__x_far_bound, WALL_SIZE
        ), random.randrange(self.__y_close_bound, self.__y_far_bound, WALL_SIZE)
        self.shape.x = x
        self.shape.y = y
