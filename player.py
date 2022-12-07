import pygame
import sys
from utilities import KeepRefs
import renderer
class Player(KeepRefs):
    _renderer = renderer.Renderer
    screen = _renderer.screen
    score = 0
    def __init__(self,name):
        print ("Konstruktor gestartet")
        super(Player, self).__init__()
        self.name = name
        self.life = 5
        self.state = "alive"
        #Player Private Vars
        self.X = 400
        self.Y = 520
        self.animation_Walk_Steps = 0 
        
        self.stepsRight =0
        self.stepsLeft = 0
        self.stepsJump = 0
        self.stepsIdle = 0
        res = self.LoadRessources()
        self.direction = [0,0,0,0]
#[links,rechts,stand,sprung]
#game constants
        self.speed = 6
        self.height_v = 70
        self.width_v = 100
        self.jumpvar = -16
        self.jmpspeed = 5
        self.walksoundcount = -16
    def __del__(self):
        print ("Destruktor gestartet")   
    def LoadRessources(self):
        print ("Load Player Ressources")
        self.sound_PlayerJump = pygame.mixer.Sound("sound/jump2.wav")  
        self.sound_PlayerJump.set_volume(0.1)  
        self.sound_PlayerWalk = pygame.mixer.Sound("sound/grasswalk.wav")
        self.Sprites_Player_Idle = [pygame.image.load("assets/animations/player/Idle (1).png"), 
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
        self.Sprites_Player_Idle_scaled = []
        for img in self.Sprites_Player_Idle:
            newimg = pygame.transform.scale(img, (120, 120))
            self.Sprites_Player_Idle_scaled.append(newimg)

        self.Sprites_Player_Jump = [pygame.image.load("assets/animations/player/Jump (1).png"), 
                       pygame.image.load("assets/animations/player/Jump (2).png"),
                       pygame.image.load("assets/animations/player/Jump (3).png"),
                       pygame.image.load("assets/animations/player/Jump (4).png"),
                       pygame.image.load("assets/animations/player/Jump (5).png"),
                       pygame.image.load("assets/animations/player/Jump (6).png"),
                       pygame.image.load("assets/animations/player/Jump (7).png"),
                       pygame.image.load("assets/animations/player/Jump (8).png"),
                       pygame.image.load("assets/animations/player/Jump (9).png"),
                       pygame.image.load("assets/animations/player/Jump (10).png")]
        self.Sprites_Player_Jump_scaled = []
        for img in self.Sprites_Player_Jump:
            newimg = pygame.transform.scale(img, (120, 120))
            self.Sprites_Player_Jump_scaled.append(newimg)
        self.Sprites_Player_Run = [pygame.image.load("assets/animations/player/Run (1).png"), 
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
        self.Sprites_Player_RunRight_scaled = []  
        self.Sprites_Player_RunLeft_scaled = []
        for img in self.Sprites_Player_Run:
            newimg = pygame.transform.scale(img, (120, 120))
            self.Sprites_Player_RunRight_scaled.append(newimg)
            newimg = pygame.transform.scale(img, (120, 120))
            newimg = pygame.transform.flip(newimg,True,False)
            self.Sprites_Player_RunLeft_scaled.append(newimg)
        print ("Load Player Ressources done")
    def Tick(self):
        global _renderer, keyPressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()    
        self.playerHitbox = pygame.Rect(self.X+5,self.Y+30,self.width_v-60,self.height_v)
        if self.direction==[1,0,0,0]:
           self.playerHitbox = pygame.Rect(self.X+50,self.Y+30,self.width_v-60,self.height_v)     
        keyPressed = pygame.key.get_pressed()
        if self.jumpvar == -16:
            self.direction=[0,0,1,0]
        if keyPressed[pygame.K_UP] and self.jumpvar == -16:
            self.jumpvar = 15
            self.direction=[0,0,0,1]
        if keyPressed[pygame.K_LEFT] and not self.playerHitbox.colliderect(Player._renderer.screenEndLeft):
        #if keyPressed[pygame.K_LEFT]:
            self.X-=self.speed
            self.direction=[1,0,0,0]
        if keyPressed[pygame.K_RIGHT]and not self.playerHitbox.colliderect(Player._renderer.screenEndRight):
        #if keyPressed[pygame.K_RIGHT]:
            self.X+=self.speed  
            self.direction=[0,1,0,0]
        if self.direction[0] or self.direction[1]:
            if self.walksoundcount == -16:         
                pygame.mixer.Sound.play(self.sound_PlayerWalk)
                self.walksoundcount = 320
            if self.walksoundcount > 0:
                        self.walksoundcount -= 1
            if self.walksoundcount == 0:
                self.walksoundcount =-16
                pygame.mixer.Sound.stop(self.sound_PlayerWalk)
       
        if self.jumpvar == 15:
            pygame.mixer.Sound.play(self.sound_PlayerJump)
        if self.jumpvar >= -15:
            n = 1
            if self.jumpvar < 0:
                n= -1
            self.Y -=(self.jumpvar**2)*0.17*n
            self.jumpvar -= 1
    #steht oder springt
        if self.direction[2] or self.direction[3]:
            self.stepsLeft =0
            self.stepsRight =0
            self.walksoundcount =-16
            pygame.mixer.Sound.stop(self.sound_PlayerWalk)
        if self.direction[2]:
            self.stepsIdle +=1   
        if self.direction[3]:
            self.stepsJump +=1   
        if self.direction[0]:
            self.stepsLeft +=1        
        if self.direction[1]:
            self.stepsRight +=1 
        #self.Draw()
    def Draw(self):
        #print ("Draw")
        #Animation vars
        if self.stepsIdle == 75:
            self.stepsIdle =0
        if self.stepsLeft == 75:
            self.stepsLeft =0
        if self.stepsRight == 75:
            self.stepsRight =0
        if self.stepsJump == 50:
            self.stepsJump =0  
        #Draw    
        if self.direction[2]:
            Player.screen.blit(self.Sprites_Player_Idle_scaled[self.stepsIdle//5],(self.X,self.Y))    
        if self.direction[3]:
            Player.screen.blit(self.Sprites_Player_Jump_scaled[self.stepsJump//5],(self.X,self.Y))
        if self.direction[0]:
            if self.animation_Walk_Steps == 14:
                self.animation_Walk_Steps = 0
            else:
                self.animation_Walk_Steps += 1    
            Player.screen.blit(self.Sprites_Player_RunLeft_scaled[self.animation_Walk_Steps],(self.X-15,self.Y))   
        if self.direction[1]:
            if self.animation_Walk_Steps == 14:
                self.animation_Walk_Steps = 0
            else:
                self.animation_Walk_Steps += 1 
            Player.screen.blit(self.Sprites_Player_RunRight_scaled[self.animation_Walk_Steps],(self.X,self.Y)) 
        #pygame.draw.rect(Player.screen,(255,255,0),pygame.Rect(self.X+50,self.Y+30,self.width_v-60,self.height_v))

