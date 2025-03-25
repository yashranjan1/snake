from enum import Enum
from typing import Optional

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WALL_SIZE
from square import ObjectType, Square


class DirectionType(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class SnakePart:
    def __init__(
        self,
        x: int,
        y: int,
        size: float,
        color: pygame.Color,
        next: Optional["SnakePart"] = None,
    ):
        self.__current: Square = Square(x, y, size, color, ObjectType.SNAKE)
        self.__next: Optional["SnakePart"] = next

    def update(self, x: int, y: int):
        next_x, next_y = self.get_x(), self.get_y()
        self.__current.shape.x = x
        self.__current.shape.y = y
        if self.__next:
            self.__next.update(next_x, next_y)

    def draw(self, screen: pygame.SurfaceType):
        self.__current.draw(screen)
        if self.__next:
            self.__next.draw(screen)

    def get_x(self):
        return self.__current.shape.x

    def get_y(self):
        return self.__current.shape.y


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.__head = SnakePart(
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WALL_SIZE, pygame.Color("white")
        )
        self.__direction = DirectionType.RIGHT

    def change_direction(self, direction: DirectionType):
        if (
            self.__direction == DirectionType.RIGHT
            or self.__direction == DirectionType.LEFT
        ) and (direction == DirectionType.UP or direction == DirectionType.DOWN):
            self.__direction = direction
        elif (
            self.__direction == DirectionType.UP
            or self.__direction == DirectionType.DOWN
        ) and (direction == DirectionType.RIGHT or direction == DirectionType.LEFT):
            self.__direction = direction

    def move(self):
        match (self.__direction):
            case DirectionType.UP:
                new_head_x, new_head_y = (
                    self.__head.get_x(),
                    self.__head.get_y() - WALL_SIZE,
                )
            case DirectionType.LEFT:
                new_head_x, new_head_y = (
                    self.__head.get_x() - WALL_SIZE,
                    self.__head.get_y(),
                )
            case DirectionType.DOWN:
                new_head_x, new_head_y = (
                    self.__head.get_x(),
                    self.__head.get_y() + WALL_SIZE,
                )
            case DirectionType.RIGHT:
                new_head_x, new_head_y = (
                    self.__head.get_x() + WALL_SIZE,
                    self.__head.get_y(),
                )

        self.__head.update(new_head_x, new_head_y)

    def draw(self, screen: pygame.SurfaceType):
        self.__head.draw(screen)
