# VentoLand · ventoland.it

Sito di VentoLand. Statico, costruito con [Astro](https://astro.build), pubblicato su Cloudflare Pages a ogni push su `main`.

## Come aggiorno il sito (senza sapere programmare)

Tutto il contenuto è in file di testo `.md` dentro `src/content/`. Li modifichi direttamente su GitHub (icona matita) o sul PC, fai commit, e in un minuto il sito è aggiornato.

### Aggiungere / modificare un prodotto
Un file per prodotto in `src/content/prodotti/`. Il nome del file è l'indirizzo della pagina (`maestrale.md` → `ventoland.it/prodotti/maestrale`).

```md
---
nome: Maestrale
tagline: Una riga che dice cosa fa.
tipo: software          # software | firmware | hardware
stato: disponibile      # disponibile | beta | in-arrivo
prezzo: 49 €
buy_url: https://...    # link checkout Lemon Squeezy (quando c'è)
piattaforme: [Windows]
immagine: /img/maestrale.jpg
ordine: 1               # ordine nella griglia
---
Testo libero in markdown: cos'è, a chi serve, caratteristiche, requisiti.
```

### Aggiungere uno spettacolo in "Sul campo"
Un file per lavoro in `src/content/campo/`. Copia `esempio-spettacolo.md`, rinominalo, cambia i dati.

```md
---
titolo: Nome spettacolo
data: 2026-06-15
luogo: Teatro X, Città
ruolo: Lighting designer
prodotti: [maestrale, ventonet]   # nomi file dei prodotti usati
video: https://youtu.be/...       # opzionale, YouTube o Vimeo
galleria: [/img/show-1.jpg, /img/show-2.jpg]
---
Due righe su cosa è successo.
```

### Carosello in home
Metti le foto in `public/img/hero/` (jpg/png/webp, 1600 px di larghezza, formato 16:9). Vanno in ordine alfabetico: `01-tour.jpg`, `02-maestrale.png`...

### Immagini e video
Mettili in `public/img/` e `public/video/`. Nel testo li richiami come `/img/nomefile.jpg`. Tieni le foto sotto 500 KB (ridimensiona a 1600 px di larghezza).
Il video in home: `public/video/hero.mp4`, poi sostituisci il blocco segnaposto in `src/pages/index.astro`.

### Documentazione
File `.md` in `src/content/docs/<prodotto>/`. Campi in cima: `titolo`, `prodotto`, `ordine`.

### Testi fissi
- Home: `src/pages/index.astro`
- About / contatti: `src/pages/about.astro`
- Colori e font: `src/styles/global.css`

## Sviluppo in locale (opzionale)
```
npm install
npm run dev      # anteprima su http://localhost:4321
npm run build    # genera dist/
```

## Deploy
Cloudflare Pages collegato a questo repo. Build command `npm run build`, output `dist`. Ogni push su `main` va online.
