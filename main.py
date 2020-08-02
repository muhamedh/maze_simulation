from pygame.locals import *
import time
import sys
import pygame
import random
# This is a test branch
width = 2
height = 2

while width % 2 == 0 and height % 2 == 0:
    print('Please input odd number larger than 7...')
    height = int(input())
    width = height


DISPLAY_WIDTH = (width * 10)
DISPLAY_HEIGHT = (height * 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

v_width = int((width-1) / 2)
v_height = int((height - 1) / 2)


board = [[0 for i in range(width)] for j in range(height)]

visited = [[0 for i in range(int((width - 1) / 2))]
           for j in range(int((height-1)/2))]
stack = [(1, 1)]
directions = [[-2, 0, 'S'], [2, 0, 'J'], [0, -2, 'Z'], [0, 2, "I"]]

for i in range(v_height):
    for j in range(v_width):
        visited[i][j] = 0

visited[0][0] = 1

for i in range(height):
    for j in range(width):
        if i % 2 != 0 and j % 2 != 0:
            board[i][j] = 0
        else:
            board[i][j] = 1

while len(stack) != 0:
    curr_point = stack[-1]
    curr_x = curr_point[0]
    curr_y = curr_point[1]
    stack.pop()
    random.shuffle(directions)
    # print()
    # print(curr_x, curr_y)
    # for i in range(v_height):
    #     line_str = ''
    #     for j in range(v_width):
    #         line_str += str(visited[i][j])
    #     print(line_str)
    # for i in range(height):
    #     line_str = ''
    #     for j in range(width):
    #         line_str += str(board[i][j])
    #     print(line_str)
    # input()
    for x in directions:
        curr_x = curr_point[0]
        curr_y = curr_point[1]
        curr_x += x[0]
        curr_y += x[1]
        heading = x[2]
        # print(curr_x, curr_y, heading)

        if(curr_x >= 1 and curr_x < height - 1 and curr_y > 0 and curr_y < width - 1):
            # print('call:' + str(curr_x) + ' ' + str(curr_y))
            if(visited[int((curr_x-1)/2)][int((curr_y-1)/2)] == 0):
                visited[int((curr_x-1)/2)][int((curr_y-1)/2)] = 1
                if heading == 'S':
                    board[curr_x+1][curr_y] = 0
                elif heading == 'J':
                    board[curr_x-1][curr_y] = 0
                elif heading == 'I':
                    board[curr_x][curr_y-1] = 0
                elif heading == 'Z':
                    board[curr_x][curr_y+1] = 0
                #board[curr_x][curr_y] = 0
                # print(curr_x, curr_y)
                stack.append((curr_x, curr_y))

board[1][0] = 0
#board[width-2][height-1] = 0

for i in range(height):
    line_str = ''
    for j in range(width):
        line_str += str(board[i][j])
    print(line_str)

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
pygame.display.set_caption('Maze Game')

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

while True:
    DISPLAY.fill(WHITE)
    for i in range(height):
        for j in range(width):
            if(board[i][j] == 1):
                pygame.draw.rect(DISPLAY, BLACK, ((i*10), (j*10), 10, 10))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
