import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen to show
screen = pygame.display.set_mode((800, 600))

# title, icon and background
pygame.display.set_caption('Space Invasion')
icon = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\back_space.jpg')


# Player variables
img_player = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\space.png')
player_x = 368
player_y = 500
player_x_change = 0

# Enemy variables
img_enemy = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\misterio.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(64, 200)
enemy_x_change = 1
enemy_y_change = 50

# bullet variables
img_bullet = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\bala.png')
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 1
show_bullet = False

# Player method
def player(x, y):
    screen.blit(img_player, (x, y))

# Enemy method
def enemy(x, y):
    screen.blit(img_enemy, (x, y))

# Bullet method
def bullet(x, y):
    global show_bullet
    show_bullet = True
    screen.blit(img_bullet, (x + 22.5, y + 10))

# Game loop
execution = True
while execution:

    # RGB
    #screen.fill((205, 144, 228))

    # Background
    screen.blit(background, (0, 0))

    # Events loop
    for event in pygame.event.get():

        # Close event
        if event.type == pygame.QUIT:
            execution = False

        # Key press event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            # bullet
            if event.key == pygame.K_SPACE:
                bullet(player_x, bullet_y)

        # Key release event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Modify player location
    player_x += player_x_change

    # Keep the player in the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Modify the enemy location
    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change = 1
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -1
        enemy_y += enemy_y_change

    # bullet movement
    if show_bullet:
        bullet(player_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # Update the screen
    pygame.display.update()