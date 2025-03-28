from typing import List, Optional, Tuple

import pygame

from constants import (BOUND_HEIGHT, BOUND_WIDTH, OFFSET_X, OFFSET_Y,
                       SCREEN_HEIGHT, SCREEN_WIDTH, WALL_SIZE)
from fruit import Fruit
from game_state import GameState
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


def render_text(
    txt: str,
    size: int,
    pos: Tuple[int, int],
    color: str,
    screen: pygame.SurfaceType,
    bg_color: Optional[str] = None,
) -> pygame.Rect:
    font = pygame.font.Font("freesansbold.ttf", size)

    text = font.render(txt, True, pygame.Color(color))
    rect = text.get_rect()
    rect.center = pos
    if bg_color:
        pygame.draw.rect(screen, pygame.Color(bg_color), rect)
    screen.blit(text, rect)
    return rect


def main() -> None:
    points = 0
    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    walls: List[Wall] = []
    dt = 0

    for i in range(OFFSET_X, OFFSET_X + BOUND_WIDTH + 1, WALL_SIZE):
        top = Wall(i, OFFSET_Y, WALL_SIZE, pygame.Color("white"))
        bottom = Wall(i, OFFSET_Y + BOUND_HEIGHT, WALL_SIZE, pygame.Color("white"))
        walls.extend([top, bottom])

    for i in range(OFFSET_Y, OFFSET_Y + BOUND_HEIGHT + 1, WALL_SIZE):
        left = Wall(OFFSET_X, i, WALL_SIZE, pygame.Color("white"))
        right = Wall(OFFSET_X + BOUND_WIDTH, i, WALL_SIZE, pygame.Color("white"))
        walls.extend([left, right])

    state = GameState.MENU
    snake = Snake()
    fruit = Fruit()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if state == GameState.MENU:
            render_text(
                "SNAKE", 96, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), "white", screen
            )
            start_button = render_text(
                "Play",
                54,
                (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100),
                "black",
                screen,
                "white",
            )
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(pygame.mouse.get_pos()):
                        state = GameState.ONGOING

        elif state == GameState.LOST:
            render_text(
                "GAME OVER", 72, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), "red", screen
            )
            start_button = render_text(
                "Play Again",
                54,
                (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100),
                "black",
                screen,
                "white",
            )
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(pygame.mouse.get_pos()):
                        state = GameState.ONGOING
                        snake = Snake()
                        points = 0
                        fruit = Fruit()

        elif state == GameState.ONGOING:
            screen.fill("#000000")

            render_text(
                f"Points: {points}",
                32,
                (SCREEN_WIDTH // 2, (SCREEN_HEIGHT - BOUND_HEIGHT) // 4),
                "white",
                screen,
            )

            snake.draw(screen)
            fruit.draw(screen)

            move_check(snake)
            dt = (dt + 1) % 30

            for wall in walls:
                wall.draw(screen)

            if dt == 0:
                snake.move()
                if snake.has_collided_with(fruit):
                    points += 10
                    snake.has_eaten_fruit()
                    fruit.respawn(snake)
                elif snake.has_collided_with_wall(walls):
                    state = GameState.LOST

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
