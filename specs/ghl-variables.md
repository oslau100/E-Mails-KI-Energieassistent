# GHL Variables

## Hinweis
Alle Platzhalter müssen exakt so geschrieben werden wie hier angegeben.

## Opportunity Fields
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

## Contact Fields
- {{ contact.first_name }}
- {{ contact.postal_code }}
- {{ contact.city }}
- {{ contact.empfehlungslink }}

## Custom Values
- {{custom_values.absender_email}}
- {{custom_values.absender_name}}
- {{custom_values.empfehlungsportal_url}}
- {{custom_values.empfehlungsprmie}}

## Nutzung in Emails

### Personalisierung
- {{ contact.first_name }}
- {{ contact.city }}
- {{ contact.postal_code }}

### Messaging / Relevanz
- {{ opportunity.savings_text }}
- {{ opportunity.energieart }}
- {{ opportunity.cta_text }}

### Routing / Kontext
- {{ opportunity.savings_bucket }}
- {{ opportunity.scenario }}
- {{ opportunity.email_lang }}

### CTA Ziel
- {{ opportunity.offer_url }}
- {{ contact.empfehlungslink }} (nur in ausgewählten Referral-Mails)

### Vergleich / Conversion Layer
- {{ opportunity.aktueller_anbieter }}
- {{ opportunity.neuer_anbieter }}
- {{ opportunity.aktuelle_monatliche_kosten_ }}
- {{ opportunity.neuer_monatlicher_preis_ }}

### Empfehlungsprogramm
- {{custom_values.empfehlungsportal_url}}
- {{custom_values.empfehlungsprmie}}

## Regeln
- Placeholder niemals umformatieren
- Placeholder niemals übersetzen
- Placeholder niemals mit Beispieldaten ersetzen
- Placeholder-Syntax exakt beibehalten
- `{{ opportunity.energieart }}` gezielt und natürlich einsetzen (Betreff, Preheader, Einstieg, CTA-Kontext)
