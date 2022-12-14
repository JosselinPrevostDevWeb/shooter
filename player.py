import pygame
from projectile import Projectile
import animation

# création de la classe "Player"
# (un "sprite" est un élement mobile du jeux)
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500  

    def update_animation(self):
        self.animate()

    def damage(self, amount):
        if self.health - amount >= 0:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):        
        # paramètres = surface où dessiner, code rgb, [x, y, largeur, épaisseur]
        # dessiner back (mettre bg avant car sinon, recouvre la barre de vie!!)
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 50, self.rect.y, self.max_health, 7])
        # dessiner la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y, self.health, 7])



    def launch_projectile(self):
        # créer une instance de la classe "Projectile"
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        # checker si joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def  move_left(self):
        self.rect.x -= self.velocity