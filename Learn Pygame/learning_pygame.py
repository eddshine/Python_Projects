import pygame, random
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sfx = pygame.mixer.Sound('./audio/jump.mp3')
        self.jump_sfx.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sfx.play()
            

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0

            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            fly_frame_1 = pygame.image.load('./graphics/fly/fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('./graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900, 1100), y_pos))
    
    def obstacle_animation(self):
       self.animation_index += 0.1
       if self.animation_index >= len(self.frames):
            self.animation_index = 0
       self.image = self.frames[int(self.animation_index)]
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    
    def update(self):
        self.obstacle_animation()
        self.rect.x -= 6
        self.destroy()

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: 
        return True

def display_score():
    time = int(pygame.time.get_ticks() / 1000) - def_time
    score_surface = game_font.render(f'{time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            screen.blit(snail_surface if obstacle_rect.bottom == 300 else fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0

        print(player_index)
        player_surf = player_walk[int(player_index)]
            
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Guard!, May baliw dito!!!')
clock = pygame.time.Clock()
game_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
game_active = False
def_time = 0
score = display_score()
backgroundMusic = pygame.mixer.Sound('./audio/music.wav')
backgroundMusic.set_volume(0.5)
backgroundMusic.play(loops = -1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

#plain_color_surface = pygame.Surface((40, 80))
#plain_color_surface.fill('yellowgreen')

sky_surface = pygame.image.load('./graphics/Sky.png').convert()
ground_surface = pygame.image.load('./graphics/ground.png').convert()


snail_frame_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('./graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('./graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]



obstacle_rect_list = []

player_walk_1 = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surf = player_walk[player_index]
player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

#Intro Screen
player_stand = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))
player_gravity = 0

game_title = game_font.render('Oh No!.. Cringe', False, (111, 196, 169))
game_title_rect = game_title.get_rect(center = (400, 80))

game_message = game_font.render('Press SPACE to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    #FLAPPY BIRD STYLE GRAVITY
                    #player_gravity = -10
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    #print('MOUSE 1')
                    player_gravity = -20
             
            if event.type == obstacle_timer:
                #obtacle_choice = random.choice(['snail','fly'])
                obstacle_group.add(Obstacle(random.choice(['snail','fly'])))
                #obstacle_rect_list.append(random.choice([snail_surface.get_rect(bottomright = (random.randint(900, 1100), 300)),fly_surface.get_rect(bottomright = (random.randint(900, 1100), 210))]))
            #if event.type == pygame.KEYUP:
                #print('KEY UP!')

            if event.type == snail_animation_timer:
                snail_frame_index = 1 if snail_frame_index == 0 else 0
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                fly_frame_index = 1 if fly_frame_index == 0 else 0
                fly_surface = fly_frames[fly_frame_index]
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #snail_rect.left = 800
                game_active = True
                def_time = int(pygame.time.get_ticks() / 1000)
        
        
    if game_active:
        #draw all elements
        #update everything
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        #screen.blit(plain_color_surface, (((600/2) - (40/2)), ((600/2) - (80/2))))
    
            
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
        #pygame.draw.ellipse(screen,(2, 5, 5), pygame.Rect(50, 200, 100, 100))

        
        #screen.blit(score_surface, score_rect)
        
        # snail_rect.x += -5
        # if snail_rect.right  < -60: snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
        #    print('Jump')

            
        

        #PLAYER
        #FLAPPY BIRD STYLE GRAVITY
        #player_gravity += 0.5
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300: player_rect.bottom = 300
        
        #player_animation()
        #screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        #collision_sprite()
        # Obstacle Movements
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
            #if pygame.mouse.get_pressed() == (True, False, False):
                #print('MOUSE 1')
                #player_gravity = -20
            #elif pygame.mouse.get_pressed() == (False, True, False):
                #print('MOUSE 2')
            #elif pygame.mouse.get_pressed() == (False, False, True):
                #print('MOUSE 3')
            
        # collision
        #if snail_rect.colliderect(player_rect):
            #game_active = False
        #game_active = collisions(player_rect, obstacle_rect_list)
        game_active = collision_sprite()
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title, game_title_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        score_message = game_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 320))
        
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.update()
    clock.tick(60)