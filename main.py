# Pygame
import pygame

import loader
from text import Text

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
image = loader.load_image("assets/char.png")

x = 0
y = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(image, (x, y))
    keys = pygame.key.get_pressed()
    dt = clock.get_time()/1000
    speed = 50
    if keys[pygame.K_LEFT]:
        x -= speed * dt

    if keys[pygame.K_RIGHT]:
        x += speed * dt

    if keys[pygame.K_UP]:
        y -= speed * dt

    if keys[pygame.K_DOWN]:
        y += speed * dt

    Text("this is a text object!" ,("Calibri", 15), (255, 255, 255), (400, 300)).render(screen)

    clock.tick(60)
    pygame.display.flip()

