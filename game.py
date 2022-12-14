import pygame
from player import Player
from monster import Mummy
from monster import Alien
from sounds import SoundManager
from comet_event import CometFallEvent

# Création de la classe "Game" qui sera la classe contenant les autres

# classe pour rpz le jeux entier
class Game:
    def __init__(self):
        # définir si le jeux à commencer
        self.is_playing = False
        # autres élements
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.commet_event = CometFallEvent(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        # gérer le son
        self.sound_manager = SoundManager()
        # initialiser un score à 0
        self.score = 0
        # pour utiliser une police du système
        # self.font = pygame.font.SysFont("monospace", 16)
        # pour utiliser un police perso (il faut la dl et mettre le .ttf dans le dossier)
        self.font = pygame.font.Font("PygameAssets-main/PottaOne-Regular.ttf", 25)

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # reset le jeux quand game over
        self.all_monsters = pygame.sprite.Group()
        self.commet_event.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.commet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')

    ## Déportation du contenu de la boucle de jeux
    def update(self, screen):

        # afficher le score de la dernière partie
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        ############# le joueur ##########################
        # le joueur (sera positionner par rapport aux coordonées de "player.rect")
        screen.blit(self.player.image, self.player.rect)
        # barre de vie du joueur
        self.player.update_health_bar(screen)
        # update de l'animation
        self.player.update_animation()

        # barre d'évenement du jeux
        self.commet_event.update_bar(screen)

        ########## Projectiles ########################
        # récupérer les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # appliquer l'ensemble des images du groupe "Projectile"
        self.player.all_projectiles.draw(screen)

        ############## Monstres ###########################
        # récupérer les monstrer
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
        # déssiner les monstres
        self.all_monsters.draw(screen)

        ########### Commettes ##########################
        # récup les commettes
        for comet in self.commet_event.all_comets:
            comet.fall()
        # déssiner les comettes
        self.commet_event.all_comets.draw(screen)



        
        # voir ou le joueur souhaite se déplacer
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


 

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)