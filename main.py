import pygame, sys
import settings


class Game():
    def __init__(self):
        self.platforms = [
            top_platform.get_rect(topleft = (350, 190)),
            top_platform.get_rect(topleft = (650, 190)),
            mid_platform.get_rect(topleft = (150, 370)),
            mid_platform.get_rect(topleft = (675, 370)),
            bottom_platform.get_rect(topleft = (400, 550))
        ]


    def forces(self, player):
        # Gravity
        player.y_vel += gravity

        # Friction
        if player.x_vel >= friction:
            player.x_vel -= friction
        elif player.x_vel <= -friction:
            player.x_vel += friction
        else:
            player.x_vel = 0

        # Max speed
        if player.x_vel > max_xvel:
            player.x_vel = max_xvel
        elif player.x_vel < -max_xvel:
            player.x_vel = -max_xvel
        elif player.y_vel > max_yvel:
            player.y_vel = max_yvel
        elif player.y_vel < -max_yvel:
            player.y_vel = -max_yvel


    def collisions(self, player):
        # Ground
        if player.rect.bottom >= SCREEN_HEIGHT:
            player.y_vel = 0
            player.rect.y = SCREEN_HEIGHT - 100
            player.collision = True
        else:
            player.collision = False

        # Platform
        for platform in self.platforms:
            if player.rect.colliderect(platform) and player.y_vel >= 0 and player.rect.y < platform.top - 80 and player.platform_coll:
                player.y_vel = 0
                player.rect.y = platform.top - 100
                player.collision = True
                break


class Player():
    def __init__(self, x, y, player_image, ctrls):
        self.x_vel = 0
        self.y_vel = 0
        self.ctrls = ctrls
        self.surf = player_image
        self.rect = self.surf.get_rect(topleft = (x, y))


    def update(self):
        self.rect.centerx += self.x_vel
        self.rect.centery += self.y_vel


    def move(self, pressed_keys):
        if pressed_keys[self.ctrls["move_left"]]:
            self.x_vel -= 0.5
        if pressed_keys[self.ctrls["move_right"]]:
            self.x_vel += 0.5
        if pressed_keys[self.ctrls["jump"]] and self.collision:
            self.y_vel -= 12
        if pressed_keys[self.ctrls["move_down"]]:
            self.y_vel += 0.5
            self.platform_coll = False
        else:
            self.platform_coll = True


# Game variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 100
gravity = 0.4
friction = 0.3
max_xvel = 10
max_yvel = 14

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projet Personnel")
clock = pygame.time.Clock()

# Load images
red_player = pygame.image.load("Assets/basic_red_player.png").convert_alpha()
red_player = pygame.transform.scale(red_player, (PLAYER_WIDTH, PLAYER_HEIGHT))

blue_player = pygame.image.load("Assets/basic_blue_player.png").convert_alpha()
blue_player = pygame.transform.scale(blue_player, (PLAYER_WIDTH, PLAYER_HEIGHT))

top_platform = pygame.image.load("Assets/basic_top_platform.png").convert_alpha()
mid_platform = pygame.image.load("Assets/basic_mid_platform.png").convert_alpha()
bottom_platform = pygame.image.load("Assets/basic_bottom_platform.png").convert_alpha()

# Create game
game = Game()

# Create Players
player1 = Player(1100, 100, blue_player, settings.controls["wasd"])
player2 = Player(100, 100, red_player, settings.controls["arrows"])
players = [player1, player2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Background
    screen.fill((0, 0, 0))

    # Platforms
    screen.blit(top_platform, game.platforms[0])
    screen.blit(top_platform, game.platforms[1])
    screen.blit(mid_platform, game.platforms[2])
    screen.blit(mid_platform, game.platforms[3])
    screen.blit(bottom_platform, game.platforms[4])

    # Players
    for player in players:
        player.move(pygame.key.get_pressed())
        game.forces(player)
        player.update()

        game.collisions(player)

        screen.blit(player.surf, player.rect)

    pygame.display.update()
    clock.tick(60)
