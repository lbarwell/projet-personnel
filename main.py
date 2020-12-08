import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Projet Personnel") # Name of game
clock = pygame.time.Clock()

# Import background
background = pygame.image.load("Assets/basic-background.png").convert()
screen.blit(background, (0, 0))

# Import and display platforms
ctr_left_platform = pygame.image.load("Assets/basic-mid-platform.png").convert()
ctr_left_platform_rect = ctr_left_platform.get_rect(topleft = (150, 370))
screen.blit(ctr_left_platform, ctr_left_platform_rect)

ctr_right_platform = pygame.image.load("Assets/basic-mid-platform.png").convert()
ctr_right_platform_rect = ctr_right_platform.get_rect(topleft = (675, 370))
screen.blit(ctr_right_platform, ctr_right_platform_rect)

bottom_platform = pygame.image.load("Assets/basic-low-platform.png").convert()
bottom_platform_rect = bottom_platform.get_rect(topleft = (400, 545))
screen.blit(bottom_platform, bottom_platform_rect)

top_left_platform = pygame.image.load("Assets/basic-high-platform.png").convert()
top_left_platform_rect = top_left_platform.get_rect(topleft = (350, 195))
screen.blit(top_left_platform, top_left_platform_rect)

top_right_platform = pygame.image.load("Assets/basic-high-platform.png").convert()
top_right_platform_rect = top_right_platform.get_rect(topleft = (650, 195))
screen.blit(top_right_platform, top_right_platform_rect)

# Import players
player1 = pygame.image.load("Assets/basic-red-player.png").convert()
player1_rect = player1.get_rect(center = (200, 335))

player2 = pygame.image.load("Assets/basic-blue-player.png").convert()
player2_rect = player2.get_rect(center = (1000, 335))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display players
    screen.blit(player1, player1_rect)
    screen.blit(player2, player2_rect)

    pygame.display.update()
    clock.tick(60)
