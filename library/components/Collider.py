from core.component import Component


class Collider(Component):
    ALL_COLLIDERS = []
    def __init__(self, gameObject, on_collision, offset=(0,0), size=(10,10)):
        """Initializes the Collider component."""
        super(Collider, self).__init__(gameObject)
        self.offset = offset
        self.size = size
        self.on_collision = on_collision
        Collider.ALL_COLLIDERS.append(self)
        self._entered = []

    def world_rect(self):
        """Returns the rectangle representing the collider in world coordinates."""
        return (
            self.gameObject.absolutePosition[0] + self.offset[0],
            self.gameObject.absolutePosition[1] + self.offset[1],
            self.size[0],
            self.size[1]
        )

    def intersect(self, other):
        """Returns True if this collider intersects with another collider."""
        rect1 = self.world_rect()
        rect2 = other.world_rect()

        return not (rect1[0] + rect1[2] < rect2[0] or
                    rect1[0] > rect2[0] + rect2[2] or
                    rect1[1] + rect1[3] < rect2[1] or
                    rect1[1] > rect2[1] + rect2[3])

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos):
        """Checks for collisions with other colliders and triggers the on_collision callback."""
        for collider in Collider.ALL_COLLIDERS:
            if collider is not self and self.intersect(collider):
                if collider not in self._entered:
                    self._entered.append(collider)
                    print(collider.gameObject, "collided with", self.gameObject)
                    self.on_collision(collider.gameObject)

        for collider in self._entered:
            if not self.intersect(collider):
                self._entered.remove(collider)
