from settings import *


class CreateGrid:
    def __init__(self, screen):
        self.screen = screen

        # Create a grid surface
        self.line_surface = screen.copy()
        self.line_surface.fill((0, 255, 0))
        self.line_surface.set_colorkey((0, 255, 0))
        self.line_surface.set_alpha(200)

    def draw_grid(self):
        for col in range(COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR,  (x, 0), (x, self.screen.get_height()), 1)

        for row in range(ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (0, y), (self.screen.get_width(), y), 1)

        self.screen.blit(self.line_surface, (0, 0))
