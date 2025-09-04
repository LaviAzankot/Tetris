from settings import *


class Shape:
    def __init__(self, group):
        self.group = group
        self.shapes = []
        self.blocks = []

        self.create_shape()

    def create_shape(self):
        # Choose a random shape
        shape = choice(list(SHAPES.items()))[1]

        # Get shape values
        block_positions = shape['shape']
        color = shape['color']

        # Create blocks and retriv the rect object
        random_x = randint(1, 8)
        self.blocks = [Block(self.group, list(pos), random_x, color).rect for pos in block_positions]
        # Add the new shape to the shapes list
        self.shapes.append(self.blocks)

    def move_down(self):
        if not self.detect_collision(collision_type="down"):
            # If there's not a collision move left
            self.make_move(moving_distance=MOVING_DISTANCE_VERTICALLY, x=False)
            print("Move down")
        else:
            # If it hit the bottom create a new shape
            self.create_shape()

    def move_right(self):
        if not self.detect_collision(collision_type="right"):
            # If there's not a collision move right
            self.make_move(moving_distance=MOVING_DISTANCE_HORIZONTALLY)
            print("Move right")

    def move_left(self):
        if not self.detect_collision(collision_type="left"):
            # If there's not a collision move left
            self.make_move(moving_distance=-MOVING_DISTANCE_HORIZONTALLY)
            print("Move left")

    def detect_shape_collision(self, block, collision_type):
        # Loop through each previous_block
        for previous_shape in range(len(self.shapes) - 1):
            previous_shape = self.shapes[previous_shape]
            for previous_i in range(len(previous_shape)):
                previous_block = previous_shape[previous_i]

                # Get the grid of the blocks
                x_grid = block.x / CELL_SIZE
                y_grid = block.y / CELL_SIZE

                previous_x_grid = previous_block.x / CELL_SIZE
                previous_y_grid = previous_block.y / CELL_SIZE

                # Check down shape collision

                # Down collision - if they have the same x grid and y grid + 1 is the same as previous y grid
                if collision_type == "down" and x_grid == previous_x_grid and y_grid + 1 == previous_y_grid:
                    return True

    def detect_collision(self, collision_type):
        for i in range(len(self.blocks)):
            block = self.blocks[i]

            # Shape collision
            if self.detect_shape_collision(block, "down"):
                return True

            # Down collision
            elif collision_type == "down" and block.y + MOVING_DISTANCE_VERTICALLY >= 800:
                return True
            # Right collision or right shape collision
            elif collision_type == "right" and block.x + MOVING_DISTANCE_HORIZONTALLY >= 400:
                return True
            # Left collision or left shape collision
            elif collision_type == "left" and block.x - MOVING_DISTANCE_HORIZONTALLY < 0:
                return True

    def make_move(self, moving_distance, x=True):
        for i in range(len(self.blocks)):
            block = self.blocks[i]
            if x:
                # Move left or right
                # If to the left its -40
                # So block.x += -40   ==  block.x -= 40
                block.x += moving_distance

            # if not x then its y
            else:
                # Move down
                block.y += moving_distance

            self.blocks[i] = block


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, random_x, color):
        # Create a block
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        # Position
        self.pos = pos
        x = (self.pos[0] + random_x) * CELL_SIZE
        y = self.pos[1] * CELL_SIZE
        self.rect = self.image.get_rect(topleft=(x, y))
