import pygame
import sys
from player import Player
#from renderer import renderer
#_renderer = renderer() 
_player = Player()
#_player = player()
#init pygame
pygame.init
pygame.display.set_caption("Justigame")
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()
font = pygame.font.SysFont(None, 24)

#ressources
background = pygame.image.load("assets/Full-Background.png")
background = pygame.transform.scale(background, (1280, 720))
Sprites_Player_Idle = [pygame.image.load("assets/animations/player/Idle (1).png"), 
                        pygame.image.load("assets/animations/player/Idle (2).png"),
                        pygame.image.load("assets/animations/player/Idle (3).png"),
                        pygame.image.load("assets/animations/player/Idle (4).png"),
                        pygame.image.load("assets/animations/player/Idle (5).png"),
                        pygame.image.load("assets/animations/player/Idle (6).png"),
                        pygame.image.load("assets/animations/player/Idle (7).png"),
                        pygame.image.load("assets/animations/player/Idle (8).png"),
                        pygame.image.load("assets/animations/player/Idle (9).png"),
                        pygame.image.load("assets/animations/player/Idle (10).png"),
                        pygame.image.load("assets/animations/player/Idle (11).png"),
                        pygame.image.load("assets/animations/player/Idle (12).png"),
                        pygame.image.load("assets/animations/player/Idle (13).png"),
                        pygame.image.load("assets/animations/player/Idle (14).png"),
                        pygame.image.load("assets/animations/player/Idle (15).png")]
Sprites_Player_Idle_scaled = []
for img in Sprites_Player_Idle:
    newimg = pygame.transform.scale(img, (120, 120))
    Sprites_Player_Idle_scaled.append(newimg)

Sprites_Player_Jump = [pygame.image.load("assets/animations/player/Jump (1).png"), 
                       pygame.image.load("assets/animations/player/Jump (2).png"),
                       pygame.image.load("assets/animations/player/Jump (3).png"),
                       pygame.image.load("assets/animations/player/Jump (4).png"),
                       pygame.image.load("assets/animations/player/Jump (5).png"),
                       pygame.image.load("assets/animations/player/Jump (6).png"),
                       pygame.image.load("assets/animations/player/Jump (7).png"),
                       pygame.image.load("assets/animations/player/Jump (8).png"),
                       pygame.image.load("assets/animations/player/Jump (9).png"),
                       pygame.image.load("assets/animations/player/Jump (10).png")]
Sprites_Player_Jump_scaled = []
for img in Sprites_Player_Jump:
    newimg = pygame.transform.scale(img, (120, 120))
    Sprites_Player_Jump_scaled.append(newimg)
Sprites_Player_Run = [pygame.image.load("assets/animations/player/Run (1).png"), 
                        pygame.image.load("assets/animations/player/Run (2).png"),
                        pygame.image.load("assets/animations/player/Run (3).png"),
                        pygame.image.load("assets/animations/player/Run (4).png"),
                        pygame.image.load("assets/animations/player/Run (5).png"),
                        pygame.image.load("assets/animations/player/Run (6).png"),
                        pygame.image.load("assets/animations/player/Run (7).png"),
                        pygame.image.load("assets/animations/player/Run (8).png"),
                        pygame.image.load("assets/animations/player/Run (9).png"),
                        pygame.image.load("assets/animations/player/Run (10).png"),
                        pygame.image.load("assets/animations/player/Run (11).png"),
                        pygame.image.load("assets/animations/player/Run (12).png"),
                        pygame.image.load("assets/animations/player/Run (13).png"),
                        pygame.image.load("assets/animations/player/Run (14).png"),
                        pygame.image.load("assets/animations/player/Run (15).png")]
Sprites_Player_RunRight_scaled = []  
Sprites_Player_RunLeft_scaled = []
for img in Sprites_Player_Run:
    newimg = pygame.transform.scale(img, (120, 120))
    Sprites_Player_RunRight_scaled.append(newimg)
    newimg = pygame.transform.scale(img, (120, 120))
    newimg = pygame.transform.flip(newimg,True,False)
    Sprites_Player_RunLeft_scaled.append(newimg)

animation_Walk_Steps = 0    
sound_PlayerJump = pygame.mixer.Sound("sound/jump2.wav")  
sound_PlayerJump.set_volume(0.1)  
sound_PlayerWalk = pygame.mixer.Sound("sound/grasswalk.wav") 
#set Window
screen = pygame.display.set_mode([1280,720])
clock = pygame.time.Clock()
#Player Private Vars
X = 400
Y = 520
totalFrames = 0
direction = [0,0,0,0]
stepsRight =0
stepsLeft = 0
stepsJump = 0
stepsIdle = 0
#[links,rechts,stand,sprung]
#game constants
speed = 6
height_v = 70
width_v = 100
jumpvar = -16
jmpspeed = 5
walksoundcount = -16
screenEndLeft = pygame.draw.rect(screen,(0,0,0),(1,0,20,720),0)
screenEndRight = pygame.draw.rect(screen,(0,0,0),(1279,0,20,720),0)
#Draw function
def drawScreen():
    global stepsRight,stepsLeft,stepsIdle,stepsJump,animation_Walk_Steps
    screen.blit(background,(0,0))
    if stepsIdle == 75:
        stepsIdle =0
    if stepsLeft == 75:
        stepsLeft =0
    if stepsRight == 75:
        stepsRight =0
    if stepsJump == 50:
        stepsJump =0  
    if direction[2]:
        screen.blit(Sprites_Player_Idle_scaled[stepsIdle//5],(X,Y))    
    if direction[3]:
        screen.blit(Sprites_Player_Jump_scaled[stepsJump//5],(X,Y))
    if direction[0]:
            if animation_Walk_Steps == 14:
                animation_Walk_Steps = 0
            else:
                animation_Walk_Steps += 1    
            screen.blit(Sprites_Player_RunLeft_scaled[animation_Walk_Steps],(X-15,Y))   
    if direction[1]:
            if animation_Walk_Steps == 14:
                animation_Walk_Steps = 0
            else:
                animation_Walk_Steps += 1 
            screen.blit(Sprites_Player_RunRight_scaled[animation_Walk_Steps],(X,Y))     
    screen.blit(texTotalframes, (20, 20))    
    #pygame.draw.rect(screen,(255,255,0),(X,Y,width_v,height_v))
    pygame.display.update()


        
#Main Loop
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    playerHitbox = pygame.Rect(X,Y,width_v,height_v)    
    keyPressed = pygame.key.get_pressed()
    if jumpvar == -16:
        direction=[0,0,1,0]
    if keyPressed[pygame.K_UP] and jumpvar == -16:
        jumpvar = 15
        direction=[0,0,0,1]
    if keyPressed[pygame.K_LEFT] and not playerHitbox.colliderect(screenEndLeft):
        X-=speed
        direction=[1,0,0,0]
    if keyPressed[pygame.K_RIGHT]and not playerHitbox.colliderect(screenEndRight):
        X+=speed  
        direction=[0,1,0,0]
    if direction[0] or direction[1]:
        if walksoundcount == -16:         
            pygame.mixer.Sound.play(sound_PlayerWalk)
            walksoundcount = 320
        if walksoundcount > 0:
            walksoundcount -= 1
        if walksoundcount == 0:
            walksoundcount =-16
            pygame.mixer.Sound.stop(sound_PlayerWalk)
       
    if jumpvar == 15:
        pygame.mixer.Sound.play(sound_PlayerJump)
    if jumpvar >= -15:
        n = 1
        if jumpvar < 0:
            n= -1
        Y -=(jumpvar**2)*0.17*n
        jumpvar -= 1
    #steht oder springt
    if direction[2] or direction[3]:
        stepsLeft =0
        stepsRight =0
        walksoundcount =-16
        pygame.mixer.Sound.stop(sound_PlayerWalk)
    if direction[2]:
        stepsIdle +=1   
    if direction[3]:
        stepsJump +=1   
    if direction[0]:
        stepsLeft +=1        
    if direction[1]:
        stepsRight +=1 
    totalFrames +=1   
     
    texTotalframes = font.render(str(totalFrames), True, (255,0,0))    
    drawScreen()
    clock.tick(60)