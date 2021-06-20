import pygame
import random

# Initialise pygame
pygame.init()

# Initialise pygame mixer
pygame.mixer.init()

# Create a screen
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Set Title and Icon
pygame.display.set_caption("Bouncing Ball Simulator")
icon = pygame.image.load("AssetsProgram10/basketball-ball.png")
pygame.display.set_icon(icon)

# Player Image
playerImg = pygame.image.load("AssetsProgram10/ball.png")

# Play Button and Location
playBtn = pygame.image.load("AssetsProgram10/play-button.png")
playBtnX = 340
playBtnY = 180

# Pause Button and Location
pauseBtn = pygame.image.load("AssetsProgram10/pause-button.png")
pauseBtnX = 350
pauseBtnY = 180

# Paused Text Image and Location
pausedImg = pygame.image.load("AssetsProgram10/Paused.png")
pausedImgX = 265
pausedImgY = 300

# Instruction and Location
instruction = pygame.image.load("AssetsProgram10/Start-Instruction.png")
instructionX = 260
instructionY = 310

# Loading beat
pygame.mixer.music.load("AssetsProgram10/catching-basketball.mp3")

# Setting the volume
pygame.mixer.music.set_volume(0.7)


# Method to load player in game
def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))

# Method to load paused image in game
def showPausedImage():
    screen.blit(pausedImg, (pausedImgX, pausedImgY))

# Method to load instruction image in game
def showInstruction():
    screen.blit(instruction, (instructionX, instructionY))


# Method to show the play button in game start
def playButtion():
    screen.blit(playBtn, (playBtnX, playBtnY))


# Method to show the pause button in game
def pauseButton():
    screen.blit(pauseBtn, (pauseBtnX, pauseBtnY))


# Method for complete game loop
def gameLoop():
    # Filling background screen with color
    screen.fill((204, 255, 255))

    # Variable to keep check running status of game
    is_running = True

    # Variable to check is game is started or not
    is_started = False

    # Variable to check if game is paused or not
    is_paused = False

    # Player Image Location
    playerX = 400
    playerY = 536

    # Player position change coordinates
    positionChangeX = random.random()
    positionChangeY = random.random()

    # Game loop
    while is_running:
        # Quit game if close button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if is_paused == False and event.key == pygame.K_SPACE:
                    pauseButton()
                    showPausedImage()
                    pygame.display.update()
                    is_paused = True

        # Start Game if space is pressed and game is not started yet
        if is_started == False:

            # Background color at start
            screen.fill((204, 255, 255))

            # Showing play button
            playButtion()
            # Showing instruction
            showInstruction()

            pygame.display.update()

            # Starting game is 'SPACE' button is pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        is_started = True
                if event.type == pygame.QUIT:
                    is_running = False

        elif is_paused == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        is_paused = False

        else:
            # Background color at start
            screen.fill((204, 255, 255))

            # Showing player in game
            player(playerX, playerY)
            pygame.display.update()

            # Logic for player position change
            if playerX <= 0 and playerY <= 0:
                # Top left corner
                pygame.mixer.music.play()
                print("In top left corner")
                if positionChangeX < 0:
                    positionChangeX *= -1
                if positionChangeY < 0:
                    positionChangeY *= -1

            elif playerX + 64 >= screenWidth and playerY <= 0:
                # Top right corner
                pygame.mixer.music.play()
                print("In top right corner")
                if positionChangeX > 0:
                    positionChangeX *= -1
                if positionChangeY < 0:
                    positionChangeY *= -1

            elif playerX <= 0 and playerY + 64 >= screenHeight:
                # Bottom left corner
                pygame.mixer.music.play()
                print("In bottom left corner")
                if positionChangeX < 0:
                    positionChangeX *= -1
                if positionChangeY > 0:
                    positionChangeY *= -1

            elif playerX + 64 >= screenWidth and playerY + 64 >= screenHeight:
                # Bottom right corner
                pygame.mixer.music.play()
                print("In bottom right corner")
                if positionChangeX > 0:
                    positionChangeX *= -1
                if positionChangeY > 0:
                    positionChangeY *= -1

            elif playerY <= 0 and 64 < playerX < screenWidth - 64:
                # Top window touch
                pygame.mixer.music.play()
                print("In top")
                if positionChangeY < 0:
                    positionChangeY *= -1

            elif playerX <= 0 and 64 < playerY < screenHeight - 64:
                # Left window touch
                pygame.mixer.music.play()
                print("In left")
                if positionChangeX < 0:
                    positionChangeX *= -1

            elif playerY >= screenHeight - 64 and 64 < playerX < screenWidth - 64:
                # Bottom window touch
                pygame.mixer.music.play()
                print("In bottom")
                if positionChangeY > 0:
                    positionChangeY *= -1
            elif playerX >= screenWidth - 64 and 64 < playerY < screenHeight - 64:
                # Right window touch
                pygame.mixer.music.play()
                print("In right")
                if positionChangeX > 0:
                    positionChangeX *= -1

            playerX += positionChangeX
            playerY += positionChangeY


# Starting Game by calling method
gameLoop()
pygame.quit()
