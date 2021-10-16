# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1700, 900], pygame.RESIZABLE)


class Circle:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.pos_x = self.start_x
        self.pos_y = self.start_y

        self.vector_x = random.uniform(-1, 1)
        self.vector_y = random.uniform(-1, 1)
        self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

        pygame.draw.circle(screen, (0, 0, 255), (self.pos_x, self.pos_y), 75)

    def update(self):
        if (abs(self.start_x - self.pos_x) < 100) and (abs(self.start_x + self.pos_x) > 100) and \
                (abs(self.start_y - self.pos_y) < 100) and (abs(self.start_y + self.pos_y) > 100):
            self.pos_x = self.pos_x + self.vector_x
            self.pos_y = self.pos_y + self.vector_y

        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), 35)


circles = []
running = True
while running:
    pygame.time.delay(10)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    if not circles:
        for i in range(100):
            circles.append(Circle(random.uniform(1, 1500), random.uniform(1, 1500)))
    else:
        for circle in circles:
            circle.update()

    # Flip the display
    pygame.display.update()
