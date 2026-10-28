# PONG — Huisstijl

Versie 1.0 · oktober 2026 · Van toepassing op: spel (`index.html`), handleiding, PDF en GitHub-pagina

> **Merkbelofte:** *De klassieker, opnieuw uitgevonden — voor 1 tot 8 spelers.*
> PONG is retro in uitstraling, modern in gebruik: donker speelveld, neonaccenten, één scherm, geen installatie.

---

## 1. Logo

| Variant | Bestand | Gebruik |
|---|---|---|
| Primair logo (donkere achtergrond) | `assets/logo.svg` | Websiteheader, PDF-cover, presentaties op donkere achtergrond |
| Logo voor lichte achtergrond | `assets/logo-licht.svg` | Documenten en webpagina's met witte/lichte achtergrond |
| Icoon | `assets/logo-icon.svg` | Favicon, app-icoon, sociale media, kleine formaten |

**Opbouw:** het icoon toont het speelveld in vogelperspectief — een groene peddel (links), een blauwe peddel (rechts), de witte bal en de gestippelde middenlijn, in een afgerond indigo vlak. Het woordmerk `PONG` staat in hoofdletters met brede letterspatiëring; de **N is altijd Neon Groen**.

**Regels:**

- Vrije ruimte rond het logo: minimaal de hoogte van de bal (de `x` in het icoon) aan alle zijden.
- Minimale breedte: 120 px (primair logo), 24 px (icoon).
- Niet uitrekken, roteren, vervormen of van schaduw/omlijning voorzien.
- Geen andere kleuren gebruiken dan het palet hieronder; de groene `N` nooit weghalen.
- Op foto's of drukke achtergronden: plaats het icoon op een vlak in Nachtblauw (`#0F0F1A`) of Speelveld Indigo (`#12122B`).

## 2. Kleuren

### Basispalet

| Naam | Hex | RGB | Gebruik |
|---|---|---|---|
| Nachtblauw | `#0F0F1A` | 15, 15, 26 | Pagina-achtergrond |
| Speelveld Indigo | `#12122B` | 18, 18, 43 | Speelveld, logo-vlak, kaarten |
| Rand Indigo | `#3A3A5C` | 58, 58, 92 | Randen, scheidingslijnen |
| Neon Groen | `#4ADE80` | 74, 222, 128 | Primair: Speler 1 links, hoofdknop, de `N` in het logo |
| Arcade Blauw | `#60A5FA` | 96, 165, 250 | Secundair: Speler 2 / computer rechts |
| Sterrenwit | `#EEEEEE` | 238, 238, 238 | Tekst en bal op donkere achtergrond |
| Gedimd Paarsgrijs | `#9A9AB8` | 154, 154, 184 | Bijtekst, onderschriften, hulptekst |

### Spelerspalet (modus 8 spelers)

Elke speler heeft een vaste kleur, altijd gecombineerd met een spelersnummer (P1–P8) zodat kleur nooit de enige informatie is:

| Speler | Kleur | Hex |
|---|---|---|
| P1 | Neon Groen | `#4ADE80` |
| P2 | Turkoois | `#2DD4BF` |
| P3 | Arcade Blauw | `#60A5FA` |
| P4 | Paars | `#A78BFA` |
| P5 | Oranje | `#FB923C` |
| P6 | Roze | `#F472B6` |
| P7 | Geel | `#FACC15` |
| P8 | Rood | `#F87171` |

Uitgeschakelde spelers worden altijd grijs (`#3A3A3A`) weergegeven.

## 3. Typografie

| Element | Lettertype | Stijl |
|---|---|---|
| Koppen en logo | `'Segoe UI', Arial, sans-serif` | Vet (700), hoofdletters, letterspatiëring 0,35 em voor de hoofdtitel |
| Lopende tekst | `'Segoe UI', Arial, sans-serif` | Normaal (400), 1 rem |
| Scores en cijfers | Zelfde lettertype | `font-variant-numeric: tabular-nums`, vet, zodat cijfers niet verspringen |
| Code en toetsen | Systeemfont in `<kbd>`-stijl | Achtergrond `#2A2A48`, rand `#4A4A70`, afgeronde hoeken 4 px |

Er worden geen externe (web)fonts geladen: het spel werkt volledig offline en zonder installatie.

## 4. Vormtaal en componenten

- **Afgeronde hoeken:** 6 px (peddels), 8 px (knoppen en chips), 10 px (speelveld en overlays). Nooit scherpe hoeken op interactieve elementen.
- **Knoppen:** achtergrond `#1E1E32`, rand 1 px Rand Indigo, tekst Sterrenwit. Actieve modusknop: volledig Neon Groen met Nachtblauw tekst.
- **Overlay (start/pauze/einde):** Nachtblauw met 72% dekking over het speelveld, gecentreerde tekst, één duidelijke hoofdknop.
- **Spelers-chips (8 spelers):** rand van 2 px in de spelerskleuren, nummer + positie + levens + besturing in één oogopslag.
- **Iconografie:** alleen vormen uit het spel zelf (peddel, bal, middenlijn). Geen stockiconen.

## 5. Toon en taal

- **Taal:** Nederlands, korte zinnen, vriendelijk en direct ("Druk op Spatie om te beginnen").
- **Aanspreking:** je-vorm, geen jargon; speltermen (peddel, serveer, leven) worden bij eerste gebruik uitgelegd in de handleiding.
- **Hoofdletters** alleen voor de merknaam PONG en voor statussen in het spel (bijv. `GEPAUZEERD`).

## 6. Toegankelijkheid

- Tekst heeft minimaal contrastniveau AA op Nachtblauw (Sterrenwit en Gedimd Paarsgrijs voldoen).
- Kleur is nooit de enige drager van informatie: spelers hebben ook een nummer (P1–P8) en een positielabel.
- Het volledige spel is met het toetsenbord te bedienen; alle modi zijn zonder muis speelbaar.

## 7. Bestanden

| Bestand | Inhoud |
|---|---|
| `assets/logo.svg` | Primair logo |
| `assets/logo-licht.svg` | Logo voor lichte achtergrond |
| `assets/logo-icon.svg` | Icoon / favicon |
| `huisstijl.md` | Dit document |
| `handleiding.md` | Gebruikershandleiding (Markdown) |
| `docs/huisstijl-en-handleiding.html` | Printklare webversie van huisstijl + handleiding |
| `Pong-Huisstijl-en-Handleiding.pdf` | Gegenereerde PDF (zie `scripts/maak-pdf.py`) |
