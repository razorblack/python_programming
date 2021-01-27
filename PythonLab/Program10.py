import pygame

# Initialise pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Set Title and Icon
pygame.display.set_caption("Bouncing Ball Simulator")
icon = pygame.image.load("basketball-ball.png")
pygame.display.set_icon(icon)

# Player Image
playerImg = pygame.image.load("ball.png")
playerX = 400
playerY = 540

def player():
    screen.blit(playerImg, (playerX, playerY))

def playButtion():
    playBtn = pygame.image.load("play-button.png")
    playBtnX = 350
    playBtnY = 230
    screen.blit(playBtn, (playBtnX, playBtnY))

def gameLoop():
    # Game Loop
    screen.fill((204, 255, 255))

    running = True
    while running:
        # Start Game if space is pressed
        if isGameStarted() == True:
            screen.fill((204, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            player()
            pygame.display.update()


def isGameStarted():
    screen.fill((204, 255, 255))
    playButtion()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Start game if space id pressed
                return True