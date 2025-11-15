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

# Carica lo sfondo, Mario e i blocchi
background = pygame.image.load("C:/Users/Asus/downloads/sfondo.png").convert()
mario_img = pygame.image.load("C:/Users/Asus/downloads/mario.png").convert_alpha()
block_img = pygame.image.load("C:/Users/Asus/downloads/blocco.png").convert_alpha()

# --- Ridimensionamento ---
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mario_img = pygame.transform.scale(mario_img, (60, 60))
block_width, block_height = 150, 40
block_img = pygame.transform.scale(block_img, (block_width, block_height))

# --- Piattaforme ---
platforms = [
    pygame.Rect(100, 480, block_width, block_height),
    pygame.Rect(300, 370, block_width, block_height),
    pygame.Rect(500, 260, block_width, block_height),
    pygame.Rect(650, 150, block_width, block_height),
]

# --- Funzione per disegnare piattaforme ---
def draw_platforms():
    for platform in platforms:
        screen.blit(block_img, (platform.x, platform.y))
        
# --- Giocatore ---
player = pygame.Rect(40, HEIGHT - 90, 60, 60)
vel_y = 0
on_ground = False

# Clock per controllare il framerate
clock = pygame.time.Clock()

# Ciclo principale
running = True
# TODO: ciclo while per far si che se il giocatore vuole chiudere la finestra il gioco termini

    # Disegna lo sfondo
    screen.blit(background, (0, 0))

    # Aggiorna lo schermo
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
