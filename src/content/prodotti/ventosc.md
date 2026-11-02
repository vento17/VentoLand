---
nome: VentOSC
tagline: Un fader master OSC in una scatolina. Slider sul telefono o potenziometro fisico → OSC via Ethernet a 20 Hz, verso fino a 6 destinazioni.
tipo: firmware
stato: beta
prezzo: gratis
docs_url: /docs/ventosc/installazione
piattaforme: [ESP32 WT32-ETH01]
tags: [esp32, firmware, free]
ordine: 2
---

## Cos'è

VentOSC trasforma un WT32-ETH01 (ESP32 con Ethernet) in un controllo master remoto: un singolo valore, da 0 a 1, che esce come messaggio OSC `/master` su UDP verso fino a sei indirizzi IP contemporaneamente.

Il valore lo muovi in due modi, anche insieme:

- **Dal telefono.** La scheda apre un access point WiFi (`VentOSC`), ti colleghi, apri `192.168.4.1` e trovi uno slider verticale a tutto schermo. Nessuna app da installare.
- **Da un potenziometro.** Un knob sull'ingresso analogico, rilevato automaticamente all'avvio: se c'è, comanda lui e lo slider sul telefono lo segue in tempo reale.

L'OSC viaggia sulla porta Ethernet, separata dal WiFi di controllo, così non rubi banda alla rete di show.

## Perché

Perché un master dimmer per i driver LED su una rete Art-Net non dovrebbe richiedere un computer acceso. VentOSC è il "volume generale" che resta attaccato al rack: lo giri, i VentoLed / VentoNet o qualunque cosa ascolti OSC si abbassano insieme.

## Caratteristiche

- Stream OSC continuo a 20 Hz (un float, indirizzo e porta configurabili, default `/master` su 8000)
- Fino a 6 destinazioni IP in parallelo
- Ethernet con IP statico o DHCP, hostname `ventosc`
- Access point WiFi con SSID e password personalizzabili
- Knob con range di uscita impostabile (min / max, anche invertito) e smoothing
- Tutta la configurazione dalla pagina web, salvata in memoria non volatile
- Pagina `/info` con stato link, IP, target e knob per il debug al volo

## Requisiti

- Una scheda WT32-ETH01
- Un adattatore USB-seriale per il primo flash
- Opzionale: potenziometro 10 kΩ tra 3.3 V, GND e GPIO35

## Stato

Beta. Il firmware funziona ed è in uso; manca solo il giro di prova su più impianti prima di chiamarlo stabile. Si installa con il flasher incluso, senza ambiente di sviluppo.
