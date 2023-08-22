import pygame
import numpy as np
import sys
import time

pygame.init()

width, height = 640, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("maze using bfs")

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

start_node = (1, 1)
end_node = (7, 8)

queue = []
visited = []
path = {}

queue.append(start_node)
pathway = [end_node]

maze_layout = [
    "##########",
    "#S_______#",
    "#_##_##_##",
    "#__#_____#",
    "#_##_##_##",
    "#__#__#__#",
    "#_##_##_##",
    "#_______E#",
    "#_##_##_##",
    "##########"
]

maze_array = np.array([list(row) for row in maze_layout])

rect_size = (64, 64)


def change_coordinate(x, r, c):
    return (x[0] + r, x[1] + c)

def backtrack(parent):
    while True:
        neighbor_found = False
        for dir in directions:
            neighbor = change_coordinate(parent, dir[0], dir[1])
            if maze_layout[neighbor[1]][neighbor[0]] != "#" and (parent == start_node or parent == neighbor):
                pathway.append(neighbor)
                parent = neighbor
                neighbor_found = True
                break
        if parent == start_node or not neighbor_found:
            break

def bfs(queue, visited):
    while queue:
        parent_node = queue.pop(0)
        neighbor_nodes = []

        if parent_node == end_node:
            return

        for i in directions:
            coordinate = change_coordinate(parent_node, i[0], i[1])

            if coordinate not in visited and maze_layout[coordinate[1]][coordinate[0]] != "#":
                queue.append(coordinate)
                visited.append(coordinate)
                neighbor_nodes.append(coordinate)

        path[parent_node] = neighbor_nodes


bfs(queue, visited)
backtrack(end_node)

for i in range(10):
    for k in range(10):
        if maze_layout[i][k] == "S":
            playerX = k * rect_size[0]
            playerY = i * rect_size[0]

clock = pygame.time.Clock()  # Create a clock object
index = 0  # Index for current position in pathway

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    for i in range(10):
        for k in range(10):
            if maze_layout[i][k] == "#":
                pygame.draw.rect(screen, black, (k * rect_size[0], i * rect_size[1], rect_size[0], rect_size[1]))
            elif maze_layout[i][k] == "E":
                pygame.draw.rect(screen, red, (k * rect_size[0], i * rect_size[1], rect_size[0], rect_size[1]))

    if index < len(pathway):
        playerX = pathway[index][0] * rect_size[0]
        playerY = pathway[index][1] * rect_size[0]
        pygame.draw.rect(screen, (0, 0, 255), (playerX, playerY, rect_size[0], rect_size[1]))
        pygame.display.update()
        index += 1
        time.sleep(1)  # Add a 1-second delay

    pygame.display.update()

    if index >= len(pathway):
        running = False

pygame.quit()
sys.exit()

