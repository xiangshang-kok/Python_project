import pygame
# 初始化
pygame.init()

# 创建一个窗口
screen = pygame.display.set_mode((640, 480))
# 更改窗口名称
pygame.display.set_caption("是男人就坚持100秒")

# 填充颜色
screen.fill((255, 255, 255))
ball_y = 30
ball_x = 320
# 重力加速度
g = 9.8*100
# 设置y轴速度，x轴速度
vy, vx = 0, 0

# 方块的位置
rx, ry = 300, 470
# 方块的宽高
w, h = 100, 10
# 方块的移动速度
rect_speed = 10
# 刷新窗口
pygame.display.update()

FPS = 60
# 帧率计时器
clock = pygame.time.Clock()
# 画圆


def draw_circle():
    global ball_y, ball_x, vy, vx, g, FPS, screen, rx, ry
    green_ball = pygame.draw.circle(
        screen, (255, 128, 0), (ball_x, ball_y), 30)
    vy += g*1/FPS
    ball_y += vy*1/FPS
    ball_x += vx*1/FPS
    # 左边界限定
    if ball_x <= 30:
        vx = -vx
        ball_x = 30
    # 右边界限定
    if ball_x >= 610:
        vx = -vx
        ball_x = 610
    # 上边界限定
    if ball_y <= 30:
        vy = -vy
        ball_y = 30

    if ball_y >= 500:
        rect = resultMenu()
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            mx, my = pygame.mouse.get_pos()
            if rect.x < mx < rect.x+rect.width:
                if rect.y < my < rect.y+rect.height:
                    ball_x = 320
                    ball_y = 30
                    rx = 300
                    ry = 470
                    vx, vy = 0, 0

                    # if ball_y >= 450:
                    #     vy = -vy
                    #     ball_y = 450
    return green_ball


def draw_rect():
    # 键盘控制左右移动
    global rx, ry, w, h, screen
    key = pygame.key.get_pressed()
    if(key[pygame.K_a]):
        rx -= rect_speed
    elif key[pygame.K_d]:
        rx += rect_speed
    if rx <= 0:
        rx = 0
    if rx >= 540:
        rx = 540
    # 画方块
    return pygame.draw.rect(screen, (128, 255, 0), (rx, ry, w, h))


def timer():
    time = pygame.time.get_ticks
    return time


def resultMenu():
    # 1.字体文件的路径
    # 2.字号
    f = pygame.font.Font("E:\Python_project\img\STHUPO.TTF", 80)
    # 渲染字体  -->True抗锯齿
    over = f.render("Game Over", True, (255, 0, 0))
    btn = f.render("Restart", True, (250, 0, 255))
    over_x = 320-(over.get_width())/2
    over_y = 240-(over.get_height())/2-30
    screen.blit(over, (over_x, over_y))
    btn_x = 320-(btn.get_width())/2
    btn_y = 240-(btn.get_height())/2+30
    r = screen.blit(btn, (btn_x, btn_y))
    return r


while True:
    # 画小球
    # (屏幕，颜色，圆心坐标，半径，线宽=0)
    screen.fill((255, 255, 255))
    green_ball = draw_circle()
    yellow_ball = draw_rect()
    if green_ball.colliderect(yellow_ball):
        vy = -vy
        ball_y = 440
        if -0.5 < vx < 0.5:
            # 小球打在板的左侧
            if ball_x < rx+w/2:
                vx = -g*1/FPS*((rx+w/2-ball_x)/3)
            else:
                yx = g*1/FPS*((ball_x-rx-w/2)/3)

    # 固定帧率为设定帧率
    clock.tick(FPS)
    pygame.display.update()
   # 遍历所有触发的事件
    for event in pygame.event.get():
        # 如果点击了X按钮
        if event.type == pygame.QUIT:
            # 关闭程序
            exit()
    pass
