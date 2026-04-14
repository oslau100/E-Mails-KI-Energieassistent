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
- increase open rates with stronger, relevant subject lines
- increase click-through rates with clearer CTA lead-ins
- increase conversions with natural objection handling
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

Mission messaging should be integrated selectively (not in every email), especially in:
- selected spart emails
- selected neueinzug emails
- selected spart_nicht emails
- selected loop emails
- all referral emails

## Mandatory CTA rule
Every email must contain exactly one CTA destination link.

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
- naturally handle objections ("ich will nichts falsch machen", "ich kenne mich nicht aus", "ich kümmere mich später")
- include a deliberate length mix (short spikes + medium + selected longer emails)

### spart_nicht
- build trust through honesty
- no fake savings claims
- positive reframe
- market monitoring mindset
- explain why ongoing monitoring emails still create value
- include selective mission framing

### neueinzug
- emphasize timing
- use Grundversorgung framing (avoid Standardtarif wording)
- acknowledge move-related overwhelm naturally
- make action feel easy and quick
- include a deliberate length mix

### loop
- lighter than entry sequences
- mix insights, reminders, soft conversion, and selected referral prompts
- should not feel repetitive
- should keep trust high
- include selective mission framing
- most loop emails still use tariff recommendation CTA
- only selected loop emails use referral CTA

## HTML and layout rules
The emails must look as plain and personal as possible.

Mandatory style:
- text-first
- minimal HTML
- no visual marketing layout
- no buttons
- no images
- no icons
- no banners
- no cards
- no boxed sections
- no hero areas
- no multi-column sections

CTA implementation:
- CTA must appear as a normal text link
- no button styling

## Copy rules
- actively optimize subject lines for open rate
- write preheaders that add relevance, consequence, or utility
- vary hooks across emails
- not all emails should be ultra-short
- include short spikes selectively, not universally
- keep tone: trustworthy + calm + clear
- use {{ opportunity.energieart }} where it improves relevance

## Important constraints
- no fake urgency
- no deceptive scarcity
- no misleading claims
- no outdated hardcoded savings numbers
- use {{ opportunity.savings_text }} when dynamic savings language is needed
- keep plain email style intact
