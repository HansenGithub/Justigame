import pygame
import sys

#import player
from utilities import KeepRefs
pygame.init()
pygame.font.init()
class Renderer:
    #_player = player.Player
    steps = 0
    font = pygame.font.SysFont('Comic Sans MS', 24)
     #screen ends
     #set Window
    screen = pygame.display.set_mode([1280,720])
    screenEndLeft = pygame.draw.rect(screen,(0,0,0),(1,0,20,720),0)
    screenEndRight = pygame.draw.rect(screen,(0,0,0),(1279,0,20,720),0)
    def __init__(self):
        
        self.background = pygame.image.load("assets/Full-Background.png")
        self.background = pygame.transform.scale(self.background, (1280, 720)) 
        self.ui_heartfull = pygame.image.load("assets/ui/health_full.png")
        self.ui_heartfull= pygame.transform.scale(self.ui_heartfull, (50, 50))
        self.ui_heartempty = pygame.image.load("assets/ui/health_empty.png")
        self.ui_heartempty= pygame.transform.scale(self.ui_heartempty, (50, 50))  
    def tick(self,ClassesToRender):
        _lifeshift = 0
        #background
        Renderer.screen.blit(self.background,(0,0))
        for object in ClassesToRender:
            for r in object.get_instances():
                r.Draw()
                if r.name == "player1":
                    textScore = Renderer.font.render(str(r.score), True, (255,0,0))
                    for i in range(0,r.life):
                        Renderer.screen.blit(self.ui_heartfull,((1180-50*i),10)) 
                        _lifeshift = (1180-50*i)-50
                    if r.life < 5:
                        for i in range(0,(5-r.life)):
                            Renderer.screen.blit(self.ui_heartempty,(_lifeshift-50*i,10))    
        #ui
        Renderer.screen.blit(textScore,(0,0)) 
         
        pygame.display.update()