import pygame
from Move import MoveImg
from Player import Bird
import random
background = pygame.image.load("./day02/img/background.png")
ground = pygame.image.load("./day02/img/ground.png")
bound_top = pygame.image.load("./day02/img/bound_up.png")
bound_down = pygame.image.load("./day02/img/bound_down.png")
b_player = pygame.image.load("./day02/img/bird_blue_0.png")

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
player = Bird(screen, b_player, (120, 100))


def bounds_f(pos_x):
    y = random.randint(130, 539)

    # 上面的管子
    b_t = MoveImg(screen, bound_top, (pos_x, y-526), 4, -69, (WIDTH+225, 0))
    b_d = MoveImg(screen, bound_down, (pos_x, y), 4, -69, (WIDTH+225, 0))
    return b_t, b_d


all_bound = []
for i in range(3):
    all_bound.append(bounds_f(300+225*i))
# 结束菜单


def endMenu():
    global player
    # 载入字体
    font = pygame.font.Font(None, 80)
    # 用字体写字
    font_word = font.render('Game Over', True, 'red')
    while True:
        # screen.fill(())
        screen.blit(font_word, (70, 200))
        clock.tick(FPS)
        pygame.display.update()
        # 点击×事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = Bird(screen, b_player, (120, 100))
                    all_bound.clear()
                    for temp in range(3):
                        all_bound.append(bounds_f(350+225*temp))
                    return


# 存储所有的rect对象
collider = []
while True:

    bg1.move()
    bg2.move()

    for t in all_bound:
        r3 = t[0].move()
        r4 = t[1].moveRandom(130, 539)
        t[0].y = t[1].y-526
        collider.append(r3)
        collider.append(r4)
    r1 = g1.move()
    r2 = g2.move()
    collider.append(r1)
    collider.append(r2)

    p1 = player.fall()
    c = p1.collidelist(collider)
    if c != -1:
        endMenu()
    # 清空列表
    collider.clear()
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.jump(20)
