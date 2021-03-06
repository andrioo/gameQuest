# KidsCanCode - Game Development with Pygame video series
# Jumpy! 
# Video link: https://www.youtube.com/watch?v=8LRI0RLKyt0
# Player movement
# © 2019 KidsCanCode LLC / All rights reserved.

# Week of march 23 - Lore
# Modularity, Github, import as, 

# pygame, sprites, and settings are imported into main.py
import pygame as pg
from pygame.sprite import Group
import random
from settings import *
from sprites import *

# defines class
class Game:
    def __init__(self):
        # initialize the game window to pop up
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # starts a new game
        self.all_sprites = Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ground = Platform(0, HEIGHT-40, WIDTH, 40)
        plat1 = Platform(200, 400, 150, 20)
        plat2 = Platform(150, 300, 150, 20)
# Added a third platform
        plat3 = Platform(10, 200, 300, 20)
# Adds a fourth platform
        plat4 = Platform(200, 100, 350, 20)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        self.all_sprites.add(plat1)
        self.platforms.add(plat1)
        self.all_sprites.add(plat2)
        self.platforms.add(plat2)
# Puts in platform 3 (the platform which I added)
        self.all_sprites.add(plat3)
        self.platforms.add(plat3)
# Puts in platform 4 into the game (the second platform I have added)
        self.all_sprites.add(plat4)
        self.platforms.add(plat4)
        # for plat in range(1,10):
        #     plat = Platform(random.randint(0, WIDTH), random.randint(0, HEIGHT), 200, 20)
        #     self.all_sprites.add(plat)
        #     self.platforms.add(plat)
        self.run()


    def run(self):
        # the game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            if self.player.rect.top > hits[0].rect.top:
                print("OUCH! I've hit the top of my head :(")
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
                self.player.hitpoints -= 10
                print(self.player.hitpoints)
            # print("Ouch!")
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top+1
            

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # the game start screen
        pass

    def show_go_screen(self):
        # game over
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
