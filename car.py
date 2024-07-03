import pygame
class Car:
    def __init__(slef, x, y, direction) -> None:
        slef.direction = direction
        if direction == "right":
            slef.sprite = pygame.image.load("assets/car_right.png")
        elif direction == "left":
            slef.sprite = pygame.image.load("assets/car_left.png")
        slef.size = [150, 66]
        slef.sprite = pygame.transform.scale(slef.sprite, slef.size)
        slef.position = [x, y]        
        slef.speed = 5
        

    def get_hitbox(slef):
        return pygame.Rect(slef.position, slef.position)
    
    def draw(slef, window):
        window.blit(slef.sprite, slef.position)
    
    def move(slef):
        slef.position[0] += slef.speed