import pygame
import sys

# Inizializzazione di Pygame
pygame.init()

# Costanti
#TODO: disegna lo schermo con larghezza(WIDTH) = 800 e altezza(HEIGHT) = 600
#TODO: disegna il titolo del gioco con GAME_TITLE = ...

# Creazione finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Carica lo sfondo
background = pygame.image.load("sfondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Clock per controllare il framerate
clock = pygame.time.Clock()

# Ciclo principale
running = True
# TODO: ciclo while per far si che se il giocatore clicca X il gioco termini

    # Disegna lo sfondo
    screen.blit(background, (0, 0))

    # Aggiorna lo schermo
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
