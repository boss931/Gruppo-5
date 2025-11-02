# Lezione 3: Aggiungere i gusci cadenti e il sistema di vite

## Introduzione

Nella Lezione 2 abbiamo aggiunto Mario, la gravità e le piattaforme.  
Ora rendiamo il gioco **dinamico e impegnativo** introducendo i **gusci cadenti**, che Mario dovrà evitare per non perdere vite.  
Implementeremo anche il **sistema delle vite** e la **logica di Game Over**.

---

## Obiettivi didattici

- Creare oggetti che cadono dall’alto (gusci) con velocità casuale.  
- Rilevare le collisioni tra Mario e i gusci.  
- Gestire un contatore delle vite e mostrarlo sullo schermo.  
- Implementare la schermata di Game Over.

---

## Concetti chiave

### 1. Sprite dinamici

Finora abbiamo usato sprite statici (piattaforme).  
Ora introduciamo sprite che **si muovono automaticamente** e si **rigenerano** quando escono dallo schermo.

### 2. Gestione delle collisioni tra sprite

Con `pygame.sprite.spritecollide()` possiamo verificare se due sprite si toccano.  
In questo caso, useremo la funzione per controllare se Mario è stato colpito da un guscio.

### 3. Sistema delle vite

Gestiremo una variabile `vite` che decrementa a ogni collisione.  
Quando `vite == 0`, il gioco termina mostrando “Game Over”.

---

## Preparazione

Nella cartella del progetto (`salva_la_principessa`), assicurati di avere:

- `sfondo.png` — lo sfondo del livello.  
- `mario.png` — il personaggio.  
- `guscio.png` — l’immagine del guscio.

Crea un file `lesson_3.py`.

---

## Codice completo e commentato

```python
import pygame
import random
import sys

# Inizializza Pygame
pygame.init()

# Costanti principali
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
MOVE_SPEED = 5
JUMP_POWER = 12
MAX_FALL_SPEED = 20
NUM_GUSCI = 5

# Colori
WHITE = (255, 255, 255)
RED = (255, 0, 0)
COLOR_PLATFORM = (120, 80, 40)

# Finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salva la Principessa - Lezione 3")
clock = pygame.time.Clock()

# Font per testo
font = pygame.font.SysFont("arial", 28, bold=True)

# Carica immagini
background = pygame.image.load("sfondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mario_img = pygame.image.load("mario.png").convert_alpha()
guscio_img = pygame.image.load("guscio.png").convert_alpha()

# Classi
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(COLOR_PLATFORM)
        self.rect = self.image.get_rect(topleft=(x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(mario_img, (60, 80))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.pos_y = float(self.rect.y)
        self.vel_y = 0
        self.on_ground = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += MOVE_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -JUMP_POWER
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += GRAVITY
        if self.vel_y > MAX_FALL_SPEED:
            self.vel_y = MAX_FALL_SPEED
        self.pos_y += self.vel_y
        self.rect.y = int(self.pos_y)

    def check_vertical_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0 and self.rect.bottom - int(self.vel_y) <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.pos_y = float(self.rect.y)
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0 and self.rect.top - int(self.vel_y) >= platform.rect.bottom:
                    self.rect.top = platform.rect.bottom
                    self.pos_y = float(self.rect.y)
                    self.vel_y = 0

    def update(self, platforms):
        self.handle_input()
        self.apply_gravity()
        self.check_vertical_collisions(platforms)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Guscio(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(guscio_img, (50, 50))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-400, -50)
        self.speed = random.uniform(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset()

# Gruppi
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
gusci = pygame.sprite.Group()

# Piattaforme
ground = Platform(0, HEIGHT - 50, WIDTH, 50)
platform1 = Platform(150, 430, 200, 20)
platform2 = Platform(420, 320, 180, 20)
platform3 = Platform(620, 210, 150, 20)
platforms.add(ground, platform1, platform2, platform3)
all_sprites.add(ground, platform1, platform2, platform3)

# Player
player = Player(50, HEIGHT - 150)
all_sprites.add(player)

# Gusci
for _ in range(NUM_GUSCI):
    guscio = Guscio()
    gusci.add(guscio)
    all_sprites.add(guscio)

# Vite
vite = 3
game_over = False

# Loop principale
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        player.update(platforms)
        gusci.update()

        # Collisione con gusci
        if pygame.sprite.spritecollide(player, gusci, False):
            vite -= 1
            if vite <= 0:
                game_over = True
            else:
                player.rect.x, player.rect.y = 50, HEIGHT - 150
                player.pos_y = float(player.rect.y)

    # Disegno
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Mostra vite
    vite_text = font.render(f"Vite: {vite}", True, WHITE)
    screen.blit(vite_text, (20, 20))

    # Game over
    if game_over:
        over_text = font.render("GAME OVER - Premi ESC per uscire", True, RED)
        screen.blit(over_text, (WIDTH // 2 - 200, HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## Spiegazioni e approfondimenti

### Gestione dei gusci
Ogni guscio è un `Sprite` che cade costantemente verso il basso con una velocità casuale.  
Quando esce dallo schermo, viene riposizionato sopra la finestra (`reset()`), creando un ciclo infinito di ostacoli.

### Collisioni
Usiamo `pygame.sprite.spritecollide(player, gusci, False)` per controllare se Mario viene colpito.  
Ogni collisione riduce il numero di vite e riposiziona il giocatore.

### Game Over
Quando `vite` raggiunge 0, `game_over` diventa `True` e il gioco mostra un messaggio statico fino a che il giocatore preme **ESC**.

---

## Esercizi proposti

1. **Aggiungi una pausa di invincibilità** dopo una collisione (es. 2 secondi).  
2. **Aumenta la difficoltà** nel tempo: più gusci, o più veloci.  
3. **Aggiungi effetti sonori**: un suono per le collisioni e uno per il game over.  
4. **Visualizza un’icona di cuore** accanto alle vite.  
5. **Crea un sistema di punteggio** basato sul tempo sopravvissuto.

---

## Riepilogo

In questa lezione abbiamo:

- Creato gli ostacoli (gusci) che cadono dall’alto.  
- Gestito collisioni e decremento delle vite.  
- Implementato una schermata di Game Over.  

Nella **Lezione 4**, aggiungeremo **il menu iniziale**, **le schermate di vittoria** e **di sconfitta**, rendendo il gioco completo e presentabile.

[Continua alla Lezione 4 →](Lezione_4.md)
