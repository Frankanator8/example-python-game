from core.gamerunner import GameRunner
from example.ball import Ball
from example.gameover import GameOver
from example.paddle import Paddle
from example.reflector import Reflector
from library.components.TextRender import TextRender


class ExampleRunner(GameRunner):
    def __init__(self):
        super().__init__()
        ball = Ball()
        self.add_gameObject(ball)
        self.add_gameObject(Reflector(800, 0, self.rootGameObject))
        self.add_gameObject(Reflector(0, 0, self.rootGameObject))
        self.add_gameObject(Reflector(0, 600, self.rootGameObject, vertical=False))
        self.add_gameObject(Reflector(0, 0, self.rootGameObject, vertical=False))
        gameOver = GameOver(self.rootGameObject)
        self.add_gameObject(gameOver)
        self.add_gameObject(Paddle(350, 500, self.rootGameObject, gameOver))

        self.add_gameObject(TextRender(self.rootGameObject, "Example Game\nUse A/D or Arrow Keys to move", ("Arial", 24), (255, 255, 255), outline=2, outline_color=(0, 0, 0)))