import numpy as np

maze_layout = [
    "##########", "#S_______#", "#_##_##_##", "#__#_____#", "#_##_##_##",
    "#__#__#__#", "#_##_##_##", "#_______E#", "#_##_##_##", "##########"
]

maze_array = np.array([list(row) for row in maze_layout])
# L, R, U, D
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
queue = []
visited = []

print(maze_array)

start_node = (1, 1)
end_node = (7, 8)

path = {}

queue.append(start_node)
pathway = [end_node]

def backtrack(parent, start_node, end_node, path):

    while True:

        if parent == start_node or parent == (1, 2) or parent == (2, 1):
            break

        for key in path.keys():
            valueList = list(path[key])
            for k in range(0, len(valueList)):
                if valueList[k] == parent:
                    # should be appending parent
                    parent = key
                    pathway.append(parent)

    pathway.reverse()
    print("\nPathway:", pathway)
    print("Length of Path: ", len(pathway))


def bfs(queue, visited):
    while queue:
        current_node = queue.pop(0)
        neighbor_nodeList = []

        if current_node == end_node:
            return

        for i in directions:
            neighbor_node = updateCoordinate(current_node, i[0], i[1])
            r = neighbor_node[0]
            c = neighbor_node[1]

            if neighbor_node not in visited and maze_array[r][c] != "#":
                queue.append(neighbor_node)
                visited.append(neighbor_node)
                neighbor_nodeList.append(neighbor_node)

        path[current_node] = neighbor_nodeList


def updateCoordinate(x, r, c):
    return (x[0] + r, x[1] + c)


bfs(queue, visited)
backtrack(end_node, start_node, end_node, path)

for x, y in pathway:
    if maze_array[x][y] != 'E':
        maze_array[x][y] = 'x'

print(maze_array) # labels the path w E, will work on creating random mazes (using another algo)
