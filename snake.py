from enum import Enum
from typing import List, Optional, Tuple

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, WALL_SIZE
from square import ObjectType, Square
from wall import Wall


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

    def update(self, x: int, y: int, snake: "Snake"):
        next_x, next_y = self.get_x(), self.get_y()
        self.__current.shape.x = x
        self.__current.shape.y = y
        if self.__next:
            self.__next.update(next_x, next_y, snake)
        else:
            snake.set_after_tail((next_x, next_y))

    def draw(self, screen: pygame.SurfaceType):
        self.__current.draw(screen)
        if self.__next:
            self.__next.draw(screen)

    def has_collided_with(self, obj: Square):
        return self.__current.has_collided_with(obj)

    def get_x(self):
        return self.__current.shape.x

    def get_y(self):
        return self.__current.shape.y

    def get_next(self):
        return self.__next

    def set_next(self, next: "SnakePart"):
        self.__next = next

    def has_next(self):
        return True if self.__next is not None else False

    def is_on(self, x: int, y: int) -> bool:
        if self.__current.shape.x == x and self.__current.shape.y == y:
            return True
        elif self.__next:
            self.__next.is_on(x, y)
        else:
            return False


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        next = SnakePart(
            SCREEN_WIDTH // 2 - WALL_SIZE,
            SCREEN_HEIGHT // 2,
            WALL_SIZE,
            pygame.Color("white"),
        )
        self.__head = SnakePart(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            WALL_SIZE,
            pygame.Color("white"),
            next,
        )
        self.__tail = next
        self.__after_tail: Tuple[int, int]
        self.__direction = DirectionType.RIGHT

    def set_after_tail(self, new_after_tail: Tuple[int, int]):
        self.__after_tail = new_after_tail

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

        self.__head.update(new_head_x, new_head_y, self)

    def has_collided_with(self, obj: Square):
        return self.__head.has_collided_with(obj)

    def has_collided_with_wall(self, walls: List[Wall]):
        for wall in walls:
            if self.has_collided_with(wall):
                return True
        return False

    def draw(self, screen: pygame.SurfaceType):
        self.__head.draw(screen)

    def has_eaten_fruit(self):
        new_part = SnakePart(
            self.__after_tail[0], self.__after_tail[1], WALL_SIZE, pygame.Color("white")
        )
        self.__tail.set_next(new_part)
        self.__tail = new_part

    def get_head(self):
        return self.__head

    def is_on(self, x: int, y: int) -> bool:
        return self.__head.is_on(x, y)
