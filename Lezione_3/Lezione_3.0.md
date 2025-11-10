# 🏰 Salva la Principessa – Lezione 3  
**Nuove funzionalità: gusci cadenti, vite e Game Over**

In questa lezione il gioco viene esteso introducendo:

- Gusci cadenti che il giocatore deve evitare  
- Sistema di vite con icone grafiche  
- Schermata di Game Over che blocca il gioco e permette di ricominciare  

L'obiettivo è imparare a gestire **oggetti dinamici**, **collisioni**, **stati di gioco** e **UI grafica**.

---

## 1. Nuove costanti di gioco

```python
DROP_SPEED_MIN = 3
DROP_SPEED_MAX = 6
DROP_SPAWN_TIME = 1200  # millisecondi tra uno spawn e l'altro
MAX_VITE = 3

Spiegazione dettagliata:
	•	DROP_SPEED_MIN e DROP_SPEED_MAX definiscono un intervallo di velocità casuale per ogni guscio, rendendo la caduta più imprevedibile.
	•	DROP_SPAWN_TIME regola la frequenza dei gusci. Senza di esso, i gusci sarebbero generati ogni frame, rendendo il gioco impossibile.
	•	MAX_VITE stabilisce il numero massimo di vite del giocatore e serve sia per la logica del gioco sia per il disegno dei cuori sullo schermo.

Usare costanti permette di modificare facilmente il comportamento del gioco.

⸻

2. Liste e variabili di stato dei nemici e delle vite

drops = []
last_drop_time = pygame.time.get_ticks()
vite = MAX_VITE

Spiegazione dettagliata:
	•	drops contiene tutti i gusci attivi sullo schermo. Ogni guscio è un dizionario (x, y, speed).
	•	last_drop_time memorizza il tempo in cui è stato generato l’ultimo guscio.
	•	vite contiene le vite correnti del giocatore e viene decrementato quando subisce un colpo.

Questo approccio permette di gestire oggetti dinamici in modo flessibile.

⸻

3. Funzione draw_vite() – visualizzazione delle vite

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

Spiegazione approfondita:
	•	Disegna i cuori in alto a sinistra.
	•	Cuori pieni → vite disponibili; cuori grigi → vite perse.
	•	BLEND_RGBA_MULT scurisce la copia dell’immagine senza modificare l’originale.
	•	Funzione flessibile, facilmente adattabile a icone o posizione diversa.

⸻

4. Funzione game_over_screen() – gestione Game Over

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

Spiegazione approfondita:
	•	Blocca il gioco su uno schermo nero con messaggio.
	•	L’utente deve premere R per ricominciare.
	•	Gestisce anche la chiusura della finestra (QUIT).
	•	Permette di creare stati di gioco distinti senza strutture complesse.

⸻

5. Generazione dei gusci

now = pygame.time.get_ticks()
if now - last_drop_time >= DROP_SPAWN_TIME:
    x_pos = random.randint(0, WIDTH - 40)
    speed = random.randint(DROP_SPEED_MIN, DROP_SPEED_MAX)
    drops.append({"x": x_pos, "y": -40, "speed": speed})
    last_drop_time = now

Spiegazione approfondita:
	•	Ogni DROP_SPAWN_TIME millisecondi viene creato un guscio.
	•	x_pos casuale per variare la posizione di spawn.
	•	speed casuale per rendere la caduta più imprevedibile.
	•	Il guscio è aggiunto alla lista drops.
	•	last_drop_time aggiornato per il prossimo spawn.

⸻

6. Aggiornamento posizione e collisioni dei gusci

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

Spiegazione approfondita:
	•	drops[:] è una copia della lista per poter rimuovere elementi senza problemi.
	•	Aggiorna la posizione verticale dei gusci.
	•	Rimuove gusci usciti dallo schermo.
	•	Controlla collisione con il player (colliderect).
	•	Se collisione → decrementa vite e rimuove il guscio.
	•	Se vite = 0 → chiama Game Over, resetta vite, posizione player e lista dei gusci.

⸻

7. Disegno dei gusci e delle vite

for drop in drops:
    screen.blit(guscio_img, (drop["x"], drop["y"]))
draw_vite(vite)

Spiegazione approfondita:
	•	Disegna tutti i gusci attivi sullo schermo.
	•	Aggiorna la UI delle vite.
	•	Mantiene separata la logica di gioco dalla grafica, migliorando la leggibilità e manutenibilità del codice.

⸻

8. Flusso di gioco aggiornato

[spawn guscio ogni DROP_SPAWN_TIME ms]
              ↓
[guscio cade a velocità casuale]
              ↓
[collisione con player?]
       ↙           ↘
     sì             no
      ↓              ↓
vite -= 1          continua a cadere
      ↓
vite == 0 ?
       ↙       ↘
     sì           no
      ↓            ↓
Game Over       continua il gioco

Questo diagramma mostra chiaramente la sequenza logica del gioco.

⸻

🔧 Concetti principali appresi
	•	Gestione del tempo con pygame.time.get_ticks()
	•	Liste dinamiche e dizionari per nemici multipli
	•	Collisioni tra oggetti (Rect.colliderect)
	•	UI grafica dinamica (icone vite)
	•	Stati di gioco: Game Over, reset e ripartenza
	•	Separazione tra logica di gioco e disegno grafico

⸻

Questo README ti permette di comprendere ogni parte introdotta nella Lezione 3, riscriverla da zero e applicare lo stesso approccio per futuri aggiornamenti del gioco.

---

Se vuoi, posso anche creare una **versione con diagrammi visivi e schemi dei gusci**, pronta da aggiungere al README per renderlo ancora più chiaro su GitHub.  

Vuoi che faccia anche quello?
