# Email System – Tarif Funnel (DACH)

Dieses Repository enthält ein skalierbares HTML-Email-System für GoHighLevel.

## Ziel
Dieses System soll:
- Open Rate durch klare, persönliche Betreffzeilen und Preheader erhöhen
- Click Rate durch use-case-klare CTA-Sprache erhöhen
- Conversion durch Relevanz, Kontext und Einwandbehandlung verbessern
- Vertrauen aufbauen und langfristig halten
- später sauber mehrsprachig ausgerollt werden können

## Mission
Wir unterstützen Haushalte dabei, mehr Transparenz bei Strom- und Gastarifen zu gewinnen.
Unser Ziel ist Klarheit statt Tarifchaos.

## Szenarien
- spart
- spart_nicht
- neueinzug
- loop

## Sequenz-Struktur
- spart = 10 Emails
- neueinzug = 10 Emails
- spart_nicht = 4 Emails
- loop = 15 Emails

## `{{ opportunity.savings_text }}` (final)
Diese Werte sind verbindlich und dürfen nicht verändert werden.

- `neueinzug` = `unnötige Mehrkosten beim Start`
- `spart_nicht` = `gut und sinnvoll eingestellt`
- `low` = `etwas mehr als nötig`
- `mid` = `spürbar mehr als nötig`
- `high` = `mehrere hundert Euro pro Jahr zu viel`
- `very_high` = `über 500€ pro Jahr zu viel`

### Satzlogik pro Segment
- `spart`: `Du zahlst aktuell {{ opportunity.savings_text }}` oder `Das bedeutet für dich: {{ opportunity.savings_text }}`
- `spart_nicht`: `Du bist aktuell {{ opportunity.savings_text }}` oder `Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}`
- `neueinzug`: `So vermeidest du {{ opportunity.savings_text }}` oder `Beim Umzug vermeidest du {{ opportunity.savings_text }}`

## CTA-Regel (final)
Jede Email enthält genau einen CTA-Link im Body.

### Standard
Die meisten Emails verlinken auf:
- {{ opportunity.offer_url }}

### Business-Logik hinter Standard-CTA
Die Person hat bereits eine persönliche Empfehlung angefordert.
Daher CTA-Meaning in Nicht-Referral-Mails:
- wir haben bereits auf Basis der Angaben eine sichere {{ opportunity.energieart }}-Empfehlung ermittelt
- Empfehlung jetzt direkt ansehen
- Klarheit/Sicherheit vor allgemeinem „erstmal prüfen“-Framing

### Referral / Empfehlungsprogramm
Nur ausgewählte Loop-Emails nutzen Empfehlungs-CTAs über:
- {{ contact.empfehlungslink }}

Diese Emails müssen mission-led und hilfreich bleiben (nicht money-first).

## Design-Prinzip
Die Emails sollen wie persönliche Nachrichten wirken:
- textbasiert
- schlicht
- direkt

### Deshalb gilt
- keine Buttons
- keine Bilder im Body
- kein komplexes Marketing-Layout
- nur ein CTA-Link im Body
- Signatur ist das einzige leicht formatierte Element (inkl. kleinem Logo)

## Verwendete GHL Variablen
Siehe `specs/ghl-variables.md`.

## Final Messaging-Standards
- In jeder Nicht-Referral-Mail muss {{ opportunity.energieart }} im Body stehen.
- Zusätzlich muss {{ opportunity.energieart }} im Subject oder Preheader stehen.
- Zusätzliche Zeilen nur selektiv, wenn sie Kontext + Einwandbehandlung verbessern.
- Verboten: fake-transaktionale, irreführende oder unklare Formulierungen (z. B. „dein aktueller Stand“).

### Bridge-Line-Regel (Conversion)
- Keine generischen Beruhigungsphrasen wie "Du musst nichts überstürzen" oder "Der Check verpflichtet dich zu nichts".
- Stattdessen kurze, logische Brücken nutzen: Vergleich, Konsequenz, nächster sinnvoller Schritt.
