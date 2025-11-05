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
DROP_SPAWN_TIME = 1200  # tempo tra le ondate di gusci (ms)
MAX_VITE = 3

# --- Colori ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- Setup finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salva la Principessa - Lezione 3")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32, bold=True)

# --- Caricamento immagini ---
mario_img = pygame.image.load("mario.png").convert_alpha()
background = pygame.image.load("sfondo.png").convert()
block_img = pygame.image.load("blocco.png").convert_alpha()
guscio_img = pygame.image.load("guscio.png").convert_alpha()
cuore_img = pygame.image.load("fungo.png").convert_alpha()

# --- Ridimensionamento immagini ---
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mario_img = pygame.transform.scale(mario_img, (60, 60))
guscio_img = pygame.transform.scale(guscio_img, (40, 40))
block_img = pygame.transform.scale(block_img, (150, 40))
cuore_img = pygame.transform.scale(cuore_img, (32, 32))

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

# --- Funzione per disegnare le vite ---
def draw_vite(vite):
    x_offset = 20
    y_offset = 20
    for i in range(MAX_VITE):
        heart_x = x_offset + i * 40
        if i < vite:
            screen.blit(cuore_img, (heart_x, y_offset))
        else:
            cuore_grigio = cuore_img.copy()
            cuore_grigio.fill((120, 120, 120, 255), None, pygame.BLEND_RGBA_MULT)
            screen.blit(cuore_grigio, (heart_x, y_offset))

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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False

# --- Ciclo principale ---
running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimento orizzontale
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
    for drop in drops[:]:
        drop["y"] += drop["speed"]
        if drop["y"] > HEIGHT:
            drops.remove(drop)
        else:
            drop_rect = pygame.Rect(drop["x"], drop["y"], 40, 40)
            if drop_rect.colliderect(player):
                vite -= 1
                drops.remove(drop)
                if vite <= 0:
                    game_over_screen()
                    vite = MAX_VITE
                    drops.clear()
                    player.x, player.y = 50, HEIGHT - 150

    # Disegno
    screen.blit(background, (0, 0))
    for platform in platforms:
        screen.blit(block_img, (platform.x, platform.y))
    screen.blit(mario_img, (player.x, player.y))
    for drop in drops:
        screen.blit(guscio_img, (drop["x"], drop["y"]))
    draw_vite(vite)

    pygame.display.flip()

pygame.quit()
sys.exit()
