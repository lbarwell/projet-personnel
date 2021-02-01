import pygame, sys


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surf = pygame.Surface((30, 70))
        self.surf.fill((139, 0, 0))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            self.y += 5
        if pressed_keys[pygame.K_LEFT]:
            self.x -= 5
        if pressed_keys[pygame.K_RIGHT]:
            self.x += 5


pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Projet Personnel") # Name of game
clock = pygame.time.Clock()

# Players
player1 = Player(200, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Background color
    screen.fill((255, 255, 255))

    # Platforms
    cl_pf = pygame.Surface((375, 20))
    cl_pf_rect = cl_pf.get_rect(topleft = (150, 370))
    screen.blit(cl_pf, cl_pf_rect)

    cr_pf = pygame.Surface((375, 20))
    cr_pf_rect = cr_pf.get_rect(topleft = (675, 370))
    screen.blit(cr_pf, cr_pf_rect)

    b_pf = pygame.Surface((400, 20))
    b_pf_rect = b_pf.get_rect(topleft = (400, 545))
    screen.blit(b_pf, b_pf_rect)

    tl_pf = pygame.Surface((200, 20))
    tl_pf_rect = tl_pf.get_rect(topleft = (350, 195))
    screen.blit(tl_pf, tl_pf_rect)

    tr_pf = pygame.Surface((200, 20))
    tl_pf_rect = tr_pf.get_rect(topleft = (650, 195))
    screen.blit(tr_pf, tl_pf_rect)

    # Display players
    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys)

    screen.blit(player1.surf, (player1.x, player1.y))

    pygame.display.update()
    clock.tick(60)
