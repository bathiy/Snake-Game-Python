# 🐍 Snake Game (Python Turtle - OOP)

This is a classic Snake Game implemented using Python's `turtle` graphics module. The game is designed using **Object-Oriented Programming (OOP)** principles, making it modular, easy to understand, and extend.

## 🎮 Game Features

- Smooth snake movement using keyboard arrows (`↑ ↓ ← →`)
- Food appears randomly — snake grows when it eats
- Scoreboard keeps track of the score
- Game over when:
  - The snake hits the wall
  - The snake collides with itself
- Press **Enter** (`Return` key) to restart the game after it ends

  ## 🧠 Concepts Used

- Object-Oriented Programming
  - Each major part of the game (`Snake`, `Food`, `Score`) is implemented as a class
- `turtle` module for graphical rendering
- Keyboard event handling (`onkey`)
- Collision detection using position comparison
- Game loop using `time.sleep()` and `screen.update()`

## ▶️ How to Run

1. Make sure you have Python installed (preferably 3.6+).
2. Clone this repository or download the files.
3. Run
`python main.py`
