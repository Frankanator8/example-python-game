class Component:
    """
    Base class for all components.
    Components add specific functionality to game objects.
    """
    def __init__(self, gameObject):
        super().__init__()
        """Initialize the component with a reference to its game object."""
        self.gameObject = gameObject

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos):
        """Update the component. To be overridden by subclasses. Runs every game tick."""
        pass