import pygame
from shapes import Shape
from grid import CreateGrid
from timer import Timer

pygame.init()
# Display
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris 🎮")
display_surface = pygame.display.get_surface()

# Initialize objects
grid = CreateGrid(screen)
group = pygame.sprite.Group()
shape = Shape(group)

# Timer
START_SPEED = 800
vertical_timer = Timer(START_SPEED, True, shape.move_down)
vertical_timer.activate()

# Music
pygame.mixer.init()
pygame.mixer.music.load("music/tetris_music.mp3")
pygame.mixer.music.play(-1)

game_on = True
while game_on:
    # Events
    for event in pygame.event.get():
        # Close event
        if event.type == pygame.QUIT:
            GAME_ON = False

        # If mouse is pressed
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     shape.y_coord = 850

        # If keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                shape.move_down()
            elif event.key == pygame.K_LEFT:
                shape.move_left()
            elif event.key == pygame.K_RIGHT:
                shape.move_right()
            # elif event.key == pygame.K_RCTRL:
            #     shape.rotate()

    # Fill the  screen with black background
    screen.fill((0, 0, 0))

    # Update vertical_timer and move_down() every 1 sec
    vertical_timer.update()

    # Draw the shapes on screen
    group.draw(screen)

    # Create grid
    grid.draw_grid()

    pygame.display.update()
    pygame.display.flip()

pygame.quit()

