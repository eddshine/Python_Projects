import pygame
import sys
from player import Player
import obstacles
from alien_obstacle import Alien, ExtraAlien
from random import choice, randint
from laser import Laser


class Game:
    def __init__(self):
        # Player setup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Health and Score setup
        self.lives = 3
        self.lives_surface = pygame.image.load('resources/images/live_1.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.lives_surface.get_size()[0] * 2 + 20)
        self.score = 0
        self.score_font = pygame.font.Font('resources/fonts/Pixeled.ttf', 20)

        # Obstacle setup
        self.shape = obstacles.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_position = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.obstacle_generator(self.obstacle_x_position, x_start=(screen_width / 15), y_start=480)

        # Alien obstacle setup
        self.aliens = pygame.sprite.Group()
        self.aliens_laser = pygame.sprite.Group()
        self.alien_setup(6, 8)
        self.alien_direction = 1

        # Extra alien setup
        self.extra_alien = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(40, 80)

        # Music(SFX) setup
        self.music_bg_sfx = pygame.mixer.Sound('resources/sfx/music.wav')
        self.music_bg_sfx.set_volume(0.2)
        self.music_bg_sfx.play(loops=-1)
        self.laser_sfx = pygame.mixer.Sound('resources/sfx/laser.wav')
        self.laser_sfx.set_volume(0.4)
        self.explosion_sfx = pygame.mixer.Sound('resources/sfx/explosion.wav')
        self.explosion_sfx.set_volume(0.4)
        self.player_hit_sfx = pygame.mixer.Sound('resources/sfx/player_hit.wav')
        self.player_hit_sfx.set_volume(1)

        obstacle_hit_volume = 0.8
        self.obstacle_hit_1_sfx = pygame.mixer.Sound('resources/sfx/obstacle_hit_1.wav')
        self.obstacle_hit_1_sfx.set_volume(obstacle_hit_volume)
        self.obstacle_hit_2_sfx = pygame.mixer.Sound('resources/sfx/obstacle_hit_2.wav')
        self.obstacle_hit_2_sfx.set_volume(obstacle_hit_volume)
        self.obstacle_hit_3_sfx = pygame.mixer.Sound('resources/sfx/obstacle_hit_3.wav')
        self.obstacle_hit_3_sfx.set_volume(obstacle_hit_volume)

        self.obstacle_hit_sfx_generator = choice([self.obstacle_hit_1_sfx, self.obstacle_hit_2_sfx, self.obstacle_hit_3_sfx])

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacles.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def obstacle_generator(self, offset, x_start, y_start):
        for x in offset:
            self.create_obstacle(x_start, y_start, x)

    def alien_setup(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):

                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
            self.aliens_laser.add(laser_sprite)
            self.laser_sfx.play()

    def alien_pos_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_downward_movement(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_downward_movement(2)

    def alien_downward_movement(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra_alien.add(ExtraAlien(choice(['right', 'left']), screen_width))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):

        # Player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # Obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    self.obstacle_hit_sfx_generator.play()
                    laser.kill()

                # Alien collision
                alien_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                if alien_hit:
                    for alien in alien_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sfx.play()

                # Extra collision
                if pygame.sprite.spritecollide(laser, self.extra_alien, True):
                    self.score += 500
                    laser.kill()

        # Alien laser
        if self.aliens_laser:
            for laser in self.aliens_laser:

                # Obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    self.obstacle_hit_sfx_generator.play()
                    laser.kill()

                # Player collision
                if pygame.sprite.spritecollide(laser, self.player, False):
                    self.player_hit_sfx.play()
                    laser.kill()
                    self.lives -= 1

                    if self.lives == 3:
                        self.lives_surface = pygame.image.load('resources/images/live_1.png').convert_alpha()
                    elif self.lives == 2:
                        self.lives_surface = pygame.image.load('resources/images/live_2.png').convert_alpha()
                    elif self.lives == 1:
                        self.lives_surface = pygame.image.load('resources/images/live_3.png').convert_alpha()
                    else:
                        pygame.quit()
                        sys.exit()

        # Aliens, Obstacle collision
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)
                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for lives in range(self.lives):
            x = self.live_x_start_pos + (self.lives_surface.get_size()[0] + 10)
            screen.blit(self.lives_surface, (x, 8))

    def display_score(self):
        score_surface = self.score_font.render(f'Score: {self.score}', False, 'white')
        score_rect = score_surface.get_rect(topleft=(10, -10))
        screen.blit(score_surface, score_rect)

    def run(self):
        self.player.update()
        self.aliens_laser.update()
        self.extra_alien.update()

        self.aliens.update(self.alien_direction)
        self.alien_pos_checker()
        self.extra_alien_timer()
        self.collision_checks()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.aliens_laser.draw(screen)
        self.extra_alien.draw(screen)
        self.display_lives()
        self.display_score()


class CRT:
    def __init__(self):
        self.crt_effect = pygame.image.load('resources/images/tv.png')
        self.crt_effect = pygame.transform.scale(self.crt_effect, (screen_width, screen_height))

    def create_crt_lines(self):
        lines_height = 3
        line_amount = (screen_height / lines_height)

        for line in range(int(line_amount)):
            y_pos = line * lines_height
            pygame.draw.line(self.crt_effect, 'black', (0, y_pos), (screen_width, y_pos), 1)

    def draw(self):
        self.crt_effect.set_alpha(95)
        self.create_crt_lines()
        screen.blit(self.crt_effect, (0, 0))


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    pygame.display.set_caption('Space Invader')
    game_icon = pygame.image.load('resources/images/favicon.png')
    pygame.display.set_icon(game_icon)
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()
    crt_effect = CRT()

    alien_laser_cooldown = pygame.USEREVENT + 1
    pygame.time.set_timer(alien_laser_cooldown, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == alien_laser_cooldown:
                game.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()
        crt_effect.draw()
        pygame.display.flip()
        clock.tick(60)
