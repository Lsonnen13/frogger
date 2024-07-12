import pygame
class Car:
    def __init__(slef, x, y, direction, speed) -> None:
        slef.direction = direction
        if direction == "right":
            slef.sprite = pygame.image.load("assets/car_right.png")
        elif direction == "left":
            slef.sprite = pygame.image.load("assets/car_left.png")
        slef.size = [150, 60]
        slef.sprite = pygame.transform.scale(slef.sprite, slef.size)
        slef.position = [x, y]        
        slef.speed = speed
        

    def get_hitbox(slef):
        return pygame.Rect(slef.position, slef.position)
    
    def draw(slef, window):
        window.blit(slef.sprite, slef.position)
    
    def move(slef):
        if slef.direction == "right":
            slef.position[0] += slef.speed
        elif slef.direction == "left":
            slef.position[0] -= slef.speed        