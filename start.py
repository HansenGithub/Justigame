import pygame
import sys
import player
import renderer
import sheep
import random
import blacksheep
import hendlbomber
import brathendl
#init pygame
pygame.init()
pygame.display.set_caption("Justigame")
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.font.init()
pygame.mixer.set_num_channels(20)

_player = player.Player("player1")
_renderer = renderer.Renderer() 
clock = pygame.time.Clock()
#_sheep = sheep.Sheep("sheep1",50,0) 
totalFrames = 0
entityList =[]
pygame.mixer.music.load('sound/forest.mp3')
pygame.mixer.music.play(-1)
        
#Main Loop
game_running = True
ClassesToRender =[_player,sheep.Sheep,blacksheep.BlackSheep,hendlbomber.Hendlbomber,brathendl.Brathendl]
while game_running:  
    if _player.state == "alive":  
        totalFrames +=1 
        if totalFrames % 300 == 0:
            entityList.append(sheep.Sheep("test",random.randint(10,300),0))
        if totalFrames % 500 == 0:
            entityList.append(blacksheep.BlackSheep("test",random.randint(10,300),0)) 
        if totalFrames % 2000 == 0:
            entityList.append(hendlbomber.Hendlbomber("test",random.randint(10,300),0)) 
                
        _player.Tick()  
        _renderer.tick(ClassesToRender) 
        for r in sheep.Sheep.get_instances():
            if r.state == "delete":
                player.Player.score += 1
                entityList.remove(r)
                del r
            else:    
                r.Tick()
        for r in blacksheep.BlackSheep.get_instances():
            if r.state == "delete":
                
                entityList.remove(r)
                del r
            elif r.state == "hitPlayer":
                r.state = "delete"
                if _player.life >= 1:
                    _player.life -= 1
                else:
                    _player.state == "dead"        
            else:    
                r.Tick()
        for r in hendlbomber.Hendlbomber.get_instances():
            if r.command == "bomb" and r.state !="delete":
                entityList.append(brathendl.Brathendl("test",r.X,0))
            if r.state == "delete":
                entityList.remove(r)
                del r
            else:    
                r.Tick()  
        for r in brathendl.Brathendl.get_instances():
            if r.state == "delete":
                entityList.remove(r)
                del r
            elif r.state == "hitPlayer":
                r.state = "delete"
                if _player.life >= 1:
                    _player.life -= 1
                else:
                    _player.state == "dead"    
            else:    
                r.Tick()              
    if _player.state == "dead":
         font = pygame.font.SysFont('Comic Sans MS', 42)
         textGameOver = renderer.Renderer.font.render("Game Over", True, (255,0,0))
         renderer.Renderer.screen.blit(textGameOver,(0,400))
         _renderer.tick(ClassesToRender)   
    #drawScreen()
    clock.tick(60)