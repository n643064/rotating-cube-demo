import pygame
from util import *
def prepare(p):
    return 400 + p[0], 400 + p[1]

def main(model_path):
    model = read_model(model_path)
    if not model:
        print("Couldn't load model.")
        quit(1)
    pygame.init()
    window = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen = pygame.Surface((800, 800))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
        screen.fill((50, 50, 50))


        for i in range(0, len(model)):
            model[i] = rotate_x(model[i], 0.5)
            model[i] = rotate_y(model[i], 0.5)
            model[i] = rotate_z(model[i], 0.5)
            pygame.draw.line(screen, (255, 255, 255), prepare(model[i][0]), prepare(model[i][1]), 2)

        window.blit(pygame.transform.scale(screen, window.get_size()), (0, 0))
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main("cube.model")