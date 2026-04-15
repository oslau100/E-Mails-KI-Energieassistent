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

## savings_text Source of Truth (final)
- neueinzug = unnötige Mehrkosten beim Start
- spart_nicht = gut und sinnvoll eingestellt
- low = etwas mehr als nötig
- mid = spürbar mehr als nötig
- high = mehrere hundert Euro pro Jahr zu viel
- very_high = über 500€ pro Jahr zu viel

## Satzlogik je Szenario
- spart: `Du zahlst aktuell {{ opportunity.savings_text }}` oder `Das bedeutet für dich: {{ opportunity.savings_text }}`
- spart_nicht: `Du bist aktuell {{ opportunity.savings_text }}` oder `Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}`
- neueinzug: `So vermeidest du {{ opportunity.savings_text }}` oder `Beim Umzug vermeidest du {{ opportunity.savings_text }}`

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
