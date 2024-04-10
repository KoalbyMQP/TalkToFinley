import pygame
import sys
import ConverseWithFinleyWithActions

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Create a Pygame window
window_size = (800, 480)  # Increased window height to accommodate the image
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Clickable Button')

# Load the image and resize it
image = pygame.image.load("pradDAWG.png")  # Replace "your_image.png" with the path to your PNG image
image = pygame.transform.scale(image, (150, 150))  # Resize the image

# Load the font
font = pygame.font.Font("Power Smurf.otf", 36)  # Replace "your_font.ttf" with the path to your font file

# Render text on the button with black color
text = font.render("Start Speaking With Finley", True, (0, 0, 0))  # Black text color
text_rect = text.get_rect(center=(window_size[0] // 2, 157))  # Center the text horizontally and set vertical position

# Define colors
peach = (255, 182, 155)
dark_peach = (255, 182, 155)
light_peach = (255, 237, 220)
black = (0, 0, 0)
gray = (150, 150, 150)
white = (255, 255, 255)

# Calculate button size based on text size
button_width = text.get_width() + 40
button_height = text.get_height() + 20

# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect((window_size[0] - button_width) // 2, 125, button_width, button_height)  # Center the button

# Start the main loop
while True:
    # Set the frame rate
    clock.tick(60)

    # Fill the display with color
    screen.fill(peach)

    # Get events from the event queue
    for event in pygame.event.get():
        # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
            sys.exit()

        # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if button_rect.collidepoint(event.pos):
                ConverseWithFinleyWithActions.main()

    # Draw background rectangle
    pygame.draw.rect(screen, gray, button_rect)

    # Draw inner rectangle
    inner_rect = button_rect.inflate(-10, -10)  # Shrink by 10 pixels on each side
    pygame.draw.rect(screen, white, inner_rect)

    # Check if the mouse is over the button. This will create the button hover effect
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, light_peach, button_rect)
        image_rect = image.get_rect(center=(window_size[0] // 2, button_rect.bottom+100))  # Center the image horizontally and set vertical position
        # screen.blit(image, image_rect)
    else:
        pygame.draw.rect(screen, white, button_rect)

    # Draw button borders
    pygame.draw.rect(screen, black, button_rect, 2)

    # Show the button text
    screen.blit(text, text_rect)

    # Blit the image below the button


    # Update the game state
    pygame.display.update()
