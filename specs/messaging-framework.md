# Messaging Framework

## Grundprinzip
Kommunikation für den deutschen DACH-Energiemarkt: klar, vertrauenswürdig, handlungsstark.

## Performance-Ziele
- höhere Open Rate über bessere Betreffzeilen
- höhere Klickrate über klare CTA-Sprache
- höhere Conversion über Relevanz und Einwandbehandlung

## Form-Prinzip
Die Emails sollen wie persönliche Nachrichten wirken, nicht wie Newsletter.

Pflicht:
- textbasiert
- schlicht
- persönlicher Ton
- CTA als normaler Hyperlink

Verboten:
- Buttons
- Bilder
- Banner/Boxen
- komplexes Marketing-Layout
- fake-transaktionale Betreffmuster ("deine Anfrage", "wir warten auf Rückmeldung")

## Betreffzeilen-Regeln
- konkret, klar, natürlich
- persönlich statt werblich
- selektive Personalisierung mit {{ contact.first_name }} und {{ opportunity.energieart }}
- keine irreführenden Betreffzeilen
- keine Fake-Dringlichkeit
- keine Support-/Ticket-Simulation
- nicht abstrakt oder sloganhaft formulieren

## Preheader-Regeln
- ergänzt den Betreff
- erhöht Relevanz
- kurze offene Schleife möglich
- kein Fake-Service- oder Fake-Waiting-Frame
- soll bei Bedarf den Kontext „Empfehlung bereits ermittelt“ stützen

## Selektive Zusatzzeile
- Wenn der Sprung zum CTA zu abrupt ist, darf genau eine zusätzliche Zeile ergänzt werden.
- Funktion der Zeile: Einwandbehandlung, Vertrauensaufbau oder Relevanzbrücke.
- Diese Ergänzung erfolgt selektiv, nicht pauschal in jeder Mail.
- 1–2 zusätzliche Sätze sind erlaubt, wenn Kontext + Einwandbehandlung konkret verbessert werden.

## Verbotene / doppeldeutige Formulierungen
- "dein aktueller Stand"
- "dein Tarif-Status"
- "deine Situation"
- "deine Daten"

## Einwandbehandlung
Selektiv ergänzen:
- "du musst nichts überstürzen"
- "der Check verpflichtet dich zu nichts"
- "wenn kein Vorteil da ist, bleibt alles wie es ist"
- "du entscheidest danach in Ruhe"

## Signatur-Regel
- Unter Grußformel/Absendername eine dezente HTML-Signatur nutzen.
- Erlaubte Bestandteile: Brandname, kleines Logo, Adresse, Impressum, Datenschutz.
- Die Signatur ist das einzige Element mit leicht stärkerer Formatierung.
- CTA bleibt als normaler Textlink im Body und pro Mail einzigartig.

## Business CTA Logic
- User has already requested a personal tariff recommendation.
- CTA copy should frame this as a pre-computed, safer recommendation based on provided data.
- Avoid regressing to early-funnel “do a generic check” phrasing.

## Mandatory {{ opportunity.energieart }} placement
- In every non-affiliate email: use {{ opportunity.energieart }} in subject or preheader and in body copy.
- Referral emails may use it optionally.

## Szenario-Fokus
- spart: klarer Verlustfokus, {{ opportunity.savings_text }} sichtbar machen
- spart_nicht: Ehrlichkeit + Monitoring statt Druck
- neueinzug: Grundversorgung als teure Default-Option klar benennen
- loop: Reaktivierung, Rhythmus, mission-led Referral in ausgewählten Mails
