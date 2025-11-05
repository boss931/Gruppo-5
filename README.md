# Gruppo-5
DAL PARADIGMA PROCEDURALE ALLA OOP

**Titolo progetto:** *Salva la Principessa – Corso in 4 lezioni per creare un videogioco con Python e Pygame*

# Salva la Principessa - Videogioco in Python con Pygame

Questo progetto è un corso diviso in 4 lezioni che guida passo dopo passo nella creazione di un videogioco in Python utilizzando la libreria **Pygame**.

Alla fine del corso avrai sviluppato un vero videogioco chiamato **"Salva la Principessa"**, ispirato alle meccaniche platform: il giocatore controlla Mario, salta sulle piattaforme evitando ostacoli e deve raggiungere la principessa per vincere la partita.

---

## Obiettivo del gioco
- Controlli **Mario**
- Devi raggiungere **la principessa Peach**
- Devi evitare **i gusci che cadono dall’alto**
- Hai **3 vite**. Se le perdi tutte → *Game Over*
- Se raggiungi Peach → *Hai vinto*

---

## Contenuto del corso

| Lezione | Argomento | Cosa impari |
|---------|-----------|-------------|
| **Lezione 1** | Creazione finestra e movimento del personaggio | Come avviare Pygame, creare la finestra e far muovere Mario |
| **Lezione 2** | Piattaforme e gravità | Mario può saltare e camminare sulle piattaforme |
| **Lezione 3** | Ostacoli e vite | Implementazione dei gusci cadenti e sistema delle vite |
| **Lezione 4** | Menu + Vittoria e Game Over | Schermata iniziale, fine partita e codice finale completo |

---

## Struttura dei file

```

📁 salva_la_principessa/
│
├── Lezione_1.md
├── Lezione_2.md
├── Lezione_3.md
├── Lezione_4.md
├── salva_la_principessa.py      <-- codice finale completo
│
├── mario.png
├── peach.png
├── orso.png
├── sfondo.png
├── blocco.png
├── guscio.png
└── fungo.png

````

> Tutte le immagini devono trovarsi nella stessa cartella del file `.py`.

---

## Tecnologie utilizzate
- **Python 3.x**
- **Pygame** (per grafica, eventi e gestione input)
- Struct `pygame.Rect` per collisioni e gestione personaggi/oggetti

Per installare Pygame:

```bash
pip install pygame
````

---

## Avvio del gioco

Esegui:

```bash
python salva_la_principessa.py
```

---

## Funzionamento del gioco

| Tasto             | Azione                    |
| ----------------- | ------------------------- |
| Frecce ← →        | Muovi il personaggio      |
| Barra Spaziatrice | Salto                     |
| Invio             | Avvia la partita dal menu |

---

## Cosa imparerai realmente

Durante il corso imparerai a:

* Gestire input da tastiera
* Usare le immagini in un videogioco
* Implementare la gravità
* Gestire collisioni tra oggetti
* Creare un ciclo di gioco completo

Questi concetti sono **alla base dello sviluppo dei videogiochi**.

---

## Crediti e utilizzo

Puoi usare questo progetto:

* per imparare Python
* come base per creare altri platform game
* come progetto scolastico / portfolio

---

Buon divertimento con il tuo gioco!
**E ricorda: salva la principessa!**

[Inizia con la Lezione 1→](../main/Lezione_1/Lezione_1.md)
