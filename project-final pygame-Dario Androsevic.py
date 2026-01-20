import sys

import pygame
from pygame import mixer


def main():
    mixer.init()
    pygame.init()

    clock = pygame.time.Clock() # limit loop to 60 fps
    fps = 60

    # Screen setup
    screen_width = 800
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dario's Geometry Dash")

    # Player setup
    player_width = 30
    player_height = 30
    player_x = 100
    player_y = screen_height - 70
    player_color = (0, 200, 255)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    gravity = 0.8 # downward acceleration
    # ---- BEGIN: USED AI ----
    jump_strength = -12 # negative because y goes down
    # ---- END ----
    y_velocity = 0
    on_ground = True
    player_y_pos = float(player_rect.y)

    # Ground setup
    ground_y = screen_height - 40
    ground_color = (200, 200, 200)
    ground_rect = pygame.Rect(0, ground_y, screen_width, 30)

    # Spike setup
    spike_color = (0, 0, 0)
    spike_height = 30
    scroll_speed = 5  # how fast the game moves left
    # list of spike obstacles
    # USED AI To help, but I created this myself ____Beginning
    spikes = [
        {"x": 400, "y": ground_y, "width": 30, "height": spike_height},
        {"x": 550, "y": ground_y, "width": 30, "height": spike_height},
        {"x": 650, "y": ground_y, "width": 30, "height": spike_height},
    ] # USED AI To help, but I created this myself ____END

    # Finish line
    finish_width = 20
    finish_color = (255, 0, 0)
    finish_rect = pygame.Rect(750, ground_y - 30, finish_width, 30) # finish line hitbox

    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and on_ground:
            y_velocity = jump_strength
            on_ground = False # Player is in air

        # ---- BEGIN:USED AI TO SOLVE THIS - applying gravity and moving the cube
        y_velocity += gravity
        player_y_pos += y_velocity
        player_rect.y = int(player_y_pos)
        # ____ END

        # ground collision
        if player_rect.bottom >= ground_y:
            player_rect.bottom = ground_y
            y_velocity = 0
            on_ground = True # player is on ground

            # ---- BEGIN: USED AI TO SOLVE SPEED - Move spikes and finish line left for auto-run
        for spike in spikes:
            spike["x"] -= scroll_speed
        finish_rect.x -= scroll_speed
            # ____ END

        # Collision detection with spikes
        for spike in spikes:
            spike_rect = pygame.Rect(
                spike["x"],
                spike["y"] - spike["height"],
                spike["width"],
                spike["height"],
            )
            if player_rect.colliderect(spike_rect):
                print("Game Over! You hit a spike.")
                run = False # stops game if spike is hit

            # Finish line
        if player_rect.colliderect(finish_rect):
            print("Congratulations! You finished the level!")
            run = False # stops game when u reach finish line

        screen.fill((200, 200, 200)) # clear screen with background color
        pygame.draw.rect(screen, ground_color, ground_rect) # draw ground
        pygame.draw.rect(screen, player_color, player_rect) # draw player

        for spike in spikes: # draw each spike
            points = [
                (spike["x"] + spike["width"] // 2, spike["y"] - spike["height"]),
                (spike["x"], spike["y"]),
                (spike["x"] + spike["width"], spike["y"]),
            ]
            pygame.draw.polygon(screen, spike_color, points) # draw spike shape

        # finish line
        pygame.draw.rect(screen, finish_color, finish_rect)

        pygame.display.update() # update the screen

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
