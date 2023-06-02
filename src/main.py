import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Set the screen to show
screen = pygame.display.set_mode((800, 600))

# title, icon and background
pygame.display.set_caption('Space Invasion')
icon = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\back_space.jpg')

# music
mixer.music.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\background_music.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Player variables
img_player = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\space.png')
player_x = 368
player_y = 500
player_x_change = 0

# Enemy variables
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_quantity = 8

for e in range(enemy_quantity):
    img_enemy.append(
        pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\misterio.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(64, 200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(15)

# bullet variables
img_bullet = pygame.image.load('C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\bala.png')
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
show_bullet = False

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# Final text
final_font = pygame.font.Font('freesansbold.ttf', 50)


def final_text():
    my_final_font = final_font.render("END OF THE GAME", True, (255, 255, 255))
    screen.blit(my_final_font, (60, 200))


# Method to show the score
def show_score(x, y):
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x, y))


# Player method
def player(x, y):
    screen.blit(img_player, (x, y))


# Enemy method
def enemy(x, y, ene):
    screen.blit(img_enemy[ene], (x, y))


# Bullet method
def bullet(x, y):
    global show_bullet
    show_bullet = True
    screen.blit(img_bullet, (x + 22.5, y + 10))


# Method to detect a collision
def have_collision(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False


# Game loop
execution = True
while execution:

    # RGB
    # screen.fill((205, 144, 228))

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
                bullet_sound = mixer.Sound(
                    'C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\shot.mp3')
                bullet_sound.play()

                if not show_bullet:
                    bullet_x = player_x
                    bullet(bullet_x, bullet_y)

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
    for e in range(enemy_quantity):

        # End of the game
        if enemy_y[e] > 420:
            for k in range(enemy_quantity):
                enemy_y[k] = 1000
            final_text()
            break

        enemy_x[e] += enemy_x_change[e]

        if enemy_x[e] <= 0:
            enemy_x_change[e] = 1
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -1
            enemy_y[e] += enemy_y_change[e]

        # Collision
        collision = have_collision(enemy_x[e], enemy_y[e], bullet_x, bullet_y)

        if collision:
            collision_sound = mixer.Sound(
                'C:\\Users\\Sebastian Medina\\Documents\\Projects\\Space_invasion\\src\\hit.mp3')
            collision_sound.play()
            bullet_y = 500
            show_bullet = False
            score += 1
            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(64, 200)

        enemy(enemy_x[e], enemy_y[e], e)

    # bullet movement
    if bullet_y <= -64:
        bullet_y = 500
        show_bullet = False

    if show_bullet:
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)

    # show score
    show_score(text_x, text_y)

    # Update the screen
    pygame.display.update()