#This file was created by: Ivan Verduzco
'''
Gsmr designs truths:
goals, rules, feedback, what the verb, and will it form a sentence

health bar, kill enemies, morving enemies

'''
# import libraries and 
import pygame as pg
from settings import *
from sprites import *
from random import randint
import sys
from os import path

# 2 underscores _ before and after init


# define game class
class Game:
    # create init funtion
    def __init__(self):
        # Initialize Pygame
        pg.init()
        # Set Pygame window name and size
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        # get pygame clock and start running pygame
        self.clock = pg.time.Clock()
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
# Create run method which runs the whole GAME

    def new(self):
        print("create new game...")
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.Coins = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        # self.player1 = Player(self, 1, 1)
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'B':
                    Mob(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)

    
     #funtion to call while running
    def run(self):
        # create while loop that triggers when running = true
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

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    def events(self):
        for event in pg.sevent.get():
            if event.type == pg.QUIT:
                self.quit()
#            if event.type == pg.KEYDOWN:
#                if event.key == pg.K_LEFT:
#                    self.player.move(dx=-1)
#                if event.key == pg.K_RIGHT:
#                    self.player.move(dx=1)
#                if event.key == pg.K_UP:
#                    self.player.move(dy=-1)
#                if event.key == pg.K_DOWN:
#                    self.player.move(dy=1)
# Instantiate the game...
g = Game()
# use game method run to run the game
#g.show_start_screen()
while True:
    g.new()
    g.run()
    #g.show_start_screen()