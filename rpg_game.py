import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'RPG Crossy Game'
# Colors using RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

class Game:

    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

            print(event)

        # game_screen.blit(player_image, (375, 375))

        pygame.display.update()
        clock.tick(self.TICK_RATE)


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# player_image = pygame.image.load('player.png')
# player_image = pygame.transform.scale(player_image, (50, 50))


    # Rectangle (x, y, width, height)
    # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
    # Circle (x, y, radius)
    # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)


pygame.quit()
quit()