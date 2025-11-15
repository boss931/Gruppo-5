import pygame
import sys
import random

pygame.init()

# --- Costanti ---
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.8
JUMP_POWER = 20
SPEED = 5
DROP_SPEED_MIN = 3
DROP_SPEED_MAX = 6
DROP_SPAWN_TIME = 1200
MAX_VITE = 3

# --- Colori ---
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0, 0, 0)

# --- Setup finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salva la Principessa - Lezione 3")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32, bold=True)

# --- Caricamento immagini ---
mario_img = pygame.image.load("C:/Users/Asus/downloads/mario.png").convert_alpha()
background = pygame.image.load("C:/Users/Asus/downloads/sfondo.png").convert()
block_img = pygame.image.load("C:/Users/Asus/downloads/blocco.png").convert_alpha()
# TODO: caricare l'immagine del guscio che cadrà dall'alto
# TODO: caricare l'immagine del cuore/fungo che rappresenta la vita

# --- Ridimensionamento immagini ---
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mario_img = pygame.transform.scale(mario_img, (60, 60))
block_img = pygame.transform.scale(block_img, (150, 40))
# TODO: ridimensionare l'immagine del guscio (40,40)
# TODO: ridimensionare l'immagine del cuore (32,32)

# --- Giocatore ---
player = pygame.Rect(50, HEIGHT - 150, 60, 60)
vel_y = 0
on_ground = False
vite = MAX_VITE

# --- Piattaforme ---
platforms = [
    pygame.Rect(100, 480, 150, 40),
    pygame.Rect(300, 370, 150, 40),
    pygame.Rect(500, 260, 150, 40),
    pygame.Rect(650, 150, 150, 40),
]

# --- Gusci cadenti ---
drops = []
last_drop_time = pygame.time.get_ticks()


# --- Funzione per disegnare le vite in alto a sinistra ---
def draw_vite(vite):
    # TODO: disegnare le vite (cuori colorati) finché vite > 0
    # TODO: se la vita è finita, disegnare la versione grigia
    pass


# --- Funzione Game Over ---
def game_over_screen():
    screen.fill(BLACK)
    message = font.render("Hai perso! Premi R per riprovare.", True, WHITE)
    screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # TODO: uscire da questa schermata quando il giocatore preme R
            pass


# --- Ciclo principale ---
running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimento orizzontale (Lezione 2)
    if keys[pygame.K_LEFT]:
        player.x -= SPEED
        if player.left < 0:
            player.left = 0
    if keys[pygame.K_RIGHT]:
        player.x += SPEED
        if player.right > WIDTH:
            player.right = WIDTH

    # Salto 
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = -JUMP_POWER
        on_ground = False

    # Gravità
    vel_y += GRAVITY
    player.y += int(vel_y)

    # Collisioni piattaforme
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if vel_y > 0 and player.bottom - vel_y <= platform.top:
                player.bottom = platform.top
                vel_y = 0
                on_ground = True
            elif vel_y < 0 and player.top - vel_y >= platform.bottom:
                player.top = platform.bottom
                vel_y = 0

    # Pavimento
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
        vel_y = 0
        on_ground = True

    # Generazione gusci
    now = pygame.time.get_ticks()
    if now - last_drop_time >= DROP_SPAWN_TIME:
      x_pos = random.randint(0, WIDTH - 40)
      speed = random.randint(DROP_SPEED_MIN, DROP_SPEED_MAX)
      drops.append({"x": x_pos, "y": -40, "speed": speed})
      last_drop_time = now

    # Aggiornamento gusci
    # TODO: aggiornare la posizione dei gusci (caduta)
    # TODO: se un guscio colpisce il giocatore -> togli una vita
    # TODO: se le vite finiscono -> chiamare game_over_screen()
    pass

    # --- Disegno ---
    screen.blit(background, (0, 0))
    for platform in platforms:
        screen.blit(block_img, (platform.x, platform.y))
    screen.blit(mario_img, (player.x, player.y))
    for drop in drops:
        # TODO: mostrare a schermo un oggetto (il guscio) nella sua posizione
    # TODO: aggiorna la grafica delle vite del giocatore

    pygame.display.flip()

  pygame.quit()
  sys.exit()

    pygame.display.flip()

pygame.quit()
sys.exit()
