# AGENTS.md

## Project
This repository contains high-converting HTML email sequences for an energy tariff funnel in GoHighLevel.

## Current rollout phase
Phase 1 = German only (`de`).

## Scenarios
- spart
- spart_nicht
- neueinzug
- loop

## Sequence lengths
- spart = 10 emails
- neueinzug = 10 emails
- spart_nicht = 4 emails
- loop = 15 emails

## Core objective
Create persuasive but trustworthy HTML emails for the German DACH energy market.

The system should:
- increase open rate, click rate, and conversion
- build trust
- feel personal
- stay easy to localize later
- remain easy to import into GoHighLevel
- separate workflow logic from email rendering

## Mandatory CTA rule
Every email must contain a CTA.

### Default CTA rule
Most emails must use the tariff recommendation CTA and link to:
- {{ opportunity.offer_url }}

### CTA business logic (final)
For non-referral emails, CTA framing must reflect the real use case:
- a personal recommendation has already been determined based on user input
- recommendation must be framed as a safe option
- CTA language should point to “now view your recommendation”, not “start a generic check”

### Referral CTA rule
Only selected loop emails may use referral / recommendation CTAs.
Referral emails must be mission-led and helpful, never spammy affiliate style.

## Data rules
- Use only approved GoHighLevel variables.
- Preserve placeholders exactly as provided.
- Do not rename variables.
- Do not invent fields.
- Keep placeholder spacing exactly as provided.

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

## savings_text source of truth (final)
- neueinzug = unnötige Mehrkosten beim Start
- spart_nicht = gut und sinnvoll eingestellt
- low = etwas mehr als nötig
- mid = spürbar mehr als nötig
- high = mehrere hundert Euro pro Jahr zu viel
- very_high = über 500€ pro Jahr zu viel

### Mandatory savings_text sentence structure
- spart:
  - Du zahlst aktuell {{ opportunity.savings_text }}
  - Das bedeutet für dich: {{ opportunity.savings_text }}
- spart_nicht:
  - Du bist aktuell {{ opportunity.savings_text }}
  - Bei deinem {{ opportunity.energieart }}-Tarif bist du aktuell {{ opportunity.savings_text }}
- neueinzug:
  - So vermeidest du {{ opportunity.savings_text }}
  - Beim Umzug vermeidest du {{ opportunity.savings_text }}

Do not mix these meanings across segments.

## Subject line rules (open rate)
- clear, personal, concrete
- not ad-like
- no fake support/service framing
- no fake-transactional framing (e.g. “deine Anfrage”, “wir warten auf Rückmeldung”, “bitte antworten”)
- no misleading urgency
- vary structures (question, statement, timing, relevance)

## Preheader rules
- must complement the subject
- should increase relevance and clarity
- can create a soft open loop
- no fake urgency or fake “we are waiting” framing
- no fake ticket/support wording

## {{ opportunity.energieart }} rule (final)
For every non-affiliate/referral mail:
- {{ opportunity.energieart }} must appear in subject or preheader
- and must appear in the body
Do not force it in referral mails when unnatural.

## Selective bridge-line rule
- Keep current structure and add exactly one extra line only where needed.
- Allowed function of this extra line: objection handling, trust bridge, or relevance bridge before CTA.
- Do not add this line to every email; use it selectively.


## Anti-reassurance rule (conversion)
Do not use generic postponement/pressure-relief lines as CTA bridges in non-referral mails.
Avoid especially:
- "Du musst nichts überstürzen."
- "Du entscheidest danach in Ruhe."
- "Der Check verpflichtet dich zu nichts."
- "Wenn kein Vorteil da ist, bleibt alles wie es ist."

Use one short logic-driven bridge instead (comparison, consequence, quick clarity, practical next step).

## Prohibited / ambiguous phrases
Do not use:
- "dein aktueller Stand"
- "dein Tarif-Status"
- "deine Situation"
- "deine Daten"

## HTML and layout rules
- plain, personal, text-first style
- no buttons
- no images in body content (exception: small logo only inside the signature block)
- no decorative marketing layout
- CTA must be a normal text link
- exactly one CTA link per email

## Signature rule
- Add a consistent, lightly formatted HTML signature below greeting + sender name.
- Signature may include: brand name, small logo, address, impressum link, datenschutz link.
- Signature should stay subtle and text-first, never banner-like.

## Important constraints
- no fake urgency
- no deceptive scarcity
- no misleading claims
- use dynamic variables where relevant
- every email must include a CTA
- most CTAs should drive to {{ opportunity.offer_url }}

## File structure
- emails/locales/de/spart/
- emails/locales/de/spart_nicht/
- emails/locales/de/neueinzug/
- emails/locales/de/loop/
- specs/
