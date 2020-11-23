import random


class MoveImg:
    # pyhton类的构造方法
    def __init__(self, screen, image, pos, speed, bound, mpos):
        # 图片要移动的图片
        self.image = image
        # 图片初始位置
        self.x, self.y = pos
        # 图片移动速度
        self.speed = speed
        # 图片边界
        self.bound = bound
        # 图片瞬移位置
        self.mx, self.my = mpos
        # 要画到哪个屏幕上
        self.screen = screen

    def move(self):
        self.x -= self.speed
        if self.x <= self.bound:
            temp = self.bound-self.x
            self.x = self.mx-temp
        return self.screen.blit(self.image, (self.x, self.y))

    def moveRandom(self, min, max):
        self.x -= self.speed
        if self.x <= self.bound:
            temp = self.bound-self.x
            self.x = self.mx-temp
            self.y = random.randint(min, max)

        return self.screen.blit(self.image, (self.x, self.y))
