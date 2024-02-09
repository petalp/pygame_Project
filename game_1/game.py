import pygame
import sys

from script.entities import PhysicsEntity
from script.utilities import load_image,load_images
from script.tilemap import Tilemap

class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption('ninja game')
        self.screen_size = pygame.display.set_mode((1700, 900))
        self.display = pygame.Surface((850, 450))
        self.clock = pygame.time.Clock()

        self.assests = {
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player' : load_image('entities/player.png')
        }
        self.movement = [False, False]


        #player
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.tilemap = Tilemap(self, tile_size=16)
        
        
        
        
    def run(self):
        while True:
            self.display.fill((14, 219, 248))
            self.tilemap.render(self.display)
            self.player.render(self.display)

            print(self.tilemap.tile_around(self.player.pos))

            self.player.update(movement=(self.movement[1] - self.movement[0], 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen_size.blit(pygame.transform.scale(self.display,self.screen_size.get_size()),  (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()