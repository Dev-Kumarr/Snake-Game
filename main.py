import pygame
import sys
import random

pygame.init()

up = (0, -10)
down = (0, 10)
left = (-10, 0)
right = (10, 0)

state = 0
directoin = 0
score = 0
xpos = 300
ypos = 300
pause = 0
easy = -1
scoreTime = 0

screen = pygame.display.set_mode((640, 640))

clock = pygame.time.Clock()

#snake
snake = []
rect = pygame.Rect(30, 30, 10, 10)
rect1 = pygame.Rect(20, 30, 10, 10)    
snake.append(rect)

while True:
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Times new Roman", 70)
    text = font.render("1. EASY MODE", True, (158, 16, 16))
    text1 = font.render("2. HARD MODE", True, (158, 16, 16))
    screen.blit(text, (100, 220))
    screen.blit(text1, (100, 370))


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_1:
                easy = 1
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                easy = 0

    pygame.display.flip()

    if easy == 0 or easy == 1:
        break
            

def snakeEatsFood(self, other):
    if (self.topleft[0] <= other.topleft[0]+5 and self.topleft[0] >= other.topleft[0]-5) and (self.topleft[1] <= other.topleft[1]+5 and self.topleft[1] >= other.topleft[1]-5):
        return True
    return False

def turn(d, self):
    if d == 1:
        x = self[0].topleft[0]
        y = self[0].topleft[1]-10

    if d == 2:
        x = self[0].topleft[0]
        y = self[0].topleft[1]+10

    if d == 3:
        x = self[0].topleft[0]-10
        y = self[0].topleft[1]

    if d == 4:
        x = self[0].topleft[0]+10
        y = self[0].topleft[1]
    
    body = pygame.Rect(x, y, 10, 10)
    self.insert(0, body)
    self.pop(len(self)-1)

while True:

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = (pause+1)%2


    clock.tick(20)

    #food
    food =  pygame.Rect(xpos, ypos, 10, 10)

    if snakeEatsFood(snake[0], food):
        score = score + 1
        while True:
            xpos = random.choice(range(0, 600))
            ypos = random.choice(range(0, 600))
            if xpos % 10 == 0 and ypos % 10 == 0:
                break

        if state == 1:
            x = snake[len(snake)-1].topleft[0]
            y = snake[len(snake)-1].topleft[1]+10

        if state == 2:
            x = snake[len(snake)-1].topleft[0]
            y = snake[len(snake)-1].topleft[1]-10

        if state == 3:
            x = snake[len(snake)-1].topleft[0]+10
            y = snake[len(snake)-1].topleft[1]

        if state == 4:
            x = snake[len(snake)-1].topleft[0]-10
            y = snake[len(snake)-1].topleft[1]

        body = pygame.Rect(x, y, 10, 10)
        snake.append(body)

    if len(snake) > 2:
        for i in range(1, len(snake)):
            #if snake bites itself
            if pygame.Rect.contains(snake[0], snake[i]):
                scoreTime = 1

    if easy == 0:
        screencolour = (0, 0, 255)
        if snake[0].topleft[0] == 0 or snake[0].topleft[0] > 640 or snake[0].topleft[1] < 0 or snake[0].topleft[1] > 640:
            scoreTime = 1
    
    if easy == 1:
        if snake[0].topleft[0] < 0: snake[0].topleft = (630, snake[0].topleft[1])
        if snake[0].topleft[1] < 0: snake[0].topleft = (snake[0].topleft[0], 630)
        if snake[0].topleft[0] > 630: snake[0].topleft = (0, snake[0].topleft[1])
        if snake[0].topleft[1] > 630: snake[0].topleft = (snake[0].topleft[0], 0)
        screencolour = (150, 150, 150) 
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.key == pygame.K_UP and state != 2:
                state = 1
                direction = 1
            if event.key == pygame.K_DOWN and state != 1:
                state = 2
                direction = 2
            if event.key == pygame.K_LEFT and state != 4:
                state = 3
                direction = 3
            if event.key == pygame.K_RIGHT and state != 3:
                state = 4
                direction = 4
            if event.key == pygame.K_SPACE:
                pause = (pause+1)%2


    if state == 1:
        #moveUp
        if len(snake) > 1: turn(direction, snake)
        else:
            snake[0].move_ip(up)
    if state == 2:
        #moveDown
        if len(snake) > 1: turn(direction, snake)
        else:
            snake[0].move_ip(down)
    if state ==3:
        #moveLeft
        if len(snake) > 1: turn(direction, snake)
        else:
            snake[0].move_ip(left)
    if state == 4:
        #moveRight
        if len(snake) > 1: turn(direction, snake)
        else:
            snake[0].move_ip(right)

    while scoreTime:
        screen.fill(screencolour)
        font = pygame.font.SysFont("Times new Roman", 70)
        text0 = font.render("SCORE : ", True, (158, 16, 16)) 
        text = font.render(str(score), True, (158, 16, 16))
        screen.blit(text0, (100, 270))
        screen.blit(text, (380, 270))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        pygame.display.flip()
        

    screen.fill(screencolour)

    pygame.draw.rect(screen, (200, 0, 0), food)
    for i in range(0, len(snake)):
        if i%2 == 0:
            colour = (255, 255, 255)
        else:
            colour = (0, 0, 0)
        pygame.draw.rect(screen, colour, snake[i])
    
    pygame.display.flip()
    pygame.display.update()
