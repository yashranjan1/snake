from enum import Enum

import pygame


class ObjectType(Enum):
    WALL = 1
    SNAKE = 2
    FRUIT = 3


class Square:
    def __init__(
        self, x: float, y: float, size: float, color: pygame.Color, type: ObjectType
    ) -> None:
        self.shape = pygame.Rect(x, y, size, size)
        self.color = color
        self.type = type

    def update(self) -> None:
        pass

    def draw(self, surface: pygame.SurfaceType) -> None:
        pygame.draw.rect(surface, self.color, self.shape)
