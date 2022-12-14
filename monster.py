import pygame
import random
import animation

class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
        self.loot_amount = 10

    # vitesse de chaque entité
    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    # score quand tué
    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # infliger des dégats
        self.health -= amount

        # vérifier si mort health <= 0
        if self.health <= 0:
            # réaparaitre comme nv monstre (pour éviter de surcharger ram avec nv monstres)
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(2, self.default_speed)
            self.health = self.max_health

            # augmenter le score
            self.game.add_score(self.loot_amount)

            # checker si barre des comettes est chargée
            if self.game.commet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

                # appel de attempt_fall
                self.game.commet_event.attempt_fall()

    def update_health_bar(self, surface):        
        # dessiner back (mettre bg avant car sinon, recouvre la barre de vie!!)
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        # dessiner la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def update_animation(self):
        self.animate(loop=True)


    def forward(self):
        # checker si pas de collision avec groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

        # infliger dégats
        else:
            self.game.player.damage(self.attack)


# définir classe pour la momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(5)
        self.set_loot_amount(10)


# définir classe pour l'aliène
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.set_speed(3)
        self.attack = 0.8
        self.set_loot_amount(25)
