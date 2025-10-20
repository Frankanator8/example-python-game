# Example Python Framework

This is for those who are new to game development and have some previous knowledge of CS principles. It implements a game engine in Python and Pygame.

Usage:

The framework is roughly based on Unity, in that everything is represented in GameObjects and Components. GameObjects have a absolute/local transform and follow a tree hierarchy, and its behavior can be modified by Components.
You can add GameObjects to the runner (which adds to the "root" gameObject), find the runner via GameRunner.GLOBAL_RUNNER, and code updates via update() in both components and GameObjects.

For further help/questions/bug reports pls email [hfl2114@columbia.edu](mailto:hfl2114@columbia.edu)
