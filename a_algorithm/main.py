import numpy as np
import heapq
import matplotlib.pyplot as plt

grid_size = 100
forest_test = np.zeros((grid_size, grid_size))  #normal: 0, fire 1

forest_test[30:70, 30:70] = 1  #fire location
start = (5, 5)  #start
goal = (95, 95) #end

def a_star(grid, start, goal):

    def heuristic(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5  #Euclidean distance

    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                if grid[neighbor] == 1:  # 장애물 회피
                    continue

                move_cost = 1.414 if dx != 0 and dy != 0 else 1
                tentative_g_score = g_score[current] + move_cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return []

path = a_star(forest_test, start, goal)

plt.figure(figsize=(6, 6))
plt.imshow(forest_test, cmap="gray_r")
for x, y in path:
    plt.scatter(y, x, c="red", s=10)

plt.scatter(start[1], start[0], c="green", marker="o", label="Start")
plt.scatter(goal[1], goal[0], c="blue", marker="o", label="Goal")
plt.legend()
plt.title(f"A* length: {len(path)}")
plt.show()
