import pygame
import random
from pygame.locals import *
import sys
from ship import Ship

pygame.init()
screen_info = pygame.display.Info()

# set width and height of the screen
screen_size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(screen_size)
color = (0, 127, 255)
clock = pygame.time.Clock()


player = Ship((20, 200))

# setup game variables
numlevels = 4
level = 1






def main():
  global Level, NumLevels
  while level <= numlevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
          player.speed[0] = 10
        if event.key == pygame.K_a:
          player.speed[0] = -10
        if event.key == pygame.K_w:
          player.speed[1] = -10
        if event.key == pygame.K_s:
          player.speed[1] = 10
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
          player.speed[0] = 0
        if event.key == pygame.K_a:
          player.speed[0] = 0
        if event.key == pygame.K_w:
          player.speed[1] = 0
        if event.key == pygame.K_s:
          player.speed[1] = 0
    player.update()
    screen.fill(color)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
if __name__ == '__main__':
  main()