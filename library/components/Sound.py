import pygame

from core.component import Component


class Sound(Component):
    _SOUND_CACHE = {}
    def __init__(self, gameObject, file_path):
        super().__init__(gameObject)
        self.file_path = file_path
        self.sound = self.load_sound(file_path)
        self._play = False

    def _load_sound(self, name):
        if name in Sound._SOUND_CACHE.keys():
            return Sound._SOUND_CACHE[name]
        sound = pygame.mixer.Sound(name)
        Sound._SOUND_CACHE[name] = sound
        return sound

    def play(self):
        self._play = True

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos):
        if self._play:
            self.sound.play()
            self._play = False