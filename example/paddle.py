import pygame

from core.component import Component
from core.gameObject import GameObject
from example.reflector import ReflectorComponent
from library.components.ImageRender import ImageRender


class Paddle(GameObject):
    def __init__(self, x, y, parent, gameOver):
        super().__init__(x, y, parent)
        self.add_component(ImageRender(self, "example/assets/lebron.jpg", (100, 10)))
        self.add_component(ReflectorScore(self, gameOver))
        self.add_component(LRMovement(self))

class LRMovement(Component):
    def __init__(self, game_object, speed=200):
        super().__init__(game_object)
        self.speed = speed

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos):
        if keys[pygame.K_LEFT]:
            self.gameObject.localPosition = (self.gameObject.localPosition[0] - self.speed * dt,
                                             self.gameObject.localPosition[1])
        if keys[pygame.K_RIGHT]:
            self.gameObject.localPosition = (self.gameObject.localPosition[0] + self.speed * dt,
                                             self.gameObject.localPosition[1])

class ReflectorScore(ReflectorComponent):
    def __init__(self, game_object, gameOver, vertical=False, size=(100, 10)):
        super().__init__(game_object, vertical=vertical, size=size)
        self.on_collision = self.on_reflect
        self.game_over = gameOver

    def on_reflect(self, ball):
        self.game_over.score += 1
        super().bounce_ball(ball)