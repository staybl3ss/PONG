# Pong Game

A two-player Pong game built with Python using object-oriented programming (OOP) and the `turtle` graphics module. This is a game I created after making the Snake Game, as I had more confidence in building different rule-oriented systems with the turtles module. I wanted to recreate another childhood game that would be somewhat more difficult than the Snake game. In this project, I had to consider variable difficulties and speeds, whereas in the Snake game everything is relatively constant in difficulty.

# Goal

The goal of this project was to:
- Reinforce object-oriented programming skills using an interactive format.
- Build a visually interactive game using Python that I am familiar with from childhood.
- Understand game loops, how to code in collision detection, and account for listening to real-time keyboard inputs.

# Core Logic

- The game consists of a two-dimensional field with two paddles on each side and a bouncing ball.
- Two adjacent players can control the paddles using keyboard buttons (W/S for left, Up/Down for right).
- The ball only bounces off the top and bottom walls and the paddles, if you hits the opposing player's side, you gain a point.
- If the player misses the ball, the opponent scores a point.
- Score is tracked and displayed on the screen, as you continue to bounce the ball back-and-forth, the speed of the ball will increase, thus making the game get more difficult until a point is scored.

# Features

- Real-time collision detection
- Paddle movement with keyboard input
- Scoreboard
- Ball position and speed resets and restarts after each point is scored

## 📚 Concepts Used

- Classes (for paddles, ball, scoreboard)
- Game loop using `while`
- Event-driven input handling
- Collision and boundary detection
- Variable speed/difficulty
