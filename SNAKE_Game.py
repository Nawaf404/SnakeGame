
import pygame # For SNAKE GAME
import time
import random # For Random Food

pygame.init() # initialze library game

print('''
    |--------------------------------------|
    |      Instructions for The Game 🐍    |
    | +++++++++++++++++++++++++++++++++}   |
    | {  - The Game Will Display On    }   |
    | {          Another Window        }   |
    | {++++++++++++++++++++++++++++++++}   |
    |                                      |
    |   /________________________________\ |
    |  |     Your Score will be Above    | |
    |  |_________________________________| | 
    |                                      |
    |  _----------------------------------_|
    | |Maybe the food won't show in First| |
    | \__________________________________/ |
    |                                      |
    | |___________________________________| |
    | |if you Out from the Limit, WIll    ||
    | |Lose and will SHow message with Red||
    | |___________________________________||
    |                                      |
    |  ................................... |
    | .   U Can Quit with Keyword Q      . |
    | .  AND continue With C             . |
    | .................................... |
    |                                      |
    | #################################### |
    | # if you press Arrow Up and right  # |
    | #Or Wrap around the Snake will Lose# |
    | #################################### |
    |                                      |
    | " if You Eat Food , will be long "   |
    | " and will print "Yummy" inc CCL     |
    |                                      |
    |       Has Developed By Nawaf [+]     |
    |     And the All of Code is from      |
    |       https://edureka.co             |
    |     My GITHUB : Nawaf404             |
    |______________________________________|
    |           E  n  j  o   y  :)         |
    |______________________________________|
''')

white = (255, 255, 255) # With Colors scheme RGB .. Used in PyGame
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# for use color we need to use scheme color RGB .. 0-255

zero = 90
dis_width = 600 # width of the Screen or Window
dis_height = 400 # Height of the Screen or Window

dis = pygame.display.set_mode((dis_width,dis_height)) # SET : The Size ,, {dis_width same 600}

pygame.display.set_caption('Snake game by Nawaf ') # Name of the Game or Title


snake_block = 10 # size of snake
snake_speed = 15 # speed of snake

font_style = pygame.font.SysFont("bahnschrift", 25) # ALERT for LOSe
score_font = pygame.font.SysFont("comicsansms", 25) # Score

clock = pygame.time.Clock()

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], 15, 15])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [zero, dis_height/2])

def gameLoop(): # Creating a function
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # food
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost ! Press Q-Quit or C-Play Again ", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True # if press Q will Out
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() # continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allow to Exit if Click QUIT Button [ X ]
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # if user press Arrow Left will go to left with 10
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True  # if it exceeds the limits will Out from the Game

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) # to make the background blue..
        pygame.draw.rect(dis, red, [foodx, foody, 15, 15]) # draw the food
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0] # while snake eat ? long more
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update() # will update the data, will add new features

        if x1 == foodx and y1 == foody:
            print("Yummy !") # print on console
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed) # the speed of snake
    pygame.quit()
    quit()

gameLoop()

# Source : https://www.edureka.co/blog/snake-game-with-pygame/