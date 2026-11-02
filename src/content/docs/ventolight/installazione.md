---
titolo: Installazione e configurazione
prodotto: VentoLight
ordine: 1
---

## Cosa serve

- **ESP32 Dev Module** (ESP-WROOM-32) con porta USB
- Sensore **AS7265x**
- Opzionale, per il DMX: transceiver **RS-485** (MAX485 o SN75176) e un connettore XLR
- Un PC Windows o un Mac per il flash

## Cablaggio

**Sensore AS7265x** (tutto a 3.3 V):

| ESP32 | AS7265x |
|---|---|
| 3V3 | VCC / 3V3 |
| GND | GND |
| GPIO4 | SDA |
| GPIO5 | SCL |

Gli altri pin del modulo (INT, RST, TX, RX) non servono.

**Uscita DMX** (transceiver RS-485):

| ESP32 | Transceiver |
|---|---|
| GPIO17 | DI |
| GPIO21 | DE e /RE, uniti |
| GND | GND |

A e B del transceiver vanno ai pin 3 e 2 dell'XLR, GND al pin 1.

## Flash del firmware

Il flasher è un programma autonomo: contiene il firmware, non richiede Python, Arduino o esptool.

1. Collega l'ESP32 via USB. Se non compare nessuna porta COM / seriale, installa il driver USB dalla cartella `Drivers` del pacchetto.
2. Avvia `VENTOLIGHT_Flasher.exe` (Windows) o `VENTOLIGHT_Flasher.app` (macOS; al primo avvio tasto destro → *Apri* se Gatekeeper lo blocca).
3. Scegli la porta.
4. Lascia spento *Erase board before flashing* per un aggiornamento normale; accendilo per una pulizia completa.
5. Premi **Flash**.

## Primo accesso

Appena accesa, la scheda apre una rete WiFi:

| | |
|---|---|
| SSID | `VENTOLIGHT` |
| Pagina di controllo | `http://4.3.2.1` |

La password è stampata nel pacchetto del flasher. Collega telefono o PC a quella rete e apri l'indirizzo.

## La pagina web

**Monitor** — stato del sensore, indice di intensità, classificazione cool / neutral / warm con barra warmth, bucket 1..10, temperatura del sensore e spettro delle 12 bande visibili. Se il sensore non è rilevato, il monitor mostra il risultato della scansione I²C per capire se è un problema di cablaggio.

**DMX Triggers** — la griglia dei trigger. Di fabbrica ce ne sono 9: tre fasce di intensità × tre di colore, tutti sul canale 1 con valori da 1 a 9. Per ognuno puoi cambiare canale e valore DMX, poi *Save*. I range di intensità e colore sono la griglia fissa: ogni trigger copre una fascia di intensità (bassa / media / alta) e una di colore (cool / neutral / warm). Con **+** e **−** aggiungi o togli trigger (fino a 18). Il trigger attivo si accende; premendone uno lo **forzi manualmente** — utile per provare le cue del recorder senza aspettare la luce giusta. Premilo di nuovo per tornare in automatico.

**OSC** — indirizzo IP di destinazione (default broadcast `4.3.2.255`), porta (`9000`), address (`/ventolight/light`) e i 4 slot del messaggio. Ogni slot può essere: `intensity`, `warmth`, `trigger`, `temperature`, `bucket`, `cool`, `green`, `warm`. *Save OSC* applica subito.

Tutto quello che salvi (trigger, numero di trigger, OSC) resta in memoria anche spegnendo la scheda. Per tornare ai valori di fabbrica, flasha con *Erase board before flashing* acceso.

## Come ragiona il DMX

La scheda trasmette un frame DMX completo in continuo (~30 fps). Tutti i canali sono a 0 tranne quello del trigger attivo, che vale il numero impostato. Se nessun trigger corrisponde alla lettura, il frame è tutto a 0.

Su un recorder tipo VentoNet basta assegnare a ogni valore una cue: la luce cambia, cambia il trigger, cambia la cue.

## Calibrare nello spazio

L'indice di intensità **non è in lux**: è un numero relativo ricavato dalle bande visibili. Il modo giusto di impostare le soglie è stare nello spazio dell'installazione nei momenti che contano (mattina, sera, luci accese, luci spente), leggere i valori sul Monitor e scrivere i range dei trigger di conseguenza. Tienili un po' larghi: la luce oscilla.

## Problemi comuni

- **Sensore non rilevato** — controlla 3.3 V e GND, poi SDA su GPIO4 e SCL su GPIO5 (sui moduli i pin sono spesso etichettati TX/RX). Il Monitor mostra gli indirizzi I²C trovati: se c'è `0x49`, il sensore risponde.
- **Temperatura "too hot" / "too cold"** — il sensore è fuori dal suo range di lavoro; la misura resta valida ma meno affidabile.
- **Il DMX non arriva** — verifica DE+/RE su GPIO21 e DI su GPIO17, e che A/B non siano invertiti sull'XLR.
