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
    pygame.draw.rect(screen, white, bat1)
    pygame.draw.rect(screen, white, bat2)
    pygame.draw.rect(screen, white, bat3)
    pygame.draw.rect(screen, white, bat4)
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
        else:
            bat1.y -= bat_speed
    if key[pygame.K_s]:
        if bat1.y >= height - bat_size_a:
            bat1.y = height - bat_size_a
        else:
            bat1.y += bat_speed

    #right bat
    if key[pygame.K_UP]:
        if bat2.y <= 0:
            bat2.y = 0
        else:
            bat2.y -= bat_speed
    if key[pygame.K_DOWN]:
        if bat2.y >= height - bat_size_a:
            bat2.y = height - bat_size_a
        else:
            bat2.y += bat_speed

    #top bat
    if key[pygame.K_c]:
        if bat3.x <= 0:
            bat3.x = 0
        else:
            bat3.x -= bat_speed
    if key[pygame.K_v]:
        if bat3.x >= width - bat_size_a:
            bat3.x = width - bat_size_a
        else:
            bat3.x += bat_speed
        
    #bottom bat
    if key[pygame.K_o]:
        if bat4.x <= 0:
            bat4.x = 0
        else:
            bat4.x -= bat_speed
    if key[pygame.K_p]:
        if bat4.x >= width - bat_size_a:
            bat4.x = width - bat_size_a
        else:
            bat4.x += bat_speed

    #ball movement
    ball.x += ball_speedx 
    ball.y += ball_speedy 

    #if ball.colliderect(bat3) or ball.colliderect(bat4)

    #bat collision
    if ball.colliderect(bat1) or ball.colliderect(bat2):
        ball_speedx = -ball_speedx
    if ball.colliderect(bat3) or ball.colliderect(bat4):
        ball_speedy = -ball_speedy

    #scoring
    #left
    if ball.x == 0:
        left_score -= 1
        ball.x = 500
        ball.y = 500

    #right
    if ball.x == 1000:
        right_score -= 1
        ball.x = 500
        ball.y = 500

    #top
    if ball.y == 0:
        top_score -=1
        ball.x = 500
        ball.y = 500

    #bottom
    if ball.y == 1000:
        top_score -=1
        ball.x = 500   
        ball.y = 500
 
    if left_score == 0 and right_score == 0 and top_score == 0 and bottom_score == 0:
        pygame.quit()
        sys.exit()    

    #display scores
    left_score_text = font.render("Left Score = " + "♥" * left_score, True, white)
    right_score_text = font.render("Right Score = " + "♥" * right_score, True, white)
    top_score_text = font.render("Top Score = " + "♥" * top_score, True, white)
    bottom_score_text = font.render("Bottom Score = " + "♥" * bottom_score, True, white)

    screen.blit(left_score_text, ((10, 10)))
    screen.blit(right_score_text, ((990 - (right_score_text.get_width ()), 990 - (bottom_score_text.get_height()))))
    screen.blit(top_score_text, ((990 - (top_score_text.get_width ()), 10))) 
    screen.blit(bottom_score_text, ((10 , 990 - (bottom_score_text.get_height())))) 

    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)

#important stuff for quitting
pygame.quit()
sys.exit()