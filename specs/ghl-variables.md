# GHL Variables

## Hinweis
Platzhalter exakt beibehalten (inkl. Klammern, Punkten, Leerzeichen).

## Opportunity
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

## Contact
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

## savings_text Source of Truth
- neueinzug = unnötige Mehrkosten beim Start
- spart_nicht = gut aufgestellt
- low = etwas mehr als nötig
- mid = spürbar mehr als nötig
- high = mehrere hundert Euro pro Jahr zu viel
- very_high = über 500€ pro Jahr zu viel

## Pflicht-Satzlogik
- spart: `Du zahlst aktuell {{ opportunity.savings_text }}` / `Das bedeutet für dich: {{ opportunity.savings_text }}`
- spart_nicht: `Dein {{ opportunity.energieart }}-Tarif ist aktuell {{ opportunity.savings_text }}` / `Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}`
- neueinzug: `So vermeidest du {{ opportunity.savings_text }}` / `Beim Umzug vermeidest du {{ opportunity.savings_text }}`

## Nutzungsregeln
- In Nicht-Referral-Mails muss `{{ opportunity.energieart }}` in Subject oder Preheader und zusätzlich im Body vorkommen.
- Standard-CTA zeigt auf `{{ opportunity.offer_url }}`.
- Referral-CTA nur in ausgewählten Loop-Mails auf `{{ contact.empfehlungslink }}`.
- Keine neuen Variablen erfinden oder umbenennen.
