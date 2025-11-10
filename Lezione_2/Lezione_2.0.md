# Lezione 2: Aggiungere la Gravità e i Movimenti di Mario
# Immagini
![immagine schermata](../immagini/x_readme/Schermata_principale2.png)
## Introduzione
Benvenuto alla **Lezione 2** del corso *Salva la Principessa*!  
Nella lezione precedente hai imparato a creare una finestra con Pygame e impostare uno sfondo, contente anche le piattaforme e il personaggio.
Ora daremo vita al nostro gioco aggiungendo:
- Un sistema di **gravità** realistico.
- La possibilità per Mario di muoversi tramite la tastiera, e dunque **saltare e camminare**.
-
In questa lezione iniziamo a costruire le fondamenta della fisica di gioco, un passaggio chiave per rendere il movimento del personaggio realistico, stabile e dare vita alla dinamica del videogioco.

---
## Obiettivi della Lezione
- Comprendere il concetto di coordinate e rettangoli (`Rect`) in Pygame.  Spostare nella lezione 1
- Applicare una gravità costante e gestire i salti.  
- Implementare le collisioni tra Mario e le piattaforme solide in maniera corretta.
- Mantenere lo stesso stile visivo e proporzioni del gioco completo.
---
## Concetti Teorici Fondamentali
### 1. Coordinate in Pygame (spostare in lezione 1)
In Pygame, il punto **(0,0)** si trova in **alto a sinistra** dello schermo:  
- l’asse **x** cresce verso destra,  
- l’asse **y** cresce verso il basso.  
Ogni immagine o oggetto è rappresentato da un **rettangolo (Rect)** che definisce posizione e dimensioni.  
I `Rect` sono anche usati per rilevare **collisioni**, grazie a metodi come `colliderect()`.
### 2. Gravità e Velocità Verticale
Per simulare la gravità, usiamo una variabile `vel_y` che rappresenta la velocità verticale del giocatore.  
A ogni frame aggiungiamo una costante `GRAVITY` a `vel_y`, poi aggiorniamo la posizione `y` di Mario:
```python
vel_y += GRAVITY
player.y += int(vel_y)
```
Quando Mario salta, impostiamo `vel_y` a un valore negativo (es. `-JUMP_POWER`), e la gravità lo riporterà giù gradualmente.
### 3. Collisioni con Piattaforme
Per evitare che Mario attraversi il terreno o le piattaforme, verifichiamo se il suo `Rect` collide con quello delle piattaforme.  
In caso di collisione, correggiamo la posizione e azzeriamo la velocità verticale, simulando l’impatto con il suolo.
---
## Preparazione del Progetto   (spostare in lezione 1)
Assicurati di avere nella tua cartella di progetto `salva_la_principessa` i seguenti file:
- `sfondo.png` → lo sfondo del livello  
- `mario.png` → il personaggio principale  
- `blocco.png` → immagine per le piattaforme  
Ora andremo a creare un nuovo file Python chiamato **lesson_2.py** dove daremo vita al nostro gioco:
---

```python
import pygame
import sys
# --- Inizializzazione ---
pygame.init()
# --- Costanti di Gioco ---
WIDTH, HEIGHT = 800, 600
FPS = 60
(Lezione 1)
Iniziamo definendo i parametri fisici del gioco:
GRAVITY = 0.8 # indica quanto velocemente cade il personaggio
JUMP_POWER = 20 # indica la potenza del salto, maggiore è la potenza e più Mario salta in alto
SPEED = 5 # velocità di movimento orizzontale (quanto si sposta a sinistra/destra)
Definiamo i colori nel formato RGB:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 90, 40)
# --- Setup Finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salva la Principessa - Lezione 2")
clock = pygame.time.Clock()
# --- Caricamento Immagini ---
background = pygame.image.load("sfondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
Definiamo la grafica del personaggio:
mario_img = pygame.image.load("immagine salvata per il personaggio").convert_alpha() # .convert_alpha() mantiene la trasparenza (utile se il PNG ha sfondo trasparente).
mario_img = pygame.transform.scale(mario_img, (60, 60)) # scala l’immagine a 60×60 pixel
E delle piattaforme:
block_img = pygame.image.load("immagine salvata per la piattaforma").convert_alpha()
block_img = pygame.transform.scale(block_img, (150, 40))
# --- Definizione Oggetti di Gioco ---
player = pygame.Rect(50, HEIGHT - 150, 60, 60)
vel_y = 0
on_ground = False
# pygame.Rect(...): crea un rettangolo per gestire posizione e collisioni del giocatore.
• (50, HEIGHT - 150): posizione iniziale.
• (60, 60): larghezza e altezza.
vel_y: velocità verticale (inizialmente 0).
on_ground: indica se il personaggio è sul terreno/piattaforma (utile per i salti).

# --- Creazione Piattaforme ---
platforms = [
    pygame.Rect(100, 480, 150, 40),
    pygame.Rect(300, 370, 150, 40),
    pygame.Rect(500, 260, 150, 40),
    pygame.Rect(650, 150, 150, 40),
]
 Crea una lista di piattaforme (rettangoli) posizionate a varie altezze.
Ogni piattaforma ha coordinate (x, y, larghezza, altezza).
# --- Ciclo Principale di Gioco ---
running = True
while running:
    dt = clock.tick(FPS)
    # Gestione Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Input da Tastiera
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= SPEED
    if keys[pygame.K_RIGHT]:
        player.x += SPEED
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = -JUMP_POWER
        on_ground = False
# pygame.key.get_pressed(): restituisce lo stato di tutti i tasti.
Frecce sinistra/destra → spostano il giocatore.
K_SPACE (barra spaziatrice) → fa saltare il personaggio solo se on_ground è True.
Il salto funziona impostando la velocità verticale negativa (-JUMP_POWER).

    # Gravità
    vel_y += GRAVITY
    player.y += int(vel_y)
# A ogni frame, la gravità aumenta vel_y (la caduta accelera). Poi aggiorna la posizione verticale del giocatore.

    # Collisioni con le Piattaforme
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            # Se cade sulla piattaforma
            if vel_y > 0 and player.bottom - vel_y <= platform.top:
                player.bottom = platform.top
                vel_y = 0
                on_ground = True
            # Se colpisce dal basso
            elif vel_y < 0 and player.top - vel_y >= platform.bottom:
                player.top = platform.bottom
                vel_y = 0
# colliderect() controlla se il giocatore tocca una piattaforma.
Se sta cadendo (vel_y > 0), si “ferma” sopra la piattaforma.
Se sta saltando (vel_y < 0), viene bloccato dal basso.
on_ground = True permette di saltare di nuovo.
    # Pavimento (bordo inferiore)
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
        vel_y = 0
        on_ground = True
# Se il giocatore cade sotto la finestra, viene riportato al fondo e fermato.
    # Limiti Laterali
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
# Impedisce al giocatore di uscire dai bordi sinistro e destro della finestra.
    # --- Disegno su Schermo ---
    screen.blit(background, (0, 0))
    for platform in platforms:
        screen.blit(block_img, (platform.x, platform.y))
    screen.blit(mario_img, (player.x, player.y))
 # blit() disegna un’immagine su un’altra superficie:
1. Sfondo.
2. Tutte le piattaforme.
3. Il personaggio (mario_img).
    pygame.display.flip()
# aggiorna il display

# Chiude Pygame in modo ordinato e termina il programma.
pygame.quit()
sys.exit()
```
---
## Spiegazione del Codice
### 1. Gravità e Salto
Il parametro `GRAVITY` definisce l’accelerazione verso il basso.  
Ogni frame, `vel_y` aumenta e viene sommato alla posizione `y` del giocatore.
Il salto avviene impostando `vel_y` a un valore negativo. Quando `on_ground` è `True`, Mario può saltare; in aria, no.
### 2. Collisioni Verticali
Controlliamo se Mario entra in contatto con una piattaforma tramite `player.colliderect(platform)`.
- Se la collisione avviene **dall’alto**, fermiamo la caduta e posizioniamo Mario esattamente sopra la piattaforma.  
- Se la collisione avviene **dal basso**, blocchiamo la salita e annulliamo la velocità.
### 3. Controllo dei Bordi
Impediamo al giocatore di uscire dallo schermo, controllando `player.left` e `player.right`.
### 4. Frame Rate
`clock.tick(FPS)` mantiene la velocità di aggiornamento costante.  
Con 60 FPS, il movimento risulterà fluido e naturale.
---
## Challenge
1. **Crea più piattaforme:** aggiungi nuove righe alla lista `platforms`.  
2. **Cambia la gravità:** prova valori tra `0.5` e `1.2` per vedere come cambia la sensazione del salto.  
3. **Aggiungi suono al salto:** usa `pygame.mixer.Sound("salto.wav").play()`.  
4. **Disegna contorni di debug:** usa `pygame.draw.rect(screen, (255,0,0), player, 2)` per vedere i `Rect`.  
---
## Riepilogo
In questa lezione hai imparato a:
- Gestire movimento e salto del personaggio.  
- Applicare la gravità.  
- Implementare collisioni verticali.  
- Mantenere il controllo stabile dei bordi dello schermo.
Nella **Lezione 3**, aggiungeremo i **gusci cadenti**, il **sistema di vite**, e la logica di **game over**.
[Continua alla Lezione 3 →](Lezione_3.md)
