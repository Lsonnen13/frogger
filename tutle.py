import pygame
class Tutle:
    def __init__(slef, x, y, sink = False):
        slef.size = [90, 70]
        slef.sprite = pygame.image.load("assets/tutle.png")
        slef.sprite = pygame.transform.scale(slef.sprite, slef.size)
        slef.sinkingsprite = pygame.image.load("assets/sinkingtutle.png")
        slef.sinkingsprite = pygame.transform.scale(slef.sinkingsprite, slef.size)
        slef.position = [x, y]        
        slef.speed = 3.5
        slef.sink = sink
        slef.state = "normal"
        
        

    def get_hitbox(slef):
        return pygame.Rect(slef.position, slef.size)
    
    def draw(slef, window):
        window.blit(slef.sprite, slef.position)
    
    def move(slef):
        slef.position[0] -= slef.speed 