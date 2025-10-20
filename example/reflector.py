from core.component import Component
from core.gameObject import GameObject
from library.components.Collider import Collider


class Reflector(GameObject):
    def __init__(self, x, y, parent, vertical=True):
        super().__init__(x, y, parent)
        self.vertical = vertical
        self.add_component(ReflectorComponent(self, (1, 600) if self.vertical else (800, 1), vertical=vertical))


class ReflectorComponent(Collider):
    def __init__(self, gameObject, size, vertical=True):
        super().__init__(gameObject, self.bounce_ball, (0, 0), size)
        self.vertical = vertical

    def bounce_ball(self, ball):
        if abs(ball.localDirection - 45) < 1e-5:
            if self.vertical:
                ball.localDirection = 135
            else:
                ball.localDirection = 315
        elif abs(ball.localDirection - 135) < 1e-5:
            if self.vertical:
                ball.localDirection = 45
            else:
                ball.localDirection = 225
        elif abs(ball.localDirection - 225) < 1e-5:
            if self.vertical:
                ball.localDirection = 315
            else:
                ball.localDirection = 135
        elif abs(ball.localDirection - 315) < 1e-5:
            if self.vertical:
                ball.localDirection = 225
            else:
                ball.localDirection = 45
