
import pygame
import sys

# --- Inizializzazione ---
pygame.init()

# --- Costanti ---
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.8
JUMP_POWER = 20
SPEED = 5
BOUNCE_POWER = 10

# --- Colori ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

# --- Finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salva la Principessa - Lezione 2")
clock = pygame.time.Clock()

# --- Caricamento immagini ---
background = pygame.image.load("sfondo.png").convert()

# --- Ridimensionamento ---
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# --- Giocatore ---
player = pygame.Rect(50, HEIGHT - 150, 60, 60)
vel_y = 0
on_ground = False

# --- Ciclo principale ---
running = True
while running:
    dt = clock.tick(FPS)

    # --- Eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Input tastiera ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= SPEED
        if player.left < 0:
            player.left = 0
    if keys[pygame.K_RIGHT]:
        player.x += SPEED
        if player.right > WIDTH:
            player.right = WIDTH
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = -JUMP_POWER
        on_ground = False

    # --- Gravità ---
    vel_y += GRAVITY
    player.y += int(vel_y)

    # --- Collisioni con piattaforme ---
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            # Se stiamo cadendo e tocchiamo la piattaforma
            if vel_y > 0 and player.bottom - vel_y <= platform.top:
                player.bottom = platform.top
                vel_y = 0
                on_ground = True
            # Se stiamo salendo e colpiamo sotto
            elif vel_y < 0 and player.top - vel_y >= platform.bottom:
                player.top = platform.bottom
                vel_y = BOUNCE_POWER

    # --- Pavimento ---
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
        vel_y = 0
        on_ground = True

    # --- Disegno ---
    screen.blit(background, (0, 0))
    draw_platforms()
    screen.blit(mario_img, (player.x, player.y))

    pygame.display.flip()

pygame.quit()
sys.exit()
