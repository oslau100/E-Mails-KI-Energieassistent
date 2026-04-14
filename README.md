# Email System – Tarif Funnel (DACH)

Dieses Repository enthält ein skalierbares HTML-Email-System für GoHighLevel.

## Ziel
Dieses System soll:
- Open Rate durch klare, persönliche Betreffzeilen und Preheader erhöhen
- Click Rate durch konkrete, verständliche CTA-Sprache erhöhen
- Conversion durch Einwandbehandlung und Relevanz verbessern
- Vertrauen aufbauen und langfristig halten
- das Thema Energie verständlicher machen
- später sauber mehrsprachig ausgerollt werden können

## Mission
Wir unterstützen Haushalte dabei, mehr Transparenz beim Thema Strom- und Gastarife zu gewinnen und gezielte Einsparpotenziale zu erkennen.

Unser Ziel ist Klarheit statt Tarifchaos: verständliche Hinweise statt komplexer Vergleichslogik.

## Szenarien
- spart
- spart_nicht
- neueinzug
- loop

## Sequenz-Struktur

### Haupt-Sequenzen
- spart = 10 Emails
- neueinzug = 10 Emails
- spart_nicht = 4 Emails

### Loop
- 15 Emails
- startet nach der jeweiligen Einstiegsszenario-Sequenz
- dient Reaktivierung, Markt-Awareness, Reminder und ausgewählten Empfehlungs-Impulsen

## CTA-Regel
Jede Email enthält einen klaren CTA.

### Standard
Die meisten Emails verlinken auf die Tarifempfehlung:
- {{ opportunity.offer_url }}

### Referral / Empfehlungsprogramm
Nur ausgewählte Loop-Emails nutzen Empfehlungs-CTAs.
Diese Emails müssen mission-led bleiben:
- mehr Haushalten Orientierung geben
- Liebsten helfen
- Klarheit teilen

## Design-Prinzip
Die Emails sollen bewusst sehr einfach aussehen:
- textbasiert
- schlicht
- persönlich
- direkt

Nicht wie Newsletter, sondern wie persönliche Nachrichten.

### Deshalb gilt
- keine Buttons
- keine Bilder im Body
- keine komplexen Layouts
- CTA als normaler Hyperlink im Text
- genau ein CTA-Link pro Email

## Phase 1
Aktuell wird nur die deutsche Master-Version gebaut.

## Verwendete GHL Variablen

### Opportunity
- {{ opportunity.cta_text }}
- {{ opportunity.savings_text }}
- {{ opportunity.savings_bucket }}
- {{ opportunity.scenario }}
- {{ opportunity.email_lang }}
- {{ opportunity.offer_url }}
- {{ opportunity.energieart }}
- {{ opportunity.aktueller_anbieter }}
- {{ opportunity.neuer_anbieter }}
- {{ opportunity.aktuelle_monatliche_kosten_ }}
- {{ opportunity.neuer_monatlicher_preis_ }}

### Contact
- {{ contact.first_name }}
- {{ contact.postal_code }}
- {{ contact.city }}
- {{ contact.empfehlungslink }}

### Custom Values
- {{custom_values.absender_email}}
- {{custom_values.absender_name}}
- {{custom_values.empfehlungsportal_url}}
- {{custom_values.empfehlungsprmie}}
- {{custom_values.brandname}}
- {{custom_values.logo}}
- {{custom_values.strae_und_hausnummer}}
- {{custom_values.plz_und_stadt}}
- {{custom_values.impressum_url}}
- {{custom_values.datenschutz_url}}

## Betreffzeilen-Regeln (Open Rate)
- persönlich und konkret formulieren
- klar statt vage
- nicht nach Werbung und nicht nach Fake-Service-Mail klingen
- {{ contact.first_name }} und {{ opportunity.energieart }} selektiv nutzen
- keine irreführenden Betreffzeilen (z. B. „Dringend“, „Wir benötigen Rückmeldung“) ohne realen Kontext
- keine fake-transaktionalen Muster (z. B. „deine Anfrage“, „wir warten auf Rückmeldung“)

## Preheader-Regeln
- ergänzt den Betreff sinnvoll
- erzeugt Relevanz ohne Druck
- darf kurze offene Schleifen setzen
- keine Fake-Dringlichkeit und kein falscher Service-Kontext
- kein Support-/Ticket-Framing ohne realen Kontext

## Selektive Zusatzzeile vor CTA
- Bestehende Email-Struktur bleibt erhalten.
- Genau eine zusätzliche Zeile wird nur dann ergänzt, wenn der CTA-Sprung zu abrupt ist.
- Zweck der Zusatzzeile: Einwandbehandlung, Vertrauensbrücke oder Relevanzverstärkung.

## Signatur-Standard
Unter der Grußformel wird eine leichte HTML-Signatur genutzt:
- {{custom_values.brandname}}
- kleines Logo über {{custom_values.logo}}
- {{custom_values.strae_und_hausnummer}}
- {{custom_values.plz_und_stadt}}
- Impressum- und Datenschutz-Links

Die Signatur ist das einzige stärker formatierte Element und bleibt bewusst dezent.

## Klare Sprachregeln
Vermeiden (doppeldeutig/unklar):
- „dein aktueller Stand"
- „dein Tarif-Status"
- „deine Situation"
- „deine Daten"

## Wichtige Regel zur Empfehlungsprämie
`{{custom_values.empfehlungsprmie}}` soll nur den nackten Wert enthalten, z. B.:
- 30€
- 50€

## Workflow-Prinzip
Die Logik liegt in GoHighLevel. Der Workflow setzt die Variablen vor dem Versand.

Die Emails enthalten keine Entscheidungslogik.

## Struktur
- emails/locales/de/spart/
- emails/locales/de/spart_nicht/
- emails/locales/de/neueinzug/
- emails/locales/de/loop/
- specs/
