import pygame 
class Fly:

    def __init__(slef, x, y, speed,resetx):
        slef.size = [70,60]
        slef.position = [x, y]
        slef.sprite = pygame.image.load("assets/fly.png")
        slef.sprite = pygame.transform.scale(slef.sprite, slef.size)
        slef.speed = speed
        slef.resetx = resetx

    def get_hitbox(slef):
        return pygame.Rect(slef.position, slef.size)
    
    def draw(slef, window):
        window.blit(slef.sprite, slef.position)
    
    def draw_icon(slef, window):
        window.blit(slef.sprite, (10, window.get_height() - 100))


    def move(slef):
        slef.position[0] += slef.speed