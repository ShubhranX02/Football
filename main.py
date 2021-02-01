import pygame, sys
from time import sleep
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Football")

# print(pygame.font.get_fonts())

goals_team_1 = 0
goals_team_2 = 0

myfont = pygame.font.SysFont('Comic Sans MS', 40)
myfont3 = pygame.font.SysFont('arialblack', 23)




def check_in(start, stop, var):
    for x in range(start, stop):
        if var == x:
            return True
    return False

def is_collided_with(obj, obj_to_check_with):
    return obj.colliderect(obj_to_check_with)

height = 600
width = 1000
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0 ,0)
orange = (255, 100, 0)
blue = (0, 100, 255)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))


nike_logo = pygame.image.load('nike.jpg').convert_alpha()
nike_logo1 = pygame.transform.scale(nike_logo, (20, 20))
nike_logo = nike_logo1

team1_text = myfont3.render("TEAM 1", False, (orange))
team2_text = myfont3.render("TEAM 2", False, (blue))


# important variables
ball_x = 500
ball_y = 300


player1_team1_sprint = 6
player1_team1_x = 100
player1_team1_y = 300
player1_team1_color = (0, 0, 0)

player2_team1_sprint = 6
player2_team1_x = 200
player2_team1_y = 150
player2_team1_color = (0, 0, 0)

player3_team1_sprint = 6
player3_team1_x = 200
player3_team1_y = 450
player3_team1_color = (0, 0, 0)

player4_team1_sprint = 6
player4_team1_x = 300
player4_team1_y = 300
player4_team1_color = (0, 0, 0)

player5_team1_sprint = 6
player5_team1_x = 400
player5_team1_y = 300
player5_team1_color = (0, 0, 0)

player1_team2_sprint = 6
player1_team2_x = width-100
player1_team2_y = 300
player1_team2_color = (0, 0, 0)

player2_team2_sprint = 6
player2_team2_x = width-200
player2_team2_y = 150
player2_team2_color = (0, 0, 0)

player3_team2_sprint = 6
player3_team2_x = width-200
player3_team2_y = 450
player3_team2_color = (0, 0, 0)

player4_team2_sprint = 6
player4_team2_x = width-300
player4_team2_y = 300
player4_team2_color = (0, 0, 0)

player5_team2_sprint = 6
player5_team2_x = width-400
player5_team2_y = 300
player5_team2_color = (0, 0, 0)

mov_speed = 5
sprint_speed = 15
ball_mov_speed = 15
ball_kick = 40

team1_control_player = 5
team2_control_player = 5



while True:
    pygame.time.delay(50)
    clock = pygame.time.Clock()


    textsurface = myfont.render(f'{goals_team_1} - {goals_team_2}', False, (0, 0, 0))



    player1_team1 = ball_x - player1_team1_x + ball_y - player1_team1_y
    player2_team1 = ball_x - player2_team1_x + ball_y - player2_team1_y
    player3_team1 = ball_x - player3_team1_x + ball_y - player3_team1_y
    player4_team1 = ball_x - player4_team1_x + ball_y - player4_team1_y
    player5_team1 = ball_x - player5_team1_x + ball_y - player5_team1_y

    player1_team2 = ball_x - player1_team2_x + ball_y - player1_team2_y
    player2_team2 = ball_x - player2_team2_x + ball_y - player2_team2_y
    player3_team2 = ball_x - player3_team2_x + ball_y - player3_team2_y
    player4_team2 = ball_x - player4_team2_x + ball_y - player4_team2_y
    player5_team2 = ball_x - player5_team2_x + ball_y - player5_team2_y

    boundary_rect1 = pygame.draw.rect(screen, (green), (0, 0, width, 10))
    boundary_rect2 = pygame.draw.rect(screen, (green), (0, height, 10, height))
    boundary_rect3 = pygame.draw.rect(screen, (green), (width-10, 0, 20, height))
    boundary_rect4 = pygame.draw.rect(screen, (green), (0, height-10, width, 20))


    # sprint
    #player1_team1_sprint_bar = pygame.draw.rect(screen, (red), (player1_team1_x-20, player1_team1_y+40, 40, 10)), \
                               #pygame.draw.rect(screen, (black), (player1_team1_x-22, player1_team1_y-42, 42, 12), 2)


    # player movements


    if ball_x > player2_team1_x and team1_control_player != 2 and player2_team1_x < width - 10:
        player2_team1_x += 1
    if ball_x < player1_team1_x and team1_control_player != 2 and player2_team1_x > width - 10:
        player2_team1_x -= 1
    if ball_x < player3_team1_x and team1_control_player != 3 and player3_team1_x < width - 10:
        player2_team1_x -= 1
    if ball_x > player3_team1_x and team1_control_player != 3 and player3_team1_x > 10:
        player3_team1_x += 1
    if ball_x > player4_team1_x and team1_control_player != 4 and player4_team1_x < width - 10:
        player4_team1_x += 1
    if ball_x < player4_team1_x and team1_control_player != 4 and player4_team1_x > 10:
        player4_team1_x -= 1
    if ball_x > player5_team1_x and team1_control_player != 5 and player5_team1_x < width - 10:
        player5_team1_x += 1
    if ball_x < player5_team1_x and team1_control_player != 5 and player5_team1_x > 10:
        player5_team1_x -= 1



    if ball_x > player2_team2_x and team2_control_player != 2 and player2_team2_x < width - 10:
        player2_team2_x += 1
    if ball_x < player2_team2_x and team2_control_player != 2 and player2_team2_x > 10:
        player2_team2_x -= 1
    if ball_x > player3_team2_x and team2_control_player != 3 and player3_team2_x < width - 10:
        player3_team2_x += 1
    if ball_x < player3_team2_x and team2_control_player != 3 and player3_team2_x > 10:
        player3_team2_x -= 1
    if ball_x > player4_team2_x and team2_control_player != 4 and player4_team2_x < width - 10:
        player4_team2_x += 1
    if ball_x < player4_team2_x and team2_control_player != 4 and player4_team2_x > 10:
        player4_team2_x -= 1
    if ball_x > player5_team2_x and team2_control_player != 5 and player5_team2_x < width - 10:
        player5_team2_x += 1
    if ball_x < player5_team2_x and team2_control_player != 5 and player5_team2_x > 10:
        player5_team2_x -= 1







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    # switch
    if keys[pygame.K_RSHIFT]:
        team2_control_player += 1
        if team2_control_player == 6:
            team2_control_player = 1
        sleep(0.2)

    if keys[pygame.K_e]:
        team1_control_player += 1
        if team1_control_player == 6:
            team1_control_player = 1
        sleep(0.2)

    # team 1
    if team1_control_player == 1:
        player1_team1_color = red
    else:
        player1_team1_color = black

    if team1_control_player == 2:
        player2_team1_color = red
    else:
        player2_team1_color = black

    if team1_control_player == 3:
        player3_team1_color = red
    else:
        player3_team1_color = black

    if team1_control_player == 4:
        player4_team1_color = red
    else:
        player4_team1_color = black

    if team1_control_player == 5:
        player5_team1_color = red
    else:
        player5_team1_color = black

    # team 2
    if team2_control_player == 1:
        player1_team2_color = red
    else:
        player1_team2_color = black
    if team2_control_player == 2:
        player2_team2_color = red
    else:
        player2_team2_color = black
    if team2_control_player == 3:
        player3_team2_color = red
    else:
        player3_team2_color = black
    if team2_control_player == 4:
        player4_team2_color = red
    else:
        player4_team2_color = black
    if team2_control_player == 5:
        player5_team2_color = red
    else:
        player5_team2_color = black

    # movement
    if keys[pygame.K_w]:
        if team1_control_player == 1 and player1_team1_y > 20:
            player1_team1_y -= mov_speed

        if team1_control_player == 2 and player2_team1_y > 20:
            player2_team1_y -= mov_speed

        if team1_control_player == 3 and player3_team1_y > 20:
            player3_team1_y -= mov_speed

        if team1_control_player == 4 and player4_team1_y > 20:
            player4_team1_y -= mov_speed

        if team1_control_player == 5 and player5_team1_y > 20:
            player5_team1_y -= mov_speed

    if keys[pygame.K_a]:
        if team1_control_player == 1 and player1_team1_x > 20:
            player1_team1_x -= mov_speed

        if team1_control_player == 2 and player2_team1_x > 20:
            player2_team1_x -= mov_speed

        if team1_control_player == 3 and player3_team1_x > 20:
            player3_team1_x -= mov_speed

        if team1_control_player == 4 and player4_team1_x > 20:
            player4_team1_x -= mov_speed

        if team1_control_player == 5 and player5_team1_x > 20:
            player5_team1_x -= mov_speed

    if keys[pygame.K_s]:
        if team1_control_player == 1 and player1_team1_y < height-20:
            player1_team1_y += mov_speed

        if team1_control_player == 2 and player2_team1_y < height-20:
            player2_team1_y += mov_speed

        if team1_control_player == 3 and player3_team1_y < height-20:
            player3_team1_y += mov_speed

        if team1_control_player == 4 and player4_team1_y < height-20:
            player4_team1_y += mov_speed

        if team1_control_player == 5 and player5_team1_y < height-20:
            player5_team1_y += mov_speed

    if keys[pygame.K_d]:
        if team1_control_player == 1 and player1_team1_x < width-20:
            player1_team1_x += mov_speed

        if team1_control_player == 2 and player2_team1_x < width-20:
            player2_team1_x += mov_speed

        if team1_control_player == 3 and player3_team1_x < width-20:
            player3_team1_x += mov_speed

        if team1_control_player == 4 and player4_team1_x < width-20:
            player4_team1_x += mov_speed

        if team1_control_player == 5 and player5_team1_x < width-20:
            player5_team1_x += mov_speed

    if keys[pygame.K_UP]:
        if team2_control_player == 1 and player1_team2_y > 20:
            player1_team2_y -= mov_speed

        if team2_control_player == 2 and player2_team2_y > 20:
            player2_team2_y -= mov_speed

        if team2_control_player == 3 and player3_team2_y > 20:
            player3_team2_y -= mov_speed

        if team2_control_player == 4 and player4_team2_y > 20:
            player4_team2_y -= mov_speed

        if team2_control_player == 5 and player5_team2_y > 20:
            player5_team2_y -= mov_speed

    if keys[pygame.K_LEFT]:
        if team2_control_player == 1 and player1_team2_x > 20:
            player1_team2_x -= mov_speed

        if team2_control_player == 2 and player2_team2_x > 20:
            player2_team2_x -= mov_speed

        if team2_control_player == 3 and player3_team2_x > 20:
            player3_team2_x -= mov_speed

        if team2_control_player == 4 and player4_team2_x > 20:
            player4_team2_x -= mov_speed

        if team2_control_player == 5 and player5_team2_x > 20:
            player5_team2_x -= mov_speed

    if keys[pygame.K_DOWN]:
        if team2_control_player == 1 and player1_team2_y < height-20:
            player1_team2_y += mov_speed

        if team2_control_player == 2 and player2_team2_y < height-20:
            player2_team2_y += mov_speed

        if team2_control_player == 3 and player3_team2_y < height-20:
            player3_team2_y += mov_speed

        if team2_control_player == 4 and player4_team2_y < height-20:
            player4_team2_y += mov_speed

        if team2_control_player == 5 and player5_team2_y < height-20:
            player5_team2_y += mov_speed

    if keys[pygame.K_RIGHT]:
        if team2_control_player == 1 and player1_team2_x < width-20:
            player1_team2_x += mov_speed

        if team2_control_player == 2 and player2_team2_x < width-20:
            player2_team2_x += mov_speed

        if team2_control_player == 3 and player3_team2_x < width-20:
            player3_team2_x += mov_speed

        if team2_control_player == 4 and player4_team2_x < width-20:
            player4_team2_x += mov_speed

        if team2_control_player == 5 and player5_team2_x < width-20:
            player5_team2_x += mov_speed












    screen.fill(green)

    # main
    footrect = pygame.draw.rect(screen, (green), (ball_x - 15, ball_y - 15, 30, 30), 1)
    goal_1 = pygame.draw.rect(screen, (white), (8, height / 2 - 72, 32, 144), 0)
    goal_2 = pygame.draw.rect(screen, (white), (width - 40, height / 2 - 72, 32, 144), 0)
    player5_team2_rect = pygame.draw.rect(screen, (green), (player5_team2_x - 17, player5_team2_y - 17, 34, 34), 1)
    player4_team2_rect = pygame.draw.rect(screen, (green), (player4_team2_x - 17, player4_team2_y - 17, 34, 34), 1)
    player3_team2_rect = pygame.draw.rect(screen, (green), (player3_team2_x - 17, player3_team2_y - 17, 34, 34), 1)
    player2_team2_rect = pygame.draw.rect(screen, (green), (player2_team2_x - 17, player2_team2_y - 17, 34, 34), 1)
    player1_team2_rect = pygame.draw.rect(screen, (green), (player1_team2_x - 17, player1_team2_y - 17, 34, 34), 1)
    player5_team1_rect = pygame.draw.rect(screen, (green), (player5_team1_x - 17, player5_team1_y - 17, 34, 34), 1)
    player4_team1_rect = pygame.draw.rect(screen, (green), (player4_team1_x - 17, player4_team1_y - 17, 34, 34), 1)
    player3_team1_rect = pygame.draw.rect(screen, (green), (player3_team1_x - 17, player3_team1_y - 17, 34, 34), 1)
    player2_team1_rect = pygame.draw.rect(screen, (green), (player2_team1_x - 17, player2_team1_y - 17, 34, 34), 1)
    player1_team1_rect = pygame.draw.rect(screen, (green), (player1_team1_x - 17, player1_team1_y - 17, 34, 34), 1)


    # field
    # try_line = pygame.draw.line(screen, (white), (0, height/2), (width, height/2), 2)
    holder = pygame.draw.rect(screen, (white), (width/2-50, 0, 100, 50), 0)

    holder2 = pygame.draw.rect(screen, (white), (200, 0, 100, 30), 0)
    holder2_holder = pygame.draw.rect(screen, (black), (197, 0, 106, 33), 3)
    holder3 = pygame.draw.rect(screen, (white), (width-300, 0, 100, 30), 0)
    holder3_holder = pygame.draw.rect(screen, (black), (width-303, 0, 106, 33), 3)

    screen.blit(team1_text, (200, 0))
    screen.blit(team2_text, (width-300, 0))

    de_line = pygame.draw.circle(screen, (white), (141, 300), 60, 2)
    de_line2 = pygame.draw.circle(screen, (white), (width-141, 300), 60, 2)
    cover_up_box = pygame.draw.rect(screen, (green), (60, height/2-60, 81, 120))
    cover_up_box2 = pygame.draw.rect(screen, (green), (width-141, height / 2 - 60, 80, 120))
    line2 = pygame.draw.line(screen, (white), (width/2, 0),(width/2, height), 2)
    line3 = pygame.draw.line(screen, (white), (41, 0), (41, height), 2)
    line4 = pygame.draw.line(screen, (white), (width-41, 0), (width-41, height), 2)
    de_box = pygame.draw.rect(screen, (white), (41, height/2-100, 100, 200), 2)
    de_box2 = pygame.draw.rect(screen, (white), (width-141, height / 2 - 100, 100, 200), 2)
    centre_circle = pygame.draw.circle(screen, (white), (500, 300), 100, 2)
    post_b1 = pygame.draw.line(screen, (0, 0, 0), (5, height/2 - 75), (5, height/2 + 75), 3)
    post_b2 = pygame.draw.line(screen, (0, 0, 0), (5, height/2 - 75), (40, height/2 - 75), 3)
    post_b3 = pygame.draw.line(screen, (0, 0, 0), (5, height/2 + 75), (40, height/2 + 75), 3)
    post_o1 = pygame.draw.line(screen, (0, 0, 0), (width - 5, height / 2 - 75), (width - 5, height / 2 + 75), 3)
    post_o2 = pygame.draw.line(screen, (0, 0, 0), (width - 5, height / 2 - 75), (width - 40, height / 2 - 75), 3)
    post_o3 = pygame.draw.line(screen, (0, 0, 0), (width - 5, height / 2 + 75), (width - 40, height / 2 + 75), 3)
    goal_line1 = pygame.draw.line(screen, (black), (15, height/2-75), (15, height/2+75), 2)
    goal_line2 = pygame.draw.line(screen, (black), (25, height / 2 - 75), (25, height / 2 + 75), 2)
    goal_line3 = pygame.draw.line(screen, (black), (35, height / 2 - 75), (35, height / 2 + 75), 2)

    goal_line4 = pygame.draw.line(screen, (black), (width - 15, height / 2 - 75), (width - 15, height / 2 + 75), 2)
    goal_line5 = pygame.draw.line(screen, (black), (width - 25, height / 2 - 75), (width - 25, height / 2 + 75), 2)
    goal_line6 = pygame.draw.line(screen, (black), (width - 35, height / 2 - 75), (width - 35, height / 2 + 75), 2)
    goal_line7 = pygame.draw.line(screen, (black), (5, height / 2 - 60), (40, height / 2 - 60), 2)
    goal_line8 = pygame.draw.line(screen, (black), (5, height / 2 - 40), (40, height / 2 - 40), 2)
    goal_line9 = pygame.draw.line(screen, (black), (5, height / 2 - 20), (40, height / 2 - 20), 2)
    goal_line10 = pygame.draw.line(screen, (black), (5, height / 2), (40, height / 2), 2)
    goal_line11 = pygame.draw.line(screen, (black), (5, height / 2 + 20), (40, height / 2 + 20), 2)
    goal_line12 = pygame.draw.line(screen, (black), (5, height / 2 + 40), (40, height / 2 + 40), 2)
    goal_line13 = pygame.draw.line(screen, (black), (5, height / 2 + 60), (40, height / 2 + 60), 2)

    goal_line17 = pygame.draw.line(screen, (black), (width - 5, height / 2 - 60), (width - 40, height / 2 - 60), 2)
    goal_line18 = pygame.draw.line(screen, (black), (width-5, height / 2 - 40), (width-40, height / 2 - 40), 2)
    goal_line19 = pygame.draw.line(screen, (black), (width-5, height / 2 - 20), (width-40, height / 2 - 20), 2)
    goal_line20 = pygame.draw.line(screen, (black), (width-5, height / 2), (width-40, height / 2), 2)
    goal_line21 = pygame.draw.line(screen, (black), (width-5, height / 2 + 20), (width-40, height / 2 + 20), 2)
    goal_line22 = pygame.draw.line(screen, (black), (width-5, height / 2 + 40), (width-40, height / 2 + 40), 2)
    goal_line23 = pygame.draw.line(screen, (black), (width-5, height / 2 + 60), (width-40, height / 2 + 60), 2)
    line1 = pygame.draw.line(screen, (0, 0, 0), (0, 0), (width, 0), 1)



    # other main


    football = pygame.draw.circle(screen, (white), (ball_x, ball_y), 15), \
               screen.blit(nike_logo, (ball_x-10, ball_y-10)), \
               pygame.draw.circle(screen, (black), (ball_x - 1, ball_y - 1), 16, 2)

    # team 1

    player1_team1 = pygame.draw.circle(screen, (orange), (player1_team1_x, player1_team1_y), 20), \
                    pygame.draw.circle(screen, (player1_team1_color), (player1_team1_x, player1_team1_y), 22, 2)

    player2_team1 = pygame.draw.circle(screen, (orange), (player2_team1_x, player2_team1_y), 20), \
                    pygame.draw.circle(screen, (player2_team1_color), (player2_team1_x, player2_team1_y), 22, 2)

    player3_team1 = pygame.draw.circle(screen, (orange), (player3_team1_x, player3_team1_y), 20), \
                    pygame.draw.circle(screen, (player3_team1_color), (player3_team1_x, player3_team1_y), 22, 2)

    player4_team1 = pygame.draw.circle(screen, (orange), (player4_team1_x, player4_team1_y), 20), \
                    pygame.draw.circle(screen, (player4_team1_color), (player4_team1_x, player4_team1_y), 22, 2)

    player5_team1 = pygame.draw.circle(screen, (orange), (player5_team1_x, player5_team1_y), 20), \
                    pygame.draw.circle(screen, (player5_team1_color), (player5_team1_x, player5_team1_y), 22, 2)

    # team 2

    player1_team2 = pygame.draw.circle(screen, (blue), (player1_team2_x, player1_team2_y), 20), \
                    pygame.draw.circle(screen, (player1_team2_color), (player1_team2_x, player1_team2_y), 22, 2)

    player2_team2 = pygame.draw.circle(screen, (blue), (player2_team2_x, player2_team2_y), 20), \
                    pygame.draw.circle(screen, (player2_team2_color), (player2_team2_x, player2_team2_y), 22, 2)

    player3_team2 = pygame.draw.circle(screen, (blue), (player3_team2_x, player3_team2_y), 20), \
                    pygame.draw.circle(screen, (player3_team2_color), (player3_team2_x, player3_team2_y), 22, 2)

    player4_team2 = pygame.draw.circle(screen, (blue), (player4_team2_x, player4_team2_y), 20), \
                    pygame.draw.circle(screen, (player4_team2_color), (player4_team2_x, player4_team2_y), 22, 2)

    player5_team2 = pygame.draw.circle(screen, (blue), (player5_team2_x, player5_team2_y), 20), \
                    pygame.draw.circle(screen, (player5_team2_color), (player5_team2_x, player5_team2_y), 22, 2)



    # football movement

    if is_collided_with(player1_team1_rect, footrect) or is_collided_with(player2_team1_rect, footrect) or \
        is_collided_with(player3_team1_rect, footrect) or is_collided_with(player4_team1_rect, footrect) or \
            is_collided_with(player5_team1_rect, footrect) or is_collided_with(player1_team2_rect, footrect) or \
            is_collided_with(player2_team2_rect, footrect) or is_collided_with(player3_team2_rect, footrect) or \
            is_collided_with(player4_team2_rect, footrect) or is_collided_with(player5_team2_rect, footrect):
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and ball_y > 25:
            if (keys[pygame.K_q] or keys[pygame.K_RCTRL]) and ball_y > 40:
                y = 0
                while y < ball_kick:
                    ball_y -= 10
                    y += 10
            else:
                ball_y -= ball_mov_speed
                sleep(0.1)

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ball_x > 25:
            if (keys[pygame.K_q] or keys[pygame.K_RCTRL]) and ball_x > 40:
                y = 0
                while y < ball_kick:
                    ball_x -= 10
                    y += 10
            else:
                ball_x -= ball_mov_speed
                sleep(0.1)

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ball_x < width-25:
            if (keys[pygame.K_q] or keys[pygame.K_RCTRL]) and ball_y < width-200:
                y = 0
                while y < ball_kick:
                    ball_x += 10
                    y += 10
                    sleep(0.1)
            else:
                ball_x += ball_mov_speed

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ball_y < height-25:
            if (keys[pygame.K_q] or keys[pygame.K_RCTRL]) and ball_y < height-100:
                y = 0
                while y < ball_kick:
                    ball_y += 10
                    y += 10
            else:
                ball_y += ball_mov_speed
                sleep(0.1)

        elif keys[pygame.K_q] or keys[pygame.K_RCTRL]:
            yy = random.randrange(1, 5)
            if yy == 1 and ball_x < width - 10:
                ball_x += 10
            if yy == 2 and ball_y < height - 10:
                ball_y += 10
            if yy == 3 and ball_y > 10:
                ball_y += 10
            if yy == 4 and ball_x > 10:
                ball_x += 10

    if is_collided_with(footrect, boundary_rect1):
        ball_y += 10
    if is_collided_with(footrect, boundary_rect2):
        ball_x += 10
    if is_collided_with(footrect, boundary_rect3):
        ball_x -= 10
    if is_collided_with(footrect, boundary_rect4):
        ball_y -= 10















    holder_holder = pygame.draw.rect(screen, (black), (width / 2 - 53, 0, 106, 53), 3)

    # victory statements
    if is_collided_with(goal_1, footrect):
        myfont4 = pygame.font.SysFont('arialblack', 100)
        goals_team_2 += 1
        textsurface3 = myfont4.render("GOAL!!", False, (blue))
        screen.blit(textsurface3, (width/2-150, height/2-50))
        pygame.display.update()
        ball_x = 500
        ball_y = 300

        player1_team1_x = 100
        player1_team1_y = 300
        player1_team1_color = (0, 0, 0)

        player2_team1_x = 200
        player2_team1_y = 150
        player2_team1_color = (0, 0, 0)

        player3_team1_x = 200
        player3_team1_y = 450
        player3_team1_color = (0, 0, 0)

        player4_team1_x = 300
        player4_team1_y = 300
        player4_team1_color = (0, 0, 0)

        player5_team1_x = 400
        player5_team1_y = 300
        player5_team1_color = (0, 0, 0)

        player1_team2_x = width - 100
        player1_team2_y = 300
        player1_team2_color = (0, 0, 0)

        player2_team2_x = width - 200
        player2_team2_y = 150
        player2_team2_color = (0, 0, 0)

        player3_team2_x = width - 200
        player3_team2_y = 450
        player3_team2_color = (0, 0, 0)

        player4_team2_x = width - 300
        player4_team2_y = 300
        player4_team2_color = (0, 0, 0)

        player5_team2_x = width - 400
        player5_team2_y = 300
        player5_team2_color = (0, 0, 0)

        team1_control_player = 5
        team2_control_player = 5
        sleep(2.0)

    if is_collided_with(goal_2, footrect):
        myfont4 = pygame.font.SysFont('arialblack', 100)
        goals_team_1 += 1
        textsurface3 = myfont4.render("GOAL!!", False, (orange))
        screen.blit(textsurface3, (width/2-150, height/2-50))
        pygame.display.update()
        ball_x = 500
        ball_y = 300

        player1_team1_x = 100
        player1_team1_y = 300
        player1_team1_color = (0, 0, 0)

        player2_team1_x = 200
        player2_team1_y = 150
        player2_team1_color = (0, 0, 0)

        player3_team1_x = 200
        player3_team1_y = 450
        player3_team1_color = (0, 0, 0)

        player4_team1_x = 300
        player4_team1_y = 300
        player4_team1_color = (0, 0, 0)

        player5_team1_x = 400
        player5_team1_y = 300
        player5_team1_color = (0, 0, 0)

        player1_team2_x = width - 100
        player1_team2_y = 300
        player1_team2_color = (0, 0, 0)

        player2_team2_x = width - 200
        player2_team2_y = 150
        player2_team2_color = (0, 0, 0)

        player3_team2_x = width - 200
        player3_team2_y = 450
        player3_team2_color = (0, 0, 0)

        player4_team2_x = width - 300
        player4_team2_y = 300
        player4_team2_color = (0, 0, 0)

        player5_team2_x = width - 400
        player5_team2_y = 300
        player5_team2_color = (0, 0, 0)

        team1_control_player = 5
        team2_control_player = 5

        sleep(2.0)

    if goals_team_2 == 3:
        myfont2 = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface2 = myfont.render('TEAM 2 WINS!', False, (blue))
        screen.blit(textsurface2, (width/2-135, height/2-60))
        sleep(1.0)
        pygame.display.update()
        sleep(5.0)
        sys.exit()

    if goals_team_1 == 3:
        myfont2 = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface2 = myfont.render('TEAM 1 WINS!', False, (orange))
        screen.blit(textsurface2, (width/2-135, height/2-60))
        sleep(1.0)
        pygame.display.update()
        sleep(5.0)
        sys.exit()

    screen.blit(textsurface, (width / 2 - 45, -5))

    pygame.display.update()








