# Email System – Tarif Funnel (DACH)

Dieses Repository enthält ein skalierbares HTML-Email-System für GoHighLevel.

## Ziel
Dieses System soll:
- Conversion steigern
- Vertrauen aufbauen
- das Thema Energie verständlicher machen
- Haushalten helfen, unnötige Kosten zu vermeiden
- später sauber mehrsprachig ausgerollt werden können

## Mission
Wir unterstützen Haushalte dabei, mehr Transparenz beim Thema Strom- und Gastarife zu gewinnen und gezielte Einsparpotenziale zu erkennen.

In unserer täglichen Arbeit sehen wir immer wieder, wie unübersichtlich der Energiemarkt für viele Menschen geworden ist. Unterschiedliche Anbieter, ständig wechselnde Tarife und komplexe Vertragsbedingungen erschweren es, den wirklich passenden Tarif zu finden. Viele Haushalte setzen sich erst dann mit ihrem Energievertrag auseinander, wenn unerwartet hohe Nachzahlungen entstehen oder die Kosten plötzlich steigen.

Genau hier setzen wir an. Mit unserem digitalen Energieassistenten bieten wir ein System, das Tarife automatisch überprüft, Jahresabrechnungen analysiert und verständlich aufzeigt, wo Einsparungen möglich sind oder Auffälligkeiten bestehen. So wird aus einem komplexen Thema eine klare und nachvollziehbare Lösung.

Unser Ziel ist es, möglichst vielen Haushalten zu helfen, ihre Energiekosten besser zu verstehen, unnötige Ausgaben zu vermeiden und langfristig zu sparen – ganz ohne komplizierte Vergleiche oder zusätzlichen Aufwand.

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
Jede Email enthält einen CTA.

### Standard
Die meisten Emails verlinken auf die Tarifempfehlung:
- {{ opportunity.offer_url }}

### Referral / Empfehlungsprogramm
Nur ausgewählte Loop-Emails nutzen Empfehlungs-CTAs.
Diese Emails sollen nicht wie klassisches Affiliate-Marketing wirken, sondern wie ein hilfreicher Beitrag zur Mission:
- mehr Haushalten Orientierung geben
- Liebsten helfen
- Transparenz weitergeben
- unnötige Kosten vermeiden helfen

## Design-Prinzip
Die Emails sollen bewusst sehr einfach aussehen.

Sie sollen:
- textbasiert
- schlicht
- persönlich
- direkt
wirken.

Nicht wie Newsletter, sondern eher wie eine persönliche Mail.

### Deshalb gilt
- keine Buttons
- keine Bilder
- keine komplexen Layouts
- keine Banner
- keine Marketing-Optik
- CTA als normaler Hyperlink im Text

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

## Wichtige Regel zur Empfehlungsprämie
`{{custom_values.empfehlungsprmie}}` soll nur den nackten Wert enthalten, zum Beispiel:
- 30€
- 50€

Nicht:
- 50€ Amazon Gutschein
- 50€ für jede erfolgreiche Empfehlung

Die sprachliche Einbettung erfolgt in der jeweiligen Email.

## Workflow-Prinzip
Die Logik liegt in GoHighLevel.

Der Workflow setzt vor dem Versand:
- scenario
- savings_bucket
- savings_text
- cta_text
- offer_url
- email_lang

Die Emails enthalten keine Entscheidungslogik.

## Struktur
- emails/locales/de/spart/
- emails/locales/de/spart_nicht/
- emails/locales/de/neueinzug/
- emails/locales/de/loop/
- specs/

## Reihenfolge
1. Setup-Files anlegen
2. Deutsche Master-Emails bauen
3. HTML in GHL testen
4. Importprozess standardisieren
5. Loop validieren
6. Später lokalisieren

## Wichtige Regeln
- keine festen veraltbaren Zahlen in statischen Emails
- keine Logik im HTML
- keine zusätzlichen Variablen erfinden
- gleiche Placeholder-Syntax überall beibehalten
- jede Email braucht einen CTA
- die meisten CTAs gehen auf die Tarifempfehlung
- Empfehlungs-Emails müssen missionsgetrieben und hilfreich wirken
- Emails sollen optisch so basic wie möglich sein
