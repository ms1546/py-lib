import sys
import random

import pygame

pygame.init()

window_size = (1000, 1000)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Maze Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

maze_width, maze_height = 25, 25
block_size = 40

maze = [[1 for x in range(maze_width)] for y in range(maze_height)]

def generate_maze(x, y):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    random.shuffle(dir)
    for dx, dy in dir:
        nx, ny = x + dx*2, y + dy*2
        if 0 <= nx < maze_width and 0 <= ny < maze_height and maze[ny][nx] == 1:
            maze[y+dy][x+dx] = 0
            maze[ny][nx] = 0
            generate_maze(nx, ny)

maze[1][1] = 0
generate_maze(1, 1)

def draw_maze():
    for y in range(maze_height):
        for x in range(maze_width):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, rect)

player_pos = [1, 1]
player_size = 30

def draw_player():
    player_rect = pygame.Rect(
        player_pos[0]*block_size + (block_size - player_size) / 2,
        player_pos[1]*block_size + (block_size - player_size) / 2,
        player_size,
        player_size)
    pygame.draw.rect(screen, RED, player_rect)

def move_player(dx, dy):
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy
    if maze[new_y][new_x] == 0 or maze[new_y][new_x] == 2:
        player_pos[0] = new_x
        player_pos[1] = new_y
        if maze[new_y][new_x] == 2:
            print("Goal reached! Game Over.")
            pygame.quit()
            sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)
            elif event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)

    screen.fill(WHITE)
    draw_maze()
    draw_player()

    pygame.display.flip()

pygame.quit()
sys.exit()
