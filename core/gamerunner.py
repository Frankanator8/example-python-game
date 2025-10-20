import pygame
from core.gameObject import GameObject

class GameRunner:
    # you will likely not need to use/modify this class that much, as it contains mostly pygame stuff
    GLOBAL_RUNNER = None
    def __init__(self, dimensions=(800, 600), gameTitle="My Game", maxFrames=-1):
        """Initializes the game runner with the specified dimensions, title, and frame limit."""
        pygame.init()
        self.rootGameObject = GameObject(0, 0, None)
        self.screen = pygame.display.set_mode(dimensions, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(gameTitle)
        self.clock = pygame.time.Clock()
        self.running = True
        self.maxFrames = maxFrames
        GameRunner.GLOBAL_RUNNER = self

    def add_gameObject(self, gameObject):
        """Adds a game object to the root game object."""
        self.rootGameObject.add_child(gameObject)

    def remove_gameObject(self, gameObject):
        self.rootGameObject.remove_child(gameObject)

    def run(self):
        """Starts the main game loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            keys = pygame.key.get_pressed()
            mousePos = pygame.mouse.get_pos()
            mouseClicked = pygame.mouse.get_pressed()
            dt = self.clock.get_time() / 1000

            self.rootGameObject.update(self.screen, dt, keys, mouseClicked, mousePos)

            if self.maxFrames > 0:
                self.clock.tick(self.maxFrames)

            else:
                self.clock.tick()
            pygame.display.flip()

