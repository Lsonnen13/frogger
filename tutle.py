import pygame
class Tutle:
    def __init__(slef, x, y):
        slef.sprite = pygame.image.load("assets/tutle.png")
        slef.size = [90, 70]
        slef.sprite = pygame.transform.scale(slef.sprite, slef.size)
        slef.position = [x, y]        
        slef.speed = 3.5
        
        

    def get_hitbox(slef):
        return pygame.Rect(slef.position, slef.position)
    
    def draw(slef, window):
        window.blit(slef.sprite, slef.position)
    
    def move(slef):
        slef.position[0] -= slef.speed 