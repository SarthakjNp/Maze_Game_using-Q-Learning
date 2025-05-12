import pygame
import time
from maze_env import MazeEnv
from agent import QLearningAgent

pygame.init()

GRID_SIZE = 5
CELL_SIZE = 100
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
GREY  = (200, 200, 200)

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Maze Game with Q-Learning")
clock = pygame.time.Clock()

def draw_maze(env):
    screen.fill(WHITE)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            val = env.maze[x][y]
            if (x, y) == tuple(env.agent_pos):
                pygame.draw.rect(screen, BLUE, rect)
            elif (x, y) == env.goal:
                pygame.draw.rect(screen, GREEN, rect)
            elif val == -1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GREY, rect, 1)
    pygame.display.flip()

env = MazeEnv(size=GRID_SIZE)
agent = QLearningAgent()

episodes = 100

for ep in range(episodes):
    env.reset_maze()
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_maze(env)
        clock.tick(FPS)

        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
        total_reward += reward

    print(f"Episode {ep + 1}: Total Reward = {total_reward}")
    time.sleep(0.5)

pygame.quit()