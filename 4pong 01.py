import pygame #import pygame
import sys #imports system
import random #imports random
pygame.init()

#set variables
width = 1000
height = 1000
fps=60
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

#create screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('4 Player Pong')

#define variables
clock = pygame.time.Clock()
left_score = 5
right_score = 5
top_score = 5
bottom_score = 5
font = pygame.font.SysFont('Ariel', 60)

#random number gen
ran_x = random.randint(1, 10)
ran_y = random.randint(1, 10)

#the bats
bat_size_a = 75
bat_size_b = 15
bat_speed = 7
bat1 = pygame.Rect(50, 500 - (bat_size_a //2), bat_size_b, bat_size_a)
bat2 = pygame.Rect(935, 500 - (bat_size_a //2), bat_size_b, bat_size_a)
bat3 = pygame.Rect(500 - (bat_size_a //2), 50, bat_size_a, bat_size_b)
bat4 = pygame.Rect(500 - (bat_size_a //2), 935, bat_size_a, bat_size_b)
bat1.y
bat2.y
bat3.x
bat4.x
bat1.y = 500 - (bat_size_a //2)
bat2.y = 500 - (bat_size_a //2)
bat3.x = 500 - (bat_size_a //2)
bat4.x = 500 - (bat_size_a //2)

#ball speed
ball_speedx = 1 * ran_x
ball_speedy = 1 * ran_y

#ball draw
ballradius=8
ball = pygame.Rect(width // 2, height // 2, ballradius, ballradius)

#background
run = True
while run:
    screen.fill(black)
    #display scores
    left_score_text = font.render("Lives = " + str(left_score), True, red)
    right_score_text = font.render("Lives = " + str(right_score), True, blue)
    top_score_text = font.render("Lives = " + str(top_score), True, green)
    bottom_score_text = font.render("Lives = " + str(bottom_score), True, yellow)

    #scoring
    #left
    if ball.x == 0:
        left_score -= 1
        ball_speedx = 0
        ball_speedy = 0
        ball.x = 500
        ball.y = 500
    if left_score == 0:
        ball_speedx = -ball_speedx

    #right
    if ball.x == 1000:
        right_score -= 1
        ball_speedx = 0
        ball_speedy = 0
        ball.x = 500
        ball.y = 500
    if right_score == 0:
        ball_speedx = -ball_speedx
    
    #top
    if ball.y == 0:
        top_score -= 1
        ball_speedx = 0
        ball_speedy = 0
        ball.x = 500
        ball.y = 500
    if top_score == 0:
        ball_speedy = -ball_speedy
    
    #bottom
    if ball.y == 1000:
        bottom_score -= 1
        ball_speedx = 0
        ball_speedy = 0
        ball.x = 500
        ball.y = 500
    if top_score == 0:
        ball_speedy = -ball_speedy

    screen.blit(left_score_text, ((10, 10)))
    screen.blit(right_score_text, ((990 - (right_score_text.get_width ()), 990 - (bottom_score_text.get_height()))))
    screen.blit(top_score_text, ((990 - (top_score_text.get_width ()), 10))) 
    screen.blit(bottom_score_text, ((10 , 990 - (bottom_score_text.get_height()))))

    if left_score != 0:
        pygame.draw.rect(screen, red, bat1)
    if right_score != 0:
        pygame.draw.rect(screen, blue, bat2)
    if top_score != 0:
        pygame.draw.rect(screen, green, bat3)
    if bottom_score != 0:
        pygame.draw.rect(screen, yellow, bat4)
    pygame.draw.circle(screen, (white), (ball.x, ball.y), ballradius, ballradius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #bat movement
    key = pygame.key.get_pressed()

    #left bat
    if key[pygame.K_w]:
        if bat1.y <= 0:
            bat1.y = 0
        elif bat1.colliderect(bat3) or bat1.colliderect(bat4):
            bat1.y = bat1.y + bat_speed
        else:
            bat1.y -= bat_speed
    if key[pygame.K_s]:
        if bat1.y >= height - bat_size_a:
            bat1.y = height - bat_size_a
        elif bat1.colliderect(bat3) or bat1.colliderect(bat4):
            bat1.y = bat1.y - bat_speed
        else:
            bat1.y += bat_speed

    #right bat
    if key[pygame.K_UP]:
        if bat2.y <= 0:
            bat2.y = 0
        elif bat2.colliderect(bat3) or bat2.colliderect(bat4):
            bat2.y = bat2.y + bat_speed
        else:
            bat2.y -= bat_speed
    if key[pygame.K_DOWN]:
        if bat2.y >= height - bat_size_a:
            bat2.y = height - bat_size_a
        elif bat2.colliderect(bat3) or bat2.colliderect(bat4):
            bat2.y = bat2.y - bat_speed
        else:
            bat2.y += bat_speed

    #top bat
    if key[pygame.K_o]:
        if bat3.x <= 0:
            bat3.x = 0
        elif bat3.colliderect(bat1) or bat3.colliderect(bat2):
            bat3.x = bat3.x + bat_speed
        else:
            bat3.x -= bat_speed
    if key[pygame.K_p]:
        if bat3.x >= width - bat_size_a:
            bat3.x = width - bat_size_a
        elif bat3.colliderect(bat1) or bat3.colliderect(bat2):
            bat3.x = bat3.x - bat_speed
        else:
            bat3.x += bat_speed
        
    #bottom bat
    if key[pygame.K_v]:
        if bat4.x <= 0:
            bat4.x = 0
        elif bat4.colliderect(bat1) or bat4.colliderect(bat2):
            bat4.x = bat4.x + bat_speed
        else:
            bat4.x -= bat_speed
    if key[pygame.K_b]:
        if bat4.x >= width - bat_size_a:
            bat4.x = width - bat_size_a
        elif bat4.colliderect(bat1) or bat4.colliderect(bat2):
            bat4.x = bat4.x - bat_speed
        else:
            bat4.x += bat_speed

    #ball movement
    ball.x += ball_speedx 
    ball.y += ball_speedy 

    #bat/ball collision
    if ball.colliderect(bat1) and left_score != 0:
        ball_speedx = -ball_speedx
    if ball.colliderect(bat2) and right_score != 0:
        ball_speedx = -ball_speedx
    if ball.colliderect(bat3) and top_score != 0:
        ball_speedy = -ball_speedy
    if ball.colliderect(bat4) and bottom_score != 0:
        ball_speedy = -ball_speedy

    

    #respawning balls
    if key[pygame.K_SPACE]:
        ran_x = random.randint(1, 10)
        ran_y = random.randint(1, 10)
        ball_speedx = 1 * ran_x
        ball_speedy = 1 * ran_y

    #ending game
    if left_score == 0 and right_score == 0 and top_score == 0 and bottom_score == 0:
        pygame.quit()
        sys.exit()    

    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)

#important stuff for quitting
pygame.quit()
sys.exit()
