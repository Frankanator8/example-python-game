from core.gameObject import GameObject
from core.gamerunner import GameRunner
from example.ball import Ball
from library.components.Collider import Collider
from library.components.TextRender import TextRender


class GameOver(GameObject):
    def __init__(self, parent):
        super().__init__(0, 600, parent)
        self.score = 0
        self.add_component(Collider(self, self.game_over, (0, 0), (800, 10)))

    def game_over(self, other):
        if isinstance(other, Ball):
            GameRunner.GLOBAL_RUNNER.remove_gameObject(other)
            text = GameObject(300, 250, self.parent)
            text.add_component(TextRender(text, "Game Over\nScore: " + str(self.score), ("Arial", 48), (255, 0, 0), outline=3, outline_color=(0, 0, 0)))
            GameRunner.GLOBAL_RUNNER.add_gameObject(text)
