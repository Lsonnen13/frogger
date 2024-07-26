import pygame
class Log:
    def __init__(slef, x, y, speed, width) -> None:
        slef.sprite = pygame.image.load("assets/big_twig.png")
        slef.size = [width, 70]
        slef.sprite = pygame.transform.scale(slef.sprite, slef.size)
        slef.position = [x, y]        
        slef.speed = speed
        
        

    def get_hitbox(slef):
        return pygame.Rect(slef.position, slef.position)
    
    def draw(slef, window):
        window.blit(slef.sprite, slef.position)
    
    def move(slef):
        slef.position[0] += slef.speed 