import pygame
from Move import MoveImg
from Player import Bird
import random
background = pygame.image.load("./day02/img/background.png")
ground = pygame.image.load("./day02/img/ground.png")
bound_top = pygame.image.load("./day02/img/bound_up.png")
bound_down = pygame.image.load("./day02/img/bound_down.png")
pygame.init()
WIDTH, HEIGHT = 382, 681
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# 创建两个背景板的移动对象
bg_speed = 5
bg1 = MoveImg(screen, background, (0, 0), bg_speed, -WIDTH, (WIDTH, 0))
bg2 = MoveImg(screen, background, (WIDTH, 0), bg_speed, -WIDTH, (WIDTH, 0))

g1 = MoveImg(screen, ground, (0, 568), 4, -WIDTH, (WIDTH, 0))
g2 = MoveImg(screen, ground, (WIDTH, 568), 4, -WIDTH, (WIDTH, 0))


def bounds_f(pos_x):
    y = random.randint(130, 539)

    # 上面的管子
    b_t = MoveImg(screen, bound_top, (pos_x, y-526), 4, -69, (WIDTH+225, 0))
    b_d = MoveImg(screen, bound_down, (pos_x, y), 4, -69, (WIDTH+225, 0))
    return b_t, b_d


all_bound = []
for i in range(3):
    all_bound.append(bounds_f(200+225*i))

while True:
    bg1.move()
    bg2.move()
    for t in all_bound:
        t[0].move()
        t[1].moveRandom(130, 539)
        t[0].y = t[1].y-526
    g1.move()
    g2.move()
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
