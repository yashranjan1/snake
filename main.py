import pygame


def main() -> None:
    pygame.init()
    pygame.display.set_mode((500, 800))
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
