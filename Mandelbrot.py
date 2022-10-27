import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mandelbrot Set")

def fractal():
    for y in range(400):
        for x in range(400):
            zx, zy = cx, cy = -2 + 2.5 * x / 400.0, -1.25 + 2.5 * y / 400.0
            for i in range(25):
                zx, zy = zx * zx - zy * zy + cx, 2 * zx * zy + cy
                if zx * zx + zy * zy > 4:
                    break
                screen.set_at((x, y), ((250 - 25 * i) * 0x10101))
                pygame.display.update()


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))

        fractal()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()