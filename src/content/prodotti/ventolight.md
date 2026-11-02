---
nome: VentoLight
tagline: Sensore di luce spettrale che legge intensità e temperatura colore dell'ambiente e li trasforma in trigger DMX e OSC. Per installazioni che reagiscono alla luce reale.
tipo: firmware
logo: /logo/prodotti/ventolight.jpg
stato: beta
prezzo: gratis
docs_url: /docs/ventolight/installazione
piattaforme: [ESP32 WROOM-32]
tags: [esp32, firmware, free]
ordine: 6
---

## Cos'è

VentoLight è un ESP32 con un sensore spettrale **AS7265x** (18 bande, da 410 a 940 nm). Ogni secondo circa legge la luce che arriva davvero nello spazio e ne ricava due numeri: un **indice di intensità** e un valore di **warmth** da 0 a 1 (cool / neutral / warm).

Da quei due numeri decide in quale **trigger** si trova — una griglia configurabile di fasce intensità × colore — e lo comunica in due modi:

- **DMX512** in uscita (RS-485), con un canale e un valore per ogni trigger: perfetto per richiamare le cue di un recorder come VentoNet.
- **OSC** in broadcast sulla sua rete WiFi, con fino a 4 valori a scelta (intensità, warmth, trigger, temperatura, bande singole).

Tutto si vede e si regola da una pagina web ospitata dalla scheda: monitor live con spettro a 12 bande, griglia dei trigger con soglie modificabili, forzatura manuale di un trigger per provare le cue, configurazione OSC.

## Perché

Perché un'installazione in un museo o in una mostra vive con la luce del posto: mattina, pomeriggio, nuvole, faretti accesi o spenti. VentoLight è l'occhio che permette allo spettacolo di accorgersene, senza un PC e senza calibrare luxmetri: si fissano le soglie sul posto, guardando i valori reali.

Nasce per un allestimento in Marocco, dove doveva reagire sia a quanta luce c'era sia al suo colore.

## Caratteristiche

- Sensore spettrale AS7265x via I²C, LED di bordo spenti per non inquinare la misura
- Indice di intensità relativo + warmth 0..1 + bucket 1..10 + temperatura interna del sensore
- Fino a 18 trigger configurabili (canale DMX, valore, range intensità, range colore)
- Uscita DMX continua a 250 kbaud con la stessa logica di VentoNet
- OSC UDP in broadcast, indirizzo/porta/slot configurabili
- Access point WiFi autonomo con pagina web di monitor e configurazione
- Flasher standalone per Windows e macOS: non serve installare nulla sul PC

## Requisiti

- ESP32 Dev Module / ESP-WROOM-32 con USB
- Modulo sensore AS7265x (SparkFun o compatibile)
- Per il DMX: un transceiver RS-485 (MAX485 / SN75176)

## Stato

Beta. Firmware funzionante e flasher pronto. Le soglie dei trigger e la configurazione OSC per ora si impostano a ogni accensione: la memoria permanente è il prossimo passo.
