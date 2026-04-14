# AGENTS.md

## Project
High-converting plain HTML email sequences for a German DACH energy tariff funnel in GoHighLevel.

## Scenarios and lengths
- spart: 10
- neueinzug: 10
- spart_nicht: 4
- loop: 15

## Core performance goals
- increase open rate (subject + preheader quality)
- increase click rate (clear CTA wording)
- increase conversion (relevance + objection handling)
- preserve trust and personal tone

## Hard constraints
- no redesign
- no newsletter style
- no buttons
- no body images/banners
- simple HTML structure must stay intact
- exactly one CTA link per email
- no misleading or fake-transactional framing

## CTA rules
- default CTA target: {{ opportunity.offer_url }}
- referral CTA only in selected loop emails
- referral copy must be mission-led, never spammy affiliate style

## Subject line rules
- personal, concrete, non-spammy
- may use {{ contact.first_name }} and {{ opportunity.energieart }} selectively
- avoid fake urgency / fake service prompts

Forbidden examples (unless real):
- "Wir warten auf Rückmeldung"
- "Deine Anfrage"
- "Bitte dringend antworten"
- "Letzte Erinnerung"

## Preheader rules
- complements subject
- adds relevance and soft tension
- no fake support/reminder language

## Objection/trust bridge rule
If transition to CTA is abrupt, add exactly one bridge line (selective), e.g.:
- "Du musst nichts überstürzen."
- "Der Check verpflichtet dich zu nichts."
- "Wenn kein Vorteil da ist, bleibt alles wie es ist."
- "Du entscheidest danach in Ruhe."

## Prohibited ambiguous wording
- "dein aktueller Stand"
- "dein Tarif-Status"
- "deine Situation"
- "deine Daten"

## Approved variables

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

## Signature rule
In all DE emails, include a compact HTML signature below greeting/name with:
- brand name
- small logo
- address
- impressum + datenschutz links

Only signature may be slightly formatted.
