# inspired by dvd blouncing logo.

import pygame
import random
import os

def main():
    # Initialize Pygame
    pygame.init()

    # Window Setup
    window_width = 800
    window_height = 600
    window_size = (window_width, window_height)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Catch the Square")

    # Load Background Image
    background_image = None
    try:
        background_image = pygame.image.load("mainbg.jpg")
        background_image = pygame.transform.scale(background_image, window_size)
    except pygame.error:
        print("Failed to load background image.")

    # Square Entity
    square_size = 50
    square_color = (255, 255, 0)
    square_x = random.randint(0, window_width - square_size)
    square_y = random.randint(0, window_height - square_size)
    square_speed_x = random.uniform(0.1, 0.5)  # Decreased speed in x-direction
    square_speed_y = random.uniform(0.1, 0.5)  # Decreased speed in y-direction

    # Score Tracking
    score = -50
    score_font = pygame.font.Font(None, 36)
    score_position = (10, 10)

    # Function to handle mouse click event
    def mouse_clicked():
        nonlocal score, square_x, square_y
        score += 1
        square_x = random.randint(0, window_width - square_size)
        square_y = random.randint(0, window_height - square_size)

    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mouse_clicked()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if square_x <= mouse_x <= square_x + square_size and square_y <= mouse_y <= square_y + square_size:
                    mouse_clicked()

        # Update Square Position
        square_x += square_speed_x
        square_y += square_speed_y

        # Check Boundaries and Bounce
        if square_x < 0 or square_x > window_width - square_size:
            square_speed_x *= -1
        if square_y < 0 or square_y > window_height - square_size:
            square_speed_y *= -1

        # Update Score Text
        score_text = score_font.render(f"Score: {score}", True, (255, 0, 0))

        # Draw Objects
        window.fill((0, 0, 0))  # Fill window with black color
        if background_image:
            window.blit(background_image, (0, 0))  # Blit background image
        pygame.draw.rect(window, square_color, (square_x, square_y, square_size, square_size))
        window.blit(score_text, score_position)

        # Update Display
        pygame.display.update()

        # Check Winning Condition
        if score == 14:
            winning_font = pygame.font.Font(None, 72)
            winning_text = winning_font.render("You Win!", True, (255, 0, 0))
            winning_position = (
                window_width // 2 - winning_text.get_width() // 2,
                window_height // 2 - winning_text.get_height() // 2,
            )
            window.blit(winning_text, winning_position)
            pygame.display.update()
            pygame.time.wait(5000)
            running = False

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
