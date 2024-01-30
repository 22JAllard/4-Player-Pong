import pygame #import pygame
import sys #imports system

width = 500
height = 500
fps=60
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

run = True
while run:
    screen.fill(black)
    pygame.display.flip()

pygame.quit()
sys.exit()
