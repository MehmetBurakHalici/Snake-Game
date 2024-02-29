# Import necessary libraries
import random
import sys
import pygame
from pygame.math import Vector2

# Define the class for the start screen
class StartScreen:
    def __init__(self):
        # Initialize font and create text surfaces for the title and buttons
        self.font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 60)
        self.title = self.font.render("Snake Game", True, (255, 255, 255))
        self.start_button = self.font.render("Start", True, (255, 255, 255))
        self.gameplay_button = self.font.render("Gameplay", True, (255, 255, 255))
        self.exit_button = self.font.render("Exit", True, (255, 255, 255))  # Added a new Exit button
        # Set the positions and dimensions for the title and buttons
        self.title_rect = self.title.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 4))
        self.start_button_rect = pygame.Rect(cell_number * cell_size // 4, cell_number * cell_size // 2,
                                             cell_number * cell_size // 2, cell_size * 1.5)
        self.gameplay_button_rect = pygame.Rect(cell_number * cell_size // 4, cell_number * cell_size // 1.5,
                                                cell_number * cell_size // 2, cell_size * 1.5)
        self.exit_button_rect = pygame.Rect(cell_number * cell_size // 4, cell_number * cell_size // 1.2,
                                            cell_number * cell_size // 2, cell_size * 1.5)
        # Load images for sound on and off icons and set the initial sound state
        self.speaker_on = pygame.image.load('Graphics/Sound/Sound On.png').convert_alpha()
        self.speaker_off = pygame.image.load('Graphics/Sound/Sound Off.png').convert_alpha()
        self.speaker_rect = pygame.Rect(10, 10, 30, 30)
        self.is_sound_on = True

    # Method to draw the start screen on the given surface
    def draw(self, screen):
        # Fill the screen with a background color
        screen.fill((175, 215, 70))
        # Blit the title and draw rounded rectangles for buttons
        screen.blit(self.title, self.title_rect)
        pygame.draw.rect(screen, (175, 215, 70), self.start_button_rect, border_radius=15)
        pygame.draw.rect(screen, (175, 215, 70), self.gameplay_button_rect, border_radius=15)
        pygame.draw.rect(screen, (175, 215, 70), self.exit_button_rect, border_radius=15)
        # Get rectangles for text placement
        start_button_text_rect = self.start_button.get_rect(center=self.start_button_rect.center)
        gameplay_button_text_rect = self.gameplay_button.get_rect(center=self.gameplay_button_rect.center)
        exit_button_text_rect = self.exit_button.get_rect(center=self.exit_button_rect.center)
        # Blit text onto the buttons
        screen.blit(self.start_button, start_button_text_rect.topleft)
        screen.blit(self.gameplay_button, gameplay_button_text_rect.topleft)
        screen.blit(self.exit_button, exit_button_text_rect.topleft)
        # Blit sound icon based on the sound state
        if self.is_sound_on:
            screen.blit(self.speaker_on, self.speaker_rect.topleft)
        else:
            screen.blit(self.speaker_off, self.speaker_rect.topleft)

    # Method to handle events, such as button clicks
    def handle_events(self, event):
        # Check for mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the Start button is clicked and return "start"
            if self.start_button_rect.collidepoint(event.pos):
                return "start"
            # Check if the Gameplay button is clicked and return "gameplay"
            elif self.gameplay_button_rect.collidepoint(event.pos):
                return "gameplay"
            # Check if the Exit button is clicked and exit the game
            elif self.exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            # Check if the sound icon is clicked and toggle the sound state
            if self.speaker_rect.collidepoint(event.pos):
                self.toggle_sound()
        return None

    # Method to toggle the sound state and pause/resume background music accordingly
    def toggle_sound(self):
        self.is_sound_on = not self.is_sound_on

        if self.is_sound_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

# Define the class for the gameplay screen
class GameplayScreen:
    def __init__(self):
        # Initialize font and create text surfaces for instructions
        self.font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
        self.instructions = [
            "Welcome to Snake Game!",
            "",
            "How to play:",
            "1. Control the snake using the arrow keys.",
            "2. Eat the fruits scattered on the board to grow bigger.",
            "3. Avoid hitting the walls or yourself as it will end the game.",
            "",
            "Tips for success:",
            "- Plan your moves in advance to avoid getting trapped.",
            "- Be strategic when picking berries to maximize your length.",
            "- The longer you are, the harder the game becomes.",
            "",
            "Press 'Start' to embark on your snake adventure!",
            "Good luck and have fun!"
        ]
        # Create a back button
        self.back_button = self.font.render("Back", True, (255, 255, 255))
        self.back_button_rect = pygame.Rect(cell_number * cell_size // 4, cell_number * cell_size // 1.2,
                                            cell_number * cell_size // 2, cell_size * 1.5)

    # Method to draw the gameplay screen on the given surface
    def draw(self, screen):
        # Fill the screen with a background color
        screen.fill((175, 215, 70))
        # Blit instructions onto the screen
        for i, text in enumerate(self.instructions):
            text_rendered = self.font.render(text, True, (255, 255, 255))
            text_rect = text_rendered.get_rect(
                center=(cell_number * cell_size // 2, cell_number * cell_size // 4 + i * 30))
            screen.blit(text_rendered, text_rect.topleft)
        # Draw a rounded rectangle for the back button
        pygame.draw.rect(screen, (175, 215, 70), self.back_button_rect, border_radius=15)
        # Get a rectangle for text placement
        back_button_text_rect = self.back_button.get_rect(center=self.back_button_rect.center)
        # Blit text onto the back button
        screen.blit(self.back_button, back_button_text_rect.topleft)

    # Method to handle events, such as button clicks
    def handle_events(self, event):
        # Check for mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the Back button is clicked and return "back"
            if self.back_button_rect.collidepoint(event.pos):
                return "back"
        return None

# Define the class for the restart screen
class RestartScreen:
    def __init__(self):
        # Initialize font and create text surfaces for the prompt and buttons
        self.font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 40)
        self.prompt_text = self.font.render("Do you want to play again?", True, (255, 255, 255))
        self.yes_button = self.font.render("Yes", True, (255, 255, 255))
        self.no_button = self.font.render("No", True, (255, 255, 255))
        # Set the position for the prompt text
        self.prompt_rect = self.prompt_text.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 2))
        # Calculate the dimensions and positions for the buttons
        button_width = max(self.yes_button.get_width(), self.no_button.get_width())
        button_height = self.yes_button.get_height()
        button_spacing = 20
        self.yes_button_rect = pygame.Rect((cell_number * cell_size - button_width * 2 - button_spacing) // 2,
                                           cell_number * cell_size // 1.5,
                                           button_width, button_height)
        self.no_button_rect = pygame.Rect(self.yes_button_rect.right + button_spacing,
                                          cell_number * cell_size // 1.5,
                                          button_width, button_height)
        # Create an overlay surface for visual effect
        self.overlay_surface = pygame.Surface((cell_number * cell_size, cell_number * cell_size), pygame.SRCALPHA)
        self.overlay_surface.fill((175, 215, 70))

    # Method to draw the restart screen on the given surface
    def draw(self, screen, background_surface):
        # Blit the background surface, overlay, prompt text, and buttons on the screen
        screen.blit(background_surface, (0, 0))
        screen.blit(self.overlay_surface, (0, 0))
        screen.blit(self.prompt_text, self.prompt_rect.topleft)
        pygame.draw.rect(screen, (175, 215, 70), self.yes_button_rect, border_radius=15)
        pygame.draw.rect(screen, (175, 215, 70), self.no_button_rect, border_radius=15)
        screen.blit(self.yes_button, (self.yes_button_rect.x + (self.yes_button_rect.width - self.yes_button.get_width()) // 2,
                                      self.yes_button_rect.y))
        screen.blit(self.no_button, (self.no_button_rect.x + (self.no_button_rect.width - self.no_button.get_width()) // 2,
                                     self.no_button_rect.y))

    # Method to handle events, such as button clicks
    def handle_events(self, event):
        # Check for mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the Yes button is clicked and return True
            if self.yes_button_rect.collidepoint(event.pos):
                return True
            # Check if the No button is clicked and return False
            elif self.no_button_rect.collidepoint(event.pos):
                return False
        return None

# Define the class for the snake
class SNAKE:
    def __init__(self):
        # Initialize snake properties
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        # Load snake head images
        self.head_up = pygame.image.load('Graphics/snake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snake/head_left.png').convert_alpha()

        # Load snake tail images
        self.tail_up = pygame.image.load('Graphics/snake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snake/tail_left.png').convert_alpha()

        # Load other body segment images
        self.body_vertical = pygame.image.load('Graphics/snake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snake/body_horizontal.png').convert_alpha()
        self.body_tr = pygame.image.load('Graphics/snake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snake/body_bl.png').convert_alpha()

        # Load crunch sound
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    # Method to draw the snake on the screen
    def draw_snake(self, screen):
        # Update head and tail graphics
        self.update_head_graphics()
        self.update_tail_graphics()

        # Draw each segment of the snake
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    # Method to update the head graphics based on the direction
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    # Method to update the tail graphics based on the direction
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    # Method to move the snake
    def move_snake(self):
        # Check if a new block is to be added
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    # Method to add a new block to the snake
    def add_block(self):
        self.new_block = True

    # Method to play the crunch sound
    def play_crunch_sound(self):
        self.crunch_sound.play()

    # Method to reset the snake
    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

# Define the class for the fruit
class FRUIT:
    def __init__(self):
        # Load fruit images
        self.fruit_images = {
            "apple": pygame.image.load('Graphics/fruit/apple.png').convert_alpha(),
            "blackberry": pygame.image.load('Graphics/fruit/blackberry.png').convert_alpha(),
            "peach": pygame.image.load('Graphics/fruit/peach.png').convert_alpha(),
            "pear": pygame.image.load('Graphics/fruit/pear.png').convert_alpha(),
            "pineapple": pygame.image.load('Graphics/fruit/pineapple.png').convert_alpha()
        }
        # Randomize the initial fruit position and type
        self.randomize()

    # Method to draw the fruit on the screen
    def draw_fruit(self, screen):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.fruit_images[self.fruit_type], fruit_rect)

    # Method to randomize the fruit position and type
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.fruit_type = random.choice(["apple", "blackberry", "peach", "pear", "pineapple"])

# Define the class for the main game
class MAIN:
    def __init__(self):
        # Initialize game components
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.start_screen = StartScreen()
        self.game_active = False

    # Method to update the game state
    def update(self):
        if self.game_active:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

    # Method to draw game elements on the screen
    def draw_elements(self, screen):
        if self.game_active:
            self.draw_grass(screen)
            self.fruit.draw_fruit(screen)
            self.snake.draw_snake(screen)
            self.draw_score(screen)
        else:
            self.start_screen.draw(screen)

    # Method to check for collisions between snake and fruit
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    # Method to check for game over conditions
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    # Method to handle game over
    def game_over(self):
        self.snake.reset()
        self.game_active = False

    # Method to draw the grass background on the screen
    def draw_grass(self, screen):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    # Method to draw the score on the screen
    def draw_score(self, screen):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = fruit_box.get_rect(midright=(score_rect.left, score_rect.centery))
        screen.blit(score_surface, score_rect)
        screen.blit(fruit_box, apple_rect)

    # Method to reset the game
    def reset(self):
        self.snake.reset()
        self.game_active = True

# Set up Pygame and mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Set up game constants and events
cell_size = 40
cell_number = 20
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# Set up the game screen
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit_box = pygame.image.load('Graphics/fruit/fruit_box.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

# Initialize game screens and components
main_game = MAIN()
start_screen = StartScreen()
gameplay_screen = GameplayScreen()
restart_screen = RestartScreen()
current_screen = "start"
background_surface = pygame.Surface((cell_number * cell_size, cell_number * cell_size))
background_surface.fill((175, 215, 70))

# Load background music
pygame.mixer.music.load("Sound/Gramatik - Muy Tranquilo.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if current_screen == "start":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                result = start_screen.handle_events(event)
                if result == "start":
                    main_game.game_active = True
                    current_screen = "game"
                elif result == "gameplay":
                    current_screen = "gameplay"
        elif current_screen == "game":
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, +1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(+1, 0)
            if not main_game.game_active:
                current_screen = "restart"
        elif current_screen == "gameplay":
            result = gameplay_screen.handle_events(event)
            if result == "back":
                current_screen = "start"
        elif current_screen == "restart":
            result = restart_screen.handle_events(event)
            if result is not None:
                if result:
                    main_game.reset()
                    current_screen = "game"
                else:
                    current_screen = "start"

    screen.fill((175, 215, 70))

    if current_screen == "start":
        start_screen.draw(screen)
    elif current_screen == "game":
        main_game.draw_elements(screen)
    elif current_screen == "gameplay":
        gameplay_screen.draw(screen)
    elif current_screen == "restart":
        restart_screen.draw(screen, background_surface)

    pygame.display.update()
    clock.tick(60)