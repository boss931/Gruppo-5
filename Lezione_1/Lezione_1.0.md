
# Lezione 1: Iniziare lo sviluppo del gioco con Pygame
 
# Immagini
![immagine schermata](../immagini/x_readme/Schermata_principale1.png)
 
## Introduzione
 
Benvenuto nella serie di lezioni **“Salva la Principessa”**!  
In questo corso imparerai a creare un semplice videogioco 2D con **Pygame**, una libreria Python pensata per sviluppare giochi in modo semplice e divertente.Alla fine di questo percorso, avrai costruito un gioco completo in cui **Mario** deve saltare su piattaforme, evitare i gusci cadenti e raggiungere **la Principessa Peach**, salvandola da Donkey Kong che la tiene prigioniera.


---
 
## Descrizione del Gioco
 
In **“Salva la Principessa”**, il giocatore controlla Mario e deve:
- Saltare tra le piattaforme per raggiungere la principessa.
- Evitare i gusci che cadono dall’alto (ostacoli).
- Conservare tutte le vite e arrivare all’obiettivo per vincere.
 
---
 
## Come si Gioca
 
- **FRECCIA DESTRA:** Muovi Mario a destra  
- **FRECCIA SINISTRA:** Muovi Mario a sinistra  
- **BARRA SPAZIATRICE:** Fai saltare Mario 
- **ESC:** Esci dal gioco  
 
L’obiettivo è **raggiungere la Principessa Peach** senza perdere tutte le vite.
 
---
 
## Struttura Tecnica
 
1. **Inizializzazione di Pygame:** Configura l’ambiente di gioco e la finestra.  
2. **Caricamento Immagini:** Importa lo sfondo e i personaggi.  
3. **Disegno su Schermo:** Visualizza gli elementi grafici.  
4. **Ciclo Principale:** Gestisce input, aggiornamenti e rendering continuo.
 
---
 
## Struttura del Tutorial
 
Il corso è diviso in 4 lezioni progressive:
 
1. **Lezione 1:** Mostrare una finestra con lo sfondo, Mario e le piattaforme. (Parte statica del gioco)
2. **Lezione 2:** Aggiungere la gravità e implementare i diversi movimenti di Mario. (Parte dinamica del gioco)
3. **Lezione 3:** Creare i gusci cadenti e il sistema di vite.  
4. **Lezione 4:** Aggiungere il menu iniziale e le schermate di vittoria/sconfitta.  
 
Al termine delle lezioni sarai in grado di sviluppare in maniera autonoma un videogioco completo e divertente con Pygame.
 
---
 
## Introduzione a Pygame
 
### Cos’è Pygame?
 
[Pygame](https://www.pygame.org/) è una collezione di moduli Python per sviluppare videogiochi 2D.  
Offre strumenti per gestire grafica, suoni, input da tastiera e animazioni.
 
### Perché Usare Pygame?
 
- **Facile da imparare:** Interfaccia semplice e intuitiva.  
- **Integrato con Python:** Perfetto per chi conosce già il linguaggio.  
- **Multiplatform:** Funziona su Windows, macOS e Linux.  
- **Comunità attiva:** Molte risorse e tutorial disponibili online.
 
---
 
## Requisiti
 
- **Python 3.12 o superiore**  
- **Pygame** (installabile tramite `pip`)
 
---
 
## Preparazione
 
1. Installa Python 3.12 se non lo hai già.  
2. Crea una cartella di progetto dove di volta in volta inserirai i tuoi progressi nello sviluppo del gioco, ad esempio `salva_la_principessa`.  
3. Apri il terminale e crea un ambiente virtuale:
 
   ```bash
   python -m venv .venv
   ```
 
4. Attivalo:
 
   - **Windows:**  
     ```bash
     .\.venv\Scripts\activate
     ```
   - **Mac/Linux:**  
     ```bash
     source .venv/bin/activate
     ```
 
5. Installa Pygame:
 
   ```bash
   pip install pygame
   ```
 
6. Inserisci nella cartella del progetto l’immagine di sfondo, ad esempio `sfondo.png`.
 
---
 
## Codice della Lezione 1
 
In questa prima lezione creeremo un programma che mostra solo la parte statica del gioco: **una finestra con lo sfondo**, le piattaforme e Mario. 
 
Per prima cosa andremo a creare un file chiamato **lesson_1.py** e inizieremo a sviluppare il nostro codice:
Importiamo per prima cosa i moduli:
```python
import pygame
import sys

pygame: libreria Pygame, necessaria per creare giochi 2D
sys: serve per accedere a funzioni di sistema, come sys.exit() per chiudere il programma in modo pulito.

In seguito dobbiamo inizializzare il programma con: 

pygame.init()
 
e poi definire le costanti del gioco(larghezza = 800, altezza = 600 e il titolo del gioco “Salva la Principessa - Lezione 1”) 
Prova tu!
# suggerimento: per dare il titolo utilizza GAME_TITLE = …
 
Andremo poi a creare la finestra con: 
screen = pygame.display.set_mode((inserisci le variabili larghezza e altezza))
pygame.display.set_caption(inserisci la variabile per il titolo del gioco)
 
Ora aggiungiamo lo sfondo con:
background = pygame.image.load("immagine che hai salvato nella cartella per lo sfondo").convert()
convert() ottimizza l’immagine per il display
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) # che ridimensiona l’immagine per adattarla alla finestra di gioco

Creiamo un oggetto clock per limitare il numero di fotogrammi al secondo (FPS) e mantenere la velocità del gioco costante:
clock = pygame.time.Clock()
 
È arrivato il momento di implementare il ciclo principale del nostro gioco (per il momento ti do la soluzione così che tu possa capire come funziona, quando vai a fare il template prova a farlo da solo!):
running = True # questa riga di codice fa in modo che finché running sia true il gioco continui
while running:
    for event in pygame.event.get(): # recupera la lista degli eventi(es.input da tastiera)
        if event.type == pygame.QUIT:# se l’evento è pygame.QUIT(cioè l’utente clicca sulla “X” della finestra) allora running diventa false
            running = False
 # quando diventa false termina il ciclo e di conseguenza anche il gioco 

    Infine disegna lo sfondo con:
    screen.blit(background, (0, 0)) # disegna l’immagine background nella posizione (0, 0) e quindi aggiorna ciò che deve essere mostrato, ma per il momento non lo rende visibile
 
    aggiorna lo schermo: 
    pygame.display.flip()
    clock.tick(60) # momento in cui il giocatore vede cambiamenti 
 
E chiudi il programma:
pygame.quit()
sys.exit()
```
 
---
 
## Esecuzione del Programma
 
Esegui il file con:
 
```bash
python lesson_1.py
```

A questo punto vedrai apparire una finestra **800x600** con il tuo sfondo, pronta per diventare il mondo del tuo gioco.
 
---
 
## Riepilogo
 
In questa lezione hai imparato a:
 
- Inizializzare un progetto Pygame.  
- Creare una finestra di gioco.  
- Caricare e visualizzare un’immagine di sfondo.  
- Implementare il personaggio di **Mario**, controllabile con la tastiera (lezione 2).
- Sviluppare le **piattaforme** su cui Mario può atterrare.
- Gestire il ciclo principale del gioco.
 
Nella **Lezione 2** aggiungeremo la **gravità** di Mario e scopriremo come implementare i suoi movimenti, spostamento a destra e sinistra e salto, e la collisione con le piattaforme per iniziare a rendere il gioco interattivo.
 
[Continua alla Lezione 2 →](Lezione_2.md)
