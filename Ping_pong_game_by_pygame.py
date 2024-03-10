import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Game variables
ball_speed_x = 5 * random.choice([-1, 1])
ball_speed_y = 5 * random.choice([-1, 1])
ball_radius = 10
ball_pos = [WIDTH // 2, HEIGHT // 2]

paddle_width, paddle_height = 10, 100
paddle_speed = 7
player_pos = [50, HEIGHT // 2 - paddle_height // 2]
opponent_pos = [WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2]

score_player = 0
score_opponent = 0
font = pygame.font.Font(None, 36)

# Function to update ball position
def update_ball():
    global ball_pos, ball_speed_x, ball_speed_y, score_player, score_opponent

    ball_pos[0] += ball_speed_x
    ball_pos[1] += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_pos[1] <= ball_radius or ball_pos[1] >= HEIGHT - ball_radius:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (ball_pos[0] - ball_radius <= player_pos[0] + paddle_width and
        player_pos[1] - ball_radius <= ball_pos[1] <= player_pos[1] + paddle_height + ball_radius):
        ball_speed_x = -ball_speed_x
    elif (ball_pos[0] + ball_radius >= opponent_pos[0] and
          opponent_pos[1] - ball_radius <= ball_pos[1] <= opponent_pos[1] + paddle_height + ball_radius):
        ball_speed_x = -ball_speed_x

    # Ball scoring
    if ball_pos[0] <= 0:
        score_opponent += 1
        reset_ball()
    elif ball_pos[0] >= WIDTH:
        score_player += 1
        reset_ball()

# Function to reset ball position
def reset_ball():
    global ball_pos, ball_speed_x, ball_speed_y
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_speed_x = 5 * random.choice([-1, 1])
    ball_speed_y = 5 * random.choice([-1, 1])

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos[1] > 0:
        player_pos[1] -= paddle_speed
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - paddle_height:
        player_pos[1] += paddle_speed

    # AI for opponent paddle
    if opponent_pos[1] + paddle_height // 2 < ball_pos[1]:
        opponent_pos[1] += paddle_speed
    elif opponent_pos[1] + paddle_height // 2 > ball_pos[1]:
        opponent_pos[1] -= paddle_speed

    # Update ball position
    update_ball()

    # Draw elements
    pygame.draw.rect(screen, WHITE, [player_pos[0], player_pos[1], paddle_width, paddle_height])
    pygame.draw.rect(screen, WHITE, [opponent_pos[0], opponent_pos[1], paddle_width, paddle_height])
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)
    score_text = font.render(f"{score_player}   {score_opponent}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 50))

    # Refresh screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
