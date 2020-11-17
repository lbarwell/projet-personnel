import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 300), pygame.RESIZABLE)
pygame.display.set_caption("Projet Personnel") # Name of game
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(90)
