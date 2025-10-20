import pygame

from core.component import Component


class ImageRender(Component):
    _IMAGE_CACHE = {}
    def __init__(self, game_object, image_path, size=None):
        """Initializes the ImageRender component with the specified image path."""
        super().__init__(game_object)
        self._image_path = image_path
        self.size = size

        self.loaded_image, self.loaded_rect = self._load_image(image_path, size=size)

        self._last_cached_direction = 0

    def set_image_path(self, image_path):
        """Sets a new image path and reloads the image."""
        self._image_path = image_path
        self.loaded_image, self.loaded_rect = self._load_image(image_path, size=self.size)

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos):
        """Renders the image onto the display target."""
        if self.gameObject.absoluteDirection != self._last_cached_direction:
            self._last_cached_direction = self.gameObject.absoluteDirection
            self.loaded_image, self.loaded_rect = self._load_image(self._image_path, size=self.size)

        displayTarget.blit(self.loaded_image, (self.gameObject.absolutePosition[0] - self.loaded_rect.width//2, self.gameObject.absolutePosition[1] - self.loaded_rect.height//2))


    def _load_image(self, name, size=None):
        # load from cache if available
        if (name, size) in ImageRender._IMAGE_CACHE.keys():
            image =  ImageRender._IMAGE_CACHE[(name, size)].copy()

        else:
            image = pygame.image.load(name).convert_alpha()
            if size is not None:
                image = pygame.transform.scale(image, size)
            ImageRender._IMAGE_CACHE[(name, size)] = image
        return self._rotate(image, self.gameObject.absolutePosition, (image.get_width()//2, image.get_height()//2), self.gameObject.absoluteDirection)

    # rotate around a set point (in most cases, center)
    def _rotate(self, image, pos, originPos, angle): # Credit to Rabbid76 (https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame)
        # offset from pivot to center
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # rotated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # rotated image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # return image
        return rotated_image, rotated_image_rect