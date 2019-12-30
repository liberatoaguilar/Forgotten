import pygame
avatar = pygame.image.load('avatar.png')
avatarup = pygame.image.load('avatarup.png')
avatardown = pygame.image.load('avatardown.png')
avatarleft = pygame.image.load('avatarleft.png')
avatarright = pygame.image.load('avatarright.png')
unit = 50
class enemy:
    def __init__(self,x,y,touchx,touchy,img):
        self.x = x
        self.y = y
        self.touchx = touchx
        self.touchy = touchy
        self.img = img
    def show(self,display):
        display.blit(self.img,(self.x,self.y))
    def istouch(self):
        #RIGHT
        if self.touchy == self.y and self.touchx == self.x-unit:
            return 1
        #LEFT
        if self.touchy == self.y and self.touchx == self.x+unit:
            return 2
        #DOWN
        if self.touchy == self.y-unit and self.touchx == self.x:
            return 4
        #UP
        if self.touchy == self.y+unit and self.touchx == self.x:
            return 3
