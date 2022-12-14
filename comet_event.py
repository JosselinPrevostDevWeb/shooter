import pygame
from comet import Comet

# créer la classe pour gérer ces évenements
class CometFallEvent:
    # créer un compteur pour le % de la barre
    def __init__(self, game):
        self.game = game
        self.percent = 0
        self.percent_speed = 33
        self.fall_mode = False

        # définir group de sprite pour stocker les commettes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 200

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(5, 15):
            # apparition des commettes
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # action quand la barre est chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print ("plui de commet")
            self.meteor_fall()
            self.fall_mode = True # activer l'évenement

    def update_bar(self, surface):
        # chargement de la barre
        self.add_percent()




        # background de la barre
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        # fg de la barre (dynamique)
        pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])