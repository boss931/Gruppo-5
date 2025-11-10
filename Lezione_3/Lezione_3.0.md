# Salva la Principessa — Lezione 3

Questo file documenta solo le novità introdotte nella Lezione 3 rispetto alla Lezione 2.

In questa lezione sono stati aggiunti:

- Gusci che cadono dall'alto
- Sistema delle vite con icona grafica
- Schermata di Game Over con possibilità di ricominciare
- Gestione del timer per far comparire gli ostacoli in modo casuale

La logica del movimento del giocatore e delle piattaforme rimane invariata rispetto alla Lezione 2.

---

## Import aggiuntivi

import random

Serve per generare numeri casuali relativi a:
- Posizione del guscio
- Velocità di caduta

---

## Nuove costanti

DROP_SPEED_MIN = 3
DROP_SPEED_MAX = 6
DROP_SPAWN_TIME = 1200
MAX_VITE = 3

Costante                       | Descrizione
--------------------------------|------------------------------------------------
DROP_SPEED_MIN / DROP_SPEED_MAX | Velocità minima/max di caduta dei gusci
DROP_SPAWN_TIME                 | Intervallo di tempo tra uno spawn e l'altro (ms)
MAX_VITE                        | Numero massimo di vite disponibili per il giocatore

---

## Caricamento delle nuove immagini

guscio_img = pygame.image.load("guscio.png").convert_alpha()
cuore_img = pygame.image.load("fungo.png").convert_alpha()

- guscio_img: immagine dell’ostacolo cadente
- cuore_img: icona che rappresenta le vite

---

## Ridimensionamento delle immagini

guscio_img = pygame.transform.scale(guscio_img, (40, 40))
cuore_img = pygame.transform.scale(cuore_img, (32, 32))

- Gusci: 40×40 px
- Icone vite: 32×32 px

---

## Variabili aggiunte

vite = MAX_VITE
drops = []
last_drop_time = pygame.time.get_ticks()

Variabile      | Funzione
----------------|---------------------------------------------
vite           | Vite rimanenti del giocatore
drops          | Lista contenente i gusci generati
last_drop_time | Tiene traccia dell’ultimo spawn di un guscio

---

## Disegno delle vite (HUD)

def draw_vite(vite):
    ...

Disegna in alto a sinistra le vite tramite icone:
- Vita presente → cuore colorato
- Vita persa → cuore grigio

---

## Schermata di Game Over

def game_over_screen():
    ...

Mostra una schermata nera con il messaggio:

Hai perso! Premi R per riprovare.

Il gioco rimane fermo finché non viene premuto il tasto R.

---

## Generazione dei gusci cadenti

now = pygame.time.get_ticks()
if now - last_drop_time >= DROP_SPAWN_TIME:
    x_pos = random.randint(0, WIDTH - 40)
    speed = random.randint(DROP_SPEED_MIN, DROP_SPEED_MAX)
    drops.append({"x": x_pos, "y": -40, "speed": speed})
    last_drop_time = now

Funzionamento:
1. Verifica se è trascorso abbastanza tempo dall’ultimo guscio.
2. Determina una posizione casuale orizzontale.
3. Assegna una velocità di caduta casuale.
4. Aggiunge un nuovo guscio alla lista drops.

---

## Movimento dei gusci e collisione

for drop in drops[:]:
    drop["y"] += drop["speed"]

    if drop["y"] > HEIGHT:
        drops.remove(drop)

    drop_rect = pygame.Rect(drop["x"], drop["y"], 40, 40)
    if drop_rect.colliderect(player):
        vite -= 1
        drops.remove(drop)

- I gusci cadono verso il basso incrementando la coordinata Y
- Vengono rimossi se escono dallo schermo o colpiscono il giocatore
- Se vite arriva a 0 → Game Over

---

## Disegno dei nuovi elementi

for drop in drops:
    screen.blit(guscio_img, (drop["x"], drop["y"]))
draw_vite(vite)

- Disegna i gusci cadenti
- Disegna le vite (HUD)

---

## Risultato finale della Lezione 3

Funzionalità introdotta | Effetto ottenuto
------------------------|-----------------------------------
Gusci cadenti           | Aggiunge una difficoltà reale al gioco
Sistema delle vite      | Il giocatore può perdere
Game Over               | Possibilità di ripartire premendo il tasto R

