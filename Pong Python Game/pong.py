import pygame,sys,random

#Ball Animations
def ball_animations():
    global ball_speed_x, ball_speed_y, playerOne_score, playerTwo_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        play_sound_effects('./resources/sounds/boop.mp3', random.choice((0.2, 0.7)))
        ball_speed_y *= -1
        
    if ball.left <= 0:
        play_sound_effects('./resources/sounds/error1.mp3', 1.0)
        pygame.time.wait(1500)
        play_sound_effects('./resources/sounds/beep.mp3', 1.0)
        score_time = pygame.time.get_ticks()
        playerTwo_score += 1
    if ball.right >= screen_width:
        play_sound_effects('./resources/sounds/error1.mp3', 1.0)
        pygame.time.wait(1500)
        play_sound_effects('./resources/sounds/beep.mp3', 1.0)
        score_time = pygame.time.get_ticks()
        playerOne_score += 1
    
    # if ball.colliderect(player_one) or ball.colliderect(player_two) : 
    #     play_sound_effects(f'./resources/sounds/pong_{random.choice((1, 2, 3, 4, 5))}.mp3', 1.0)
    #     ball_speed_x *= -1

    #Ball collision on Player 1/Player 2 Rectangles
    if ball.colliderect(player_one) and ball_speed_x == -7: 
        if abs(ball.right - player_one.left) > 10:
            play_sound_effects(f'./resources/sounds/pong_{random.choice((1, 2, 3, 4, 5))}.mp3', 1.0)
            ball_speed_x *= -1
        if abs(ball.bottom - player_one.top) < 10 and ball_speed_y > 0:
            play_sound_effects(f'./resources/sounds/pong_{random.choice((1, 2, 3, 4, 5))}.mp3', 1.0)
            ball_speed_y *= -1
        if abs(ball.top - player_one.bottom) < 10 and ball_speed_y < 0:
            play_sound_effects(f'./resources/sounds/pong_{random.choice((1, 2, 3, 4, 5))}.mp3', 1.0)
            ball_speed_y *= -1    
    
    if ball.colliderect(player_two) and ball_speed_x == 7:
        if abs(ball.left - player_two.right) > 10:
            play_sound_effects(f'./resources/sounds/pong_{random.choice((1, 2, 3, 4, 5))}.mp3', 1.0)
            ball_speed_x *= -1
        if abs(ball.bottom - player_two.top) < 10 and ball_speed_y > 0:
            play_sound_effects(f'./resources/sounds/pong_{random.choice((1, 2, 3, 4, 5))}.mp3', 1.0)
            ball_speed_y *= -1
        if abs(ball.top - player_two.bottom) < 10 and ball_speed_y < 0:
            play_sound_effects(f'./resources/sounds/pong_{random.choice((1, 2, 3, 4, 5))}.mp3', 1.0)
            ball_speed_y *= -1    
        
        
#Player Animations
def player_animations():
    player_one.y += player_one_speed
    player_two.y += player_two_speed

    if player_one.top <= 0:
        player_one.top = 0
        
    if player_one.bottom >= screen_height:
        player_one.bottom = screen_height

    if player_two.top <= 0:
        player_two.top = 0

    if player_two.bottom >= screen_height:
        player_two.bottom = screen_height

#Ball sound effects
def play_sound_effects(file, volume):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

#Ball reset when hit on left/right sides
def ball_reset():
    global ball_speed_y, ball_speed_x, score_time
    
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        seconds_3 = game_font.render("3", False, light_gray)
        screen.blit(seconds_3, (screen_width/2 - 10, screen_height/2 + 20))
    
    if 700 < current_time - score_time < 1400:
        seconds_2 = game_font.render("2", False, light_gray)
        screen.blit(seconds_2, (screen_width/2 - 10, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        seconds_1 = game_font.render("1", False, light_gray)
        screen.blit(seconds_1, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None
    
    #pygame.time.wait(1500)
    

#General setup
pygame.mixer.init()
pygame.mixer.pre_init()
pygame.init()

clock = pygame.time.Clock()


#Setting up the main window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PyPong')


#Game Rectangles, Global variables
ball = pygame.Rect(screen_width/2 -15, screen_height/2 - 20, 30 ,30)
player_one = pygame.Rect(10, screen_height/2 - 70, 10, 140)
player_two = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
bg_color = pygame.Color(1, 20, 0)
light_gray = (200, 200, 200)
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_one_speed = 0
player_two_speed = 0

#Player scores
playerOne_score = 0
playerTwo_score = 0

#Game font
game_font = pygame.font.Font('./resources/fonts/04B_19__.TTF', 40)

#Score timer
score_time = True

while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        #Player 1 Movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_one_speed += 7
            if event.key == pygame.K_w:
                player_one_speed -= 7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_one_speed -= 7
            if event.key == pygame.K_w:
                player_one_speed += 7
        

        #Player 2 Movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_two_speed += 7
            if event.key == pygame.K_UP:
                player_two_speed -= 7
        
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_two_speed -= 7
            if event.key == pygame.K_UP:
                player_two_speed += 7
    
    ball_animations()
    player_animations()
    
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect( screen, light_gray, player_two)
    pygame.draw.rect( screen, light_gray, player_one)
    pygame.draw.rect(screen, light_gray, ball)
    pygame.draw.aaline(screen, light_gray, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_reset()

    playerOne_text = game_font.render(f'{playerOne_score}', False, light_gray)
    playerTwo_text = game_font.render(f'{playerTwo_score}', False, light_gray)
    screen.blit(playerOne_text, (600, 40))
    screen.blit(playerTwo_text, (660, 40))

    #Updating the window
    pygame.display.flip()
    clock.tick(60)