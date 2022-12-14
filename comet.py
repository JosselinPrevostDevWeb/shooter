import pygame
import random
from monster import Mummy
from monster import Alien
import math

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(4, 9)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # checker si nbs de comettes = 0 et reset les monstres
        if len(self.comet_event.all_comets) == 0:
            print("évenement fini")
            self.comet_event.reset_percent()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # checker collisions avec le sol
        if self.rect.y >= 500:
            print("sol")
            self.remove()

            # checker si il y a encore des boules de feux
            if len(self.comet_event.all_comets) == 0:
                print("plui est finie")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # checker si touche joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur touché !")
            self.remove()
            self.comet_event.game.player.damage(20)
            