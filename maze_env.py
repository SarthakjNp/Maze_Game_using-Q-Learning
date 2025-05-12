import numpy as np
import random

class MazeEnv:
    def __init__(self, size=5):
        self.size = size
        self.start = (0, 0)
        self.goal = (size - 1, size - 1)
        self.reset_maze()
        self.reset()

    def reset_maze(self):
        self.maze = np.zeros((self.size, self.size))
        for _ in range(self.size * 2):
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in [self.start, self.goal]:
                self.maze[x][y] = -1

    def reset(self):
        self.agent_pos = list(self.start)
        self.score = 100
        self.done = False
        return tuple(self.agent_pos)

    def step(self, action):
        if self.done:
            return self.reset(), 0, self.done

        x, y = self.agent_pos
        dx, dy = [(0, -1), (0, 1), (-1, 0), (1, 0)][action]
        nx, ny = x + dx, y + dy

        if 0 <= nx < self.size and 0 <= ny < self.size:
            if (nx, ny) == self.goal:
                reward = 50  # Reached the goal
                self.done = True
            elif self.maze[nx][ny] == -1:
                reward = -10  # Hit a wall
                self.score -= 10
            else:
                reward = 5  # Moved on a white surface (empty space)
                self.agent_pos = [nx, ny]
        else:
            reward = -10
            self.score -= 10

        if tuple(self.agent_pos) == self.goal:
            reward = 50
            self.done = True

        if self.score <= 0:
            self.done = True
            reward = -50

        return tuple(self.agent_pos), reward, self.done