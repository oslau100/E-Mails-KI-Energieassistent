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
- CTA framing must reflect business reality: recommendation is already pre-calculated from user inputs.
- Avoid generic “check if you pay too much” framing as primary CTA language.

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

## Subject line rules (open rate)
- clear, personal, concrete
- not ad-like
- no fake support/service framing
- {{ contact.first_name }} and {{ opportunity.energieart }} may be used selectively
- no misleading urgency
- no fake-transactional framing ("deine Anfrage", "wir warten auf Rückmeldung", "bitte dringend antworten")
- avoid vague/abstract lines; inbox relevance first

## Preheader rules
- must complement the subject
- should increase relevance and clarity
- can create a soft open loop
- no fake urgency or fake "we are waiting" framing
- no fake ticket/support wording
- should confirm context: recommendation already exists based on user data

## Selective bridge-line rule
- Keep current structure and add exactly one extra line only where needed.
- Allowed function of this extra line: objection handling, trust bridge, or relevance bridge before CTA.
- Do not add this line to every email; use it selectively.

## Energieart requirement
- In every non-affiliate email, {{ opportunity.energieart }} must appear logically in:
  - subject or preheader, and
  - body copy (not just metadata comments).

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
