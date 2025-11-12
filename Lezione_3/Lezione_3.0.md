# Lezione 3: Gusci cadenti e sistema di vite

![immagine schermata](../immagini/x_readme/Schermata_principale3.png)
![immagine game over](../immagini/x_readme/Schermata_game_over_lezione3.png)

---

## Introduzione

Nella **Lezione 2** abbiamo creato un mondo interattivo con **Mario**, la **gravità** e le **piattaforme**.  
In questa lezione, il gioco diventa più dinamico introducendo due elementi chiave:

1. **Gusci cadenti**: ostacoli lanciati dall’alto che Mario deve evitare.  
2. **Sistema di vite**: ogni volta che Mario viene colpito da un guscio, perde una vita; il gioco termina quando le vite finiscono.

Questi elementi introducono concetti di **generazione casuale**, **gestione del tempo**, **collisioni** e **feedback visivo** per lo stato di salute del giocatore.

---

## Obiettivi didattici

Al termine di questa lezione, saprai:

- Come **creare oggetti dinamici** che cadono dal cielo a intervalli casuali.  
- Come **rilevare collisioni** tra Mario e i gusci.  
- Come gestire un **sistema di vite**, sia a livello logico che visivo.  
- Come bloccare il gioco e mostrare una **schermata di Game Over**, con la possibilità di riprovare premendo **R**.  
- Concetti di **loop di gioco**, **tempo e intervalli**.

---

## Concetti chiave

### 1. Gusci cadenti

I gusci rappresentano un ostacolo variabile. Alcuni punti da considerare:

- **Generazione casuale**: la posizione orizzontale e la velocità dei gusci cambiano ad ogni ondata, rendendo il gioco imprevedibile.
- **Caduta continua**: i gusci si muovono verso il basso fino a scomparire dalla schermata.
- **Interazione con Mario**: se un guscio colpisce Mario, viene sottratta una vita.

> Questo concetto introduce l’idea di **iterazione degli oggetti nel mondo di gioco**, dove ogni guscio è aggiornato frame per frame.

---

### 2. Sistema di vite

Il giocatore ha un numero limitato di vite, rappresentate visivamente:

- **Icone grafiche** (cuori o funghi) indicano le vite rimaste.  
- Quando Mario viene colpito, il contatore diminuisce e l’icona corrispondente cambia colore o scompare.  
- Al termine delle vite, appare la **schermata nera di Game Over**, che blocca il gioco fino a che il giocatore non preme **R** per ripartire.

> Questo sistema introduce concetti di **feedback immediato** e **stato di gioco**, fondamentali per qualsiasi gioco interattivo.

---

### 3. Collisioni

Le collisioni sono fondamentali per determinare:

- Quando un guscio tocca Mario.  
- Come reagire all’impatto (perdita di vita, rimozione del guscio).  

> È importante distinguere tra **collisione logica** (variabile vite) e **collisione visiva** (sprite e animazioni).

---

### 4. Gestione del tempo

I gusci cadono a intervalli regolari, non tutti contemporaneamente.  
Per controllare il tempo di generazione dei gusci si utilizza un **timer interno al gioco**.  

- La gestione del tempo permette di creare **ritmi di gioco variabili** e di aumentare la difficoltà gradualmente.  
- Concetto chiave: ogni azione nel gioco può dipendere dal **passare dei millisecondi**, non solo dal numero di frame.

---

### 5. Schermata di Game Over e iterazione

Quando le vite finiscono:

- Lo schermo diventa **nero** o mostra un messaggio di Game Over.  
- Il gioco **attende l’input dell’utente** (premere R) per riavviare.  
- Tutti gli oggetti in gioco (Mario, gusci, piattaforme) vengono **resettati allo stato iniziale**.

> Questo introduce la logica di **iterazione condizionata**: il gioco può fermarsi, attendere input e ripartire senza chiudere l’applicazione.

---

## Approfondimenti teorici

1. **Dinamiche di gioco**  
   L’aggiunta di gusci e vite trasforma il gioco da un semplice platform a un’esperienza dinamica, dove il giocatore deve **monitorare continuamente il proprio stato e l’ambiente circostante**.

2. **Feedback visivo e psicologia del giocatore**  
   - Le vite visibili aiutano a comprendere la gravità di ogni errore.  
   - La schermata nera di Game Over crea **tensione** e stimola la **motivazione a riprovare**.

3. **Iterazione e loop di gioco**  
   - Ogni elemento (Mario, gusci, piattaforme) viene aggiornato ad ogni ciclo di gioco.  
   - Questo è un esempio pratico di **programmazione reattiva e basata sugli eventi**.

---

## Esercizi challenge

1. Modifica il numero di vite e osserva come cambia la difficoltà del gioco.  
2. Aumenta la frequenza dei gusci cadenti o varia la loro velocità.  
3. Aggiungi effetti visivi o sonori quando Mario perde una vita.  
4. Prova a implementare un **guscio “bonus”** che aumenta le vite se colpito.  

---

## Riepilogo

In questa lezione abbiamo approfondito:

- Gusci cadenti e generazione casuale degli ostacoli.  
- Iterazione di Mario e interazione con gli oggetti del gioco.  
- Sistema di vite visivo e funzionale.  
- Schermata nera di Game Over con possibilità di ripartenza tramite **R**.  
- Concetti di loop di gioco, collisioni e gestione del tempo.

Nella **Lezione 4** aggiungeremo:

- La **Principessa Peach** e **Donkey Kong** come personaggi interattivi.  
- La **schermata di vittoria**.  
- Un **menu iniziale** interattivo.

[Continua alla Lezione 4 →](../Lezione_4/Lezione_4.md)
