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
BOUNCE_POWER = 10
DROP_SPEED_MIN = 3
DROP_SPEED_MAX = 6
DROP_SPAWN_TIME = 1200
DROPS_PER_WAVE_MIN = 1
DROPS_PER_WAVE_MAX = 2
MAX_VITE = 3

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)

# --- Setup finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump to Win - Mario vs Bear")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 72)
font_small = pygame.font.SysFont("arial", 32, bold=True)

# --- Caricamento immagini ---
mario_img = pygame.image.load("mario.png").convert_alpha()
peach_img = pygame.image.load("peach.png").convert_alpha()
orso_img = pygame.image.load("orso.png").convert_alpha()
background = pygame.image.load("sfondo.png").convert()
block_img = pygame.image.load("blocco.png").convert_alpha()
guscio_img = pygame.image.load("guscio.png").convert_alpha()
cuore_img = pygame.image.load("fungo.png").convert_alpha()

# --- Ridimensionamento immagini ---
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mario_img = pygame.transform.scale(mario_img, (60, 60))
peach_img = pygame.transform.scale(peach_img, (70, 100))
orso_img = pygame.transform.scale(orso_img, (100, 100))
guscio_img = pygame.transform.scale(guscio_img, (40, 40))
block_width, block_height = 150, 40
block_img = pygame.transform.scale(block_img, (block_width, block_height))
cuore_img = pygame.transform.scale(cuore_img, (32, 32))

# --- Giocatore ---
player = pygame.Rect(50, HEIGHT - 150, 60, 60)
vel_y = 0
on_ground = False
vite = MAX_VITE

# --- Piattaforme ---
platforms = [
    pygame.Rect(100, 480, block_width, block_height),
    pygame.Rect(300, 370, block_width, block_height),
    pygame.Rect(500, 260, block_width, block_height),
    pygame.Rect(650, 150, block_width, block_height),
]

# --- Obiettivo (Peach e Orso) ---
goal = pygame.Rect(730, 50, 70, 100)
orso_rect = pygame.Rect(goal.x - 90, goal.y + 10, 100, 100)

# --- Gusci cadenti ---
drops = []
last_drop_time = pygame.time.get_ticks()

# --- Funzioni UI ---
def draw_button(rect, text, color, text_color):
    pygame.draw.rect(screen, color, rect, border_radius=15)
    pygame.draw.rect(screen, BLACK, rect, 3, border_radius=15)
    label = font_small.render(text, True, text_color)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

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

def show_message(text, color):
    """Mostra un messaggio centrato con rettangolo adattivo e testo elegante"""
    message = font.render(text, True, color)
    text_rect = message.get_rect()

    # Rettangolo dinamico basato sulla dimensione del testo
    padding_x, padding_y = 60, 40
    box_width = text_rect.width + padding_x
    box_height = text_rect.height + padding_y
    box_rect = pygame.Rect(
        (WIDTH - box_width) // 2,
        (HEIGHT - box_height) // 2,
        box_width,
        box_height
    )

    # Sfondo semitrasparente dietro il messaggio
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(150)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    # Disegno rettangolo con bordi arrotondati
    pygame.draw.rect(screen, (245, 245, 245), box_rect, border_radius=25)
    pygame.draw.rect(screen, BLACK, box_rect, 4, border_radius=25)

    # Ombra leggera sotto il testo
    shadow = font.render(text, True, (100, 100, 100))
    shadow_rect = shadow.get_rect(center=(box_rect.centerx + 2, box_rect.centery + 2))
    screen.blit(shadow, shadow_rect)

    # Testo principale
    screen.blit(message, message.get_rect(center=box_rect.center))

    pygame.display.flip()
    pygame.time.wait(3000)

def main_menu():
    """Mostra la schermata iniziale"""
    while True:
        screen.blit(background, (0, 0))
        title = font.render("Jump to Win", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))

        play_button = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 - 40, 240, 80)
        draw_button(play_button, "GIOCA", GREEN, WHITE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def victory_screen():
    screen.blit(background, (0, 0))
    show_message("Hai salvato la principessa!", GREEN)

def game_over_screen():
    screen.blit(background, (0, 0))
    show_message("Non hai salvato la principessa!", RED)

# --- Funzione principale del gioco ---
def game_loop():
    global vite, vel_y, on_ground, drops, last_drop_time
    vite = MAX_VITE
    player.x, player.y = 50, HEIGHT - 150
    vel_y = 0
    on_ground = False
    drops = []
    last_drop_time = pygame.time.get_ticks()

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

        # Collisioni
        on_ground = False
        for platform in platforms:
            if player.colliderect(platform):
                if vel_y > 0 and player.bottom - vel_y <= platform.top:
                    player.bottom = platform.top
                    vel_y = 0
                    on_ground = True
                elif vel_y < 0 and player.top - vel_y >= platform.bottom:
                    player.top = platform.bottom
                    vel_y = BOUNCE_POWER

        # Pavimento
        if player.bottom >= HEIGHT:
            player.bottom = HEIGHT
            vel_y = 0
            on_ground = True

        # Vittoria
        if player.colliderect(goal):
            victory_screen()
            return

        # Gusci
        now = pygame.time.get_ticks()
        if now - last_drop_time >= DROP_SPAWN_TIME:
            num_drops = random.randint(DROPS_PER_WAVE_MIN, DROPS_PER_WAVE_MAX)
            for _ in range(num_drops):
                x_pos = random.randint(0, WIDTH - 40)
                drops.append({"x": x_pos, "y": -40, "speed": random.randint(DROP_SPEED_MIN, DROP_SPEED_MAX)})
            last_drop_time = now

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
                        return
                    else:
                        player.x, player.y = 50, HEIGHT - 150
                        vel_y = 0

        # Disegno
        screen.blit(background, (0, 0))
        for platform in platforms:
            screen.blit(block_img, (platform.x, platform.y))
        screen.blit(orso_img, (orso_rect.x, orso_rect.y))
        screen.blit(peach_img, (goal.x, goal.y))
        screen.blit(mario_img, (player.x, player.y))
        for drop in drops:
            screen.blit(guscio_img, (drop["x"], drop["y"]))
        draw_vite(vite)

        pygame.display.flip()

# --- Loop generale ---
while True:
    main_menu()
    game_loop()
