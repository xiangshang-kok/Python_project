import pygame


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
        im = self.img
        if self.speed < 0:
            im = pygame.transform.rotate(self.img, 90)
        else:
            im = pygame.transform.rotate(self.img, -90)

        b = self.screen.blit(im, (self.x, self.y))
        return b

    def jump(self, force):
        self.speed = -force*self.g*1/self.fps
        pass
