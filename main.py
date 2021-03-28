import random
import pygame, sys
import self as self
import settings


def chunk_gen_id(self):
    for x in range(self.line_height):
        self.line = random.choices([self.diamond, self.iron, self.gold, self.dirt], weights=[1, 1, 1, self.lucking], k=self.line_width)
def chunk_gen_color(self):
    for x in range(self.line_height):
        chunk_gen_id(self)
        for x in range(self.line_width):
            self.color = self.line[x]
            pygame.draw.rect(win, self.color, (self.x_in_win, self.y_in_win, self.ore_width, self.ore_height))
            self.x_in_win += self.ore_width + self.margin
        self.y_in_win += self.ore_height + self.margin
        self.x_in_win = self.x_in_win - (self.margin * self.line_width + self.line_width * self.ore_width)
    self.y_in_win = self.y_in_win - (self.margin * self.line_height + self.line_height * self.ore_height)

pygame.init()
win = pygame.display.set_mode((self.width, self.height))
pygame.display.set_caption("Ore generator")

self.chunk = chunk_gen_color(self)
pygame.display.update()

while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    self.chunk
    pygame.display.update()
