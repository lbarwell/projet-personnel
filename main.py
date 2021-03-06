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

        if player.y_vel > max_yvel:
            player.y_vel = max_yvel
        elif player.y_vel < -max_yvel:
            player.y_vel = -max_yvel


    def collisions(self, player):
        #  Ground
        if player.rect.y > SCREEN_HEIGHT + 1000:
            player.rect.topleft = player.starting_pos
            player.x_vel = 0
            player.y_vel = 0

        # Platform
        for platform in self.platforms:
            if player.rect.colliderect(platform) and player.y_vel >= 0 and player.rect.y < platform.top - PLAYER_HEIGHT + 20 and player.platform_coll:
                player.y_vel = 0
                player.rect.y = platform.top - PLAYER_HEIGHT
                player.collision = True
                break
            else:
                player.collision = False


class Player():
    def __init__(self, starting_pos, colour, ctrls, player_image):
        self.x_vel = 0
        self.y_vel = 0
        self.starting_pos = starting_pos
        self.strength = 12
        self.colour = colour
        self.ctrls = ctrls
        self.surf = player_image
        self.rect = self.surf.get_rect(topleft = starting_pos)


    def update(self):
        # Direction
        if self.x_vel > 0:
            self.surf = player_images[self.colour]
        elif self.x_vel < 0:
            self.surf = pygame.transform.flip(player_images[self.colour], True, False)

        # Position
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

    def hit(self, pressed_keys, target):
        if pressed_keys[self.ctrls["hit"]] and player.rect.colliderect(target.rect):
            if player.rect.x < target.rect.x:
                target.x_vel = self.strength
            elif player.rect.x > target.rect.x:
                target.x_vel = -self.strength


# Game variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 138
gravity = 0.4
friction = 0.3
max_xvel = 18
max_yvel = 14

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projet Personnel")
clock = pygame.time.Clock()

# Load images
red_player = pygame.image.load("Assets/red_player.png").convert_alpha()
red_player = pygame.transform.scale(red_player, (PLAYER_WIDTH, PLAYER_HEIGHT))

blue_player = pygame.image.load("Assets/blue_player.png").convert_alpha()
blue_player = pygame.transform.scale(blue_player, (PLAYER_WIDTH, PLAYER_HEIGHT))

top_platform = pygame.image.load("Assets/top_platform.png").convert_alpha()
mid_platform = pygame.image.load("Assets/mid_platform.png").convert_alpha()
bottom_platform = pygame.image.load("Assets/bottom_platform.png").convert_alpha()

player_images = {
    "red": red_player,
    "blue": blue_player
}

# Create game
game = Game()

# Create Players
player1 = Player((1000, 100), "blue", settings.controls["wasd"], blue_player)
player2 = Player((200, 100), "red", settings.controls["arrows"], red_player)
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
    pressed_keys = pygame.key.get_pressed()

    for player in players:
        if player == player1:
            other_player = players[1]
        else:
            other_player = players[0]

        player.move(pressed_keys)
        player.hit(pressed_keys, other_player)
        game.forces(player)
        player.update()

        game.collisions(player)

        screen.blit(player.surf, player.rect)

    pygame.display.update()
    clock.tick(60)
