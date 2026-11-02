---
titolo: Installazione e configurazione
prodotto: VentOSC
ordine: 1
---

## Cosa serve

- Scheda **WT32-ETH01**
- Adattatore **USB-seriale** (3.3 V) collegato a TX0 / RX0 / GND della scheda
- Un PC Windows per il flash (il pacchetto include `esptool.exe`, non va installato nulla)

## Flash del firmware

1. Metti la scheda in modalità boot: ponticella **IO0 a GND**, poi alimenta.
2. Apri la cartella `VentOSC_Flash` e lancia `FLASH_VentOSC.bat`.
3. Lo script elenca le porte COM disponibili: scrivi quella dell'adattatore (es. `COM3`) e premi Invio.
4. A fine scrittura togli il ponticello e riavvia la scheda.

`FLASH_FACTORY_RESET.bat` fa la stessa cosa ma cancella prima tutta la memoria, riportando la configurazione ai valori di fabbrica. Usalo se hai perso la password dell'access point o l'IP Ethernet.

## Primo accesso

Appena accesa, la scheda apre una rete WiFi:

| | |
|---|---|
| SSID | `VentOSC` |
| Password | `ventosc1` |
| Pagina di controllo | `http://192.168.4.1` |

Collega il telefono a quella rete e apri l'indirizzo. In alto c'è lo slider, in basso il pulsante **Settings** apre la configurazione.

## Configurazione

Tutto si salva da **Settings → Save & Reboot**. La scheda si riavvia da sola.

**OSC**
- *Port* — porta UDP di destinazione (default `8000`)
- *Address* — indirizzo del messaggio (default `/master`). Il payload è un singolo float.

**Target IPs**
- Fino a 6 indirizzi. Lascia vuoti quelli che non usi. Lo stesso messaggio parte verso tutti, 20 volte al secondo.

**Ethernet (LAN)**
- *DHCP* oppure *Static* con IP, subnet e gateway. Di fabbrica è statico su `192.168.11.1 / 255.255.255.0`.
- L'OSC esce sempre dalla porta Ethernet, mai dal WiFi.

**Access Point (WiFi)**
- SSID e password della rete di controllo. L'indirizzo della pagina resta `192.168.4.1`.

**Knob**
- *Enable* — se spento, il potenziometro viene ignorato anche se collegato.
- *Min / Max* — il range di uscita. Lo slider lavora sempre 0–1 e viene rimappato: con `Min 1` e `Max 0` ottieni un fader invertito, con `Min 0` e `Max 255` un valore 8 bit.

## Potenziometro (opzionale)

Un potenziometro lineare da 10 kΩ: estremi a **3.3 V** e **GND**, cursore su **GPIO35**.

All'avvio la scheda campiona l'ingresso per 100 ms: se legge un valore stabile considera il knob presente e lo attiva; se il pin è flottante lo disattiva e comanda solo lo slider. Se vuoi che il knob venga riconosciuto, deve essere collegato *prima* di dare alimentazione.

Quando il knob è attivo il suo valore viene inviato anche alla pagina web, quindi lo slider sul telefono lo segue.

## Verifica

Apri `http://192.168.4.1/info` (o lo stesso percorso sull'IP Ethernet): mostra IP, stato del link, se la socket UDP è attiva, se il knob è stato rilevato e la lista dei target. È la prima cosa da guardare se l'OSC non arriva.

## Problemi comuni

- **L'OSC non arriva** — controlla su `/info` che `ETH link` sia `up` e `UDP bound` sia `yes`. Se il link è down, è il cavo o lo switch; se l'IP è `0.0.0.0`, in modalità DHCP nessuno ha risposto.
- **Lo slider non risponde** — in alto la pagina mostra ● Connected / Disconnected. Se è disconnessa si riconnette da sola ogni 2 secondi; se non lo fa, ricarica la pagina.
- **Ho perso la password** — `FLASH_FACTORY_RESET.bat`.
