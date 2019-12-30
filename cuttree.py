import pygame
treeimg = pygame.image.load("Tree.png")
blankimg = pygame.image.load('blank.png')
class tree:
    img = treeimg
    def __init__(self,x,y,touchx,touchy):
        self.x = x
        self.y = y
        self.touchx = touchx
        self.touchy = touchy
    def show(self,display):
        display.blit(self.img,(self.x,self.y))
    def istouch(self):
        if self.touchx == self.x and self.touchy == self.y:
            return True
