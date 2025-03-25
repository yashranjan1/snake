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
from snake import DirectionType, Snake
from wall import Wall


def move_check(snake: Snake):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        snake.change_direction(DirectionType.UP)

    if keys[pygame.K_RIGHT]:
        snake.change_direction(DirectionType.RIGHT)

    if keys[pygame.K_DOWN]:
        snake.change_direction(DirectionType.DOWN)

    if keys[pygame.K_LEFT]:
        snake.change_direction(DirectionType.LEFT)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    walls: List[Wall] = []
    snake = Snake()
    dt = 0

    for i in range(OFFSET_X, OFFSET_X + BOUND_WIDTH + 1, WALL_SIZE):
        top = Wall(i, OFFSET_Y, WALL_SIZE, pygame.Color("white"))
        bottom = Wall(i, OFFSET_Y + BOUND_HEIGHT, WALL_SIZE, pygame.Color("white"))
        walls.extend([top, bottom])

    for i in range(OFFSET_Y, OFFSET_Y + BOUND_HEIGHT + 1, WALL_SIZE):
        left = Wall(OFFSET_X, i, WALL_SIZE, pygame.Color("white"))
        right = Wall(OFFSET_X + BOUND_WIDTH, i, WALL_SIZE, pygame.Color("white"))
        walls.extend([left, right])

    while running:
        clock.tick(60)
        screen.fill("#000000")
        snake.draw(screen)

        move_check(snake)
        dt = (dt + 1) % 30

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for wall in walls:
            wall.draw(screen)

        if dt == 0:
            snake.move()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
