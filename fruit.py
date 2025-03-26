import random

import pygame

from constants import BOUND_HEIGHT, BOUND_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, WALL_SIZE
from snake import Snake
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

    def respawn(self, snake: Snake):
        x, y = self.get_random_pos()

        while snake.is_on(x, y):
            x, y = self.get_random_pos()
        self.shape.x = x
        self.shape.y = y

    def get_random_pos(self):
        return random.randrange(
            self.__x_close_bound, self.__x_far_bound, WALL_SIZE
        ), random.randrange(self.__y_close_bound, self.__y_far_bound, WALL_SIZE)
