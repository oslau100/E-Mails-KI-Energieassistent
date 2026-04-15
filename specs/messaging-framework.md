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

## Business-Case CTA Logik (final)
Ausgangspunkt: Nutzer hat bereits eine persönliche Empfehlung angefordert.

Daher CTA-Logik in Nicht-Referral-Mails:
- sichere {{ opportunity.energieart }}-Empfehlung wurde bereits auf Basis der Angaben ermittelt
- CTA fordert zum direkten Ansehen dieser Empfehlung auf
- je nach Szenario mit Zusatzfokus:
  - spart: Sicherheit + Ersparnis
  - neueinzug: Timing + sicherer Start
  - spart_nicht: Sicherheit + Klarheit ohne unnötige Aktion
  - loop: erneute Klarheit mit kurzem Blick

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
- 1–2 Zusatzsätze nur dann, wenn sie Conversion-relevante Funktion haben
- zulässige Funktionen: Kontext, Einwandbehandlung, CTA-Brücke
- keine pauschale Textaufblähung

## Einwandfokus nach Szenario
- spart: „lohnt sich das“, „ich will keinen Fehler“, „kein Stress“
- neueinzug: „später“, „zu viel los“, „schnell abhaken“
- spart_nicht: „warum noch Mails“, „ist das nur Werbung“
- loop: „später“, „nicht auf dem Schirm“, „kein Energie-Stress“

## Signatur-Regel
- Unter Grußformel/Absendername eine dezente HTML-Signatur nutzen.
- Erlaubte Bestandteile: Brandname, kleines Logo, Adresse, Impressum, Datenschutz.
- Die Signatur ist das einzige leicht formatierte Element.
- CTA bleibt als normaler Textlink im Body und pro Mail einzigartig.
