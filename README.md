# Hi there, I'm Sarthak Jain 👋

Welcome to my GitHub profile! I’m a **Game Developer** and **Machine Learning Enthusiast** passionate about building engaging, intelligent systems and solving real-world problems through code. You’ll find projects here spanning game development, artificial intelligence, and data science—crafted with curiosity and code.

## 👾 Maze Game with Q-Learning

One of my featured projects is a **Maze Game** where an agent learns to navigate through a randomly generated maze using **Q-learning**, a reinforcement learning technique. The agent earns rewards for smart decisions and penalties for hitting walls, learning from trial and error.

### ⚙️ Key Features:
- **Dynamic Maze Generation:** A new maze is generated each time the game starts.
- **Q-Learning Intelligence:** The agent trains and updates its Q-table to improve pathfinding over episodes.
- **Reward System:**
  - **+50** for reaching the goal (green tile).
  - **+5** for moving onto a white (safe) tile.
  - **−10** for hitting a wall (black tile).
- **Visual Simulation:** Built using `pygame` for a smooth, real-time display of the agent’s journey.

### 🗂️ File Structure:
```bash
main.py – Initializes the game loop and UI using pygame.

maze_env.py – Handles environment logic, maze generation, and agent movement.

agent.py – Implements the Q-learning algorithm and learning mechanism.

```
### 🖥️ How to Run:

```bash
git clone https://github.com/SarthajNp/maze-game.git
cd maze-game
pip install numpy pygame
python main.py
``` 
