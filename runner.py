import sys, pygame
from datetime import timedelta
pygame.init()

size = width, height = 840, 340
speed = [0, 0]
black = 255, 255, 255

screen = pygame.display.set_mode(size)

player = pygame.image.load("sprites/dinopixel.png")
background = pygame.image.load("sprites/background.png")
player = pygame.transform.scale(player, (100, 100))
playerrect = player.get_rect()
playerrect.y = 180
playerrect.x = 25
currentleg = "LEFT"
myfont = pygame.font.SysFont("monospace", 25)

clock = pygame.time.Clock()
minutes = 0
seconds = 0
milliseconds = 0
gamestart = 0
restart = 0
ranking = []

while 1:
    timelabel = myfont.render("{}:{}.{}".format(minutes, seconds, milliseconds), 1, (0,0,0))
    bestlabel = myfont.render("The Fastest", 1, (0,0,0))

    if speed[0] >= 0:
        speed[0] -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if currentleg == "RIGHT" and restart == 0 and gamestart == 0:
                    currentleg = "LEFT"
                    speed[0] += 0.5
                    gamestart = 1
                    minutes = 0
                    seconds = 0
                    milliseconds = 0
                elif currentleg == "RIGHT" and restart == 0:
                    currentleg = "LEFT"
                    speed[0] += 0.5
            if event.key == pygame.K_RIGHT:
                if currentleg == "LEFT" and restart == 0 and gamestart == 0:
                    currentleg = "RIGHT"
                    speed[0] += 0.5
                    gamestart = 1
                    minutes = 0
                    seconds = 0
                    milliseconds = 0
                elif currentleg == "LEFT" and restart == 0:
                    currentleg = "RIGHT"
                    speed[0] += 0.5
            if event.key == pygame.K_SPACE:
                # if restart == 1:
                playerrect.y = 180
                playerrect.x = 25
                minutes = 0
                seconds = 0
                milliseconds = 0
                restart = 0
                gamestart = 0


    playerrect = playerrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    if playerrect.right >= 800:
        gamestart = 0
        restart = 1
        speed = [0, 0]
        this_time = (minutes, seconds, milliseconds)
        ranking.append(this_time)
        ranking = sorted(ranking, key=lambda x:(x[0], x[1], x[2]))

    if gamestart == 1:
        if milliseconds > 1000:
            seconds += 1
            milliseconds -= 1000
        if seconds > 60:
            minutes += 1
            seconds -= 60

        milliseconds += clock.tick_busy_loop(60)

    screen.fill(black)
    if ranking:
        rankinglabel = myfont.render("{}:{}.{}".format(ranking[0][0], ranking[0][1], ranking[0][2]), 1, (0,0,0))
        screen.blit(rankinglabel, (700, 50))
    screen.blit(bestlabel, (660, 20))
    screen.blit(background, (0,0))
    screen.blit(timelabel, (20, 20))
    screen.blit(player, playerrect)
    pygame.display.flip()