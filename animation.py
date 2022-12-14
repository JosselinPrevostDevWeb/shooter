import pygame

# class d'animation
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load('PygameAssets-main/' + sprite_name + '.png')
        # ou  -> self.image = pygame.image.load(f'PygameAssets-main/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        # pour commencer à l'image 0
        self.current_image = 0
        self.images = animations.get(sprite_name)
        # pour différencier animations en boucles vs ponctuelles
        self.animation = False

    # définir méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True
    
    
    # déf une méthode pour animer le sprite
    def animate(self, loop=False):

        # checker si l'animation est déclencher
        if self.animation:

            # passer à l'image suivante
            self.current_image += 1

            # vérifier si on a atteint la dernière img
            if self.current_image >= len(self.images):
                # reset l'animation
                self.current_image = 0

                # l'animation est elle en loop?
                if not loop:
                    # désactiver l'animation
                    self.animation = False

            # modidier l'image par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# définir une fonction pour charger les images d'un sprite
# c'est pour ne charger qu'une image à la fois sinon, ça surcharge la ram!!
def load_animation_images(sprite_name):
    # charger les 24 imgs
    images = []
    # récupérer le chemin du dossier
    path = f"PygameAssets-main/{sprite_name}/{sprite_name}"
    # boucler sur chaque image
    for num in range (1, 24):
        image_path = path + str(num) + '.png' 
        # les ajouter dans la liste "images = []"      
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu
    return images

# définir un dictionnaire pour contenir les images chargé de chaque sprite (pour les garder en mémoires)
animations = {
    "mummy": load_animation_images("mummy"),
    "alien": load_animation_images("alien"),
    "player": load_animation_images("player")
}