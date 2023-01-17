import pygame


# Initialize Pygame and create window
pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake block size
block_size = 10

# Font for displaying score
font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width/2, height/2])

# Main loop
while True:
    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the snake and check for collision with walls or itself
    # Draw the snake and food on the screen
    # Update the display
    pygame.display.update()
    clock.tick(30)
