#This file was created by: Ivan Verduzco
'''
Gsmr designs truths:
goals, rules, feedback, what the verb, and will it form a sentence

health bar,  morving enemies, speed boost


'''
# import libraries and 
import pygame as pg
from settings import *
from sprites import *
from random import randint
import sys
from os import path

# 2 underscores _ before and after init
#added health bar by adding draw to display the bar 
#Defined the length and height of the bar
#fill the bar and 
def draw_health_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(surf, GREEN, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.powerups = pg.sprite.Group()  # Add a group for power-ups
        self.mobs = pg.sprite.Group()

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)  # Make sure this group is correctly referenced
                if tile == 'M':
                    Mob(self, col, row)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.mobs, False)
        for hit in hits:
            self.player.health -= 34
            if self.player.health <= 0:
                self.playing = False
        if self.player.moneybag >= 8:
            self.show_end_screen()
            self.playing = False

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        draw_health_bar(self.screen, 5, 5, 100)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.screen, "This is the start screen - press any key to play", 24, WHITE, WIDTH / 2, HEIGHT / 2)
        pg.display.flip()
        self.wait_for_key()

    def show_end_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.screen, "Good Job! You finsihed", 48, WHITE, WIDTH / 2, HEIGHT / 2)
        pg.display.flip()
        pg.time.wait(2000)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

# Instantiate the game...
g = Game()
# use game method run to run
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_start_screen()