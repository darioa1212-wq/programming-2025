import sys

import pygame
from pygame import mixer


def main():
    # Initialize Pygame
    mixer.init()
    pygame.init()

    clock = pygame.time.Clock()
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

    gravity = 0.8
    jump_strength = -12
    y_velocity = 0
    on_ground = True
    player_y_pos = float(player_rect.y)

    # Ground setup
    ground_y = screen_height - 40
    ground_height = 30
    ground_color = (200, 200, 200)
    ground_rect = pygame.Rect(0, ground_y, screen_width, ground_height)

    # Spike setup
    spike_color = (0, 0, 0)
    spike_height = 30
    scroll_speed = 5
    spikes = [
        {"x": 400, "y": ground_y, "width": 30, "height": spike_height},
        {"x": 550, "y": ground_y, "width": 30, "height": spike_height},
    ]

    # Finish line
    finish_width = 20
    finish_height = ground_height
    finish_x = 700
    finish_y = ground_y
    finish_color = (255, 0, 0)
    finish_rect = pygame.Rect(
        finish_x, finish_y - finish_height, finish_width, finish_height
    )

    run = True
    while run:
        clock.tick(fps)

        # --- Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground:
                    y_velocity = jump_strength
                    on_ground = False

        # --- Player physics ---
        y_velocity += gravity
        player_y_pos += y_velocity
        player_rect.y = int(player_y_pos)

        if player_rect.bottom >= ground_y:
            player_rect.bottom = ground_y
            y_velocity = 0
            on_ground = True

        # --- Move spikes (scrolling) ---
        for spike in spikes:
            spike["x"] -= scroll_speed

        # --- Collision detection ---
        for spike in spikes:
            spike_rect = pygame.Rect(
                spike["x"],
                spike["y"] - spike["height"],
                spike["width"],
                spike["height"],
            )
            if player_rect.colliderect(spike_rect):
                print("Game Over! You hit a spike.")
                run = False

        if player_rect.colliderect(finish_rect):
            print("Congratulations! You finished the level!")
            run = False

        # --- Drawing ---
        screen.fill((200, 200, 200))
        pygame.draw.rect(screen, ground_color, ground_rect)
        pygame.draw.rect(screen, player_color, player_rect)

        # Draw spikes
        for spike in spikes:
            points = [
                (spike["x"] + spike["width"] // 2, spike["y"] - spike["height"]),
                (spike["x"], spike["y"]),
                (spike["x"] + spike["width"], spike["y"]),
            ]
            pygame.draw.polygon(screen, spike_color, points)

        # Draw finish line
        pygame.draw.rect(screen, finish_color, finish_rect)

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
