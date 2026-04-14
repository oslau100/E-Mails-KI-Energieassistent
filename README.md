# Email System – Tarif Funnel (DACH)

Dieses Repository enthält ein skalierbares Plain-HTML-Email-System für GoHighLevel.

## Ziel
Das System soll:
- Open Rate über starke Betreffzeilen + Preheader erhöhen
- Click Rate über klare, konkrete CTA-Sprache erhöhen
- Conversion über bessere Relevanz und Einwandbehandlung erhöhen
- Vertrauen im DACH-Energiemarkt stärken

## Stilprinzip
- Plain-Email-Stil (persönlich, kurz, textbasiert)
- kein Redesign, kein Newsletter-Look
- kein Button-Design, keine Bildbanner
- einfache HTML-Struktur beibehalten

## Szenarien
- spart (10)
- neueinzug (10)
- spart_nicht (4)
- loop (15)

## CTA-Regel
- Genau **ein CTA-Link** pro Email (offer oder referral).
- Standard-CTA zeigt auf: `{{ opportunity.offer_url }}`
- Referral nur in ausgewählten loop-Emails.

## Betreffzeilen-Regeln
Betreffzeilen müssen:
- persönlich und konkret sein
- nicht werblich/spammy klingen
- keine Fake-Service-/Fake-Transaktionswirkung haben
- leichte Relevanz oder Fragespannung erzeugen

Nicht erlaubt (wenn nicht real):
- „Wir warten auf Rückmeldung“
- „Deine Anfrage“
- „Bitte dringend antworten“
- „Letzte Erinnerung“
- klassische Spamwörter wie „Gratis“, „VIP“, „Exklusiv“

## Preheader-Regeln
Preheader sollen:
- den Betreff ergänzen
- Relevanz verstärken
- ggf. eine sanfte offene Schleife erzeugen
- nicht wie falsche Service-/Reminder-Mails wirken

## Zusätzliche Vertrauens-/Einwandzeile
Wenn Problem → CTA zu abrupt ist, exakt **eine zusätzliche Zeile** ergänzen, z. B.:
- „Du musst nichts überstürzen.“
- „Der Check verpflichtet dich zu nichts.“
- „Wenn kein Vorteil da ist, bleibt alles wie es ist.“
- „Du entscheidest danach in Ruhe.“

Nur selektiv einsetzen.

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
- {{custom_values.absender_name}}
- {{custom_values.brandname}}
- {{custom_values.logo}}
- {{custom_values.strae_und_hausnummer}}
- {{custom_values.plz_und_stadt}}
- {{custom_values.impressum_url}}
- {{custom_values.datenschutz_url}}
- {{custom_values.empfehlungsportal_url}}
- {{custom_values.empfehlungsprmie}}

## Signatur-Regel
Unter Grußformel wird in allen DE-Mails eine schlichte HTML-Signatur genutzt mit:
- Absendername
- Brandname
- kleinem Logo
- Adresse
- Impressum- und Datenschutz-Link

Nur die Signatur darf leicht formatiert sein.

## Sprachverbote (doppeldeutig)
Nicht verwenden:
- „dein aktueller Stand"
- „dein Tarif-Status"
- „deine Situation"
- „deine Daten"

## Struktur
- `emails/locales/de/spart/`
- `emails/locales/de/spart_nicht/`
- `emails/locales/de/neueinzug/`
- `emails/locales/de/loop/`
- `specs/`
