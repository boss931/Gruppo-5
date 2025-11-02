# Lezione 1: Inizia lo sviluppo del gioco con Pygame

## Introduzione

Benvenuto nella serie di tutorial **Salva la Principessa – Mario vs Bear**!  
In questa serie imparerai a creare un semplice gioco platform in 2D utilizzando **Pygame**, un insieme di moduli Python pensato per lo sviluppo di videogiochi.

## Descrizione del Gioco

In **Salva la Principessa**, impersoni **Mario**, che deve saltare sulle piattaforme, evitare i gusci che cadono dal cielo e raggiungere la **Principessa Peach**, mentre un **orso** la sorveglia.

Il tuo obiettivo è salvare la principessa senza perdere tutte le vite.

## Come si Gioca

- **Freccia Destra:** Muovi Mario verso destra.  
- **Freccia Sinistra:** Muovi Mario verso sinistra.  
- **Barra Spaziatrice:** Fai saltare Mario.  
- **Evita i gusci:** Se vieni colpito, perdi una vita.  
- **Raggiungi la principessa:** Vinci la partita.

Se perdi tutte le vite, la partita termina con la sconfitta.

## Struttura Tecnica

1. **Inizializzazione di Pygame:** Creazione della finestra di gioco e avvio del motore grafico.  
2. **Gestione della Finestra:** Impostazione delle dimensioni e del titolo del gioco.  
3. **Caricamento delle Immagini:** Aggiunta dello sfondo e dei personaggi.  
4. **Gestione del Giocatore:** Movimento, gravità e salto.  
5. **Loop Principale:** Controllo continuo di eventi, logica di gioco e disegno sullo schermo.

## Struttura del Tutorial

Questo corso è diviso in **4 lezioni**. Costruiremo il gioco passo dopo passo:

1. **Lezione 1:** Creare la finestra e mostrare lo sfondo.  
2. **Lezione 2:** Aggiungere Mario, le piattaforme e la gravità.  
3. **Lezione 3:** Creare i gusci cadenti e il sistema di vite.  
4. **Lezione 4:** Aggiungere il menu, la vittoria e le schermate finali.

Alla fine del corso, avrai realizzato un videogioco 2D completo e compreso le basi fondamentali di Pygame.

## Introduzione a Pygame

### Cos’è Pygame?

[Pygame](https://www.pygame.org/) è un insieme di moduli Python progettato per scrivere videogiochi.  
Fornisce funzionalità per gestire grafica, suoni, eventi e interazioni con la tastiera e il mouse.

### Perché usare Pygame?

- **Semplice da usare:** API intuitive, ideali per chi inizia.  
- **Integrazione con Python:** Sfrutta la leggibilità e la semplicità di Python.  
- **Comunità attiva:** Tantissime risorse, tutorial e progetti condivisi.  
- **Ottimo per imparare:** Perfetto per avvicinarsi alla programmazione di giochi.

## Requisiti

- **Python 3.12** (o versione successiva)  
- **[Pygame](https://www.pygame.org/)** installato nel tuo ambiente

## Preparazione

1. Installa Python 3.12 se non lo hai già.  
2. Crea una cartella di progetto, ad esempio `salva_la_principessa`, e aprila nel tuo editor.  
3. (Facoltativo) Crea un ambiente virtuale:
   ```bash
   python -m venv .venv
Attiva l’ambiente virtuale:

Su Windows: .\.venv\Scripts\activate

Su macOS/Linux: source .venv/bin/activate

Installa Pygame:

bash
Copia codice
pip install pygame
Aggiungi nella cartella di progetto l’immagine di sfondo sfondo.png.

Codice della Lezione 1
In questa lezione creeremo un semplice programma Pygame che visualizza una finestra con un’immagine di sfondo.
Apri un nuovo file Python chiamato lesson_1.py.

Importazione di Pygame
Per prima cosa, importiamo i moduli necessari:

python
Copia codice
import pygame
import sys
Definizione delle Costanti
Definiamo la larghezza e l’altezza della finestra:

python
Copia codice
# Costanti
WIDTH, HEIGHT = 800, 600
Inizializzazione di Pygame e Creazione della Finestra
Inizializziamo Pygame e impostiamo la finestra di gioco:

python
Copia codice
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salva la Principessa - Mario vs Bear")
Caricamento dell’Immagine di Sfondo
Carichiamo lo sfondo da file e lo adattiamo alle dimensioni della finestra:

python
Copia codice
background = pygame.image.load("sfondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
Creazione del Ciclo Principale
Ora creiamo il loop principale del gioco, che rimane attivo fino alla chiusura della finestra:

python
Copia codice
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Disegna lo sfondo
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
Esecuzione del Programma
Salva il file e avvialo dal terminale:

bash
Copia codice
python lesson_1.py
Dovresti vedere una finestra 800x600 con l’immagine di sfondo.

Riepilogo
In questa prima lezione abbiamo:

Inizializzato Pygame e creato una finestra di gioco.

Caricato e visualizzato un’immagine di sfondo.

Implementato un loop principale che mantiene attivo il gioco.

Nella prossima lezione aggiungeremo Mario, le piattaforme e la gravità per iniziare a dare vita al nostro personaggio.

Continua alla Lezione 2 →
