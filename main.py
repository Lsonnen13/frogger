import pygame
from frog import Frog
from car import Car
from log import Log

# -------------- Varibles --------------------- #

window = pygame.display.set_mode(flags = pygame.FULLSCREEN)
running = True
background = pygame.image.load("assets/frogger.png")
background = pygame.transform.scale(background, (1106, 1080))
left_border = pygame.Rect(0,0, 407, window.get_height())
right_border = pygame.Rect(window.get_width() - 407, 0, 407, window.get_height())
tim = Frog()
car1a = Car(350, 930, "right", 5)
car1b = Car(1000, 930, "right", 5)
car2a = Car(933, 856, "left", 3)
car2b = Car(1362, 856, "left", 3)
car2c = Car(473, 856, "left", 3)
car3a = Car(670, 778, "right", 7)
car3b = Car(150, 778, "right", 7)
car4a = Car(900, 702, "left", 20)
car5a = Car(500, 618, "right", 6)
car5b = Car(1200, 618, "right", 5)
log1a = Log(1200, 371, 3)
clock = pygame.time.Clock()

# ----------- Functions -----------------------#

def main_game_loop():
    while running == True:
        clock.tick(60)
        event_handler()
        car1a.move()
        car1b.move()
        car2a.move()
        car2b.move()
        car2c.move()
        car3a.move()
        car3b.move()
        car4a.move()
        car5a.move()
        car5b.move()
        log1a.move()
        reset_car()
        draw()
        



def event_handler():
    event_list = pygame.event.get()
    for i in event_list:
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if i.key == pygame.K_UP or i.key == pygame.K_w:
                tim.move("w")
            if i.key == pygame.K_DOWN or i.key == pygame.K_s:
                tim.move("s")
            if i.key == pygame.K_LEFT or i.key == pygame.K_a:
                tim.move("a")
            if i.key == pygame.K_RIGHT or i.key == pygame.K_d:
                tim.move("d")
                                                                                        #(͠≖ ͜ʖ͠≖)


def draw():
    window.fill((0,0,0))
    window.blit(background, (407, 0))
    tim.draw(window)
    car1a.draw(window)
    car1b.draw(window)
    car2a.draw(window)
    car2b.draw(window)
    car2c.draw(window)
    car3a.draw(window)
    car3b.draw(window)
    car4a.draw(window)
    car5a.draw(window)
    car5b.draw(window)
    log1a.draw(window)
    pygame.draw.rect(window, (0,0,1), left_border)
    pygame.draw.rect(window, (0,0,1), right_border)
    pygame.display.update()

def reset_car():
    if car1a.position[0] >= 1513:
        car1a.position[0] = 257
    if car1b.position[0] >= 1513:
        car1b.position[0] = 257
    if car2a.position[0] <= 257:
        car2a.position[0] = 1513
    if car2b.position[0] <= 257:
        car2b.position[0] = 1513
    if car2c.position[0] <= 257:
        car2c.position[0] = 1513
    if car3a.position[0] >= 1513:
        car3a.position[0] = 257
    if car3b.position[0] >= 1513:
        car3b.position[0] = 257
    if car4a.position[0] <= 257:
        car4a.position[0] = 1513
    if car5a.position[0] >= 1513:
        car5a.position[0] = 257
    if car5b.position[0] >= 1513:
        car5b.position[0] = 257
    if log1a.position[0] >= 1513:
        log1a.position[0] = 257
    


#------------- start :D --------------#
main_game_loop()