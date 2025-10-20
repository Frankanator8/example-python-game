import math

from core.component import Component
from core.gameObject import GameObject
from library.components.Collider import Collider
from library.components.ImageRender import ImageRender


class Ball(GameObject):
    def __init__(self):
        super().__init__(400, 300, None, dir=45)  # Initialize Ball at (0,0) with direction 45 degrees
        self.add_component(ImageRender(self, "example/assets/basketball.png", size=(50, 50)))  # Add ImageRender component with ball image
        self.ballMover = BallMover(self, 200)
        self.add_component(self.ballMover)
        self.add_component(Collider(self, lambda x:self.ballMover.increase_speed(), offset=(-25, -25), size=(50, 50)))  # Add Collider component with appropriate size and offset

class BallMover(Component):
    def __init__(self, game_object, speed):
        super().__init__(game_object)
        self.speed = speed  # Speed in pixels per second

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos):
        self.gameObject.localPosition = (
            self.gameObject.localPosition[0] + self.speed * dt * math.cos(math.radians(self.gameObject.localDirection)),
            self.gameObject.localPosition[1] - self.speed * dt * math.sin(math.radians(self.gameObject.localDirection)))

    def increase_speed(self):
        self.speed *= 1.05