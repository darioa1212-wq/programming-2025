import sys

import pygame


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60

    # Screen
    screen_width = 800
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong with Score")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Font
    font = pygame.font.SysFont(None, 40)

    # Scores
    left_score = 0
    right_score = 0

    # Paddle setup
    paddle_width = 10
    paddle_height = 80
    paddle_speed = 6

    left_paddle = pygame.Rect(40, screen_height // 2 - 40, paddle_width, paddle_height)
    right_paddle = pygame.Rect(
        screen_width - 50, screen_height // 2 - 40, paddle_width, paddle_height
    )

    # Ball setup
    ball_size = 12
    ball = pygame.Rect(
        screen_width // 2 - ball_size // 2,
        screen_height // 2 - ball_size // 2,
        ball_size,
        ball_size,
    )
    ball_speed_x = 5
    ball_speed_y = 5

    run = True
    while run:
        clock.tick(fps)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.y -= paddle_speed
        if keys[pygame.K_s]:
            left_paddle.y += paddle_speed

        if keys[pygame.K_UP]:
            right_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN]:
            right_paddle.y += paddle_speed

        # Keep paddles on screen
        left_paddle.y = max(0, min(screen_height - paddle_height, left_paddle.y))
        right_paddle.y = max(0, min(screen_height - paddle_height, right_paddle.y))

        # Move ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Wall collision
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1

        # Paddle collision
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x *= -1

        # Scoring
        if ball.left <= 0:
            right_score += 1
            ball.center = (screen_width // 2, screen_height // 2)
            ball_speed_x = 5

        if ball.right >= screen_width:
            left_score += 1
            ball.center = (screen_width // 2, screen_height // 2)
            ball_speed_x = -5

        # Draw
        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.rect(screen, WHITE, ball)

        # Draw score
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)

        screen.blit(left_text, (screen_width // 4, 20))
        screen.blit(right_text, (screen_width * 3 // 4, 20))

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
