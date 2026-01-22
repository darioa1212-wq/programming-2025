# Drawing
# Author: Dario
# Date: 5 January 2026

import pygame

def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (  0,   0,   0)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    GREY  = (128, 128, 128)

    # CONSTANTS
    WIDTH = 1920
    HEIGHT = 1080
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE) # background
        # Draw a rectangle in the middle of the screen
        # Make it red
        pygame.draw.rect(screen, RED, (WIDTH / 2 - 50, HEIGHT / 2 - 50, 100, 100))
        # Draw a circle on top of the rectangle
        pygame.draw.circle(screen, BLUE, (WIDTH / 2, HEIGHT / 2), 50)

        # Draw 7 purple lines from the top-middle-right of the screen
        # to the middle-right of the screen
        # Repeats by translating down 75 px
        for offset in range(7):
            pygame.draw.line(screen, (228, 45, 216), (WIDTH/2 + 20, 20 + offset * 75), (WIDTH - 20, HEIGHT/2 - 20 + offset * 75))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
