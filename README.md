# Email System – Tarif Funnel (DACH)

Dieses Repository enthält ein skalierbares Plain-HTML-Email-System für GoHighLevel.

## Ziel
Das System soll:
- Open Rate über relevantere Betreffzeilen steigern
- CTR über klarere CTA-Einleitungen steigern
- Conversion über bessere Einwandbehandlung steigern
- Vertrauen aufbauen
- das Thema Energie verständlicher machen
- Haushalten helfen, unnötige Kosten zu vermeiden

## Stilprinzip (fix)
Kein Redesign.

Alle Emails bleiben:
- plain
- textbasiert
- ohne Buttons
- ohne Bilder
- ohne Marketing-Layout

## Mission
Wir unterstützen Haushalte dabei, beim Thema Energie klare Entscheidungen zu treffen statt im Tarif-Chaos hängen zu bleiben.

Mission-Elemente werden punktuell eingebaut (nicht in jeder Mail), besonders in:
- ausgewählten Loop-Mails
- ausgewählten spart_nicht-Mails
- ausgewählten spart/neueinzug-Mails
- allen Referral-Mails

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

## CTA-Regel
Jede Email enthält genau einen CTA-Ziellink:
- meist `{{ opportunity.offer_url }}`
- in ausgewählten Loop-Referral-Mails `{{ contact.empfehlungslink }}`

## Performance-Regeln für Copy
- Betreffzeilen aktiv auf Open Rate optimieren (konkret, relevant, neugierig; nicht clickbait)
- Preheader darf Betreff nicht nur wiederholen, sondern muss Nutzen/Konsequenz ergänzen
- CTA-Einleitung aktivierend formulieren
- Einwandbehandlung bewusst integrieren (natürlich, nicht aufgezählt)
- Nicht alle Mails ultrakurz halten: sinnvoller Längenmix aus kurz/mittel/substanzieller
- `{{ opportunity.energieart }}` gezielt für Relevanz nutzen

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

## Struktur
- emails/locales/de/spart/
- emails/locales/de/spart_nicht/
- emails/locales/de/neueinzug/
- emails/locales/de/loop/
- specs/

## Wichtige Regeln
- keine Logik im HTML
- keine zusätzlichen Variablen erfinden
- Placeholder exakt beibehalten
- jede Email braucht einen CTA
- Plain-Email-Optik unverändert beibehalten
