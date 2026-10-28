# PONG

> **De klassieker, opnieuw uitgevonden — voor 1 tot 8 spelers.**

![PONG logo](assets/logo.svg)

Een Pong-spel dat volledig in de browser draait: één HTML-bestand, geen installatie, geen internet nodig. Met een modus voor 1 speler tegen de computer, 2 spelers op één scherm, en een **Battle Royale voor 8 spelers** — twee peddels per zijde, 3 levens per speler, laatste overblijver wint.

## Spelen

Open `index.html` in een moderne browser (Chrome, Edge, Firefox, Safari) en klik op **Speel** — of druk op `Spatie`.

| Modus | Zo werkt het |
|---|---|
| 1 speler | Links tegen de computer; 4 moeilijkheidsgraden, eerste tot 10 punten |
| 2 spelers | `W`/`S` tegen de pijltjestoetsen, eerste tot 10 punten |
| 8 spelers | Battle Royale: klik op een spelers-chip om mens ↔ computer te wisselen |

Volledige besturing, spelregels, tips en probleemoplossing staan in de **handleiding**.

## Documentatie

| Document | Inhoud |
|---|---|
| [`handleiding.md`](handleiding.md) | Gebruikershandleiding |
| [`huisstijl.md`](huisstijl.md) | Huisstijl: logo, kleurenpalet, typografie, vormtaal en toon |
| [`Pong-Huisstijl-en-Handleiding.pdf`](Pong-Huisstijl-en-Handleiding.pdf) | Printbare PDF met huisstijl én handleiding (6 pagina's) |
| [`docs/huisstijl-en-handleiding.html`](docs/huisstijl-en-handleiding.html) | Web-/printversie waarvan de PDF is gemaakt |

Dezelfde huisstijl wordt overal gebruikt: het logo staat in het spel en als favicon, en de kleuren uit `huisstijl.md` zijn als variabelen (`--groen`, `--blauw`, `--nachtblauw`, …) in het spel vastgelegd.

## Bestanden

```
index.html                              het spel (zelfstandig, geen dependencies)
assets/logo.svg                         primair logo
assets/logo-licht.svg                   logo voor lichte achtergronden
assets/logo-icon.svg                    icoon / favicon
huisstijl.md                            huisstijlgids
handleiding.md                          gebruikershandleiding
docs/huisstijl-en-handleiding.html      printklare huisstijl + handleiding
Pong-Huisstijl-en-Handleiding.pdf       gegenereerde PDF
scripts/maak-pdf.py                     regenereert de PDF (Chrome headless)
```

## PDF opnieuw genereren

```powershell
python scripts/maak-pdf.py
```

Vereist Google Chrome (of Edge). Het script drukt `docs/huisstijl-en-handleiding.html` af naar `Pong-Huisstijl-en-Handleiding.pdf`, in de PONG-huisstijl.

## Techniek

Vanilla HTML/CSS/JavaScript met canvas en Web Audio voor de geluidseffecten. Geen frameworks, geen build-stap, geen tracking — alles draait lokaal.
