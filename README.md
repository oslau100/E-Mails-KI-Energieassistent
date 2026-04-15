# Email System – Tarif Funnel (DACH)

Dieses Repository enthält ein skalierbares HTML-Email-System für GoHighLevel (Phase 1: Deutsch).

## Ziel
- höhere Open Rate durch klare, relevante Betreffzeilen
- höhere Click Rate durch kontextstarke, konkrete CTA-Einleitung
- höhere Conversion durch logische Brücken statt Beruhigungsfloskeln
- Vertrauen aufbauen, ohne künstliche Dringlichkeit

## Szenarien
- spart (10)
- spart_nicht (4)
- neueinzug (10)
- loop (15)

## `{{ opportunity.savings_text }}` (verbindlich)
- neueinzug = unnötige Mehrkosten beim Start
- spart_nicht = gut und sinnvoll eingestellt
- low = etwas mehr als nötig
- mid = spürbar mehr als nötig
- high = mehrere hundert Euro pro Jahr zu viel
- very_high = über 500€ pro Jahr zu viel

### Pflicht-Satzlogik
- spart: `Du zahlst aktuell {{ opportunity.savings_text }}` oder `Das bedeutet für dich: {{ opportunity.savings_text }}`
- spart_nicht: `Dein {{ opportunity.energieart }}-Tarif ist aktuell {{ opportunity.savings_text }}` oder `Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}`
- neueinzug: `So vermeidest du {{ opportunity.savings_text }}` oder `Beim Umzug vermeidest du {{ opportunity.savings_text }}`

## CTA-Regel
Jede Email enthält genau **einen** CTA-Link im Body.

### Standard-CTA
- Ziel: `{{ opportunity.offer_url }}`
- Framing: Empfehlung ist bereits auf Basis der Angaben vorbereitet
- Sprache: „jetzt Empfehlung ansehen“, nicht „allgemein prüfen“

### Referral-CTA
- nur in ausgewählten Loop-Mails
- Ziel: `{{ contact.empfehlungslink }}`
- Ton: mission-led, hilfreich, nicht affiliate-lastig

## Conversion-Brücken (statt Beruhigungsfloskeln)
In Nicht-Referral-Mails keine generischen „kein Druck“-Sätze verwenden.

Verboten als generische Brücke:
- „Du musst nichts überstürzen.“
- „Du entscheidest danach in Ruhe.“
- „Der Check verpflichtet dich zu nichts.“
- „Wenn kein Vorteil da ist, bleibt alles wie es ist.“

Stattdessen: kurze Logik-Brücken mit
- Vergleich
- Konsequenz
- schnellem nächstem Schritt
- Kontext (z. B. Umzug, Preisänderung, Planbarkeit)

## Form-Regeln
- plain, text-first, persönlich
- keine Buttons
- keine Body-Bilder
- kein Newsletter-Layout
- Signatur bleibt subtil und konsistent

## Qualitätsregeln für Subject/Preheader
- klar, persönlich, konkret
- keine Fake-Transaktion, kein Fake-Support, keine Fake-Dringlichkeit
- hohe Strukturvielfalt über die Sequenzen
- Preheader ergänzt Betreff inhaltlich

## Variablen
Siehe `specs/ghl-variables.md`.
