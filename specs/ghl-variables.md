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
- {{custom_values.brandname}}
- {{custom_values.logo}}
- {{custom_values.strae_und_hausnummer}}
- {{custom_values.plz_und_stadt}}
- {{custom_values.impressum_url}}
- {{custom_values.datenschutz_url}}

## Nutzungsregeln (final)

### Pflichtkontext
In Nicht-Referral-Mails ist {{ opportunity.energieart }} verpflichtend:
- im Subject oder Preheader
- und im Body

### CTA Ziel
- Standard CTA: {{ opportunity.offer_url }}
- Referral CTA nur in ausgewählten Loop-Mails: {{ contact.empfehlungslink }}

### CTA-Meaning (Nicht-Referral)
CTA-Texte müssen ausdrücken:
- Empfehlung wurde bereits auf Basis der Angaben ermittelt
- Empfehlung ist eine sichere Option
- Link führt zum direkten Ansehen dieser Empfehlung

### Platzhalter-Schutz
- Placeholder niemals umformatieren
- Placeholder niemals übersetzen
- Placeholder niemals mit Beispieldaten ersetzen
- Placeholder-Syntax exakt beibehalten
- Keine neuen Variablen erfinden

## Signatur-Verwendung
Für die HTML-Signatur in deutschen Emails sind folgende Werte vorgesehen:
- {{custom_values.brandname}}
- {{custom_values.logo}}
- {{custom_values.strae_und_hausnummer}}
- {{custom_values.plz_und_stadt}}
- {{custom_values.impressum_url}}
- {{custom_values.datenschutz_url}}
