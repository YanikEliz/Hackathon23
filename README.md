# Hackathon23

# Space Debris Collision Simulation

This is a 2D simulation that models the behavior of space debris collisions, where each collision spawns a new debris object with random properties. Developed in under two hours for the RUC Hackathon 2023 Spring, the simulation utilizes Python's Pygame for rendering and Pymunk for physics calculations.

## Features

- **Real-Time Collision Detection:** Debris objects collide with each other and the simulation boundaries.
- **Dynamic Object Generation:** New debris objects are spawned with random sizes, velocities, and colors upon collision.
- **Physics Simulation:** Realistic motion and collision responses are computed using Pymunk.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YanikEliz/Hackathon23.git
   cd Hackathon23
   ```

2. **Install Dependencies:**

   Ensure you have Pygame and Pymunk installed.

## Usage

Run the simulation script:

```bash
python main.py
```

A window will open displaying the simulation. Debris objects will move and collide within the window, generating new debris upon each collision.

## Acknowledgments

- [Pygame](https://www.pygame.org/): A set of Python modules designed for writing video games.
- [Pymunk](https://www.pymunk.org/): An easy-to-use pythonic 2D physics library built on top of Chipmunk2D.

## License

This project is licensed under the MIT License.