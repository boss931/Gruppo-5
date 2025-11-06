import pygame
import sys

# Inizializzazione di Pygame
pygame.init()

# Costanti
WIDTH, HEIGHT = 800, 600
GAME_TITLE = "Salva la Principessa - Lezione 1"

# Creazione finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Carica lo sfondo
background = pygame.image.load("sfondo.png").convert()
mario_img = pygame.image.load("mario.png").convert_alpha()
block_img = pygame.image.load("blocco.png").convert_alpha()

# --- Ridimensionamento ---
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mario_img = pygame.transform.scale(mario_img, (60, 60))
block_width, block_height = 150, 40
block_img = pygame.transform.scale(block_img, (block_width, block_height))


background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Clock per controllare il framerate
clock = pygame.time.Clock()

# Ciclo principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Disegna lo sfondo
    screen.blit(background, (0, 0))

    # Aggiorna lo schermo
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
