# Messaging Framework

## Grundprinzip
Kommunikation für den deutschen DACH-Energiemarkt: klar, vertrauenswürdig, handlungsstark.

## Performance-Ziele
- höhere Open Rate über inbox-starke Betreffzeilen
- höhere Klickrate über use-case-präzise CTA-Sprache
- höhere Conversion über Kontext, Sicherheit und Einwandbehandlung

## Form-Prinzip
Die Emails sollen wie persönliche Nachrichten wirken, nicht wie Newsletter.

Pflicht:
- textbasiert
- schlicht
- persönlicher Ton
- CTA als normaler Hyperlink

Verboten:
- Buttons
- Bilder im Body
- Banner/Boxen
- komplexes Marketing-Layout
- fake-transaktionale Betreffmuster ("deine Anfrage", "wir warten auf Rückmeldung")
- unklare Formulierungen ("dein aktueller Stand", "dein Tarif-Status", "deine Situation", "deine Daten")

## savings_text Semantik (final)
- spart: Überzahlung
- spart_nicht: positiver Status
- neueinzug: vermiedene Kosten

## Pflicht-Satzmuster
- spart: `Du zahlst aktuell {{ opportunity.savings_text }}` oder `Das bedeutet für dich: {{ opportunity.savings_text }}`
- spart_nicht: `Du bist aktuell {{ opportunity.savings_text }}` oder `Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}`
- neueinzug: `So vermeidest du {{ opportunity.savings_text }}` oder `Beim Umzug vermeidest du {{ opportunity.savings_text }}`

## Business-Case CTA Logik (final)
Ausgangspunkt: Nutzer hat bereits eine persönliche Empfehlung angefordert.

Daher CTA-Logik in Nicht-Referral-Mails:
- sichere {{ opportunity.energieart }}-Empfehlung wurde bereits auf Basis der Angaben ermittelt
- CTA fordert zum direkten Ansehen dieser Empfehlung auf
- Klarheit + Sicherheit statt generischem Prüf-Frame

## Betreffzeilen-Regeln (final)
- konkret, relevant, natürlich
- persönlich statt werblich
- mix aus Frage-, Timing- und Klarheitsmustern
- keine Fake-Dringlichkeit
- kein Support-/Ticket-Sound
- kein irreführendes Framing

## Preheader-Regeln (final)
- ergänzt den Betreff inhaltlich
- erhöht Relevanz und Kontext
- darf eine sanfte offene Schleife setzen
- kein Fake-Service-/Fake-Waiting-Frame

## {{ opportunity.energieart }} Regel
In jeder Nicht-Referral-Mail:
- muss {{ opportunity.energieart }} im Subject oder Preheader enthalten sein
- und im Body enthalten sein

## Zusätzliche Kontext-/Einwand-Sätze
- maximal ein Zusatzsatz, nur wenn conversion-relevant
- zulässige Funktionen: Kontext, Einwandbehandlung, CTA-Brücke
- keine pauschale Textaufblähung
