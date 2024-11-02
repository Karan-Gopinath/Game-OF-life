import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the grid (0 = dead, 1 = alive)
def initialize_grid(N):
    return np.random.choice([0, 1], size=(N, N), p=[0.7, 0.3])

# Count live neighbors for a cell
def count_live_neighbors(grid, x, y):
    N = grid.shape[0]
    live_neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):  # Don't count the cell itself
                live_neighbors += grid[(x + i) % N][(y + j) % N]
    return live_neighbors

# Apply the rules of the game to update the grid
def update(grid):
    N = grid.shape[0]
    new_grid = grid.copy()
    for x in range(N):
        for y in range(N):
            live_neighbors = count_live_neighbors(grid, x, y)
            if grid[x, y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = 0  # Cell dies
            else:
                if live_neighbors == 3:
                    new_grid[x, y] = 1  # Cell becomes alive
    return new_grid

# Visualization using matplotlib
def visualize_game(N, generations):
    grid = initialize_grid(N)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap='binary')

    def animate(frame):
        nonlocal grid
        grid = update(grid)
        img.set_data(grid)
        return [img]

    ani = animation.FuncAnimation(fig, animate, frames=generations, interval=200, blit=True)
    plt.show()

# Parameters: Grid size and number of generations
N = 50  # Grid size (N x N)
generations = 100  # Number of generations to simulate

visualize_game(N, generations)
