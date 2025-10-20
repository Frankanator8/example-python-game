import pygame

from core.component import Component


class BasicMovement(Component):
    def __init__(self, gameObject, speed=10.0):
        super().__init__(gameObject)
        self.speed = speed

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos):
        if keys[pygame.K_LEFT]:
            self.gameObject.localPosition = (self.gameObject.localPosition[0] - self.speed * dt,
                                             self.gameObject.localPosition[1])
        if keys[pygame.K_RIGHT]:
            self.gameObject.localPosition = (self.gameObject.localPosition[0] + self.speed * dt,
                                             self.gameObject.localPosition[1])
        if keys[pygame.K_UP]:
            self.gameObject.localPosition = (self.gameObject.localPosition[0],
                                             self.gameObject.localPosition[1] - self.speed * dt)
        if keys[pygame.K_DOWN]:
            self.gameObject.localPosition = (self.gameObject.localPosition[0],
                                             self.gameObject.localPosition[1] + self.speed * dt)