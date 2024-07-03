import pygame
class Frog:
    #define the contsructer for frog # aka what happens when we makea new intance of a class
    def __init__(slef):
        slef.position = [916, 1007]
        slef.size = [88, 66]
        slef.color = [0, 50, 0]
        slef.speed = [120, 79]
        slef.sprite = pygame.image.load("assets/frogforward.png")
        slef.sprite = pygame.transform.scale(slef.sprite, slef.size)

    def get_hitbox(slef):
        return pygame.Rect(slef.position, slef.size)
    
    def draw(slef, window):
        #pygame.draw.rect(window, slef.color, slef.get_hitbox())
        window.blit(slef.sprite, slef.position)

    def move(slef, key):
        if key == "w":
            slef.position[1] -= slef.speed[1]
        elif key == "s":
            slef.position[1] += slef.speed[1]
        elif key == "a":
            slef.position[0] -= slef.speed[0]
        elif key == "d":
            slef.position[0] += slef.speed[0]

        if slef.position[1] >= 1007:
            slef.position[1] = 1007
        if slef.position[1] <= 59:
            slef.position[1] = 59
        if slef.position[0] <= 436:
            slef.position[0] = 436
        if slef.position[0] >= 1396:
            slef.position[0] = 1396

        