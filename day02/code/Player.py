class Bird:
    def __init__(self, screen, img, pos):
        self.screen = screen
        self.img = img
        self.x, self.y = pos
        self.speed = 0
        self.g = 9.8*100
        self.fps = 60
        pass

    def fall(self):
        self.speed += self.g*1/self.fps
        self.y += self.speed*1/self.fps
        b = self.screen.blit(self.img, (self.x, self.y))
        return b

    def jump(self, force):
        self.speed = -force*1/self.fps
        pass
