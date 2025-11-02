# Lezione 2: Aggiungere Mario, la gravità e le piattaforme (approfondita)

## Introduzione

Nella Lezione 1 abbiamo creato la finestra di gioco e visualizzato lo sfondo.  
In questa lezione trasformiamo lo schermo in un livello interattivo: aggiungeremo **Mario** come sprite giocabile, implementeremo la **gravità** e il **salto**, creeremo **piattaforme** e tratteremo in dettaglio la gestione delle **collisioni**.

Questa lezione spiega non solo il "come" ma anche il "perché" delle scelte tecniche: utile per capire i problemi comuni (es. *tunneling* delle collisioni, *overshoot* del salto) e come risolverli.

---

## Obiettivi didattici

- Comprendere il sistema di coordinate e l’uso di `Rect` in Pygame.  
- Implementare un player con movimento orizzontale e salto.  
- Applicare una gravità semplice ma stabile.  
- Creare piattaforme statiche su cui il player può atterrare.  
- Gestire collisioni verticali correttamente e risolvere problemi comuni.  
- Fornire esercizi e varianti per consolidare l’apprendimento.

---

## Concetti chiave

### Coordinate e `Rect`

- In Pygame l’origine `(0,0)` è in alto a sinistra.  
- Le coordinate aumentano verso destra (asse X) e verso il basso (asse Y).  
- `pygame.Rect` è un rettangolo con proprietà utili: `x`, `y`, `width`, `height`, `top`, `bottom`, `left`, `right`, `center`, ecc.  
  Serve per gestire collisioni e posizionamento degli oggetti.

### Gravità e velocità

- La gravità viene applicata sommando ogni frame un valore `g` alla velocità verticale `vel_y`.  
- La posizione verticale `y` viene aggiornata in base a `vel_y`.  
- È buona pratica mantenere `vel_y` come *float* per movimenti più fluidi e convertire in intero solo quando necessario.

### Collisioni

- Si controllano le collisioni tra il `Rect` del player e quelli delle piattaforme.  
- È importante distinguere collisioni verticali e orizzontali.  
- Problemi comuni:
  - **Tunneling:** il player attraversa una piattaforma se la velocità è troppo alta.  
  - **Overshoot:** il player “rimbalza” sopra la piattaforma.  

---

## Preparazione

Nella cartella del progetto (`salva_la_principessa`) assicurati di avere:
- `sfondo.png` — sfondo del livello  
- `mario.png` — immagine del personaggio  

Crea un file chiamato `lesson_2.py`.

---

## Codice commentato e spiegato

Il codice seguente è completo e accompagnato da commenti esplicativi.  
Copialo in `lesson_2.py`.

```python
import pygame
import sys

# Inizializza Pygame
pygame.init()

# Costanti principali
WIDTH, HEIGHT = 800, 600
FPS = 60

# Parametri fisici
GRAVITY = 0.5        # accelerazione verso il basso (pixel/frame²)
JUMP_POWER = 12      # velocità iniziale del salto (pixel/frame)
MOVE_SPEED = 5       # velocità orizzontale (pixel/frame)
MAX_FALL_SPEED = 20  # limite di velocità in caduta per evitare tunneling

# Colori (per debug)
COLOR_PLATFORM = (120, 80, 40)

# Setup finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salva la Principessa - Lezione 2")
clock = pygame.time.Clock()

# Carica lo sfondo e scala
background = pygame.image.load("sfondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
````

---

### Definizione della classe `Platform`

```python
class Platform(pygame.sprite.Sprite):
    """
    Piattaforma semplice: disegnabile, con rect per collisioni.
    In un progetto reale potresti caricare un'immagine invece di disegnare una surface.
    """
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(COLOR_PLATFORM)
        self.rect = self.image.get_rect(topleft=(x, y))
```

---

### Definizione della classe `Player`

```python
class Player(pygame.sprite.Sprite):
    """
    Player basato su immagine con controllo semplice.
    Gestisce input, gravità, salto e collisioni verticali.
    """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("mario.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.pos_y = float(self.rect.y)
        self.vel_y = 0.0
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
                    self.vel_y = 0.0
                    self.on_ground = True
                elif self.vel_y < 0 and self.rect.top - int(self.vel_y) >= platform.rect.bottom:
                    self.rect.top = platform.rect.bottom
                    self.pos_y = float(self.rect.y)
                    self.vel_y = 0.0

    def update(self, platforms):
        self.handle_input()
        self.apply_gravity()
        self.check_vertical_collisions(platforms)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
```

---

### Creazione oggetti e setup del livello

```python
# Gruppi di sprite
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Piattaforme: terreno e alcune piattaforme fluttuanti
ground = Platform(0, HEIGHT - 50, WIDTH, 50)
platform1 = Platform(150, 430, 200, 20)
platform2 = Platform(420, 320, 180, 20)
platform3 = Platform(620, 210, 150, 20)

platforms.add(ground, platform1, platform2, platform3)
all_sprites.add(ground, platform1, platform2, platform3)

# Player iniziale
player = Player(50, HEIGHT - 150)
all_sprites.add(player)
```

---

### Ciclo principale (game loop)

```python
running = True
while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(platforms)

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## Spiegazioni approfondite e note pratiche

### Perché usiamo `pos_y` come float?

Serve per accumulare frazioni di movimento che altrimenti andrebbero perse con numeri interi, garantendo movimenti fluidi.

### Perché limitiamo la velocità di caduta?

Per evitare il “tunneling”: quando il personaggio attraversa una piattaforma tra due frame a causa di velocità troppo elevate.

### Impatto dall’alto

Il controllo `self.rect.bottom - int(self.vel_y) <= platform.rect.top` serve per capire se il player stava sopra la piattaforma nel frame precedente.

### Problemi comuni

* **Incollaggio laterale:** separare le collisioni orizzontali e verticali.
* **Rimbalzi indesiderati:** verificare la direzione del movimento prima di correggere la posizione.
* **Movimento non fluido:** assicurarsi che il framerate sia stabile (`clock.tick(FPS)`).

---

## Esercizi consigliati

1. **Separare collisioni orizzontali e verticali.**
2. **Aggiungere animazioni di camminata.**
3. **Creare un file di livello** con la disposizione delle piattaforme.
4. **Implementare un doppio salto o un dash.**
5. **Attivare il debug visivo** disegnando i `Rect` sullo schermo.

---

## Riepilogo

In questa lezione abbiamo:

* Implementato Mario con movimento e salto.
* Aggiunto la gravità e la gestione delle collisioni.
* Creato piattaforme statiche.
* Analizzato problemi comuni e relative soluzioni.

**Prossima lezione:** aggiungeremo gusci cadenti come ostacoli, introdurremo le vite e il sistema di *Game Over*.

Continua alla [Lezione 3 →](#)
