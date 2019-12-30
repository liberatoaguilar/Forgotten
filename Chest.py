import pygame
chestimg = pygame.image.load('chest.png')
blankimg = pygame.image.load('blank.png')
unit = 50
class chest:
    img = chestimg
    def __init__(self,x,y,touchx,touchy):
        self.x = x
        self.y = y
        self.touchx = touchx
        self.touchy = touchy
    def show(self,display):
        display.blit(self.img,(self.x,self.y))
    def istouch(self):
        if self.touchx == self.x and self.touchy == self.y+unit:
            return True
