import pygame, random, os
BASE = os.path.dirname(os.path.abspath(__file__))

def asset(*parts):
    return os.path.join(BASE, *parts)
def rect(x,y,VH):
    if VH == 'H':
        pygame.Rect(x,y,2000,10)
    else:
        pygame.Rect(x,y,10,2000)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(asset("Boss.mp3"))  
def setvar():
    one_time = True
    start2 = False
    beatlvl1 = False
    beatlvl2 = False
    beatlvl3 = False
    screen = pygame.display.set_mode((1920,1020))
    clock = pygame.time.Clock()
    lasers = []
    running = True
    dt = 0
    homescreen = True
    damage = 3
    active = False
    counter = 0
    bosshealth = 10000
    bossalive = True
    HIT_W, HIT_H = 5, 5
    color = (60, 60, 60)
    bossx = 955
    bossy = 300
    playsong = True
    R = 255
    G = 255
    B = 255
    x = 1
    xC = random.randint(-1000, 1700)
    yC = random.randint(-1000, 800)
    XC = random.randint(-1000, 1700)
    YC = random.randint(-1000, 800)
    counter3 = 0
    counter2 = 0
    countervar = 300
    alive = True
    colorlaser = (R,G,B)
    enemy_pos = pygame.Vector2(bossx,bossy)
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    time = 0
    seconds = 0
    maxtime = 9999999
    num = 1
    hitboxenable = True
    notplayedfail = True
    start1 = True
one_time = True
start2 = False
beatlvl1 = False
beatlvl2 = False
beatlvl3 = False
screen = pygame.display.set_mode((1920,1020))
clock = pygame.time.Clock()
lasers = []
running = True
dt = 0
homescreen = True
damage = 3
active = False
counter = 0
bosshealth = 10000
bossalive = True
HIT_W, HIT_H = 5, 5
color = (60, 60, 60)
bossx = 955
bossy = 300
playsong = True
R = 255
G = 255
B = 255
x = 1
xC = random.randint(-1000, 1700)
yC = random.randint(-1000, 800)
XC = random.randint(-1000, 1700)
YC = random.randint(-1000, 800)
counter3 = 0
counter2 = 0
countervar = 300
alive = True
colorlaser = (R,G,B)
enemy_pos = pygame.Vector2(bossx,bossy)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
time = 0
seconds = 0
maxtime = 9999999
num = 1
hitboxenable = True
notplayedfail = True
start1 = True




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    mx, my = pygame.mouse.get_pos()                                                                         #mouse hitbox
    mouse_hitbox = pygame.Rect(mx - HIT_W // 2, my - HIT_H // 2, HIT_W, HIT_H)


    pygame.display.flip()

    dt = clock.tick(60) / 1000
    if homescreen:
        if beatlvl1:
            colorlvl1 = 'green'
        else:
            colorlvl1 = 'red'
        if beatlvl2:
            colorlvl2 = 'green'
        else:
            colorlvl2 = 'red'
        startscreen = pygame.Rect(-100,-100,4000,4000)
        pygame.draw.rect(screen, (200,200,200), startscreen)
        bg = pygame.Rect(555, 30, 800, 400)
        pygame.draw.rect(screen, (0,0,0), bg)
        font = pygame.font.SysFont('arial black', 150)
        text_surface = font.render("Laser", True, (255, 0, 0))
        screen.blit(text_surface, ((screen.get_width()/2) - 245, (screen.get_height()/2) - 500))
        text_surface = font.render("Mayhem", True, (255, 0, 0))
        screen.blit(text_surface, ((screen.get_width()/2) - 345, (screen.get_height()/2) - 325))
        bg2 = pygame.Rect(647, 454, 625, 60)
        pygame.draw.rect(screen, (160,160,160), bg2)
        bglvl1 = pygame.Rect(650,565,50,50)
        pygame.draw.rect(screen, (colorlvl1), bglvl1)
        font2 = pygame.font.SysFont('arial black', 40)
        text_surface2 = font2.render("Press 1 to begin level 1", True, (20, 20, 20))
        screen.blit(text_surface2, ((screen.get_width()/2) - 252, (screen.get_height()/2) + 50))
        font2 = pygame.font.SysFont('arial', 40)
        text_surface3 = font2.render("Hover mouse over enemy to deal damage", True, (20, 20, 20))
        screen.blit(text_surface3, ((screen.get_width()/2) - 300, (screen.get_height()/2) - 50))
        if beatlvl1:
            bglvl2 = pygame.Rect(650,665,50,50)
            pygame.draw.rect(screen, colorlvl2, bglvl2)
            
            fontlvl2 = pygame.font.SysFont('arial black', 40)
            text_surface4 = fontlvl2.render("Press 2 to begin level 2", True, (20, 20, 20))
            screen.blit(text_surface4, ((screen.get_width()/2) - 252, (screen.get_height()/2) + 150))
            
            
               
        
        start = pygame.key.get_pressed()                                             #movement keys
        if start[pygame.K_1]:
            counter += 1
        if counter > 2:                                                                    #how long gray screen shows
            homescreen = False                                            #movement keys
        if start[pygame.K_2]:
            start2 = True
            homescreen = False
        
    elif start1 and not start2:
        screen.fill("white")
        changex = random.randint(50,1800)
        changey = random.randint(50,900)

        time += num
        seconds = time / 60

        if playsong:
            pygame.mixer.music.play(loops=-1, fade_ms=1000)    
            pygame.mixer.music.set_volume(.0025)
            playsong = False
        if bossalive and bosshealth <= 9000: 
            counter2 += 2
            lasers = [pygame.Rect(0, yC + 200, 2000, 10), pygame.Rect(0, yC + 400, 2000, 10), pygame.Rect(0,yC + 600,2000,10),
                    pygame.Rect(0,yC + 800,2000,10),pygame.Rect(xC + 200, 0, 10, 2000),pygame.Rect(xC + 400,0,10,2000),pygame.Rect(xC + 600,0,10,2000),pygame.Rect(xC + 800,0,10,2000),
                    pygame.Rect(xC + 1000,0,10,2000),pygame.Rect(xC + 1200,0,10,2000),pygame.Rect(xC + 1400,0,10,2000),pygame.Rect(xC + 1600,0,10,2000),pygame.Rect(xC + 1800,0,10,2000),
                    pygame.Rect(0, yC - 200, 2000, 10), 
                    pygame.Rect(0, yC - 400, 2000, 10), pygame.Rect(0,yC - 600,2000,10),
                    pygame.Rect(0,yC - 800,2000,10),pygame.Rect(xC - 200, 0, 10, 2000),pygame.Rect(xC - 400,0,10,2000),pygame.Rect(xC - 600,0,10,2000),pygame.Rect(xC - 800,0,10,2000),
                    pygame.Rect(xC - 1000,0,10,2000),pygame.Rect(xC - 1200,0,10,2000),pygame.Rect(xC - 1400,0,10,2000),pygame.Rect(xC - 1600,0,10,2000),pygame.Rect(xC - 1800,0,10,2000),pygame.Rect(0, yC - 1000, 2000, 10), 
                    pygame.Rect(0, yC - 1200, 2000, 10), pygame.Rect(0,yC - 1400,2000,10),
                    pygame.Rect(0,yC - 1600,2000,10),pygame.Rect(xC - 2000, 0, 10, 2000),pygame.Rect(xC - 2200,0,10,2000),pygame.Rect(xC -2400,0,10,2000),pygame.Rect(xC - 2600,0,10,2000),
                    pygame.Rect(xC - 2800,0,10,2000),pygame.Rect(xC - 3000,0,10,2000),pygame.Rect(xC - 3200,0,10,2000),pygame.Rect(xC - 3400,0,10,2000),pygame.Rect(xC - 3600,0,10,2000),pygame.Rect(0, yC - 1800, 2000, 10), 
                    pygame.Rect(0, yC - 2000, 2000, 10), pygame.Rect(0,yC - 2200,2000,10),
                    pygame.Rect(0,yC - 2400,2000,10),pygame.Rect(xC - 3800, 0, 10, 2000),pygame.Rect(xC - 4000,0,10,2000),pygame.Rect(xC - 4200,0,10,2000),pygame.Rect(xC - 4400,0,10,2000),
                    pygame.Rect(xC - 4600,0,10,2000),pygame.Rect(xC - 4800,0,10,2000),pygame.Rect(xC - 5000,0,10,2000),pygame.Rect(xC - 5200,0,10,2000),pygame.Rect(xC - 5400,0,10,2000), pygame.Rect(0, YC + 200, 2000, 10), pygame.Rect(0, YC + 400, 2000, 10), pygame.Rect(0,YC + 600,2000,10),
                    pygame.Rect(0,YC + 800,2000,10),pygame.Rect(XC + 200, 0, 10, 2000),pygame.Rect(XC + 400,0,10,2000),pygame.Rect(XC + 600,0,10,2000),pygame.Rect(XC + 800,0,10,2000),
                    pygame.Rect(XC + 1000,0,10,2000),pygame.Rect(XC + 1200,0,10,2000),pygame.Rect(XC + 1400,0,10,2000),pygame.Rect(XC + 1600,0,10,2000),pygame.Rect(XC + 1800,0,10,2000),
                    pygame.Rect(0, YC - 200, 2000, 10), 
                    pygame.Rect(0, YC - 400, 2000, 10), pygame.Rect(0,YC - 600,2000,10),
                    pygame.Rect(0,YC - 800,2000,10),pygame.Rect(XC - 200, 0, 10, 2000),pygame.Rect(XC - 400,0,10,2000),pygame.Rect(XC - 600,0,10,2000),pygame.Rect(XC - 800,0,10,2000),
                    pygame.Rect(XC - 1000,0,10,2000),pygame.Rect(XC - 1200,0,10,2000),pygame.Rect(XC - 1400,0,10,2000),pygame.Rect(XC - 1600,0,10,2000),pygame.Rect(XC - 1800,0,10,2000),pygame.Rect(0, YC - 1000, 2000, 10), 
                    pygame.Rect(0, YC - 1200, 2000, 10), pygame.Rect(0,YC - 1400,2000,10),
                    pygame.Rect(0,YC - 1600,2000,10),pygame.Rect(XC - 2000, 0, 10, 2000),pygame.Rect(XC - 2200,0,10,2000),pygame.Rect(XC -2400,0,10,2000),pygame.Rect(XC - 2600,0,10,2000),
                    pygame.Rect(XC - 2800,0,10,2000),pygame.Rect(XC - 3000,0,10,2000),pygame.Rect(XC - 3200,0,10,2000),pygame.Rect(XC - 3400,0,10,2000),pygame.Rect(XC - 3600,0,10,2000),pygame.Rect(0, YC - 1800, 2000, 10), 
                    pygame.Rect(0, YC - 2000, 2000, 10), pygame.Rect(0,YC - 2200,2000,10),
                    pygame.Rect(0,YC - 2400,2000,10),pygame.Rect(XC - 3800, 0, 10, 2000),pygame.Rect(XC - 4000,0,10,2000),pygame.Rect(XC - 4200,0,10,2000),pygame.Rect(XC - 4400,0,10,2000),
                    pygame.Rect(XC - 4600,0,10,2000),pygame.Rect(XC - 4800,0,10,2000),pygame.Rect(XC - 5000,0,10,2000),pygame.Rect(XC - 5200,0,10,2000),pygame.Rect(XC - 5400,0,10,2000)
                    
                    
                    ]
            for laser in lasers:
                if bosshealth < 1000:
                    countervar = 135
                elif bosshealth < 2000:
                    countervar = 150
                elif bosshealth < 3000:
                    countervar = 175
                elif bosshealth < 4000:
                    countervar = 225
                elif bosshealth < 5000:
                    countervar = 250
                if counter2 < countervar:
                    pygame.draw.rect(screen, (255, 200,200), laser)
                    active = False
                elif counter2 >= countervar:
                    pygame.draw.rect(screen, (255, 0,0), laser)
                    counter3 += 1
                    active = True
                    if counter3 > 1000:
                        counter2 = 0
                        counter3 = 0
                        yC += random.randint(50,150)
                        xC += random.randint(50,150)




        speedboss = 75                                                           #boss speed and tracking
        to_player = pygame.Vector2(player_pos) - enemy_pos
        dist = to_player.length()
        if dist > 0:
            step = speedboss * dt
        if step >= dist:
            enemy_pos = pygame.Vector2(player_pos)
        else:
            enemy_pos += to_player.normalize() * step
        if bossalive:
            boss = pygame.Rect(enemy_pos.x - 15, enemy_pos.y - 15, 30, 30)                    #boss position and hitbox
            bossprinted = pygame.draw.rect(screen, (color), boss)
            boss = (int(enemy_pos.x), int(enemy_pos.y))
            bosshitbox = pygame.Rect(enemy_pos.x - 15 , enemy_pos.y - 15, 30,30)
        
            
        if bosshealth > 9333:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[///////////////]", True, (0, 255, 0))
            screen.blit(text_surface, (enemy_pos.x - 78,enemy_pos.y + 50))
        elif bosshealth > 8667:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[//////////////-]", True, (55, 200, 0))
            screen.blit(text_surface, (enemy_pos.x - 79,enemy_pos.y + 50))
        elif bosshealth > 8001:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[/////////////--]", True, (75, 180, 0))
            screen.blit(text_surface, (enemy_pos.x - 80,enemy_pos.y + 51))
        elif bosshealth > 7335:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[////////////---]", True, (95, 160, 0))
            screen.blit(text_surface, (enemy_pos.x - 81,enemy_pos.y + 51))
        elif bosshealth > 6669:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[///////////----]", True, (115, 140, 0))
            screen.blit(text_surface, (enemy_pos.x - 82,enemy_pos.y + 52))
        elif bosshealth > 6003:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[//////////-----]", True, (135, 120, 0))
            screen.blit(text_surface, (enemy_pos.x - 83,enemy_pos.y + 52))
        elif bosshealth > 5337:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[/////////------]", True, (155, 100, 0))
            screen.blit(text_surface, (enemy_pos.x - 84,enemy_pos.y + 53))
        elif bosshealth > 4671:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[////////-------]", True, (175, 80, 0))
            screen.blit(text_surface, (enemy_pos.x - 85,enemy_pos.y + 53))
        elif bosshealth > 4005:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[///////--------]", True, (195, 60, 0))
            screen.blit(text_surface, (enemy_pos.x - 86,enemy_pos.y + 54))
        elif bosshealth > 3339:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[//////---------]", True, (215, 40, 0))
            screen.blit(text_surface, (enemy_pos.x - 87,enemy_pos.y + 54))
        elif bosshealth > 2673:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[/////----------]", True, (235, 20, 0))
            screen.blit(text_surface, (enemy_pos.x - 88,enemy_pos.y + 55))
        elif bosshealth > 2007:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[////-----------]", True, (255, 0, 0))
            screen.blit(text_surface, (enemy_pos.x - 89,enemy_pos.y + 55))
        elif bosshealth > 1341:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[///------------]", True, (200, 0, 0))
            screen.blit(text_surface, (enemy_pos.x - 90,enemy_pos.y + 56))
        elif bosshealth > 675:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[//-------------]", True, (150, 0, 0))
            screen.blit(text_surface, (enemy_pos.x - 91,enemy_pos.y + 56))
        elif bosshealth > 9:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("[/--------------]", True, (100, 0, 0))
            screen.blit(text_surface, (enemy_pos.x - 92,enemy_pos.y + 57))
        elif bosshealth <= 0:
            num = 0
            font = pygame.font.Font(None, 150)
            text_surface = font.render("The boss has been defeated", True, (0, 0, 0))
            screen.blit(text_surface, (screen.get_width() / 2 - 720, screen.get_height() /2 - 300))
            font = pygame.font.SysFont('arial', 40)
            seconds2 = seconds
            if seconds2 < maxtime:
                maxtime = seconds2
            text_surface = font.render(f"Your time was {seconds2:.2f}s; Your best time was {maxtime:.2f}s", True, (20, 20, 20))
            screen.blit(text_surface, (screen.get_width() / 2 - 340, screen.get_height() /2 + 300))
            text_surface = font.render(f"Press R to continue", True, (20, 20, 20))
            screen.blit(text_surface, (screen.get_width() / 2 - 140, screen.get_height() /2 + 400))
            active = False
            bossalive = False
            hitboxenable = False
            wait = True
            if wait:
                tocontinue = pygame.key.get_pressed()
                if tocontinue[pygame.K_r]:
                    homescreen = True
                    beatlvl1 = True
            


            restart = pygame.key.get_pressed()
            if restart[pygame.K_r]:
                bossalive = False
                homescreen = True
                lasers = []
                running = True
                dt = 0
                homescreen = True
                active = False
                counter = 0
                bosshealth = 10000
                bossalive = True
                HIT_W, HIT_H = 32, 32
                color = (60, 60, 60)
                bossx = 955
                bossy = 300
                playsong = True
                R = 255
                G = 255
                B = 255
                x = 1
                xC = random.randint(-1000, 1700)
                yC = random.randint(-1000, 800)
                counter3 = 0
                counter2 = 0
                alive = True
                colorlaser = (R,G,B)
                countervar = 300
                enemy_pos = pygame.Vector2(bossx,bossy)
                player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                num = 1
                time = 0
                seconds = 0
                hitboxenable = True
                notplayedfail = True
                pygame.mixer.music.stop()


        if mouse_hitbox.colliderect(bosshitbox):
            bosshealth -= damage


            color = (150,40,40)
        else:
            color = (60,60,60)

        hitbox = pygame.Rect(player_pos.x - 40, player_pos.y -40,80,80)   
                  #players hitbox
        if hitboxenable:
            if hitbox.colliderect(bosshitbox):
                alive = False

        TB = pygame.Rect(0,0,2000,5)                                                #map borders
        TBP = pygame.draw.rect(screen,'black',TB)
        LB = pygame.Rect(0,0,5,2000)
        LBP = pygame.draw.rect(screen, 'black', LB)
        RB = pygame.Rect(1915,0,5,2000)
        RBP = pygame.draw.rect(screen, 'black', RB)
        BB = pygame.Rect(0,997,2000,5)
        BBP = pygame.draw.rect(screen,'black',BB)
        if hitbox.colliderect(RB):
            player_pos = pygame.Vector2(player_pos.x - 10, player_pos.y)
        elif hitbox.colliderect(LB):
            player_pos = pygame.Vector2(player_pos.x + 10, player_pos.y)
        elif hitbox.colliderect(BB):
            player_pos = pygame.Vector2(player_pos.x, player_pos.y - 10)
        elif hitbox.colliderect(TB):
            player_pos = pygame.Vector2(player_pos.x, player_pos.y + 10) 


        for laser in lasers:
            if hitboxenable:
                if hitbox.colliderect(laser):
                    if active:
                        alive = False
                else:
                    pass
        if alive == False:
            
            deadscreen = pygame.Rect(0, 0, 10000, 10000)
            deadscreen = (pygame.draw.rect(screen, ("black"), deadscreen))
            font = pygame.font.Font(None, 200)
            text_surface = font.render("GAME OVER", True, (255, 20, 20))
            screen.blit(text_surface, ((screen.get_width()/2) - 420, (screen.get_height()/2) - 70))
            restart = pygame.key.get_pressed()
            if restart[pygame.K_r]:
                homescreen = True
                lasers = []
                running = True
                dt = 0
                homescreen = True
                active = False
                counter = 0
                bosshealth = 10000
                bossalive = True
                HIT_W, HIT_H = 32, 32
                color = (60, 60, 60)
                bossx = 955
                bossy = 300
                playsong = True
                R = 255
                G = 255
                B = 255
                x = 1
                xC = random.randint(-1000, 1700)
                yC = random.randint(-1000, 800)
                counter3 = 0
                counter2 = 0
                alive = True
                colorlaser = (R,G,B)
                countervar = 300
                enemy_pos = pygame.Vector2(bossx,bossy)
                player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
                time = 0
                seconds = 0
                hitboxenable = True
                notplayedfail = True
                num = 1
            else:
                pass
            pygame.mixer.music.stop()
            if notplayedfail and not alive:
                fail_snd = pygame.mixer.Sound(asset('fail.mp3'))
                fail_snd.set_volume(0.1)
                fail_snd.play()
                notplayedfail = False









        if alive:
            pygame.draw.circle(screen, "blue", player_pos, 40)                           #character display
        
        keys = pygame.key.get_pressed()                                             #movement keys
        if keys[pygame.K_w]:
            player_pos.y -= 250 * dt
        if keys[pygame.K_s]:
            player_pos.y += 250 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 250 * dt
        if keys[pygame.K_d]:
            player_pos.x += 250 * dt



            """


            

            second game

            


            """






    elif start2:
        screen.fill("white")
        hitbox = pygame.Rect(player_pos.x - 40, player_pos.y -40,80,80)  
        TB = pygame.Rect(0,0,2000,5)                                                #map borders
        TBP = pygame.draw.rect(screen,'black',TB)
        LB = pygame.Rect(0,0,5,2000)
        LBP = pygame.draw.rect(screen, 'black', LB)
        RB = pygame.Rect(1915,0,5,2000)
        RBP = pygame.draw.rect(screen, 'black', RB)
        BB = pygame.Rect(0,997,2000,5)
        BBP = pygame.draw.rect(screen,'black',BB)
        if hitbox.colliderect(RB):
            player_pos = pygame.Vector2(player_pos.x - 10, player_pos.y)
        elif hitbox.colliderect(LB):
            player_pos = pygame.Vector2(player_pos.x + 10, player_pos.y)
        elif hitbox.colliderect(BB):
            player_pos = pygame.Vector2(player_pos.x, player_pos.y - 10)
        elif hitbox.colliderect(TB):
            player_pos = pygame.Vector2(player_pos.x, player_pos.y + 10) 
        if alive:
            pygame.draw.circle(screen, "blue", player_pos, 40)

        keys = pygame.key.get_pressed()                                             #movement keys
        if keys[pygame.K_w]:
            player_pos.y -= 250 * dt
        if keys[pygame.K_s]:
            player_pos.y += 250 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 250 * dt
        if keys[pygame.K_d]:
            player_pos.x += 250 * dt

        if one_time:
            setvar()
            player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2 + 400)
            counter2 = 0
            one_time = False
            changeinx = -1000
            changeiny = 200
            keepgoing = False
        mbs = [pygame.Rect(changeinx,changeiny,1000,5)




        ]
        for mb in mbs:
            pygame.draw.rect(screen, 'red', mb)
        if keepgoing == False and changeinx < 100:
            changeinx += 10
            changeiny += 5
            if changeinx == 0:
                keepgoing = True
        if changeinx > 2000 or keepgoing:
            
            changeinx -=10
            if changeinx < 100:
                pass
        #working on moving it back and forth
        













































pygame.quit()