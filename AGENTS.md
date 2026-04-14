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
- increase conversions
- build trust
- feel personal
- stay easy to localize later
- remain easy to import into GoHighLevel
- separate workflow logic from email rendering

## Mission context
The product helps households gain more transparency around electricity and gas tariffs and identify meaningful savings potential.

The brand position is:
- clarity in a complex market
- understandable guidance instead of confusion
- helping households avoid unnecessary energy costs
- reducing friction and overwhelm
- making savings understandable without complicated comparisons

This mission should influence tone, especially:
- trust framing
- educational clarity
- recommendation / affiliate emails
- long-term loop messaging

## Mandatory CTA rule
Every email must contain a CTA.

### Default CTA rule
Most emails must use the tariff recommendation CTA and link to:
- {{ opportunity.offer_url }}

### Referral CTA rule
Only selected loop emails may use referral / recommendation CTAs.
Those emails should focus on:
- helping friends and family
- contributing to a bigger mission
- helping more households gain clarity and save money

Referral emails must NOT sound like generic affiliate marketing.

## Data rules
- Use only the approved GoHighLevel variables.
- Preserve placeholders exactly as provided.
- Do not rename variables.
- Do not invent fields.
- Do not replace placeholders with hardcoded example values in final templates.
- Keep placeholder spacing exactly as provided.

## Approved variables

### Opportunity
- {{ opportunity.cta_text }}
- {{ opportunity.savings_text }}
- {{ opportunity.savings_bucket }}
- {{ opportunity.scenario }}
- {{ opportunity.email_lang }}
- {{ opportunity.offer_url }}
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

## Reward variable rule
{{custom_values.empfehlungsprmie}} must contain amount-only values, e.g.:
- 30€
- 50€

Do not assume product type inside the variable value.
The surrounding sentence belongs in the email copy.

## Scenario messaging rules

### spart
- strongest conversion intent
- use loss framing
- make overpayment feel real
- reduce fear of switching
- reinforce simplicity and safety
- CTA should usually point to the tariff recommendation
- include some shorter, sharper spike emails

### spart_nicht
- build trust through honesty
- no fake savings claims
- positive reframe
- market monitoring mindset
- CTA should still exist, but stay soft
- CTA should usually still point to the recommendation / overview page

### neueinzug
- emphasize timing
- avoid expensive default / Grundversorgung framing
- make action feel easy and quick
- CTA should usually point to the tariff recommendation

### loop
- lighter than entry sequences
- mix insights, reminders, soft conversion, and selected referral prompts
- should not feel repetitive
- should keep trust high
- most loop emails still use tariff recommendation CTA
- only selected loop emails use referral CTA

## Referral / recommendation framing rules
Referral emails must feel mission-led and helpful.

Required emotional angle:
- help us help more households
- help your loved ones make better energy decisions
- share clarity, not just a link
- reward is secondary, mission is primary

Good themes:
- "Hilf uns, deinen Liebsten zu helfen"
- "Teile Klarheit statt unnötiger Kosten"
- "Mach es anderen leichter"
- "Hilf mit, mehr Haushalten Orientierung zu geben"

Avoid:
- spammy affiliate tone
- money-first tone
- aggressive recruiting language
- MLM-like wording

## HTML and layout rules
The emails must look as plain and personal as possible.

Required design style:
- very basic email appearance
- text-first
- minimal HTML
- no visual marketing layout
- should feel like a personal email from a real person
- should feel closer to a helpful note than to a newsletter

Mandatory layout constraints:
- no buttons
- no images
- no icons
- no banners
- no cards
- no boxed sections
- no hero areas
- no complex table-based visual layout
- no decorative design elements
- no multi-column sections

CTA implementation:
- CTA must appear as a normal text link
- CTA may be placed as a plain hyperlink line
- CTA can also appear in a short sentence with a linked anchor text
- do not style CTA like a button

HTML constraints:
- keep HTML as lightweight and simple as possible
- use safe email-compatible markup
- use simple paragraphs, line breaks, and links
- minimal wrapper structure only if needed for email compatibility
- avoid unnecessary nesting
- no JavaScript

## Copy rules
- strong subject lines
- short preheaders
- varied hooks across emails
- every email must feel purposeful
- avoid repetitive intros
- avoid generic utility company language
- write natural German for people living in DACH
- trust and clarity matter more than hype
- emails should read like one person wrote to another person

## Important constraints
- no fake urgency
- no deceptive scarcity
- no misleading claims
- no outdated hardcoded savings numbers
- use {{ opportunity.savings_text }} when dynamic savings language is needed
- use {{ opportunity.cta_text }} only where it makes sense
- every email must have a CTA
- most CTAs should drive to {{ opportunity.offer_url }}

## File structure
- emails/locales/de/spart/
- emails/locales/de/spart_nicht/
- emails/locales/de/neueinzug/
- emails/locales/de/loop/
- specs/

## Naming
- spart_01.html ... spart_10.html
- spart_nicht_01.html ... spart_nicht_04.html
- neueinzug_01.html ... neueinzug_10.html
- loop_01.html ... loop_15.html

## Done criteria
A template is done when:
- HTML is valid and clean
- placeholders are intact
- subject and preheader are defined clearly
- scenario psychology is correct
- CTA is clear and present
- CTA destination matches the email’s purpose
- the email looks plain and personal
- no button-like elements exist
- no images exist
- footer uses sender values
