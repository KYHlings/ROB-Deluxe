import pygame
pygame.init()

screen_size = (800, 600)
STARTING_SCREEN = "Title Screen"


class Game:
    def __init__(self, **options):
        self.screen = options.get("screen", pygame.display.set_mode(screen_size))
        self.game_state = [STARTING_SCREEN]
        self.done = False
        self.clock = pygame.time.Clock()
        self.messages = []

    def go(self):
        while True:
            if not self.game_state:
                break
            next_state = self.game_state.pop()
            print("Going to: ", next_state)
            function_name = next_state.replace(" ", "")
            if hasattr(self, function_name):
                function = getattr(self, function_name)
                function()
            else:
                break
        print("game stopped")

    def notify(self, message):
        self.messages.append(message)

    def title_screen(self):
        self.done = False
        while not self.done:
            for message in self.messages:
                headline = message.get("headline", "")

