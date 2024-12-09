import pygame
pygame.init()
import sys
screen = pygame.display.set_mode((860,780))
pygame.display.set_caption("screen")
x = 0
bg = pygame.image.load("flabybird/images/f6.png")
ground = pygame.image.load("flabybird/images/f1.png")
birds = ["f3","f5","f7"]
fps = pygame.time.Clock()
class bird(pygame.sprite.Sprite):
     def __init__(self,x,y):
          pygame.sprite.Sprite.__init__(self)
      #    self.images = []
        #  for bir in birds:
        #       img = pygame.image.load("flabybird/images/"+ bir +".png")
        #       self.images.append(img)
          self.image = pygame.image.load("flabybird/images/f3.png")
          self.rect = self.image.get_rect()
          self.rect.center = x,y
while True:
     fps.tick(60)
     screen.blit(bg,(0,0))
     screen.blit(ground,(x,615))
     x = x - 4
     if x < -30:
          x = 0
  

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update()