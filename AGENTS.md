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

## Subject line rules (open rate)
- clear, personal, concrete
- not ad-like
- no fake support/service framing
- {{ contact.first_name }} and {{ opportunity.energieart }} may be used selectively
- no misleading urgency

## Preheader rules
- must complement the subject
- should increase relevance and clarity
- can create a soft open loop
- no fake urgency or fake "we are waiting" framing

## Prohibited / ambiguous phrases
Do not use:
- "dein aktueller Stand"
- "dein Tarif-Status"
- "deine Situation"
- "deine Daten"

## HTML and layout rules
- plain, personal, text-first style
- no buttons
- no images
- no decorative marketing layout
- CTA must be a normal text link

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
