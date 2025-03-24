import pygame

from square import ObjectType, Square


class Wall(Square):
    def __init__(self, x: float, y: float, size: float, color: pygame.Color) -> None:
        super().__init__(x, y, size, color, ObjectType.WALL)
