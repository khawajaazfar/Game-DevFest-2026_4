 # Write your code here :-)
import pygame
import math
import random
from pygame import mixer

pygame.init()  # Initialize Pygame
screen = pygame.display.set_mode((800, 533))  # Create the screen

# Background
background = pygame.image.load(r'C:\Users\diyaa\Downloads\space-background.png')

# Background sound
mixer.music.load(r'C:\Users\diyaa\Downloads\background.wav')
mixer.music.play(-1)  # Play on loop

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r'C:\Users\diyaa\Downloads\spaceship.png')  # Set the window icon
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(r'C:\Users\diyaa\Downloads\alien-ship.png')
playerX = 370  # Coordinates (less than half of 800)
playerY = 460
playerX_change = 0

# Enemy list (for multiple enemies)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r'C:\Users\diyaa\Downloads\space-invader.png'))
    enemyX.append(random.randint(0, 735))  # Coordinates (less than 800)
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Bullet
# ready - you can't see the bullet on the screen
# fire - the bullet is currently moving
bulletImg = pygame.image.load(r'C:\Users\diyaa\Downloads\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score display
font = pygame.font.SysFont("comicsansms", 32)  # Create the font object

def game_over_text():
    game_over = font.render(f"GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200, 250))


def show_score(x, y):
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_display, (x, y))

def player(x, y):  # Setting new coordinates
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):  # Setting new coordinates
    screen.blit(enemyImg[i], (x, y))  # Drawing an image of the player on the screen

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    if bullet_state == "fire":
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            # Play explosion sound
            bullet_sound = mixer.Sound(r'C:\Users\diyaa\Downloads\explosion.wav')
            bullet_sound.play()
            return True
    return False

def isPlayerCollision(playerX, playerY, enemyX, enemyY):
    # Check if the player's position collides with any enemy
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance < 27:
        return True
    return False

# Infinite loop for the game to run (to close the window when close is clicked)
running = True
score = 0
game_over = False  # Initially, game is not over
while running:
    screen.fill((255, 0, 0))  # Set screen background color
    # Setting background in this loop to be displayed throughout the game
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Close the game window if close button is pressed
        if event.type == pygame.KEYDOWN:  # KEYDOWN checks if any key in the keyboard is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":  # Fire only when bullet is ready
                    bulletX = playerX  # Stores the firing x position of the spaceship so that it remains constant
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Checking for boundaries of spaceship so it doesn't go out the bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # Subtracted 64 (the size of the icon from 800)
        playerX = 736
    game_over=False;
    # Checking for boundaries of enemy so it doesn't go out the bounds
    for i in range(num_of_enemies):
        # Game Over
        if isPlayerCollision(playerX, playerY, enemyX[i], enemyY[i]):
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over=True
            game_over_text()
            pygame.time.delay(2000)
        if game_over is "True":
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:  # Subtracted 64 (the size of the icon from 800)
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Collision detection with bullet
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1  # Increment the score
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        # Only draw enemies if the game is not over
        if not game_over:
            enemy(enemyX[i], enemyY[i], i)


    # Bullet movement
    if bulletY <= 0:
        bulletY = 460
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Show score
    show_score(10, 10)

    # Draw the player
    player(playerX, playerY)


    # RGB = Red, Green, Blue
    pygame.display.update()  # Update the display