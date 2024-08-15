import pygame
from frog import Frog
from car import Car
from log import Log
from tutle import Tutle

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
log1a = Log(1200, 371, 3, 200)
log1b = Log(800, 371, 3, 200)
log1c = Log(200, 371, 3, 200)
log2a = Log(999, 292, 4, 400)
log2b = Log(222, 292, 4, 400)
log3a = Log(222, 138, 3.5, 250)
log3b = Log(666, 138, 3.5, 250)
log3c = Log(1111, 138, 3.5, 250)
tutle1a1 = Tutle(800, 450)
tutle1a2 = Tutle(890, 450)
tutle1a3 = Tutle(980, 450)
tutle1b1 = Tutle(1200, 450)


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
        log1b.move()
        log1c.move()
        log2a.move()
        log2b.move()
        log3a.move()
        log3b.move()
        log3c.move()
        tutle1a1.move()
        tutle1a2.move()
        tutle1a3.move()
        tutle1b1.move()
        reset_car()
        reset_log()
        reset_tutle()
        draw()
        

#the order of stuff is turtle, log, log, turtle, log ok?
#the 2 layer has 3 small slow logs, the 3rd has 2 fast big logs, and the 5th has 3 mid/long logs
#first row two tutle, 4th row 3 tutle :D
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
    log1b.draw(window)
    log1c.draw(window)
    log2a.draw(window)
    log2b.draw(window)
    log3a.draw(window)
    log3b.draw(window)
    log3c.draw(window)
    tutle1a1.draw(window)
    tutle1a2.draw(window)
    tutle1a3.draw(window)
    tutle1b1.draw(window)
    tim.draw(window)
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

def reset_log():
    if log1a.position[0] >= 1513:
        log1a.position[0] = 207
    if log1b.position[0] >= 1513:
        log1b.position[0] = 207
    if log1c.position[0] >= 1513:
        log1c.position[0] = 207
    if log2a.position[0] >= 1513:
        log2a.position[0] = 7
    if log2b.position[0] >= 1513:
        log2b.position[0] = 7
    if log3a.position[0] >= 1513:
        log3a.position[0] = 157
    if log3b.position[0] >= 1513:   
        log3b.position[0] = 157
    if log3c.position[0] >= 1513:   
        log3c.position[0] = 157

def reset_tutle():
    if tutle1a1.position[0] <= 317:
        tutle1a1.position[0] = 1513
    if tutle1a2.position[0] <= 317:
        tutle1a2.position[0] = 1513
    if tutle1a3.position[0] <= 317:
        tutle1a3.position[0] = 1513
    


        
    


#------------- start :D --------------#
main_game_loop()