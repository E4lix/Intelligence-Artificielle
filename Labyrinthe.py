# Librairies
import numpy as np
import matplotlib.pyplot as plt
from mazelib import Maze
from mazelib.generate.Prims import Prims

# Random Maze
m = Maze()
m.generator = Prims(10, 10)
m.generate()
maze_grid = m.grid

# Print the Maze Grid
for row in maze_grid:
    print(" ".join(str(cell) for cell in row))

# Visualize the Maze
def visualize_maze(grid):
    plt.imshow(grid, cmap="binary")
    plt.xticks([])
    plt.yticks([])
    plt.title("Generated Maze")
    plt.show()

# Main
visualize_maze(maze_grid)