import pygame
from frog import Frog
from car import Car
from log import Log
from tutle import Tutle
import random
from fly import Fly

# -------------- Varibles --------------------- #

window = pygame.display.set_mode(flags = pygame.FULLSCREEN)
running = True
background = pygame.image.load("assets/frogger.png")
background = pygame.transform.scale(background, (1106, 1080))
left_border = pygame.Rect(0,0, 407, window.get_height())
right_border = pygame.Rect(window.get_width() - 407, 0, 407, window.get_height())
water = pygame.Rect(450, 130, 1015, 400)
winzone_1 = pygame.Rect(427.5, 32.5, 140, 100)
winzone_2 = pygame.Rect(655, 32.5, 140, 100)
winzone_3 = pygame.Rect(892.5, 32.5, 140, 100)
winzone_4 = pygame.Rect(1130, 32.5, 140, 100)
winzone_5 = pygame.Rect(1367.5, 32.5, 140, 100)
death_zone = pygame.Rect(427.5, 32.5, 1080, 100)
sinkingtutevent = pygame.event.custom_type()
sunktutevent = pygame.event.custom_type()
normaltutevent = pygame.event.custom_type()
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
tutle1b2 = Tutle(1290, 450)
tutle1b3 = Tutle(1380, 450)
tutle1c1 = Tutle(350, 450, True)
tutle1c2 = Tutle(440, 450, True)
tutle1c3 = Tutle(530, 450, True)
tutle2a1 = Tutle(600, 215)
tutle2a2 = Tutle(690, 215)
tutle2a3 = Tutle(780, 215)
tutle2b1 = Tutle(1300, 215, True)
tutle2b2 = Tutle(1390, 215, True)
tutle2b3 = Tutle(1480, 215, True)
bob = pygame.image.load("assets/safe.png")
bob = pygame.transform.scale(bob, (140, 100))
current_fly = None
claimed_zone = [False, False, False, False, False]
heart = pygame.image.load("assets/sprite_life00.png")
heart = pygame.transform.scale(heart, (200, 200))
heart_animation = [
    pygame.image.load("assets/sprite_life00.png"),
    pygame.image.load("assets/sprite_life01.png"),
    pygame.image.load("assets/sprite_life02.png"),
    pygame.image.load("assets/sprite_life03.png"),
    pygame.image.load("assets/sprite_life04.png"),
    pygame.image.load("assets/sprite_life05.png"),
    pygame.image.load("assets/sprite_life06.png"),
    pygame.image.load("assets/sprite_life07.png"),
    pygame.image.load("assets/sprite_life08.png"),
    pygame.image.load("assets/sprite_life09.png"),
    pygame.image.load("assets/sprite_life10.png"),
    pygame.image.load("assets/sprite_life11.png"),
]
i = 0
for sprite in heart_animation:
    heart_animation[i] = pygame.transform.scale(sprite, (200, 200))
    i += 1
heart_frame = 0
heart_play = False

lose_screen = pygame.image.load("assets/youlost.jpg")
lose_frame = 0
win_screen = pygame.image.load("assets/youwiiiiiiiiiiiiiiiin!.png")

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
        tutle1b2.move()
        tutle1b3.move()
        tutle1c1.move()
        tutle1c2.move()
        tutle1c3.move()
        tutle2a1.move()
        tutle2a2.move()
        tutle2a3.move()
        tutle2b1.move()
        tutle2b2.move()
        tutle2b3.move()
        current_fly.move()

        reset_car()
        reset_log()
        reset_tutle()
        reset_current_fly()
        check_death()
        check_on_water()
        if tim.has_fly == False:
            check_fly()
        check_safe()
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
        if i.type == sinkingtutevent:
            sinkingtutles = [tutle1c1, tutle1c2, tutle1c3, tutle2b1, tutle2b2, tutle2b3]
            for tutle in sinkingtutles:
                tutle.state = "sinking"
                start_sunk_timer()

        if i.type == sunktutevent:
            sunktutles = [tutle1c1, tutle1c2, tutle1c3, tutle2b1, tutle2b2, tutle2b3]
            for tutle in sunktutles:
                tutle.state = "sunk"
                start_normal_timer()

        if i.type == normaltutevent:
            normaltutles = [tutle1c1, tutle1c2, tutle1c3, tutle2b1, tutle2b2, tutle2b3]
            for tutle in normaltutles:
                tutle.state = "normal"
                start_sinking_timer( )





def draw():
    global lose_frame
    window.fill((0,0,0))
    window.blit(background, (407, 0))
    #pygame.draw.rect(window, (0, 255, 0), water)
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
    tutle1b2.draw(window)
    tutle1b3.draw(window)
    tutle1c1.draw(window)
    tutle1c2.draw(window)
    tutle1c3.draw(window)
    tutle2a1.draw(window)
    tutle2a2.draw(window)
    tutle2a3.draw(window)
    tutle2b1.draw(window)
    tutle2b2.draw(window)
    tutle2b3.draw(window)
    if tim.has_fly == False:
        current_fly.draw(window)
    pygame.draw.rect(window, (0,0,1), left_border)
    pygame.draw.rect(window, (0,0,1), right_border)
    if tim.has_fly == True:
        current_fly.draw_icon(window)
    # pygame.draw.rect(window, (255, 0, 0), death_zone)
    # pygame.draw.rect(window, (0, 255, 0), winzone_1)
    # pygame.draw.rect(window, (0, 255, 0), winzone_2)
    # pygame.draw.rect(window, (0, 255, 0), winzone_3)
    # pygame.draw.rect(window, (0, 255, 0), winzone_4)
    # pygame.draw.rect(window, (0, 255, 0), winzone_5)
    if claimed_zone[0] == True:
        window.blit(bob, (winzone_1.x, winzone_1.y))
    if claimed_zone[1] == True:
        window.blit(bob, (winzone_2.x, winzone_2.y))
    if claimed_zone[2] == True:
        window.blit(bob, (winzone_3.x, winzone_3.y))
    if claimed_zone[3] == True:
        window.blit(bob, (winzone_4.x, winzone_4.y))
    if claimed_zone[4] == True:
        window.blit(bob, (winzone_5.x, winzone_5.y))
    if tim.lives >= 1:
        window.blit(heart, (1469, 850))
    if tim.lives >= 2:
        window.blit(heart, (1580, 850))
    if tim.lives == 3:
        window.blit(heart, (1691, 850))
    if heart_play == True:
        lose_life_animation()

    tim.draw(window)
    if tim.lives <= 0:
        window.blit(lose_screen, (407, 0))
        lose_frame += 1
        if lose_frame == 300:
            pygame.quit()
            quit()
    if False not in claimed_zone:
        window.blit(win_screen, (407, 0))
    pygame.display.update()

def lose_life_animation():
    global heart_frame, heart_play
    if tim.lives == 2:
        window.blit(heart_animation[heart_frame // 5], (1691, 850))
    if tim.lives == 1:
        window.blit(heart_animation[heart_frame // 5], (1580, 850))
    if tim.lives == 0:
        window.blit(heart_animation[heart_frame // 5], (1469, 850))
    heart_frame += 1
    if heart_frame == 60:
        heart_play = False
        heart_frame = 0

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
    if tutle1b1.position[0] <= 317:
        tutle1b1.position[0] = 1513   
    if tutle1b2.position[0] <= 317:
        tutle1b2.position[0] = 1513   
    if tutle1b3.position[0] <= 317:
        tutle1b3.position[0] = 1513   
    if tutle1c1.position[0] <= 317:
        tutle1c1.position[0] = 1513   
    if tutle1c2.position[0] <= 317:
        tutle1c2.position[0] = 1513   
    if tutle1c3.position[0] <= 317:
        tutle1c3.position[0] = 1513   
    if tutle2a1.position[0] <= 317:
        tutle2a1.position[0] = 1513   
    if tutle2a2.position[0] <= 317:
        tutle2a2.position[0] = 1513   
    if tutle2a3.position[0] <= 317:
        tutle2a3.position[0] = 1513   
    if tutle2b1.position[0] <= 317:
        tutle2b1.position[0] = 1513   
    if tutle2b2.position[0] <= 317:
        tutle2b2.position[0] = 1513   
    if tutle2b3.position[0] <= 317:
        tutle2b3.position[0] = 1513

def reset_current_fly():
    if current_fly.position[0] >= 1513:
        current_fly.position[0] = current_fly.resetx

def get_car_hitboxes():
    car_list = [car1a, car1b, car2a, car2b, car2c, car3a, car3b, car4a, car5a, car5b]
    hitboxes = []
    for car in car_list:
        hitbox = car.get_hitbox()
        hitboxes.append(hitbox)
    return hitboxes

def get_log_hitboxes():
    log_list = [log1a, log1b, log1c, log2a, log2b, log3a, log3b, log3c]
    hitboxes = []
    for log in log_list:
        hitbox = log.get_hitbox()
        hitboxes.append(hitbox)
    return hitboxes

def get_tutle_hitboxes():
    tutle_list = [tutle1a1,tutle1a2, tutle1a3, tutle1b1, tutle1b2, tutle1b3, tutle1c1, tutle1c2, tutle1c3, tutle2a1, tutle2a2, tutle2a3, tutle2b1, tutle2b2, tutle2b3]
    hitboxes = []
    for tutle in tutle_list:
        if tutle.state == "normal" or tutle.state == "sinking":
            hitbox = tutle.get_hitbox()
            hitboxes.append(hitbox)
    return hitboxes

def check_death():
    if tim.get_hitbox().collidelist(get_car_hitboxes()) != -1:
        lose_life()
        return True
    else: 
        return False
    
def check_safe():
    safe_list = [winzone_1, winzone_2, winzone_3, winzone_4, winzone_5]
    for zone in safe_list:
        if zone.contains(tim.get_hitbox()) and tim.has_fly == True:
            print("you arnet ded! :D")
            idx = safe_list.index(zone)
            claimed_zone[idx] = True
            tim.position = [916, 1007]
            tim.has_fly = False
            return True
    if death_zone.colliderect(tim.get_hitbox()):
        lose_life()
        return False


def check_on_log():
    log_list = [log1a, log1b, log1c, log2a, log2b, log3a, log3b, log3c]
    log_index = tim.get_hitbox().collidelist(get_log_hitboxes())
    if log_index != -1:
        log_speed = log_list[log_index].speed
        tim.position[0] += log_speed
        return True
    else:
        return False
    
def check_on_tutle():
    if tim.get_hitbox().collidelist(get_tutle_hitboxes()) != -1:
        tim.position[0] -= 3.5
        return True
    else:
        return False

def check_on_water():
    if tim.get_hitbox().colliderect(water) == True:
        if check_on_tutle() == False:
            if check_on_log() == False:
                lose_life()

def lose_life():
    global heart_play
    tim.position = [916, 1007]
    tim.has_fly = False
    tim.lives -= 1
    heart_play = True
    
def start_sinking_timer():
    pygame.time.set_timer(sinkingtutevent, 3000, 1,)
    
def start_sunk_timer():
    pygame.time.set_timer(sunktutevent, 1000, 1)

def start_normal_timer():
    pygame.time.set_timer(normaltutevent, 2000, 1)

def spawn_fly():
    global current_fly
    log_list = [log1a, log1b, log1c, log2a, log2b, log3a, log3b, log3c]
    thechosen_log = random.choice(log_list)
    current_fly = Fly(thechosen_log.position[0], thechosen_log.position[1], thechosen_log.speed, 407-thechosen_log.size[0])

def check_fly():
    if tim.get_hitbox().colliderect(current_fly.get_hitbox()):
        tim.has_fly = True
    


#------------- start :D --------------#
start_sinking_timer()
spawn_fly()
main_game_loop()
