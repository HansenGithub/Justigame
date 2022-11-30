import pygame
import sys

class Player:
    def __init__(self):
        print ("Konstruktor gestartet")
    def __del__(self):
        print ("Destruktor gestartet")   
    def LoadRessources(self):
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
    def Tick(self):
        
        pass
    def Draw(self):
        pass
        

