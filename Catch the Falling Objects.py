import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Basket (Player)
basket_width = 100
basket_height = 20
basket_x = SCREEN_WIDTH // 2 - basket_width // 2
basket_y = SCREEN_HEIGHT - basket_height - 10
basket_speed = 10

# Falling objects
object_width = 30
object_height = 30
object_speed = 5
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height

# Score
score = 0
font = pygame.font.SysFont(None, 35)

# Function to display text
def display_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Control basket with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
        basket_x += basket_speed
    
    # Move falling object
    object_y += object_speed
    if object_y > SCREEN_HEIGHT:
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
    
    # Check for collision with basket
    if basket_y < object_y + object_height and object_y + object_height < basket_y + basket_height:
        if object_x > basket_x and object_x < basket_x + basket_width:
            score += 1
            object_y = -object_height
            object_x = random.randint(0, SCREEN_WIDTH - object_width)
    
    # Draw basket
    pygame.draw.rect(screen, BLACK, [basket_x, basket_y, basket_width, basket_height])
    
    # Draw falling object
    pygame.draw.rect(screen, RED, [object_x, object_y, object_width, object_height])
    
    # Display score
    display_text(f"Score: {score}", font, BLACK, 10, 10)
    
    # Update screen
    pygame.display.update()
    
    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
