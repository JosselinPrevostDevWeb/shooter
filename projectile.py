import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width -50
        self.rect.y = player.rect.y + (player.rect.height / 3)
        self.origin_image = self.image
        self.angle = 0

    # faire tourner projectile en déplacement
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    # fonction pour supprimer les projectiles
    def remove(self):
        self.player.all_projectiles.remove(self)

    # fonction de déplacement du projectile
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # checker collision avec monstres
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            # infliger dégats
            monster.damage(self.player.attack)

        # détruire les projectiles hors de l'écran
        if self.rect.x > 1080:
            self.remove()