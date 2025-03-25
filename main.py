from typing import List

import pygame

from constants import (
    BOUND_HEIGHT,
    BOUND_WIDTH,
    OFFSET_X,
    OFFSET_Y,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WALL_SIZE,
)
from snake import Snake
from wall import Wall


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    walls: List[Wall] = []
    snake = Snake()

    for i in range(OFFSET_X, OFFSET_X + BOUND_WIDTH + 1, WALL_SIZE):
        top = Wall(i, OFFSET_Y, WALL_SIZE, pygame.Color("white"))
        bottom = Wall(i, OFFSET_Y + BOUND_HEIGHT, WALL_SIZE, pygame.Color("white"))
        walls.extend([top, bottom])

    for i in range(OFFSET_Y, OFFSET_Y + BOUND_HEIGHT + 1, WALL_SIZE):
        left = Wall(OFFSET_X, i, WALL_SIZE, pygame.Color("white"))
        right = Wall(OFFSET_X + BOUND_WIDTH, i, WALL_SIZE, pygame.Color("white"))
        walls.extend([left, right])

    while running:
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("#000000")

        for wall in walls:
            wall.draw(screen)

        snake.move()
        snake.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
