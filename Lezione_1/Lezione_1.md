# Lezione 1: Iniziare lo sviluppo del gioco con Pygame
 
# Immagini
![immagine schermata](../immagini/x_readme/Schermata_principale1.png)
 
## Introduzione
 
Benvenuto nella serie di lezioni **“Salva la Principessa”**!  
In questo corso imparerai a creare un semplice videogioco 2D con **Pygame**, una libreria Python pensata per sviluppare giochi in modo semplice e divertente.
 
Alla fine di questa serie, avrai costruito un gioco completo in cui **Mario** deve saltare su piattaforme, evitare gusci cadenti e raggiungere **la Principessa Peach**, salvandola da Donkey Kong che la tiene prigioniera.
 
---
 
## Descrizione del Gioco
 
In **“Salva la Principessa”**, il giocatore controlla Mario e deve:
- Saltare tra le piattaforme per raggiungere la principessa.
- Evitare i gusci che cadono dall’alto.
- Conservare tutte le vite e arrivare all’obiettivo per vincere.
 
---
 
## Come si Gioca
 
- **FRECCIA DESTRA:** Muovi Mario a destra  
- **FRECCIA SINISTRA:** Muovi Mario a sinistra  
- **BARRA SPAZIATRICE:** Salta  
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
 
1. **Lezione 1:** Mostrare una finestra con lo sfondo.  
2. **Lezione 2:** Aggiungere Mario, la gravità e le piattaforme.  
3. **Lezione 3:** Creare i gusci cadenti e il sistema di vite.  
4. **Lezione 4:** Aggiungere il menu iniziale e le schermate di vittoria/sconfitta.  
 
Alla fine avrai un videogioco completo e giocabile.
 
---
 
## Introduzione a Pygame
 
### Cos’è Pygame?
 
Pygame è una collezione di moduli Python per sviluppare videogiochi 2D.  
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
2. Crea una cartella di progetto, ad esempio `salva_la_principessa`.  
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
 
In questa prima lezione creeremo un programma che mostra solo **una finestra con lo sfondo**.
 
Crea un file chiamato **lesson_1.py** e aggiungi questo codice:
 
```python
import pygame
import sys
 
# Inizializzazione di Pygame
pygame.init()
 
# Costanti
WIDTH, HEIGHT = 800, 600
GAME_TITLE = "Salva la Principessa - Lezione 1"
 
# Creazione finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)
 
# Carica lo sfondo
background = pygame.image.load("sfondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
 
# Clock per controllare il framerate
clock = pygame.time.Clock()
 
# Ciclo principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Disegna lo sfondo
    screen.blit(background, (0, 0))
 
    # Aggiorna lo schermo
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
sys.exit()
```
 
---
 
## Esecuzione del Programma
 
Esegui il file con:
 
```bash
python lesson_1.py
```
 
Vedrai apparire una finestra **800x600** con il tuo sfondo, pronta per diventare il mondo del gioco.
 
---
 
## Riepilogo
 
In questa lezione hai imparato a:
 
- Inizializzare un progetto Pygame.  
- Creare una finestra di gioco.  
- Caricare e visualizzare un’immagine di sfondo.  
- Gestire il ciclo principale del gioco.
 
Nella **Lezione 2** aggiungeremo **Mario**, la **gravità** e le **piattaforme** per iniziare a rendere il gioco interattivo.
 
[Continua alla Lezione 2 →](Lezione_2/Lezione_2.md)
