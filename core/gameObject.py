class GameObject:
    """ GameObjects are the core of this framework. It represents an entity with position, direction, parent-child relationships, customizable with components. """
    def __init__(self, x, y, parent, dir=0, children=None, components=None):
        """ Initializes a GameObject with position, parent, direction, children, and components. """
        if children is None:
            children = []
        self._x = x
        self._y = y
        self.parent = parent
        self.children = children
        self._dir = dir
        if components is None:
            components = []
        self.components = components

        self._cachedAbsolutePosition = None
        self._cachedAbsoluteDirection = None

    def update(self, displayTarget, dt, keys, mouseClicked, mousePos): # runs every game loop
        """ Updates all components and child GameObjects. """
        for component in self.components:
            component.update(displayTarget, dt, keys, mouseClicked, mousePos)

        for child in self.children:
            child.update(displayTarget, dt, keys, mouseClicked, mousePos)

    def add_component(self, component):
        """ Adds a component to the GameObject. """
        self.components.append(component)
        component.gameObject = self

    def remove_component(self, component, recursive=True):
        """ Removes a component from the GameObject. """
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if component in current.components:
                current.components.remove(component)
                component.gameObject = None
                break

            if recursive:
                for child in current.children:
                    queue.append(child)

    def add_child(self, gameObject):
        """ Adds a child GameObject. """
        self.children.append(gameObject)
        gameObject.parent = self

    def remove_child(self, gameObject):
        """ Removes a child GameObject. """
        self.children.remove(gameObject)
        gameObject.parent = None

    @property
    def absolutePosition(self): # defines position in terms of world space
        """ Calculates the absolute position of the GameObject in world space. """
        if self._cachedAbsolutePosition is not None:
            return self._cachedAbsolutePosition

        if self.parent is None:
            return (self._x, self._y)
        else:
            parent_x, parent_y = self.parent.absolutePosition
            self._cachedAbsolutePosition = (self._x + parent_x, self._y + parent_y)
            return self._cachedAbsolutePosition

    @property
    def localPosition(self): # defines position in terms of relative position to parent
        """ Returns the local position of the GameObject relative to its parent. """
        return (self._x, self._y)

    @absolutePosition.setter
    def absolutePosition(self, value:tuple):
        self._invalidate_caches()
        if self.parent is None:
            self._x, self._y = value
        else:
            parent_x, parent_y = self.parent.absolutePosition
            self._x = value[0] - parent_x
            self._y = value[1] - parent_y

    @localPosition.setter
    def localPosition(self, value:tuple):
        self._invalidate_caches()
        self._x, self._y = value

    @property
    def absoluteDirection(self): # same idea as before
        """ Calculates the absolute direction of the GameObject in world space. """
        if self._cachedAbsoluteDirection is not None:
            return self._cachedAbsoluteDirection
        if self.parent is None:
            return self._dir
        else:
            self._cachedAbsoluteDirection = self.parent.absoluteDirection + self._dir
            return self._cachedAbsoluteDirection

    @absoluteDirection.setter
    def absoluteDirection(self, value:float):
        self._invalidate_caches()
        if self.parent is None:
            self._dir = value
        else:
            self._dir = value - self.parent.absoluteDirection

    @property
    def localDirection(self): # same idea as before
        """ Returns the local direction of the GameObject relative to its parent. """
        return self._dir

    @localDirection.setter
    def localDirection(self, value:float):
        self._invalidate_caches()
        self._dir = value


    def _invalidate_caches(self):
        """ Invalidates cached absolute position and direction. """
        self._cachedAbsolutePosition = None
        self._cachedAbsoluteDirection = None
        for child in self.children:
            child._invalidate_caches()