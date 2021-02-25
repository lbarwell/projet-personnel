import pygame, sys

wasd_ctrls = {
    "move_left": pygame.K_LEFT,
    "move_right": pygame.K_RIGHT,
    "jump": pygame.K_UP,
    "move_down": pygame.K_DOWN
}

arrow_ctrls = {
    "move_left": pygame.K_a,
    "move_right": pygame.K_d,
    "jump": pygame.K_w,
    "move_down": pygame.K_s
}


class Game():
    def __init__(self):
        self.topleft_platform_rect = top_platform.get_rect(topleft = (350, 190))
        self.topright_platform_rect = top_platform.get_rect(topleft = (650, 190))
        self.midleft_platform_rect = mid_platform.get_rect(topleft = (150, 370))
        self.midright_platform_rect = mid_platform.get_rect(topleft = (675, 370))
        self.bottom_platform_rect = bottom_platform.get_rect(topleft = (400, 550))
        self.platforms = [self.topleft_platform_rect, self.topright_platform_rect, self.midleft_platform_rect, self.midright_platform_rect, self.bottom_platform_rect]


class Player():
    def __init__(self, x, y, player_image, ctrls):
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.ctrls = ctrls
        self.surf = player_image
        self.rect = self.surf.get_rect(topleft = (x, y))

    def update(self, pressed_keys):
        # Collisions
        if self.rect.bottom >= screen_height:
            self.y_vel = 0
            self.y = screen_height - 100
            self.collision = True
        else:
            self.collision = False

        for platform in game.platforms:
            if self.rect.bottom >= platform.top and self.rect.bottom <= platform.bottom and self.rect.midbottom >= platform.midleft and self.rect.midbottom <= platform.midright:
                self.y_vel = 0
                self.y = platform.top - 100
                self.collision = True
                break

        # Movement
        if pressed_keys[self.ctrls["move_left"]]:
            self.x_vel -= 0.5
        if pressed_keys[self.ctrls["move_right"]]:
            self.x_vel += 0.5
        if pressed_keys[self.ctrls["jump"]] and self.collision == True:
            self.y_vel -= 12
        if pressed_keys[self.ctrls["move_down"]]:
            self.y_vel += 0.5

        self.y_vel += gravity

        if self.x_vel >= friction:
            self.x_vel -= friction
        elif self.x_vel <= -friction:
            self.x_vel += friction
        else:
            self.x_vel = 0

        if self.x_vel > max_vel:
            self.x_vel = max_vel
        elif self.x_vel < -max_vel:
            self.x_vel = -max_vel
        elif self.y_vel > max_vel:
            self.y_vel = max_vel
        elif self.y_vel < -max_vel:
            self.y_vel = -max_vel

        self.rect.centerx += self.x_vel
        self.rect.centery += self.y_vel

# Game variables
screen_width = 1200
screen_height = 700
gravity = 0.4
friction = 0.3
max_vel = 14

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
# Name of game
pygame.display.set_caption("Projet Personnel")
clock = pygame.time.Clock()

# Load images
red_player = pygame.image.load("Assets/basic_red_player.png").convert_alpha()
blue_player = pygame.image.load("Assets/basic_blue_player.png").convert_alpha()

top_platform = pygame.image.load("Assets/basic_top_platform.png").convert_alpha()
mid_platform = pygame.image.load("Assets/basic_mid_platform.png").convert_alpha()
bottom_platform = pygame.image.load("Assets/basic_bottom_platform.png").convert_alpha()

# Create game
game = Game()

# Create Players
player1 = Player(1100, 100, blue_player, arrow_ctrls)
player2 = Player(100, 100, red_player, wasd_ctrls)
players = [player1, player2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Background
    screen.fill((255, 255, 255))

    # Platforms
    screen.blit(top_platform, game.topleft_platform_rect)
    screen.blit(top_platform, game.topright_platform_rect)
    screen.blit(mid_platform, game.midleft_platform_rect)
    screen.blit(mid_platform, game.midright_platform_rect)
    screen.blit(bottom_platform, game.bottom_platform_rect)

    # Players
    for player in players:
        screen.blit(player.surf, player.rect)

        player.update(pygame.key.get_pressed())

    pygame.display.update()
    clock.tick(60)
