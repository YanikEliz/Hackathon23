import math
import pygame
import pymunk
from random import randint

class Ball:
    def __init__(self, x, y, size, collision_type):
        self.size = size
        mass = self.size**2
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        angle = randint(0, 359)
        coeff = 40000 / mass
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, self.size))
        self.body.position = (x, y)
        self.body.velocity = (coeff * math.cos(angle * math.pi / 180), coeff * math.sin(angle * math.pi / 180))
        self.shape = pymunk.Circle(self.body, self.size)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = collision_type
        space.add(self.body, self.shape)

    def draw(self):
        x, y = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(wn, self.color, (x, y), self.size)

def create_segment(pos1, pos2):
    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_shape = pymunk.Segment(segment_body, pos1, pos2, 10)
    segment_shape.elasticity = 1
    space.add(segment_body, segment_shape)

def collide(arbiter, space, data):
    new_ball = Ball(randint(0, 600), randint(0, 600), randint(10, 20), randint(1, 4))
    balls.append(new_ball)

pygame.init()
wn = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
space = pymunk.Space()

FPS = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

balls = [Ball(randint(100, 500), randint(100, 500), randint(10, 20), i + 1) for i in range(2)]
create_segment((0, 0), (600, 0))
create_segment((600, 0), (600, 600))
create_segment((600, 600), (0, 600))
create_segment((0, 600), (0, 0))
handler = space.add_collision_handler(1, 2)
handler.separate = collide

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    wn.fill(BLACK)

    for ball in balls:
        ball.draw()

    pygame.draw.line(wn, RED, (0, 0), (600, 0), 10)
    pygame.draw.line(wn, RED, (600, 0), (600, 600), 10)
    pygame.draw.line(wn, RED, (600, 600), (0, 600), 10)
    pygame.draw.line(wn, RED, (0, 600), (0, 0), 10)

    pygame.display.flip()
    clock.tick(FPS)
    space.step(1 / FPS)

pygame.quit()
