#!/usr/bin/env python3
# importation et initialisation du module "pygame"
import pygame
import math
from game import Game
pygame.init()

# définir une clock (pour gestion des fps)
clock = pygame.time.Clock()
FPS = 60


############################ générer la fenêtre ############################
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))


########################### importer les élements ##########################

# fond d'écran
background = pygame.image.load('PygameAssets-main/bg.jpg')

# écran d'acceuil
# bannière d'acceuil
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
# bouton pour lancer la partie
play_button = pygame.image.load('PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#### pour quand la partie commence ############
# le jeux
game = Game()


#######################################################################
################### boucle de jeux ####################################
#######################################################################
# variable pour maintenir la fenêtre ouverte
running = True

while running:
    
    ############ Création des images  ############

    # créer l'image sur la surface enregistrer dans screen 
    # avec coordonnées (x, y) depuis top/left
    screen.blit(background, (0, -200))

    ################ vérifier si jeux à commencer ###########
    # si c'est le cas, intégrer les instructions contenues dans "game.update" à cet endroit de la boucle
    if game.is_playing:
        # déclencher la partie
        game.update(screen)

    # arriver sur écran d'acceuil
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    ################## mettre l'écran à jour #########################
    pygame.display.flip()

    # gestion des évenements
    for event in pygame.event.get():
        # fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeux")
        
        # détecter les commandes claviers
        # renvoie au dictionnaire dans "game.py" pour enregistrer les entrées

        # quand touche enfoncée
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        
            # détecter touche SPACE pour projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # lancer le jeux
                    game.start()
                    # jouer le click
                    game.sound_manager.play('click')

        # quand touche relachée
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # checker si cliquer sur le bouton "play_button"
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeux
                game.start()
                # jouer le click
                game.sound_manager.play('click')
    
    # fixer le nomnbre de FPS sur la clock 
    clock.tick(FPS)
